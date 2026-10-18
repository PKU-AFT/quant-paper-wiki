#!/usr/bin/env python3
"""Build English table-based navigation from the editable paper catalog."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PAPERS = json.loads((ROOT / 'data/papers.json').read_text())
GROUPS = json.loads((ROOT / 'data/categories.json').read_text())
GROUP = {g['id']: g for g in GROUPS}


def filename(p):
    return f"Paper-{p['id']:03d}-{p['slug']}.md"


def cell(value):
    return str(value).replace('|', r'\|').replace('\n', ' ')


def grid(headers, rows):
    output = ['| ' + ' | '.join(headers) + ' |',
              '| ' + ' | '.join('---' for _ in headers) + ' |']
    output += ['| ' + ' | '.join(cell(v) for v in row) + ' |' for row in rows]
    return '\n'.join(output)


def table(papers, prefix=''):
    return grid(['ID', 'Paper & notes', 'Year¹', 'Research focus', 'Paper', 'Code'], [
        [f"{p['id']:02d}", f"[{p['short_title']}]({prefix}{filename(p)})",
         p['year'], p['summary'], f"[Paper]({p['primary_url']})",
         f"[Code]({p['code_url']})" if p['code_url'] else 'To verify']
        for p in papers
    ])


def write(path, text):
    path.write_text(text.strip() + '\n')


def overview(repository=False):
    prefix = 'wiki/' if repository else ''
    title = 'PKU-AFT · Quantitative Finance Paper Wiki' if repository else 'Quantitative Finance Paper Wiki'
    nav = (f'[Full index]({prefix}All-Papers.md) · '
           f'[Reading paths]({prefix}Reading-Paths.md) · '
           f'[Experimental protocol]({prefix}Reproduction-Guide.md) · '
           f'[Sources & versions]({prefix}Sources-and-Status.md)')
    if repository:
        nav = '[Online Wiki](https://github.com/PKU-AFT/quant-paper-wiki/wiki) · ' + nav
    content = f'''# {title}

**{len(PAPERS)} papers · {len(GROUPS)} research areas · {sum(bool(p['code_url']) for p in PAPERS)} companion code links**

{nav}

## Research areas

'''
    area_rows = []
    for g in GROUPS:
        subset = [p for p in PAPERS if p['category'] == g['id']]
        area_rows.append([f"[{g['name']}]({prefix}Category-{g['id']}.md)",
                          len(subset), g['description']])
    content += grid(['Research area', 'Papers', 'Scope'], area_rows) + '\n\n## Paper directory\n\n'
    for g in GROUPS:
        subset = [p for p in PAPERS if p['category'] == g['id']]
        content += f"### {g['name']}\n\n" + table(subset, prefix) + '\n\n'
    content += (f'¹ Years refer to the linked preprint or publication version; '
                f'see [Sources & versions]({prefix}Sources-and-Status.md).\n')
    if repository:
        content += '''
## Contribute

Suggest a paper or correct a link through an [Issue](https://github.com/PKU-AFT/quant-paper-wiki/issues/new/choose). Submit reading notes and experiment records through a pull request. See [Contributing](CONTRIBUTING.md).

The editable catalog is [data/papers.json](data/papers.json). Each entry includes primary sources, companion code, a method summary, reading questions and an experiment idea.
'''
    return content


write(ROOT / 'README.md', overview(repository=True))
write(ROOT / 'wiki/Home.md', overview())
write(ROOT / 'wiki/All-Papers.md', '''# All Papers

[Home](Home.md) · [Reading paths](Reading-Paths.md)

Original IDs 01–37 are preserved. New entries should use the next available ID.

''' + table(PAPERS) + '\n\n¹ Version and year conventions are described in [Sources & versions](Sources-and-Status.md).')

for g in GROUPS:
    content = (f"# {g['name']}\n\n[Home](Home.md) · [Full index](All-Papers.md)\n\n"
               + grid(['Research area', 'Scope'], [[g['name'], g['description']]]) + '\n\n'
               + table([p for p in PAPERS if p['category'] == g['id']]))
    write(ROOT / f"wiki/Category-{g['id']}.md", content)

for p in PAPERS:
    g = GROUP[p['category']]
    code = f"[{p['code_note']}]({p['code_url']})" if p['code_url'] else p['code_note']
    rows = [
        ['Research area', f"[{g['name']}](Category-{g['id']}.md)"],
        ['Linked version year', p['year']],
        ['Paper', f"[Primary source]({p['primary_url']})"],
        ['Code', code],
        ['Method', p['summary']],
        ['Reading focus', p['reading_focus']],
        ['Experiment idea', p['first_experiment']],
        ['Source check', p['verification_status']],
        ['Independent reproduction', p['reproduction_status']],
        ['Last source check', p['last_checked']],
    ]
    content = (f"# {p['id']:02d} · {p['short_title']}\n\n"
               f"[Home](Home.md) · [Full index](All-Papers.md)\n\n"
               f"**{p['title']}**\n\n" + grid(['Item', 'Details'], rows))
    if p['extra_sources']:
        content += '\n\n## Additional sources & versions\n\n'
        content += grid(['Source', 'Link'], [[s['label'], f"[Open]({s['url']})"] for s in p['extra_sources']])
    content += '\n\n[Experimental protocol](Reproduction-Guide.md) · [Sources & versions](Sources-and-Status.md)'
    write(ROOT / 'wiki' / filename(p), content)

sidebar = f'''# Navigation

[Home](Home.md)

[All {len(PAPERS)} papers](All-Papers.md)

[Reading paths](Reading-Paths.md)

[Experimental protocol](Reproduction-Guide.md)

'''
sidebar += '\n\n'.join(f"[{g['name']}](Category-{g['id']}.md)" for g in GROUPS)
sidebar += '\n\n[Sources & versions](Sources-and-Status.md)'
write(ROOT / 'wiki/_Sidebar.md', sidebar)
write(ROOT / 'wiki/_Footer.md', 'PKU-AFT · Quantitative Finance Paper Wiki · [Repository](https://github.com/PKU-AFT/quant-paper-wiki) · [Sources & versions](Sources-and-Status.md)')
print(f'Built {len(PAPERS)} English paper cards and {len(GROUPS)} category tables.')
