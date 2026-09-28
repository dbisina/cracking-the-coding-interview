# Build Order (AI-round practice)

A tiny package manager. Given which packages depend on which, it prints an install order where every package comes after all of its dependencies.

```
graph.py          dependency graph and manifest parser
resolver.py       install-order computation
main.py           CLI entry point
test_resolver.py  tests
```

```bash
python -m pytest -q
```

Your interviewer gives you the tasks one stage at a time. An AI assistant is available in chat. It can read the code, but you make every edit yourself.

**Don't open `tutor/`.**
