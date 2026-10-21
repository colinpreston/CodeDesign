"""Code deck system: slide layouts for a Slides artifact (1920x1080, inline styles only).

Each function returns one <section> as a string. Write it to project/slides/<id>.html,
list the id in project/deck.json "order", and publish. Tokens and rules: ../references/deck-system.md.

Footer numbers: pass num as 'NN' and replace '>NN' with the slide's two-digit position once the order is final.
Highlight: wrap a phrase in **double stars** in a headline to set it in cornflower bold.

Example:
    from slides_house import *
    html = section_divider('div01', 'NN', '01', 'Revisiting the brief')
"""

NAVY = '#000050'; BODY = '#2A2F6E'; WHITE = '#FFFFFF'; PAGE = '#FFFFFF'
LIME = '#B0F467'; AQUA = '#93DFE3'; CYAN = '#00DBEE'; CORN = '#5465FF'
PERI = '#788BFF'; CORN_TEXT = '#3F4FE0'; DEEP = '#2D3BC7'; MUTED = '#5A5F8A'
PANEL = '#ECF1F4'; PALE = '#C9CDEF'
FONT = "'Poppins', Arial, sans-serif"

BASE = f"color:{NAVY};font-family:{FONT};"

DOTS = ('<svg aria-label="Dot texture" width="1920" height="1080" viewBox="0 0 1920 1080" '
        'style="position:absolute;left:0px;top:0px;width:1920px;height:1080px;opacity:0.5">'
        '<defs><pattern id="dots" width="36" height="36" patternUnits="userSpaceOnUse">'
        '<circle cx="18" cy="18" r="1.6" fill="#B9C2E6"/></pattern></defs>'
        '<rect width="1920" height="1080" fill="url(#dots)"/></svg>')


def glow(left, top, w, h, stops, at='50% 50%'):
    """A soft gradient orb. stops: list of (colour, pct)."""
    s = ', '.join(f'{c} {p}%' for c, p in stops)
    return (f'<div style="position:absolute;left:{left}px;top:{top}px;width:{w}px;height:{h}px;'
            f'background:radial-gradient(circle at {at}, {s});filter:blur(20px)"></div>')


T = 'rgba(255,255,255,0)'
GLOW_TR = glow(1100, 0, 820, 620, [(LIME, 0), (AQUA, 28), (PERI, 48), (T, 70)], '100% 0%')
GLOW_TR_SOFT = glow(1560, 0, 360, 260, [(AQUA, 0), (PERI, 40), (T, 72)], '100% 0%')
GLOW_BL = glow(0, 300, 1400, 780, [(CYAN, 0), (AQUA, 30), (T, 68)], '20% 90%')


def foot(num, src='', dark=False):
    c = PALE if dark else MUTED
    w = WHITE if dark else NAVY
    left = f'{num}' + (f' · {src}' if src else '')
    return (f'<p style="position:absolute;left:128px;bottom:56px;width:1300px;font-size:24px;color:{c}">{left}</p>'
            f'<p style="position:absolute;right:128px;bottom:48px;width:300px;text-align:right;font-size:40px;'
            f'font-weight:700;letter-spacing:-1px;color:{w}">Code</p>')


def notes(t):
    return f'<aside>{t}</aside>' if t else ''


def hl(text):
    """**word** -> highlighted span in deep cornflower bold."""
    import re
    return re.sub(r'\*\*(.+?)\*\*', rf'<span style="color:{CORN_TEXT}"><b>\1</b></span>', text)


def hl_on_dark(text):
    import re
    return re.sub(r'\*\*(.+?)\*\*', rf'<span style="color:{LIME}"><b>\1</b></span>', text)


def wash():
    """Blue gradient wash for cover, contents and statement slides. White text sits on the left (deep blue)."""
    return (f'background:linear-gradient(115deg, {DEEP} 0%, {CORN_TEXT} 40%, {CORN} 70%, {PERI} 100%);'
            + glow(1150, 0, 770, 560, [(AQUA, 0), (PERI, 40), ('rgba(120,139,255,0)', 72)], '100% 0%'))


def cover(sid, client, title_html, sub, note=''):
    return f'''<section id="{sid}" data-transition="fade" style="background:linear-gradient(115deg, {DEEP} 0%, {CORN_TEXT} 45%, {CORN} 75%, {PERI} 100%);{BASE}">
{glow(1200, 0, 720, 600, [(AQUA, 0), (PERI, 40), ('rgba(120,139,255,0)', 72)], '100% 0%')}
{glow(900, 560, 900, 520, [('#1E2AA8', 0), ('rgba(45,59,199,0)', 70)])}
<div style="position:absolute;left:128px;top:128px;width:720px;height:824px;background:{WHITE};border-radius:32px;display:flex;flex-direction:column;justify-content:center;gap:28px;padding:72px">
<p style="font-size:24px;font-weight:600;letter-spacing:4px;text-transform:uppercase;color:{NAVY}">{client}</p>
<h1 style="font-size:88px;font-weight:500;line-height:1.08;letter-spacing:-2px;color:{NAVY}">{title_html}</h1>
<p style="font-size:26px;line-height:1.4;color:{BODY}">{sub}</p>
</div>
<p style="position:absolute;left:1080px;top:400px;width:640px;font-size:180px;font-weight:700;letter-spacing:-6px;line-height:1;color:{WHITE}">Code</p>
<p style="position:absolute;left:1092px;top:600px;width:640px;font-size:36px;font-weight:600;color:{WHITE}">A WPP Media Brand</p>
{notes(note)}
</section>'''


def contents(sid, num, items, note=''):
    rows = ''.join(
        f'<div style="display:flex;flex-direction:row;gap:28px;border-top:1px solid rgba(255,255,255,0.35);padding:24px 0px 8px 0px">'
        f'<p style="width:64px;font-size:28px;font-weight:600;color:{WHITE}">{n}</p>'
        f'<div style="flex:1;display:flex;flex-direction:column;gap:6px"><p style="font-size:30px;font-weight:600;color:{WHITE}">{t}</p>'
        f'<p style="font-size:24px;line-height:1.35;color:{WHITE}">{d}</p></div></div>'
        for n, t, d in items)
    return f'''<section id="{sid}" data-transition="fade" style="background:linear-gradient(115deg, {DEEP} 0%, {CORN_TEXT} 55%, {CORN} 100%);{BASE}padding:128px 128px 160px;display:flex;flex-direction:row;gap:96px;align-items:center">
{glow(1300, 0, 620, 420, [(AQUA, 0), ('rgba(147,223,227,0)', 70)], '100% 0%')}
<h2 style="width:680px;font-size:84px;font-weight:300;line-height:1.1;letter-spacing:-2px;color:{WHITE}">What we’ll cover in this document</h2>
<div style="flex:1;display:flex;flex-direction:column;gap:12px">{rows}</div>
{foot(num, dark=True)}
{notes(note)}
</section>'''


def statement(sid, num, eyebrow, text, note='', src=''):
    return f'''<section id="{sid}" data-transition="fade" style="background:{PAGE};{BASE}padding:128px 260px 160px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:32px">
{DOTS}
<p style="font-size:24px;font-weight:500;color:{NAVY};text-align:center">{eyebrow}</p>
<h2 style="font-size:64px;font-weight:400;line-height:1.2;letter-spacing:-1px;text-align:center;color:{NAVY}">{hl(text)}</h2>
{foot(num, src)}
{notes(note)}
</section>'''


def section_divider(sid, num, n, title, note=''):
    return f'''<section id="{sid}" data-transition="fade" style="background:{PAGE};{BASE}">
{glow(0, 260, 1500, 820, [(CYAN, 0), (AQUA, 32), ('rgba(255,255,255,0)', 68)], '15% 85%')}
{glow(1150, 0, 770, 640, [(LIME, 0), (AQUA, 30), (PERI, 52), ('rgba(255,255,255,0)', 74)], '100% 0%')}
<p style="position:absolute;right:120px;top:40px;width:900px;text-align:right;font-size:360px;font-weight:500;letter-spacing:-12px;line-height:1;color:{NAVY}">{n}</p>
<p style="position:absolute;left:128px;top:470px;font-size:24px;font-weight:600;letter-spacing:4px;text-transform:uppercase;background:{WHITE};color:{NAVY};border:3px solid {LIME};border-radius:999px;padding:8px 28px">→  Section {n}</p>
<h2 style="position:absolute;left:128px;top:560px;width:1500px;font-size:150px;font-weight:500;line-height:1.0;letter-spacing:-5px;color:{NAVY}">{title}</h2>
{foot(num)}
{notes(note)}
</section>'''


def sub_divider(sid, num, pill, title, sub, extra='', note=''):
    """Smaller divider inside a section, e.g. one page of a site walk."""
    return f'''<section id="{sid}" data-transition="fade" style="background:{PAGE};{BASE}padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:28px">
{glow(1150, 0, 770, 640, [(AQUA, 0), (PERI, 40), ('rgba(255,255,255,0)', 72)], '100% 0%')}
<p style="font-size:24px;font-weight:600;letter-spacing:3px;text-transform:uppercase;background:{LIME};color:{NAVY};border-radius:999px;padding:8px 26px;align-self:flex-start">{pill}</p>
<h2 style="font-size:110px;font-weight:500;line-height:1.05;letter-spacing:-3px;width:1300px;color:{NAVY}">{title}</h2>
<p style="font-size:34px;font-weight:300;line-height:1.35;width:1200px;color:{BODY}">{sub}</p>
{extra}
{foot(num)}
{notes(note)}
</section>'''


def title_only(sid, num, eyebrow, head, body_html, right_html='', src='', note='', corner=True):
    """Left text column (eyebrow, light headline with highlights, body); evidence on the right."""
    return f'''<section id="{sid}" data-transition="fade" style="background:{PAGE};{BASE}padding:128px 128px 160px;display:flex;flex-direction:row;gap:80px;align-items:center">
{DOTS}
{GLOW_TR_SOFT if corner else ''}
<div style="width:700px;display:flex;flex-direction:column;gap:24px">
<p style="font-size:24px;font-weight:500;color:{NAVY}">{eyebrow}</p>
<h2 style="font-size:60px;font-weight:400;line-height:1.12;letter-spacing:-1px;color:{NAVY}">{hl(head)}</h2>
<div style="display:flex;flex-direction:column;gap:16px;font-size:24px;line-height:1.45;color:{BODY}">{body_html}</div>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:20px">{right_html}</div>
{foot(num, src)}
{notes(note)}
</section>'''


def key_insights(sid, num, title, items, cols=2, src='', note='', eyebrow=''):
    """Numbered insights: big light number, bold heading, short body."""
    cells = ''.join(
        f'<div style="display:flex;flex-direction:row;gap:24px"><p style="width:84px;font-size:64px;font-weight:300;line-height:1;color:{NAVY}">{n:02d}</p>'
        f'<div style="flex:1;display:flex;flex-direction:column;gap:8px"><h3 style="font-size:28px;font-weight:700;line-height:1.25;color:{NAVY}">{h}</h3>'
        f'<p style="font-size:24px;line-height:1.4;color:{BODY}">{b}</p></div></div>'
        for n, (h, b) in enumerate(items, 1))
    eb = f'<p style="font-size:24px;font-weight:500;color:{NAVY}">{eyebrow}</p>' if eyebrow else ''
    return f'''<section id="{sid}" data-transition="fade" style="background:{PAGE};{BASE}padding:112px 128px 160px;display:flex;flex-direction:column;gap:40px">
{DOTS}
{GLOW_TR_SOFT}
<div style="display:flex;flex-direction:column;gap:10px">{eb}<h2 style="font-size:60px;font-weight:400;line-height:1.12;letter-spacing:-1px;color:{NAVY}">{hl(title)}</h2></div>
<div style="display:grid;grid-template-columns:repeat({cols}, 1fr);gap:40px">{cells}</div>
{foot(num, src)}
{notes(note)}
</section>'''


def numbered_list(sid, num, title, items, src='', note=''):
    """Two-column list with hairlines, e.g. research scope."""
    cells = ''.join(
        f'<div style="display:flex;flex-direction:row;gap:24px;border-top:2px solid {NAVY};padding:18px 0px 0px 0px">'
        f'<p style="width:72px;font-size:48px;font-weight:300;line-height:1;color:{NAVY}">{n:02d}</p>'
        f'<div style="flex:1;display:flex;flex-direction:column;gap:6px"><h3 style="font-size:28px;font-weight:600;color:{NAVY}">{h}</h3>'
        f'<p style="font-size:24px;line-height:1.35;color:{BODY}">{b}</p></div></div>'
        for n, (h, b) in enumerate(items, 1))
    return f'''<section id="{sid}" data-transition="fade" style="background:{PAGE};{BASE}padding:112px 128px 160px;display:flex;flex-direction:column;gap:36px">
{DOTS}
<h2 style="font-size:60px;font-weight:400;line-height:1.12;letter-spacing:-1px;color:{NAVY}">{hl(title)}</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px 64px">{cells}</div>
{foot(num, src)}
{notes(note)}
</section>'''


def stat_panel(sid, num, stat, stat_label, eyebrow, head, body_html, src='', note=''):
    """Cornflower panel with a giant number on the left; text on the right."""
    return f'''<section id="{sid}" data-transition="fade" style="background:{PAGE};{BASE}">
{DOTS}
<div style="position:absolute;left:128px;top:96px;width:620px;height:840px;background:{CORN_TEXT};display:flex;flex-direction:column;justify-content:center;gap:20px;padding:64px">
<p style="font-size:150px;font-weight:400;letter-spacing:-4px;line-height:1;color:{WHITE}">{stat}</p>
<p style="font-size:28px;line-height:1.35;color:{WHITE}">{stat_label}</p>
</div>
<div style="position:absolute;left:840px;top:200px;width:952px;display:flex;flex-direction:column;gap:24px">
<p style="font-size:24px;font-weight:500;color:{NAVY}">{eyebrow}</p>
<h2 style="font-size:60px;font-weight:400;line-height:1.12;letter-spacing:-1px;color:{NAVY}">{hl(head)}</h2>
<div style="display:flex;flex-direction:column;gap:16px;font-size:24px;line-height:1.45;color:{BODY}">{body_html}</div>
</div>
{foot(num, src)}
{notes(note)}
</section>'''


def theme(sid, num, n, head, body, metrics, src='', note=''):
    """Theme opener: aqua-to-lime wash, big number, headline, body, 'Improved …' metrics."""
    mets = ''.join(f'<p style="font-size:26px;line-height:1.4;color:{NAVY}"><b>Improved</b> {m}</p>' for m in metrics)
    return f'''<section id="{sid}" data-transition="fade" style="background:linear-gradient(110deg, {AQUA} 0%, #BDEFD0 50%, {LIME} 100%);{BASE}padding:128px 128px 160px;display:flex;flex-direction:row;gap:56px;align-items:center">
{glow(1200, 0, 720, 520, [(PERI, 0), ('rgba(120,139,255,0)', 70)], '100% 0%')}
<p style="width:260px;font-size:220px;font-weight:400;letter-spacing:-8px;line-height:1;color:{NAVY}">{n}</p>
<div style="flex:1;display:flex;flex-direction:column;gap:28px">
<h2 style="font-size:64px;font-weight:400;line-height:1.12;letter-spacing:-1px;color:{NAVY}">{head}</h2>
<p style="font-size:26px;line-height:1.45;color:{NAVY}">{body}</p>
</div>
<div style="width:440px;display:flex;flex-direction:column;gap:8px">{mets}</div>
{foot(num, src)}
{notes(note)}
</section>'''


def recs_panel(sid, num, items, label='Recommendations', client='', note=''):
    """Dark panel listing a theme's recommendations, numbered."""
    cells = ''.join(
        f'<div style="display:flex;flex-direction:row;gap:24px"><p style="width:80px;font-size:56px;font-weight:300;line-height:1;color:{WHITE}">{n:02d}</p>'
        f'<p style="flex:1;font-size:28px;line-height:1.35;color:{WHITE}">{t}</p></div>'
        for n, t in enumerate(items, 1))
    tag = f'<p style="font-size:24px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:{LIME}">{client}</p>' if client else ''
    return f'''<section id="{sid}" data-transition="fade" style="background:{PAGE};{BASE}">
{DOTS}
<div style="position:absolute;left:128px;top:96px;width:1664px;height:800px;background:{NAVY};border-radius:24px;display:flex;flex-direction:column;justify-content:center;gap:48px;padding:80px 96px">
<p style="font-size:40px;font-weight:400;color:{WHITE}">{label}</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:48px 80px">{cells}</div>
{tag}
</div>
{foot(num)}
{notes(note)}
</section>'''


def rec_detail(sid, num, head, paras, card=None, src='', note=''):
    """One recommendation: dark panel with the headline, the case on the right, decision lines below."""
    body = ''.join(f'<p>{p}</p>' for p in paras)
    dl = ''
    if card:
        dl = (f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px 32px;border-top:2px solid {NAVY};padding:20px 0px 0px 0px">'
              + ''.join(f'<p style="font-size:24px;line-height:1.35;color:{NAVY}"><b>{k}:</b> {v}</p>' for k, v in card)
              + '</div>')
    return f'''<section id="{sid}" data-transition="fade" style="background:{PAGE};{BASE}">
{DOTS}
<div style="position:absolute;left:128px;top:96px;width:700px;height:800px;background:{NAVY};border-radius:24px;display:flex;flex-direction:column;justify-content:center;gap:28px;padding:72px">
<p style="font-size:24px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:{LIME}">Recommendation</p>
<h2 style="font-size:56px;font-weight:400;line-height:1.15;letter-spacing:-1px;color:{WHITE}">{head}</h2>
</div>
<div style="position:absolute;left:908px;top:120px;width:884px;display:flex;flex-direction:column;gap:28px">
<div style="display:flex;flex-direction:column;gap:18px;font-size:24px;line-height:1.45;color:{BODY}">{body}</div>
{dl}
</div>
{foot(num, src)}
{notes(note)}
</section>'''


def flow(sid, num, title, note=''):
    """Making research actionable: findings -> recommendations / principles -> solutions."""
    def box(l, t, w, head, txt, here=False):
        return (f'<div style="position:absolute;left:{l}px;top:{t}px;width:{w}px;display:flex;flex-direction:column;gap:8px;'
                f'background:{CORN_TEXT if not here else DEEP};border-radius:20px;padding:24px 28px">'
                f'<p style="font-size:26px;font-weight:700;color:{WHITE}">{head}</p><p style="font-size:24px;line-height:1.35;color:{WHITE}">{txt}</p></div>')
    return f'''<section id="{sid}" data-transition="fade" style="background:{PAGE};{BASE}">
{DOTS}
<h2 style="position:absolute;left:128px;top:96px;width:1200px;font-size:60px;font-weight:400;line-height:1.12;letter-spacing:-1px;color:{NAVY}">{hl(title)}</h2>
{box(128, 470, 440, 'Research findings', 'What we saw, heard and measured, against the brief')}
{box(700, 330, 500, 'Recommendations', 'The changes the evidence says will help most')}
{box(700, 640, 500, 'Themes', 'The few big problems the findings point to, to guide decisions')}
{box(1330, 470, 462, 'Solutions', 'Designed, tested and measured with you', here=True)}
<x-connector x1="568" y1="560" x2="700" y2="420" route="hv" head="end" style="color:{NAVY};border-width:3px"></x-connector>
<x-connector x1="568" y1="560" x2="700" y2="730" route="hv" head="end" style="color:{NAVY};border-width:3px"></x-connector>
<x-connector x1="1200" y1="420" x2="1330" y2="560" route="hv" head="end" style="color:{NAVY};border-width:3px"></x-connector>
<x-connector x1="1200" y1="730" x2="1330" y2="560" route="hv" head="end" style="color:{NAVY};border-width:3px"></x-connector>
<p style="position:absolute;left:700px;top:240px;width:500px;font-size:24px;font-weight:600;color:{CORN_TEXT}">↓  We are here</p>
{foot(num)}
{notes(note)}
</section>'''


def matrix(sid, num, title, quads, axis=('High effort', 'Low effort', 'High value', 'Low value'), note='', src=''):
    """Value against effort 2x2. quads: dict tl,tr,bl,br -> (label, sub, [items]). Left = high value, top = high effort.
    So bl (high value, low effort) is 'Do first'."""
    def q(l, t, key):
        lab, sub, items = quads[key]
        li = ''.join(f'<p style="font-size:24px;line-height:1.3;color:{BODY}">{x}</p>' for x in items)
        strong = key == 'bl'
        return (f'<div style="position:absolute;left:{l}px;top:{t}px;width:560px;height:300px;display:flex;flex-direction:column;gap:8px;'
                f'background:{WHITE};border:3px solid {CORN_TEXT if strong else PERI};border-radius:16px;padding:20px 24px">'
                f'<p style="font-size:26px;font-weight:700;color:{NAVY}">{lab} <span style="color:{CORN_TEXT}">· {sub}</span></p>{li}</div>')
    he, le, hv, lv = axis
    return f'''<section id="{sid}" data-transition="fade" style="background:{PAGE};{BASE}">
{DOTS}
<h2 style="position:absolute;left:128px;top:96px;width:440px;font-size:52px;font-weight:400;line-height:1.12;letter-spacing:-1px;color:{NAVY}">{hl(title)}</h2>
<div style="position:absolute;left:1214px;top:150px;width:3px;height:770px;background:{NAVY}"></div>
<div style="position:absolute;left:600px;top:540px;width:1192px;height:3px;background:{NAVY}"></div>
<p style="position:absolute;left:1066px;top:104px;width:300px;text-align:center;font-size:24px;font-weight:600">{he}</p>
<p style="position:absolute;left:1066px;top:924px;width:300px;text-align:center;font-size:24px;font-weight:600">{le}</p>
<p style="position:absolute;left:600px;top:500px;width:300px;font-size:24px;font-weight:600">← {hv}</p>
<p style="position:absolute;left:1492px;top:500px;width:300px;text-align:right;font-size:24px;font-weight:600">{lv} →</p>
{q(620, 180, 'tl')}{q(1232, 180, 'tr')}{q(620, 590, 'bl')}{q(1232, 590, 'br')}
<p style="position:absolute;left:128px;top:600px;width:440px;font-size:24px;line-height:1.4;color:{BODY}">Further left is more valuable; lower is less effort. Start bottom left.</p>
{foot(num, src)}
{notes(note)}
</section>'''


def exec_summary(sid, num, research, assets, opps, note=''):
    col = lambda h, inner: (f'<div style="flex:1;display:flex;flex-direction:column;gap:16px"><h3 style="font-size:32px;font-weight:500;color:{NAVY}">{h}</h3>'
                            f'<div style="flex:1;display:flex;flex-direction:column;gap:14px;background:{PANEL};border-radius:20px;padding:28px">{inner}</div></div>')
    r = ''.join(f'<div style="display:flex;flex-direction:column;gap:2px"><p style="font-size:26px;font-weight:600;color:{NAVY}">{a}</p><p style="font-size:24px;color:{BODY}">{b}</p></div>' for a, b in research)
    a = ''.join(f'<div style="display:flex;flex-direction:column;gap:2px"><p style="font-size:26px;font-weight:600;color:{NAVY}">{x}</p><p style="font-size:24px;color:{BODY}">{y}</p></div>' for x, y in assets)
    o = ''.join(f'<div style="display:flex;flex-direction:row;gap:16px;align-items:center"><p style="width:56px;font-size:36px;font-weight:300;color:{NAVY}">{n:02d}</p>'
                f'<p style="flex:1;font-size:24px;line-height:1.3;background:{NAVY};color:{WHITE};border-radius:12px;padding:14px 18px">{t}</p></div>' for n, t in enumerate(opps, 1))
    return f'''<section id="{sid}" data-transition="fade" style="background:{PAGE};{BASE}padding:112px 128px 160px;display:flex;flex-direction:column;gap:32px">
{DOTS}
<h2 style="font-size:60px;font-weight:500;letter-spacing:-1px;color:{CORN_TEXT}">Executive summary</h2>
<div style="display:flex;flex-direction:row;gap:32px">{col('Research', r)}{col('Assets', a)}{col('Opportunities', o)}</div>
{foot(num)}
{notes(note)}
</section>'''


def thanks(sid, head, body, contact, note=''):
    return f'''<section id="{sid}" data-transition="fade" style="background:linear-gradient(115deg, {DEEP} 0%, {CORN_TEXT} 45%, {CORN} 80%, {PERI} 100%);{BASE}padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:end;gap:24px">
{glow(1150, 0, 770, 560, [(AQUA, 0), (PERI, 40), ('rgba(120,139,255,0)', 72)], '100% 0%')}
<h2 style="font-size:110px;font-weight:400;letter-spacing:-3px;color:{WHITE}">{head}</h2>
<p style="font-size:30px;line-height:1.4;width:1100px;color:{WHITE}">{body}</p>
<p style="font-size:26px;color:{WHITE}">{contact}</p>
<p style="position:absolute;right:128px;bottom:48px;width:300px;text-align:right;font-size:40px;font-weight:700;letter-spacing:-1px;color:{WHITE}">Code</p>
{notes(note)}
</section>'''
