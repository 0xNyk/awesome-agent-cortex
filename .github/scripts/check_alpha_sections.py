#!/usr/bin/env python3
import re
import sys
from pathlib import Path

IGNORED_SECTIONS = {'Contents', 'Contributing'}
ORDERED_BLOCKS = {
    ('Agent Harnessing and Evaluation', 'Benchmark Reality Check (real-world tool use)'),
    ('Context Engineering', 'Context Engineering'),
    ('Neural Networks and Neural Linking', 'Neural Networks and Neural Linking'),
}


def parse_blocks(lines):
    blocks = []
    section = None
    block = None
    items = []

    def flush():
        if section and items:
            blocks.append((section, block or section, items.copy()))
            items.clear()

    for line in lines:
        heading = re.match(r'^(##|###)\s+(.+)$', line)
        if heading:
            flush()
            level, name = heading.groups()
            if level == '##':
                section = name.strip()
                block = None
            else:
                block = name.strip()
            continue

        item = re.match(r'^- \[([^\]]+)\]\(', line)
        if item and section not in IGNORED_SECTIONS:
            items.append(item.group(1).strip())

    flush()
    return blocks


def main():
    path = Path(sys.argv[1] if len(sys.argv) > 1 else 'README.md')
    lines = path.read_text(encoding='utf-8').splitlines()
    blocks = parse_blocks(lines)

    violations = []
    for section, block, items in blocks:
        if (section, block) in ORDERED_BLOCKS:
            continue
        normalized = [i.casefold() for i in items]
        if normalized != sorted(normalized):
            for i in range(len(items) - 1):
                if normalized[i] > normalized[i + 1]:
                    violations.append((section, block, items[i], items[i + 1]))
                    break

    if violations:
        print('Alphabetical order violations detected in curated blocks:\n')
        for section, block, a, b in violations:
            label = section if section == block else f'{section} / {block}'
            print(f'- {label}: "{a}" should come after "{b}"')
        sys.exit(1)

    print(f'Alphabetical order OK in {len(blocks)} curated blocks.')


if __name__ == '__main__':
    main()
