# Architecture

ascii-filetree is a curses directory tree viewer built with only the Python standard library.

## Runtime flow

1. The app resolves the target directory from the command line.
2. The tree builder walks directories and creates ASCII branch lines.
3. The generated lines are stored in memory as a simple list.
4. The curses UI renders a scrollable window over that list.
5. Pressing `q` exits the app.

## Main parts

- `make_tree()` builds the ASCII tree rows.
- Recursive walking handles nested folders and branch prefixes.
- `draw()` owns the curses loop, scroll offset and keyboard handling.

## Design rules

- Keep dependencies at zero.
- Avoid crashing on permission errors.
- Keep traversal depth and output size reasonable.
- Keep rendering separate from tree generation.
- Prefer plain ASCII branch characters for maximum terminal compatibility.
