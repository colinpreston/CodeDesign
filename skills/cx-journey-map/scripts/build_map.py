#!/usr/bin/env python3
"""Build a Code-format CX journey map ("customer journey full detail") from a JSON spec.

Usage:
    python3 build_map.py map.json OUT.dc.html              # Design canvas artboard (default)
    python3 build_map.py map.json OUT.html --standalone    # plain HTML page

Every card is written as literal markup (no template holes), so text stays
editable when the artboard is opened on a Design canvas.
See references/map-spec.md for the JSON format.
"""
import html, json, re, sys

COL, GAP, LABEL_W = 200, 8, 170
def span(n): return n * COL + (n - 1) * GAP
def e(s): return html.escape(str(s), quote=True)

C = {
    'objective': '#8fa14b', 'stage': '#f6a541', 'funnel_label': '#6e2c6b', 'funnel': '#a0779f',
    'label': '#545454', 'teal': '#1d7b8c', 'purple': '#6e2c6b', 'ink': '#1f1d2b', 'muted': '#4d4a57',
    'pos': '#c5cf9e', 'pos_bar': '#93a44e', 'pain': '#df8689', 'pain_bar': '#c1272d',
    'known': '#e8912d', 'needed': '#c1272d', 'hmw': '#ffeb7a', 'comms': '#6f9384',
    'tag': '#b83a14', 'cell': '#f2f2f0', 'cell_focus': '#f1edf3', 'green': '#93a44e',
}
ROW = 'display: flex; gap: 8px; align-items: stretch'
TAG_RE = re.compile(r'^(P\d+)\|(.*)$', re.S)


def badge(tag):
    return (f'<span style="display: inline-block; font-size: 10px; font-weight: 800; letter-spacing: 0.04em; '
            f'padding: 1px 6px; margin-right: 6px; background: {C["tag"]}; color: #ffffff; border-radius: 3px">{e(tag)}</span>')


def tx(t):
    """Text with an optional participant tag prefix, e.g. 'P1|Found the form easy'."""
    m = TAG_RE.match(str(t))
    return badge(m.group(1)) + e(m.group(2)) if m else e(t)


def build(spec, standalone=False):
    steps = spec['steps']
    N = len(steps)
    W = LABEL_W + GAP + span(N) + 96
    scope = spec.get('scope')
    focus = set(range(scope['from'], scope['to'] + 1)) if scope else set()
    profiles = spec.get('profiles', {})
    flow_cfg = spec.get('flow')

    def bg(n): return C['cell_focus'] if n in focus else C['cell']

    def label(t, sub=None, color=None):
        col = color or C['label']
        base = (f'width: {LABEL_W}px; flex: none; background: {col}; color: #ffffff; font-size: 20px; font-weight: 600; '
                f'padding: 18px 16px; box-sizing: border-box; display: flex; flex-direction: column; gap: 6px')
        s = f'<span style="font-size: 12px; font-weight: 400">{e(sub)}</span>' if sub else ''
        return f'<div style="{base}">{e(t)}{s}</div>'

    def row(lbl, minh, fn, sub=None):
        parts = [label(lbl, sub)]
        for i, st in enumerate(steps):
            parts.append(f'<div style="width: {COL}px; flex: none; background: {bg(i+1)}; padding: 10px 8px; box-sizing: border-box; '
                         f'display: flex; flex-direction: column; gap: 8px; min-height: {minh}px">{fn(st, i+1)}</div>')
        return f'<div style="{ROW}">' + ''.join(parts) + '</div>\n'

    def stage_row(lbl, sub, fn, color):
        parts = [label(lbl, sub, color)]
        for sg in spec['stages']:
            parts.append(fn(sg))
        return f'<div style="{ROW}">' + ''.join(parts) + '</div>\n'

    out = []
    w = out.append

    # ---- header ----
    hb = spec.get('badge', {})
    prof_lines = ''.join(
        f'<div style="display: flex; align-items: center; gap: 8px"><span style="display: inline-block; width: 14px; height: 14px; background: {p["color"]}"></span>'
        f'<span>{e(p["name"])}{": " + e(p["desc"]) if p.get("desc") else ""}</span></div>'
        for k, p in profiles.items() if not p.get('participant'))
    prof_box = ''
    if prof_lines:
        prof_box = (f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 14px 18px; border: 1px solid #d6d3d8; border-radius: 8px; font-size: 13px; min-width: 300px">'
                    f'<strong style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: {C["muted"]}">{e(spec.get("profiles_title", "Mindset profiles"))}</strong>'
                    f'{prof_lines}<span style="font-size: 12px; color: {C["muted"]}">{e(spec.get("profiles_note", ""))}</span></div>')
    tag_line = ''
    for tag, desc in spec.get('participants', {}).items():
        tag_line += f'<div style="display: flex; align-items: center; gap: 8px">{badge(tag)}<span>{e(desc)}</span></div>'
    w(f'''<div style="display: flex; align-items: center; gap: 40px; padding-bottom: 36px">
<div style="display: flex; flex-direction: column; gap: 4px; padding: 14px 22px; background: {C["ink"]}; color: #ffffff; border-radius: 10px"><span style="font-size: 30px; font-weight: 800">{e(hb.get("top", spec.get("client", "")))}</span><span style="font-size: 12px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase">{e(hb.get("sub", ""))}</span></div>
<div style="width: 2px; height: 90px; background: #d6d3d8"></div>
<div style="display: flex; flex-direction: column; gap: 8px"><h1 style="margin: 0; font-size: 60px; font-weight: 700; letter-spacing: -0.02em">{e(spec.get("title", "Customer journey full detail"))}</h1><p style="margin: 0; font-size: 20px; color: {C["muted"]}">{e(spec.get("subtitle", ""))}</p></div>
<div style="margin-left: auto; display: flex; gap: 14px; align-items: stretch">
<div style="display: flex; flex-direction: column; gap: 8px; padding: 14px 18px; border: 1px solid #d6d3d8; border-radius: 8px; font-size: 13px; min-width: 300px">
<strong style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: {C["muted"]}">Key</strong>
<div style="display: flex; align-items: center; gap: 8px"><span style="font-size: 22px; font-weight: 800; color: {C["known"]}">8%</span><span>Known data, with its source</span></div>
<div style="display: flex; align-items: center; gap: 8px"><span style="font-size: 22px; font-weight: 800; color: {C["needed"]}">?</span><span>Data needed: we don’t have it yet</span></div>
<div style="display: flex; align-items: center; gap: 8px"><span style="display: inline-block; width: 14px; height: 14px; background: {C["pos"]}"></span><span>Positive</span><span style="display: inline-block; width: 14px; height: 14px; background: {C["pain"]}; margin-left: 10px"></span><span>Pain</span></div>
<div style="display: flex; align-items: center; gap: 8px"><span style="display: inline-block; width: 14px; height: 14px; background: #d8ecf0; border: 1px solid {C["teal"]}"></span><span>Research we need to run</span></div>
{tag_line}
</div>{prof_box}</div></div>
''')

    # ---- CX objective (stages) ----
    def stage_cell(sg):
        return (f'<div style="width: {span(sg["steps"])}px; flex: none; background: {C["stage"]}; color: {C["ink"]}; font-size: 20px; font-weight: 700; '
                f'display: flex; align-items: center; padding: 0 20px; box-sizing: border-box; min-height: 52px; '
                f'clip-path: polygon(0 0, calc(100% - 18px) 0, 100% 50%, calc(100% - 18px) 100%, 0 100%, 18px 50%)">{e(sg["name"])}</div>')
    obj_label = (f'<div style="width: {LABEL_W}px; flex: none; background: {C["objective"]}; color: #ffffff; font-size: 18px; font-weight: 600; '
                 f'display: flex; align-items: center; padding: 0 16px; box-sizing: border-box; min-height: 52px">CX objective</div>')
    w(f'<div style="{ROW}">' + obj_label + ''.join(stage_cell(sg) for sg in spec['stages']) + '</div>\n')

    # ---- funnel / subscription stage band (optional) ----
    if spec.get('funnel'):
        parts = [f'<div style="width: {LABEL_W}px; flex: none; background: {C["funnel_label"]}; color: #ffffff; font-size: 17px; font-weight: 600; display: flex; align-items: center; padding: 10px 16px; box-sizing: border-box; min-height: 64px">{e(spec.get("funnel_title", "Funnel stage"))}</div>']
        for f in spec['funnel']:
            parts.append(f'<div style="width: {span(f["steps"])}px; flex: none; background: {C["funnel"]}; color: #ffffff; display: flex; flex-direction: column; justify-content: center; padding: 8px 16px; box-sizing: border-box; min-height: 64px; gap: 2px"><span style="font-size: 15px; font-weight: 700">{e(f["name"])}</span><span style="font-size: 12px">{e(f.get("desc", ""))}</span></div>')
        w(f'<div style="{ROW}">' + ''.join(parts) + '</div>\n')

    # ---- scope band (optional) ----
    if scope:
        pre = scope['from'] - 1
        pre_div = f'<div style="width: {span(pre)}px; flex: none"></div>' if pre > 0 else ''
        w(f'<div style="{ROW}"><div style="width: {LABEL_W}px; flex: none"></div>{pre_div}<div style="width: {span(scope["to"]-scope["from"]+1)}px; flex: none; border: 2px dashed {C["purple"]}; color: {C["purple"]}; font-size: 15px; font-weight: 700; display: flex; align-items: center; justify-content: center; padding: 8px; box-sizing: border-box; background: #f5eef5">{e(scope["label"])}</div></div>\n')

    # ---- customer steps ----
    w(row('Customer steps', 0, lambda st, n: (
        f'<div style="background: #ffffff; border-left: 4px solid {C["purple"]}; display: flex; flex-direction: column">'
        f'<div style="padding: 10px 10px 12px; font-size: 13px; line-height: 1.35; font-weight: 500"><span style="color: {C["purple"]}; font-weight: 800">{n} </span>{tx(st["title"])}</div>'
        f'<div style="background: #e2d8e2; padding: 4px 10px; font-size: 11px; font-weight: 600; color: #4a1d48">{e(st.get("who", ""))}</div></div>')))

    # ---- flow row ----
    if flow_cfg is not None:
        w(flow_row(flow_cfg, N, focus))

    # ---- data ----
    def fn_data(st, n):
        o = ''
        for d in st.get('data', []):
            if d.get('needed'):
                o += (f'<div style="background: #f7eef0; border: 1px dashed {C["needed"]}; padding: 10px; display: flex; flex-direction: column; gap: 4px">'
                      f'<span style="font-size: 12px; font-weight: 600; line-height: 1.3">{tx(d["label"])}</span>'
                      f'<span style="font-size: 26px; font-weight: 800; color: {C["needed"]}; line-height: 1.1">?</span>'
                      f'<span style="font-size: 10px; color: #8a1c21; font-weight: 600">Data needed</span></div>')
            else:
                o += (f'<div style="background: #ffffff; border: 1px solid {C["ink"]}; box-shadow: 3px 3px 0 #d6d3d8; padding: 10px; display: flex; flex-direction: column; gap: 4px">'
                      f'<span style="font-size: 12px; font-weight: 600; line-height: 1.3">{tx(d["label"])}</span>'
                      f'<span style="font-size: 26px; font-weight: 800; color: {C["known"]}; line-height: 1.1">{e(d["value"])}</span>'
                      f'<span style="font-size: 10px; color: {C["muted"]}">{e(d.get("source", ""))}</span></div>')
        return o
    w(row('Data', 160, fn_data, 'Known numbers and the data we still need'))

    tri_up = '<svg width="12" height="10" viewBox="0 0 12 10" aria-hidden="true"><path d="M6 0 L12 10 L0 10 Z" fill="#e4eacb"></path></svg>'
    tri_dn = '<svg width="12" height="10" viewBox="0 0 12 10" aria-hidden="true"><path d="M0 0 L12 0 L6 10 Z" fill="#f2c4c6"></path></svg>'
    w(row('Positives', 120, lambda st, n: ''.join(
        f'<div style="display: flex; background: {C["pos"]}"><div style="width: 22px; flex: none; background: {C["pos_bar"]}; display: flex; align-items: center; justify-content: center">{tri_up}</div><div style="padding: 10px; font-size: 12px; line-height: 1.35">{tx(p)}</div></div>'
        for p in st.get('positives', []))))
    w(row('Customer pains', 160, lambda st, n: ''.join(
        f'<div style="display: flex; background: {C["pain"]}"><div style="width: 22px; flex: none; background: {C["pain_bar"]}; display: flex; align-items: center; justify-content: center">{tri_dn}</div><div style="padding: 10px; font-size: 12px; line-height: 1.35">{tx(p)}</div></div>'
        for p in st.get('pains', []))))

    mag = ('<svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true"><circle cx="6.5" cy="6.5" r="5" fill="none" stroke="#6e2c6b" stroke-width="2"></circle>'
           '<path d="M10.5 10.5 L15 15" stroke="#6e2c6b" stroke-width="2"></path></svg>')
    if any(st.get('internal') for st in steps):
        w(row('Internal challenges', 140, lambda st, n: ''.join(
            f'<div style="background: #ffffff; border-left: 4px solid {C["purple"]}; display: flex; flex-direction: column"><div style="padding: 10px; display: flex; flex-direction: column; gap: 6px">{mag}<span style="font-size: 12px; line-height: 1.35">“{e(q["quote"])}”</span></div>'
            f'<div style="background: #efe8ef; padding: 4px 10px; font-size: 10px; font-weight: 600; color: #4a1d48">{e(q.get("source", ""))}</div></div>'
            for q in st.get('internal', [])), spec.get('internal_subtitle', 'What stakeholders say')))

    def fn_comms(st, n):
        o = ''
        for c in st.get('comms', []):
            if c.get('missing'):
                o += (f'<div style="border: 2px dashed {C["needed"]}; display: flex; flex-direction: column; background: #fbf3f4"><div style="padding: 10px; font-size: 12px; font-weight: 600; line-height: 1.3; color: #8a1c21">{tx(c["text"])}</div>'
                      f'<div style="background: {C["needed"]}; color: #ffffff; padding: 4px 10px; font-size: 11px; font-weight: 600">{e(c.get("channel", "Gap"))}</div></div>')
            else:
                o += (f'<div style="border: 1px solid #3f5f53; display: flex; flex-direction: column; background: #ffffff"><div style="padding: 10px; font-size: 12px; font-weight: 600; line-height: 1.3">{tx(c["text"])}</div>'
                      f'<div style="background: {C["comms"]}; color: #ffffff; padding: 4px 10px; font-size: 11px; font-weight: 600">{e(c.get("channel", ""))}</div></div>')
        return o
    w(row('Comms', 100, fn_comms))

    def fn_mind(st, n):
        o = ''
        for m in st.get('mindset', []):
            p = profiles.get(m.get('profile'), {'name': m.get('profile', ''), 'color': C['label']})
            o += (f'<div style="background: #ffffff; border: 1px solid {C["purple"]}; display: flex; flex-direction: column"><div style="padding: 10px; display: flex; flex-direction: column; gap: 4px; align-items: center; text-align: center">'
                  f'<span style="font-size: 22px; font-weight: 800; color: {p["color"]}; line-height: 0.8">“</span><span style="font-size: 12px; line-height: 1.35">{e(m["quote"])}</span>'
                  f'<span style="font-size: 10px; color: {C["muted"]}">{e(m.get("source", ""))}</span></div>'
                  f'<div style="background: {p["color"]}; color: #ffffff; padding: 5px 8px; font-size: 10px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; text-align: center">{e(p["name"])}</div></div>')
        return o
    w(row('Mindset thinking', 130, fn_mind, 'Real quotes, each with its source'))

    # ---- evidence + research (per stage) ----
    def ev_cell(sg):
        chips = ''.join(f'<span style="font-size: 11px; font-weight: 600; padding: 4px 8px; border-radius: 999px; background: #ffffff; border: 1px solid {C["teal"]}; color: #134f5a">{e(x)}</span>' for x in sg.get('evidence', []))
        ue = sg.get('user_evidence', 'No user evidence')
        ucol = C['tag'] if TAG_RE.search(ue) or 'interview' in ue.lower() else C['needed']
        chips += f'<span style="font-size: 11px; font-weight: 700; padding: 4px 8px; border-radius: 999px; background: {ucol}; color: #ffffff">{e(ue)}</span>'
        return (f'<div style="width: {span(sg["steps"])}px; flex: none; background: #eef6f8; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; gap: 8px">'
                f'<div style="display: flex; flex-wrap: wrap; gap: 6px">{chips}</div>'
                f'<p style="margin: 0; font-size: 12px; line-height: 1.35; color: #134f5a"><strong>Confidence: {e(sg.get("confidence", "low"))}.</strong> {e(sg.get("note", ""))}</p></div>')
    w(stage_row('Evidence', 'What this stage is built on today', ev_cell, C['teal']))

    pcol = {'High': C['needed'], 'Medium': '#a1640b', 'Low': C['muted']}
    def res_cell(sg):
        cards = ''.join(
            f'<div style="width: 192px; background: #d8ecf0; border: 1px solid {C["teal"]}; display: flex; flex-direction: column"><div style="padding: 10px; display: flex; flex-direction: column; gap: 6px">'
            f'<span style="font-size: 10px; font-weight: 800; letter-spacing: 0.06em; text-transform: uppercase; color: {pcol.get(r.get("priority", "Low"), C["muted"])}">{e(r.get("priority", "Low"))} priority</span>'
            f'<span style="font-size: 12px; font-weight: 700; line-height: 1.3">{e(r["question"])}</span></div>'
            f'<div style="background: {C["teal"]}; color: #ffffff; padding: 5px 10px; font-size: 11px; font-weight: 600; line-height: 1.3">{e(r.get("method", ""))}</div></div>'
            for r in sg.get('research', []))
        return (f'<div style="width: {span(sg["steps"])}px; flex: none; background: #eef6f8; padding: 12px; box-sizing: border-box; display: flex; flex-wrap: wrap; gap: 8px; align-content: flex-start; min-height: 200px">{cards}</div>')
    w(stage_row('Research needed', 'Gaps to close, with the method and priority', res_cell, C['teal']))

    w(row('HMW', 150, lambda st, n: ''.join(
        f'<div style="background: {C["hmw"]}; padding: 12px; font-size: 12px; line-height: 1.4; box-shadow: 2px 3px 0 #e2cc55"><strong>How might we</strong> {tx(h)}</div>'
        for h in st.get('hmw', []))))

    if spec.get('footnote'):
        w(f'<p style="margin: 18px 0 0; font-size: 13px; color: {C["muted"]}; max-width: 1400px">{e(spec["footnote"])}</p>\n')

    body = ''.join(out)
    root = (f'<div style="width: {W}px; box-sizing: border-box; padding: 64px 48px; background: #ffffff; '
            f"font-family: Figtree, 'Helvetica Neue', Arial, sans-serif; color: {C['ink']}; display: flex; flex-direction: column; gap: 10px\">\n{body}</div>")
    font = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&amp;display=swap">'
    title = e(spec.get('page_title', (spec.get('client', '') + ' journey full detail').strip()))
    if standalone:
        return (f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>{title}</title>\n{font}\n'
                f'<style>body{{margin:0;background:#ffffff}}</style>\n</head>\n<body>\n<div style="overflow-x: auto">{root}</div>\n</body>\n</html>\n')
    est_h = spec.get('height', 3200)
    return (f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>{title}</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n'
            f'<helmet>\n{font}\n<style>\nbody{{margin:0;background:#ffffff}}\na{{color:#6e2c6b}}a:hover{{color:#4a1d48}}\n</style>\n</helmet>\n{root}\n</x-dc>\n'
            f'<script type="text/x-dc" data-dc-script data-props=\'{{"$preview":{{"width":{W},"height":{est_h}}}}}\'>\n'
            'class Component extends DCLogic {\n  renderVals() {\n    return {};\n  }\n}\n</script>\n</body>\n</html>\n')


def flow_row(cfg, N, focus):
    """Main path line with numbered nodes, plus exits, loops and gaps, drawn as separate elements."""
    def X(n): return (n - 1) * (COL + GAP) + COL // 2
    LINE_Y = 64
    COLORS = {'tag': C['tag'], 'reentry': C['teal'], 'positive': C['green'], 'neutral': C['purple'], 'exit': C['needed']}
    fl = []
    fa = fl.append

    def up(x, y, c):
        fa(f'<div style="position: absolute; left: {x-6}px; top: {y}px; width: 0; height: 0; border-left: 6px solid transparent; border-right: 6px solid transparent; border-bottom: 9px solid {c}"></div>')

    def vline(x, y1, y2, c):
        fa(f'<div style="position: absolute; left: {x-1}px; top: {y1}px; width: 0; height: {y2-y1}px; border-left: 2px dashed {c}"></div>')

    def pill(xc, y, wdt, c, bgc, text):
        fa(f'<div style="position: absolute; left: {xc - wdt//2}px; top: {y}px; width: {wdt}px; box-sizing: border-box; padding: 6px 8px; border: 2px solid {c}; '
           f'background: {bgc}; font-size: 11px; font-weight: 700; line-height: 1.3; color: {C["ink"]}; text-align: center; border-radius: 6px">{tx(text)}</div>')

    # columns
    for n in range(1, N + 1):
        cbg = C['cell_focus'] if n in focus else C['cell']
        fa(f'<div style="position: absolute; left: {(n-1)*(COL+GAP)}px; top: 0; width: {COL}px; height: 100%; background: {cbg}"></div>')

    # loops: assign lanes so overlapping ranges get different heights
    loops = cfg.get('loops', [])
    lanes = []
    max_lane = 0
    for lp in loops:
        a, b = X(lp['from']), X(lp['to'])
        if lp['from'] == lp['to']:
            a, b = a - 70, a + 70
        lane = 0
        while any(not (b < la or a > lb) and ln == lane for la, lb, ln in lanes):
            lane += 1
        lanes.append((a, b, lane))
        max_lane = max(max_lane, lane)
        h = 110 + lane * 60
        c = COLORS.get(lp.get('kind', 'neutral'), C['purple'])
        fa(f'<div style="position: absolute; left: {a-1}px; top: {LINE_Y+14}px; width: {b-a}px; height: {h}px; border: 2px dashed {c}; border-top: none; border-radius: 0 0 14px 14px"></div>')
        up(a, LINE_Y + 12, c)
        if lp.get('both_ends'):
            up(b, LINE_Y + 12, c)
        fa(f'<div style="position: absolute; left: {a+10}px; top: {LINE_Y+14+h-46}px; width: {b-a-20}px; box-sizing: border-box; font-size: 11px; font-weight: 700; line-height: 1.3; '
           f'color: {c}; text-align: center; background: rgba(255,255,255,0.85); padding: 2px 4px">{tx(lp["label"])}</div>')

    # main line + nodes
    fa(f'<div style="position: absolute; left: {X(1)}px; top: {LINE_Y}px; width: {X(N)-X(1)+40}px; height: 0; border-top: 2px dashed {C["purple"]}"></div>')
    fa(f'<div style="position: absolute; left: {X(N)+38}px; top: {LINE_Y-6}px; width: 0; height: 0; border-top: 7px solid transparent; border-bottom: 7px solid transparent; border-left: 11px solid {C["purple"]}"></div>')
    for n in range(1, N + 1):
        nb = C['purple'] if (not focus or n in focus) else C['funnel']
        fa(f'<div style="position: absolute; left: {X(n)-12}px; top: {LINE_Y-11}px; width: 24px; height: 24px; border-radius: 50%; background: {nb}; color: #ffffff; '
           f'font-size: 11px; font-weight: 800; display: flex; align-items: center; justify-content: center">{n}</div>')

    # gaps (shown above the line)
    for g in cfg.get('gaps', []):
        a, b = X(g['from']), X(g['to'])
        fa(f'<div style="position: absolute; left: {a+24}px; top: 8px; width: {max(b-a-48, 160)}px; box-sizing: border-box; padding: 5px 8px; border: 2px dashed {C["tag"]}; '
           f'background: #fbeee9; font-size: 11px; font-weight: 700; color: {C["ink"]}; text-align: center; border-radius: 6px">{tx(g["label"])}</div>')

    # exits
    for ex in cfg.get('exits', []):
        x = X(ex['step'])
        if ex.get('above'):
            vline(x, 38, LINE_Y - 12, C['needed'])
            pill(x, 4, 190, C['needed'], '#fbf3f4', ex['label'])
        else:
            vline(x, LINE_Y + 14, LINE_Y + 34, C['needed'])
            pill(x, LINE_Y + 34, 180, C['needed'], '#fbf3f4', ex['label'])

    if cfg.get('end_label'):
        fa(f'<div style="position: absolute; left: {X(N)-150}px; top: {LINE_Y-34}px; width: 180px; font-size: 11px; font-weight: 700; color: {C["purple"]}; text-align: center">{e(cfg["end_label"])}</div>')

    flow_h = LINE_Y + 14 + 110 + max_lane * 60 + 30
    flow_h = max(flow_h, 200)
    lab = (f'<div style="width: {LABEL_W}px; flex: none; background: {C["label"]}; color: #ffffff; font-size: 20px; font-weight: 600; padding: 18px 16px; box-sizing: border-box; '
           f'display: flex; flex-direction: column; gap: 6px">Flow<span style="font-size: 12px; font-weight: 400">Main path, exits, loops and gaps</span></div>')
    return (f'<div style="{ROW}">{lab}<div style="width: {span(N)}px; flex: none; height: {flow_h}px; position: relative; background: #ffffff">'
            + ''.join(fl) + '</div></div>\n')


def validate(spec):
    errs = []
    n = len(spec.get('steps', []))
    if not n:
        errs.append('no steps')
    s = sum(sg.get('steps', 0) for sg in spec.get('stages', []))
    if s != n:
        errs.append(f'stages cover {s} steps but there are {n}')
    if spec.get('funnel'):
        f = sum(x.get('steps', 0) for x in spec['funnel'])
        if f != n:
            errs.append(f'funnel covers {f} steps but there are {n}')
    for k in ('exits', 'loops', 'gaps'):
        for it in (spec.get('flow') or {}).get(k, []):
            for key in ('step', 'from', 'to'):
                if key in it and not (1 <= it[key] <= n):
                    errs.append(f'flow {k} refers to step {it[key]}, outside 1..{n}')
    return errs


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    spec = json.load(open(sys.argv[1]))
    problems = validate(spec)
    if problems:
        print('Spec problems:\n- ' + '\n- '.join(problems))
        sys.exit(2)
    html_out = build(spec, standalone='--standalone' in sys.argv)
    open(sys.argv[2], 'w').write(html_out)
    needed = sum(1 for st in spec['steps'] for d in st.get('data', []) if d.get('needed'))
    print(f'Wrote {sys.argv[2]}: {len(spec["steps"])} steps, {len(spec["stages"])} stages, {needed} data-needed cards')
