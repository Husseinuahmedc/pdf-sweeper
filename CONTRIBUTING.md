# Contributing

This project is intentionally small and beginner-readable.

## Rules

- Use Python standard library only.
- Keep the CLI simple.
- Prefer clear code over clever code.
- Keep compatibility with Linux, Arch Linux, Windows, and macOS.
- Use `pathlib` for paths.
- Use `shutil` for copy and move operations.

## Before opening a pull request

Run:

```bash
python -m py_compile pdf_sweeper.py
```

Then manually test:

```bash
python pdf_sweeper.py
```
