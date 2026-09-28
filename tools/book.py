#!/usr/bin/env python3
"""Pull exact text from the learner's own copy of CtCI 6th ed. for the tutor.

Usage:
  python tools/book.py list [CHAPTER]        problems (all, or one chapter)
  python tools/book.py q 4.2                 question text
  python tools/book.py hint 4.2 [N]          Nth hint (1-based); no N = how many exist
  python tools/book.py sol 4.2               full solution
  python tools/book.py section big-o         concept pages (see `sections`)
  python tools/book.py sections              list section keys
  python tools/book.py pages 100-103         raw PDF pages
  python tools/book.py search "runner"       find pages mentioning a phrase

PDF lookup order: $CTCI_PDF, workbook root, workbook parent dir.
Text is OCR-derived: expect small glitches ("f a l s e", "II" for "//").
"""
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = json.loads((ROOT / "tools" / "book_index.json").read_text(encoding="utf-8"))
CACHE = ROOT / "tools" / ".cache" / "pages.json"
PDF_GLOB = "Cracking-the-Coding-Interview*.pdf"


def find_pdf():
    env = os.environ.get("CTCI_PDF")
    if env and Path(env).is_file():
        return Path(env)
    for folder in (ROOT, ROOT.parent):
        hits = sorted(folder.glob(PDF_GLOB))
        if hits:
            return hits[0]
    sys.exit("PDF not found. Set CTCI_PDF=/path/to/book.pdf or put the PDF next to the workbook.")


def extract_pages(pdf):
    try:
        import fitz  # PyMuPDF
        with fitz.open(pdf) as doc:
            return [p.get_text() for p in doc]
    except ImportError:
        pass
    try:
        import pypdfium2 as pdfium
        doc = pdfium.PdfDocument(str(pdf))
        return [doc[i].get_textpage().get_text_range() for i in range(len(doc))]
    except ImportError:
        pass
    import subprocess
    out = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, encoding="utf-8", check=True).stdout
    return out.split("\f")


def pages():
    if CACHE.is_file():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    text = extract_pages(find_pdf())
    CACHE.parent.mkdir(exist_ok=True)
    CACHE.write_text(json.dumps(text), encoding="utf-8")
    return text


def extract_hints(pdf):
    """Hint pages are two-column (#N | problem | text); plain extraction scrambles them, so use word positions."""
    import fitz
    first, last = INDEX["sections"]["hints"]
    out = {}
    with fitz.open(pdf) as doc:
        for pno in range(first - 1, last):
            page = doc[pno]
            footer_y = page.rect.height - 45
            words = page.get_text("words")
            anchors = sorted((w for w in words if w[0] < 120 and re.match(r"^#\s?\d{1,3}[.,]?$", w[4])), key=lambda w: w[1])
            body = [w for w in words if w[0] >= 160 and w[1] < footer_y]
            for i, a in enumerate(anchors):
                y0 = a[1] - 2
                y1 = anchors[i + 1][1] - 2 if i + 1 < len(anchors) else footer_y
                lines = {}
                for w in body:
                    if y0 <= w[1] < y1:
                        lines.setdefault(round(w[3]), []).append(w)
                rows = (" ".join(x[4] for x in sorted(v, key=lambda w: w[0])) for _, v in sorted(lines.items()))
                text = "\n".join(r for r in rows if not re.search(r"Cracking|Edition", r))
                out[re.sub(r"\D", "", a[4])] = text
    return out


def hints():
    cache = CACHE.with_name("hints.json")
    if cache.is_file():
        return json.loads(cache.read_text(encoding="utf-8"))
    try:
        data = extract_hints(find_pdf())
    except ImportError:
        return {}
    CACHE.parent.mkdir(exist_ok=True)
    cache.write_text(json.dumps(data), encoding="utf-8")
    return data


def tidy(text):
    text = re.sub(r"[ \t]+\n", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def page_range(a, b):
    ps = pages()
    return "\n\n".join(f"--- PDF p.{n} (book p.{n - 12}) ---\n{tidy(ps[n - 1])}" for n in range(a, b + 1))


def problem(pid):
    p = INDEX["problems"].get(pid)
    if not p:
        sys.exit(f"Unknown problem {pid}. Try: python tools/book.py list")
    return p


def slice_between(text, start_pat, stop_pats):
    m = re.search(start_pat, text)
    if not m:
        return text
    rest = text[m.start():]
    cut = len(rest)
    for sp in stop_pats:
        s = re.search(sp, rest[5:])
        if s:
            cut = min(cut, s.start() + 5)
    return rest[:cut]


def num_pat(pid):
    a, b = pid.split(".")
    return rf"(?m)^\s*{a}\s?[.,]\s?{b}\b"


def next_pid(pid):
    keys = sorted(INDEX["problems"], key=lambda k: tuple(map(int, k.split("."))))
    i = keys.index(pid)
    return keys[i + 1] if i + 1 < len(keys) else None


def cmd_q(pid):
    p = problem(pid)
    ps = pages()
    text = tidy(ps[p["question_page"] - 1] + "\n" + ps[p["question_page"]])
    nxt = next_pid(pid)
    stops = [num_pat(nxt)] if nxt else []
    stops.append(r"Hints:\s*#[\d, #]+")
    body = slice_between(text, num_pat(pid), stops)
    print(f"{pid} {p['title']}  (PDF p.{p['question_page']})\n")
    print(tidy(body))
    print(f"\n[{len(p['hints'])} hints available. Solution at PDF p.{p['solution_page']}.]")


def cmd_hint(pid, n=None):
    p = problem(pid)
    total = len(p["hints"])
    if n is None:
        print(f"{pid} {p['title']}: {total} hints (#{', #'.join(map(str, p['hints']))}). Ask for them in order: hint {pid} 1 .. {total}")
        return
    n = int(n)
    if not 1 <= n <= total:
        sys.exit(f"{pid} has hints 1..{total}")
    hnum = p["hints"][n - 1]
    positional = hints().get(str(hnum))
    if positional:
        print(f"{pid} hint {n}/{total} (book hint #{hnum}):\n{positional}")
        return
    pg = INDEX["hint_pages"][str(hnum)]
    ps = pages()
    text = ps[pg - 1] + "\n" + ps[pg]
    m = re.search(rf"#\s?{hnum}\s?[.,]\s*\n", text)
    if not m:
        print(page_range(pg, pg))
        return
    rest = text[m.end():]
    stop = re.search(r"\n#\s?\d{1,3}\s?[.,]\s*\n", rest)
    chunk = rest[: stop.start()] if stop else rest
    chunk = re.sub(r"^\s*\d{1,2}\s?[.,]\s?\d{1,2}\s*\n", "", chunk)
    chunk = re.sub(r"CrackingTheCoding.*|Cracking the Coding Interview.*|\n\s*\d{3}\s*$", "", chunk)
    print(f"{pid} hint {n}/{total} (book hint #{hnum}):\n{tidy(chunk)}")


def cmd_sol(pid):
    p = problem(pid)
    ps = pages()
    end = p.get("solution_end", p["solution_page"])
    text = "\n".join(ps[i - 1] for i in range(p["solution_page"], end + 1))
    nxt = next_pid(pid)
    body = slice_between(text, num_pat(pid), [num_pat(nxt)] if nxt else [])
    print(f"{pid} {p['title']}  (PDF p.{p['solution_page']}-{end})\n")
    print(tidy(body))


def cmd_list(chapter=None):
    for pid, p in sorted(INDEX["problems"].items(), key=lambda kv: tuple(map(int, kv[0].split(".")))):
        if chapter and pid.split(".")[0] != str(chapter):
            continue
        print(f"{pid:6} {p['title']:40} q:p.{p['question_page']:<4} sol:p.{p['solution_page']:<4} hints:{len(p['hints'])}")


def cmd_section(key):
    rng = INDEX["sections"].get(key)
    if not rng:
        sys.exit(f"Unknown section. Keys: {', '.join(INDEX['sections'])}")
    print(page_range(*rng))


def cmd_search(phrase):
    needle = phrase.lower()
    for i, t in enumerate(pages(), start=1):
        low = t.lower()
        j = low.find(needle)
        if j >= 0:
            snippet = " ".join(t[max(0, j - 60): j + 80].split())
            print(f"p.{i}: ...{snippet}...")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return
    cmd, args = argv[1], argv[2:]
    if cmd == "list":
        cmd_list(*args)
    elif cmd == "q":
        cmd_q(*args)
    elif cmd == "hint":
        cmd_hint(*args)
    elif cmd == "sol":
        cmd_sol(*args)
    elif cmd == "section":
        cmd_section(*args)
    elif cmd == "sections":
        for k, (a, b) in INDEX["sections"].items():
            print(f"{k:22} PDF p.{a}-{b}")
    elif cmd == "pages":
        a, _, b = args[0].partition("-")
        print(page_range(int(a), int(b or a)))
    elif cmd == "search":
        cmd_search(" ".join(args))
    else:
        print(__doc__)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main(sys.argv)
