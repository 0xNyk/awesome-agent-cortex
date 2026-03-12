#!/usr/bin/env python3
import re
import sys
from pathlib import Path

TARGET_SECTIONS = {
    'Agent Frameworks',
    'Voice and Multimodal Agents',
    'Agent Runtime Infrastructure',
    'MCP Ecosystem',
    'Agent Security and Robustness',
    'Agent Configs and Dotfiles',
    'Skill Engineering and Playbooks',
    'Knowledge Graphs and Memory',
    'Agent Identity and Wallets',
    'Agent Payments',
    'DeFi Agents',
    'Quant and Trading Agents',
    'Agent Observability and Testing',
    'Research Papers',
    'Communities',
}


def parse_sections(lines):
    sections = {}
    section = None
    items = []
    for line in lines:
        m = re.match(r'^##\s+(.+)$', line)
        if m:
            if section is not None:
                sections[section] = items
            section = m.group(1).strip()
            items = []
            continue
        m = re.match(r'^- \[([^\]]+)\]\(', line)
        if m and section is not None:
            items.append(m.group(1).strip())
    if section is not None:
        sections[section] = items
    return sections


def main():
    path = Path(sys.argv[1] if len(sys.argv) > 1 else 'README.md')
    lines = path.read_text(encoding='utf-8').splitlines()
    sections = parse_sections(lines)

    violations = []
    for name in sorted(TARGET_SECTIONS):
        items = sections.get(name, [])
        normalized = [i.casefold() for i in items]
        if normalized != sorted(normalized):
            for i in range(len(items) - 1):
                if normalized[i] > normalized[i + 1]:
                    violations.append((name, items[i], items[i + 1]))
                    break

    if violations:
        print('Alphabetical order violations detected in curated sections:\n')
        for section, a, b in violations:
            print(f'- {section}: "{a}" should come after "{b}"')
        sys.exit(1)

    print('Alphabetical order OK in curated sections.')


if __name__ == '__main__':
    main()
