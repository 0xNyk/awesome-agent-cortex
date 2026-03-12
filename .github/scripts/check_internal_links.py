#!/usr/bin/env python3

import os
import re
import sys
from pathlib import Path

ROOT = Path('.')

MD_FILES = []
for path in ROOT.rglob('*.md'):
    if '.git' in path.parts:
        continue
    MD_FILES.append(path)

existing = {p.as_posix() for p in MD_FILES}

link_pattern = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
fence_pattern = re.compile(r'```.*?```', re.DOTALL)
inline_code_pattern = re.compile(r'`[^`]*`')

errors = []

for md_file in MD_FILES:
    text = md_file.read_text(encoding='utf-8', errors='ignore')

    # Ignore fenced and inline code so examples like [Name](URL) do not fail.
    text = fence_pattern.sub('', text)
    text = inline_code_pattern.sub('', text)

    for match in link_pattern.finditer(text):
        raw = match.group(1).strip()

        if raw.startswith(('http://', 'https://', 'mailto:', '#')):
            continue

        if raw.startswith('<') and raw.endswith('>'):
            raw = raw[1:-1]

        raw = raw.split('#', 1)[0].split('?', 1)[0]
        if not raw or raw.startswith(('/', 'javascript:')):
            continue

        target = (md_file.parent / raw).resolve()
        try:
            rel_target = target.relative_to(ROOT.resolve()).as_posix()
        except ValueError:
            errors.append((md_file.as_posix(), raw, 'path escapes repository root'))
            continue

        if rel_target in existing:
            continue

        if not target.exists():
            errors.append((md_file.as_posix(), raw, rel_target))

if errors:
    print('Broken internal markdown links found:\n')
    for source, raw, resolved in errors:
        print(f'- {source}: ({raw}) -> {resolved}')
    print(f'\nTotal broken internal links: {len(errors)}')
    sys.exit(1)

print(f'OK: checked {len(MD_FILES)} markdown files, no broken internal links.')
