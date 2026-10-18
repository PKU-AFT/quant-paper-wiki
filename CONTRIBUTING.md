# Contributing

Contribute papers, source corrections, reading notes and reproducible experiments.

| Contribution | Include |
| --- | --- |
| New paper | Full title, primary source, research area and reason for inclusion |
| Code link | Identify author code, a demonstration or a third-party implementation |
| Reading note | Cite relevant pages, sections or equations |
| Experiment | Follow the [experimental protocol](wiki/Reproduction-Guide.md), including deviations and failed runs |

## Update the catalog

1. Edit [data/papers.json](data/papers.json). Preserve existing IDs and append new entries with the next available ID. [data/source-titles.json](data/source-titles.json) preserves the initial 37-paper list.
2. Keep the primary fields in English. Chinese source descriptions are retained in fields ending in _zh.
3. With Python 3.11 or newer, run:

       python3 scripts/build.py
       python3 scripts/check.py

4. Submit the catalog and generated Markdown together in a pull request. Update generated cards through the catalog; keep longer reading notes in separate linked pages.

Do not upload credentials, data without sharing permission or full paper copies.

## Publish the GitHub Wiki

Maintainers can run the command below after reviewing repository changes:

    python3 scripts/sync_wiki.py --push

The current gh account needs write access, and the Wiki must have an initial page. The script updates matching generated pages and preserves unrelated Wiki pages.
