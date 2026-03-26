#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

README = Path('README.md')
FLOORS = Path('.github/curation/section_floors.json')


def section_counts(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    section = None
    for line in text.splitlines():
        m = re.match(r'^##\s+(.+)$', line)
        if m:
            section = m.group(1).strip()
            counts.setdefault(section, 0)
            continue
        m = re.match(r'^- \[[^\]]+\]\(([^\)]+)\) - ', line)
        if m and section:
            counts[section] = counts.get(section, 0) + 1
    return counts


def main() -> int:
    floors = json.loads(FLOORS.read_text(encoding='utf-8'))
    counts = section_counts(README.read_text(encoding='utf-8'))

    violations = []
    for section, min_count in floors.get('floors', {}).items():
        actual = counts.get(section, 0)
        if actual < min_count:
            violations.append((section, min_count, actual))

    if violations:
        print('Section floor violations detected:\n')
        for section, minimum, actual in violations:
            print(f'- {section}: expected >= {minimum}, found {actual}')
        return 1

    print('Section floors OK.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
