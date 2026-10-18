#!/usr/bin/env python3
"""Export tracked source pages to a GitHub Wiki, preserving unrelated pages."""
from pathlib import Path
from urllib.parse import urlsplit
import argparse
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
URL='https://github.com/PKU-AFT/quant-paper-wiki.wiki.git'
parser=argparse.ArgumentParser()
parser.add_argument('--push',action='store_true',help='Commit and push generated pages')
args=parser.parse_args()
checkout=ROOT/'.wiki-checkout'
def run(*cmd):
    return subprocess.run(cmd,text=True,check=True,capture_output=True).stdout
if not checkout.exists():
    subprocess.run(['git','clone',URL,str(checkout)],check=True)
assert run('git','-C',str(checkout),'remote','get-url','origin').strip()==URL
assert not run('git','-C',str(checkout),'status','--porcelain').strip(), 'Wiki checkout has local changes; review them first'
subprocess.run(['git','-C',str(checkout),'pull','--ff-only'],check=True)
pages=sorted((ROOT/'wiki').glob('*.md'))
def convert(match):
    label,target=match.group(1),match.group(2)
    parsed=urlsplit(target)
    if parsed.scheme or target.startswith('#'): return match.group(0)
    path,sep,fragment=target.partition('#')
    assert '/' not in path and path.endswith('.md'), target
    return f'[{label}]({path[:-3]}'+(f'#{fragment}' if sep else '')+')'
for page in pages:
    output=re.sub(r'\[([^\]]*)\]\(([^)]+)\)',convert,page.read_text())
    (checkout/page.name).write_text(output)
subprocess.run(['git','-C',str(checkout),'add','--',*[p.name for p in pages]],check=True)
if not run('git','-C',str(checkout),'diff','--cached','--name-only').strip():
    print('Wiki already matches the repository sources.')
elif args.push:
    subprocess.run(['git','-C',str(checkout),'commit','-m','docs: sync quantitative paper navigation'],check=True)
    subprocess.run(['git','-C',str(checkout),'push','origin','HEAD'],check=True)
    print(f'Published {len(pages)} generated Wiki pages.')
else:
    print('Generated pages staged locally. Review git diff --cached; commit and push when ready.')
