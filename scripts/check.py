#!/usr/bin/env python3
"""Check catalog coverage, safe URLs and repository-local navigation."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import re

ROOT = Path(__file__).resolve().parents[1]
papers=json.loads((ROOT/'data/papers.json').read_text())
source=json.loads((ROOT/'data/source-titles.json').read_text())
groups=json.loads((ROOT/'data/categories.json').read_text())
assert len(source)==37
assert len(papers)>=37
assert len({p['id'] for p in papers})==len(papers), 'Duplicate paper ID'
assert len({p['primary_url'] for p in papers})==len(papers), 'Duplicate primary URL'
by_id={p['id']:p for p in papers}
for p in source:
    assert by_id[p['id']]['title']==p['title'], f"Source title changed: {p['id']}"
group_ids={g['id'] for g in groups}
for p in papers:
    assert p['category'] in group_ids
    assert p['reproduction_status'] in ('未开展','环境检查','方法演示','论文复现')
    for key in ['title','summary','reading_focus','first_experiment','last_checked']:
        assert p[key].strip(), (p['id'],key)
    urls=[p['primary_url']]+([p['code_url']] if p['code_url'] else [])
    urls += [s['url'] for s in p['extra_sources']]
    for url in urls:
        assert urlsplit(url).scheme=='https' and urlsplit(url).hostname, url
links=0
for file in [ROOT/'README.md',ROOT/'CONTRIBUTING.md',*sorted((ROOT/'wiki').glob('*.md'))]:
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',file.read_text()):
        if target.startswith(('https://','#','mailto:')): continue
        relative=unquote(target.split('#')[0])
        assert relative and (file.parent/relative).resolve().is_relative_to(ROOT), (file,target)
        assert (file.parent/relative).is_file(), (file,target)
        links+=1
cards=list((ROOT/'wiki').glob('Paper-*.md'))
assert len(cards)==len(papers), 'Missing or extra paper cards'
print(json.dumps({'papers':len(papers),'original_list_covered':len(source),'categories':len(groups),'code_links':sum(bool(p['code_url']) for p in papers),'local_links_checked':links,'paper_cards':len(cards),'status':'passed'},ensure_ascii=False))
