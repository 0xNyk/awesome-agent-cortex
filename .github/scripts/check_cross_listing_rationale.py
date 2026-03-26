#!/usr/bin/env python3
import os
import re
import subprocess
import sys
from pathlib import Path

README = Path('README.md')


def duplicate_url_counts(markdown: str) -> dict[str, int]:
    section = None
    counts: dict[str, int] = {}
    for line in markdown.splitlines():
        h = re.match(r'^##\s+(.+)$', line)
        if h:
            section = h.group(1).strip()
            continue
        m = re.match(r'^- \[[^\]]+\]\((https?://[^\)]+)\) - ', line)
        if m and section:
            url = m.group(1)
            counts[url] = counts.get(url, 0) + 1
    return counts


def load_base_readme(base_ref: str) -> str:
    cmd = ['git', 'show', f'origin/{base_ref}:README.md']
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f'Unable to load base README from origin/{base_ref}: {res.stderr.strip()}')
    return res.stdout


def main() -> int:
    event = os.getenv('GITHUB_EVENT_NAME', '')
    if event != 'pull_request':
        print('Skipping cross-listing rationale check outside pull_request events.')
        return 0

    base_ref = os.getenv('BASE_REF', 'main')
    pr_body = os.getenv('PR_BODY', '')

    current = README.read_text(encoding='utf-8')
    base = load_base_readme(base_ref)

    current_dups = duplicate_url_counts(current)
    base_dups = duplicate_url_counts(base)

    increased = []
    for url, count in current_dups.items():
        base_count = base_dups.get(url, 0)
        if count > 1 and count > base_count:
            increased.append((url, base_count, count))

    if not increased:
        print('No new cross-listings introduced.')
        return 0

    if 'Intentional cross-listings' not in pr_body:
        print('New cross-listings detected but PR body is missing required rationale section.')
        print('Add a section titled "Intentional cross-listings" to explain why duplication is useful.')
        print('\nDetected new cross-listings:')
        for url, before, after in increased:
            print(f'- {url}: {before} -> {after}')
        return 1

    print('Cross-listing rationale present in PR body.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
