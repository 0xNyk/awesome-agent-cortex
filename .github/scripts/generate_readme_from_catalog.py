#!/usr/bin/env python3
import json
from pathlib import Path

README = Path('README.md')
CATALOG = Path('data/resources.json')
START = '<!-- RESOURCES:START -->'
END = '<!-- RESOURCES:END -->'


def render_sections(catalog: dict) -> list[str]:
    lines: list[str] = []
    for section in catalog['sections']:
        lines.append(f"## {section['name']}")
        for item in section['items']:
            if item['type'] == 'entry':
                lines.append(f"- [{item['name']}]({item['url']}) - {item['description']}")
            else:
                lines.append(item['text'])
    return lines


def main() -> int:
    readme_lines = README.read_text(encoding='utf-8').splitlines()
    catalog = json.loads(CATALOG.read_text(encoding='utf-8'))

    start_marker = catalog.get('managed_block', {}).get('start_marker', START)
    end_marker = catalog.get('managed_block', {}).get('end_marker', END)

    if start_marker not in readme_lines or end_marker not in readme_lines:
        raise SystemExit('README.md is missing managed resource markers')

    sidx = readme_lines.index(start_marker)
    eidx = readme_lines.index(end_marker)
    if sidx >= eidx:
        raise SystemExit('Invalid managed marker ordering in README.md')

    rendered = render_sections(catalog)
    new_lines = readme_lines[: sidx + 1] + rendered + readme_lines[eidx:]
    content = '\n'.join(new_lines).rstrip('\n') + '\n'
    README.write_text(content, encoding='utf-8')
    print(f'Generated README managed block from {CATALOG}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
