"""Regenerate the catalog table in README.md from the front matter of every skill and the first line of every rule.
Usage: python tools/build_index.py
The README must contain the markers <!-- CATALOG:START --> and <!-- CATALOG:END -->."""
import os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
def front(path):
    t = open(path, encoding='utf-8').read(); m = re.match(r'---\n(.*?)\n---', t, re.S); d = {}
    if m:
        for line in m.group(1).splitlines():
            k = re.match(r'^(name|description|version|created):\s*"?(.*?)"?$', line.strip())
            if k: d[k.group(1)] = k.group(2)
    return d
rows = ['| Type | Name | What it does |', '|---|---|---|']
sd = os.path.join(ROOT, 'skills')
for n in sorted(os.listdir(sd)):
    p = os.path.join(sd, n, 'SKILL.md')
    if os.path.exists(p):
        d = front(p); rows.append('| skill | [%s](skills/%s/SKILL.md) | %s |' % (n, n, (d.get('description', '')[:160] + '...') if len(d.get('description', '')) > 160 else d.get('description', '')))
rd = os.path.join(ROOT, 'rules')
for n in sorted(os.listdir(rd)):
    t = open(os.path.join(rd, n), encoding='utf-8').read().splitlines()[0].lstrip('# ').strip()
    rows.append('| rule | [%s](rules/%s) | %s |' % (n, n, t))
cd = os.path.join(ROOT, 'commands')
if os.path.isdir(cd):
    for n in sorted(os.listdir(cd)):
        t = open(os.path.join(cd, n), encoding='utf-8').read(); d = front(os.path.join(cd, n))
        rows.append('| command | [%s](commands/%s) | %s |' % (n, n, d.get('description', '')[:160]))
rp = os.path.join(ROOT, 'README.md'); s = open(rp, encoding='utf-8').read()
s = re.sub(r'<!-- CATALOG:START -->.*<!-- CATALOG:END -->', '<!-- CATALOG:START -->\n' + '\n'.join(rows) + '\n<!-- CATALOG:END -->', s, flags=re.S)
open(rp, 'w', encoding='utf-8').write(s); print('catalog rows:', len(rows) - 2)
