#!/usr/bin/env python3
import curses, os, sys


def make_tree(root, limit=500):
    rows = []
    def walk(path, prefix=''):
        if len(rows) >= limit: return
        try: items = sorted(os.listdir(path), key=lambda n: (not os.path.isdir(os.path.join(path,n)), n.lower()))
        except OSError: return
        for i, name in enumerate(items):
            p = os.path.join(path, name)
            last = i == len(items)-1
            branch = '`-- ' if last else '|-- '
            rows.append(prefix + branch + name + ('/' if os.path.isdir(p) else ''))
            if os.path.isdir(p) and not os.path.islink(p):
                walk(p, prefix + ('    ' if last else '|   '))
    rows.append(os.path.abspath(root) + '/')
    walk(root)
    return rows


def draw(stdscr):
    curses.curs_set(0)
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    rows = make_tree(root)
    top = 0
    while True:
        h, w = stdscr.getmaxyx()
        stdscr.erase()
        stdscr.addstr(0, 2, 'ASCII FILETREE - j/k scroll  r rescan  q quit')
        for i, line in enumerate(rows[top:top+h-2], 2):
            stdscr.addstr(i, 0, line[:w-1])
        ch = stdscr.getch()
        if ch in (ord('q'), ord('Q')): break
        if ch in (ord('j'), curses.KEY_DOWN): top = min(max(0, len(rows)-1), top+1)
        if ch in (ord('k'), curses.KEY_UP): top = max(0, top-1)
        if ch in (ord('r'), ord('R')): rows = make_tree(root); top = 0


if __name__ == '__main__':
    curses.wrapper(draw)
