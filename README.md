# Cracking the Coding Interview: Interactive AI-Tutor Workbook

> An **unofficial** study companion. It isn't affiliated with or endorsed by Gayle Laakmann McDowell or CareerCup. **You need your own copy of the book** (6th edition PDF). None of the book's text is included in this repo.

This is an AI-tutored workbook for *Cracking the Coding Interview*, 6th edition. It covers all 189 problems, the concept chapters, Big O, system design and behavioral prep, plus **new modules for AI-era interviews** that the 2015 book predates: AI-assisted coding rounds (Meta, Google, Canva) and GenAI/LLM system design. Your AI coding agent reads `AGENTS.md` (Claude Code reads it through `CLAUDE.md`) and becomes your tutor and mock interviewer. It asks one question at a time, checks your answers, climbs a hint ladder when you're stuck, writes tests for your code, and tracks your progress with spaced repetition.

## Start

1. Clone this repo and put your PDF (`Cracking-the-Coding-Interview*.pdf`) inside it or in its parent folder. `*.pdf` is gitignored. The tool finds it in either place, or you can set `CTCI_PDF=/path/to/book.pdf`.
2. Open the folder in your agent (Claude Code, Codex, Cursor, and so on). For Claude Code:
   ```bash
   git clone https://github.com/dbisina/cracking-the-coding-interview.git && cd cracking-the-coding-interview && claude
   ```
3. Say: **"Start tutoring."** The first session asks about your language, your timeline and your level, runs a short diagnostic, and then begins.
4. In later sessions, say **"continue"**. The tutor reads `PROGRESS.md` and picks up where you left off, starting with any reviews that are due.

## Things you can say
`next` · `hint` · `stuck` · `skip` · `quiz me` · `flashcards` · `mock interview` · `ai mock` · `explain differently` · `status` · `review` · `why?`

## What's inside

| Path | What |
|---|---|
| `AGENTS.md` | Tutor protocol: teaching rules, the interview loop, the hint ladder, scoring, spaced repetition, mock mode |
| `PROGRESS.md` | Your profile, module status, problem log, review queue and mock scores. The tutor updates it |
| `curriculum/README.md` | Module map, study paths (Standard or Fast Track), pattern tags |
| `curriculum/00–20-*.md` | One module per book topic: objectives, concept checks, problem ladder, exit quiz, flashcards |
| `curriculum/21-ai-assisted-coding.md` | **New:** AI-enabled coding rounds (Meta's multi-file, 3-stage format; Google's pilot) |
| `curriculum/22-genai-system-design.md` | **New:** RAG, agents, evals, prompt injection, LLM cost/latency |
| `practice/ai-rounds/` | **New:** 3 multi-file projects (bug → feature → scale) for AI-round mocks, with hidden stage tests and reference solutions |
| `tools/book.py` | Pulls exact questions, hints, solutions and pages from your PDF |
| `workspace/` | Your code, plus the tests the tutor writes |

## The book tool

```bash
python tools/book.py list 2
```
```bash
python tools/book.py q 2.8
```
```bash
python tools/book.py hint 2.8 1
```
```bash
python tools/book.py sol 2.8
```
```bash
python tools/book.py section big-o
```

It needs Python 3 and PyMuPDF (`pip install pymupdf`). It falls back to pypdfium2 or `pdftotext` if PyMuPDF isn't installed, but hint extraction is most accurate with PyMuPDF. The first run caches the extracted text in `tools/.cache/`.

## Spoiler warning
The curriculum files contain answer keys and "key insight" columns meant for the tutor. If you want the full effect, don't read ahead. Let the tutor ask you first.

## AI-era sections: sources
Modules 21–22 and the AI questions in Module 20 draw on public reporting from 2025–2026. Formats change fast, so confirm with your recruiter.
- [Hello Interview: Meta's AI-enabled coding interview](https://www.hellointerview.com/blog/meta-ai-enabled-coding)
- [interviewing.io: How to use AI in Meta's AI-assisted coding interview](https://interviewing.io/blog/how-to-use-ai-in-meta-s-ai-assisted-coding-interview-with-real-prompts-and-examples)
- [Northeastern Careers: Google's AI-assisted coding interview (2026)](https://careers.northeastern.edu/blog/2026/05/13/googles-ai-assisted-coding-interview-2026-guide/)
- [Computerworld: companies bring back in-person interviews to counter AI cheating](https://www.computerworld.com/article/4044734/to-counter-ai-cheating-companies-bring-back-in-person-job-interviews.html)
- [Axios: in-person interviews to dodge the chatbots](https://www.axios.com/2025/08/12/in-person-job-interview-artificial-intelligence)

## Copyright
The workbook's own content (explanations, questions, answer keys) is original. Book text is only pulled at runtime from **your own copy** of the PDF. `tools/book_index.json` holds page numbers and problem titles only. Don't commit or redistribute the PDF or `tools/.cache/`. Both are gitignored.
