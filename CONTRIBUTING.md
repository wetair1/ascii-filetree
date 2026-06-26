# Contributing

Thanks for improving ascii-filetree.

## Local setup

```bash
git clone https://github.com/wetair1/ascii-filetree.git
cd ascii-filetree
python3 main.py .
```

No external dependencies are required.

## Code style

- Keep the project pure Python stdlib.
- Keep directory traversal safe and readable.
- Avoid crashing on permission errors.
- Keep the tree readable on small terminals.
- Document controls when adding new keys.

## Checks

```bash
python3 -m py_compile main.py
python3 main.py .
```

## Commit style

Use short imperative messages, for example:

- `Add depth limit option`
- `Fix scroll bounds`
- `Document controls`
