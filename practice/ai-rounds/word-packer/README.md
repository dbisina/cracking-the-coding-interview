# Word Packer (AI-round practice)

A sign-maker owns exactly **one tile per letter**, a–z. Given a list of words, the tool picks a set of words that can be printed together (no letter used twice) to use as many tiles as possible.

```
words.py        loading and normalising word lists
bits.py         letter-set bitmask helpers
packer.py       the optimiser
main.py         CLI entry point
test_packer.py  tests
```

```bash
python -m pytest -q
```

Your interviewer gives you the tasks one stage at a time. An AI assistant is available in chat. It can read the code, but you make every edit yourself.

**Don't open `tutor/`.**
