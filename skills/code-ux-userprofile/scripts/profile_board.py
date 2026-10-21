#!/usr/bin/env python3
"""Code proto-persona boards: push/pull forces profiles in the client's brand.

Usage:
    python3 profile_board.py spec.json [--out DIR] [--png]

Reads a JSON spec (see references/board-spec.md and assets/example-breitling.json) and writes,
for each profile:
    <out>/NN-<slug>.html     standalone page (Google Fonts linked), for review or rendering
    <out>/NN-<slug>.dc.html  artboard for a Claude Design canvas (first one: rename to Main.dc.html)
    <out>/NN-<slug>.png      with --png: 2x render for placing full-slide in a deck (needs playwright)

Board size defaults to 1600x1000. People in scenes should stay neutral (no age, gender or
ethnicity cues): this is a mindset artefact, not a demographic persona.
"""
import argparse, html, json, os, re, sys

DEFAULT_BRAND = {
    "primary": "#000050", "accent": "#B0F467", "accent_ink": "#000050", "ink": "#111820", "grey": "#4A5560",
    "line": "#C3C8CF", "bg": "#F2F3F5", "band": "#E4E7EB", "warn": "#8A1F1F",
    "head_font": "Poppins", "body_font": "Poppins", "head_upper": False,
    "fonts_href": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap",
}
DEFAULT_SOURCES = {
    "A": {"label": "Assumption", "style": "outline"},
    "D": {"label": "Desk research", "style": "primary"},
    "S": {"label": "Site walk", "style": "accent"},
    "I": {"label": "Interview", "style": "primary"},
    "Q": {"label": "Survey", "style": "primary"},
    "N": {"label": "Analytics", "style": "primary"},
}
DEFAULT_LABELS = {
    "goal": "Moving them to choose and commit", "back": "Holding them back",
    "tips": "What would tip them", "loses": "Where the experience loses them today",
    "job": "The job they’re hiring us for", "research": "Research to validate", "research_sub": "the why · ~10 people",
    "data": "Data to validate at scale", "data_sub": "how many · sizes the persona",
    "quote_note": "In their words · assumed; to be replaced with real interview quotes",
    "push": "Push", "pull": "Pull", "anxiety": "Anxiety", "habit": "Habit",
}

def esc(s): return html.escape(str(s))
def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

class Board:
    def __init__(self, spec):
        self.s = spec
        self.b = {**DEFAULT_BRAND, **spec.get("brand", {})}
        self.src = {**DEFAULT_SOURCES, **spec.get("sources", {})}
        self.L = {**DEFAULT_LABELS, **spec.get("labels", {})}
        self.W, self.H = spec.get("size", [1600, 1000])
        self.HEAD = f"'{self.b['head_font']}', Arial, sans-serif"
        self.BODY = f"'{self.b['body_font']}', Arial, sans-serif"
        self.UP = 'text-transform:uppercase;' if self.b.get("head_upper") else ''

    def tag(self, k):
        if not k: return ''
        b = self.b; t = self.src.get(k, {"label": k, "style": "outline"})
        st = {"outline": f'border:1px dashed {b["grey"]};color:{b["grey"]};background:#FFFFFF',
              "primary": f'background:{b["primary"]};color:#FFFFFF;border:1px solid {b["primary"]}',
              "accent": f'background:{b["accent"]};color:{b["accent_ink"]};border:1px solid {b["accent"]}'}[t.get("style", "outline")]
        return (f'<span style="display:inline-block;margin-left:6px;padding:0 6px;font:600 11px/17px {self.BODY};'
                f'letter-spacing:0.3px;text-transform:uppercase;vertical-align:1px;{st}">{esc(t["label"])}</span>')

    def items(self, lst):
        return ''.join(f'<li style="margin:0 0 7px 0;font:400 15px/21px {self.BODY};color:{self.b["ink"]}">{esc(t)}{self.tag(k)}</li>' for t, k in lst)

    def force(self, title, lst, col):
        return (f'<div style="flex:1;background:#FFFFFF;border:1px solid {self.b["line"]};border-top:5px solid {col};padding:14px 16px 8px">'
                f'<div style="font:700 24px/1 {self.HEAD};letter-spacing:1px;{self.UP}color:{col}">{esc(title)}</div><div style="height:8px"></div>'
                f'<ul style="margin:0;padding:0 0 0 18px">{self.items(lst)}</ul></div>')

    @staticmethod
    def arrow(d, col):
        path = 'M4 20h44M36 8l12 12-12 12' if d == 'r' else 'M52 20H8M20 8L8 20l12 12'
        return f'<svg width="56" height="40" viewBox="0 0 56 40" aria-hidden="true" style="flex:none;align-self:center"><path d="{path}" fill="none" stroke="{col}" stroke-width="4" stroke-linecap="square"/></svg>'

    def label(self, t, col, size=18):
        return f'<span style="font:700 {size}px/1 {self.HEAD};letter-spacing:1.5px;{self.UP}color:{col}">{esc(t)}</span>'

    def scene(self, p):
        if p.get("scene_svg"):
            return p["scene_svg"]
        b = self.b
        return (f'<div role="img" aria-label="Scene placeholder" style="width:270px;height:187px;background:{b["primary"]};display:flex;align-items:center;justify-content:center;'
                f'font:600 14px/20px {self.BODY};color:#FFFFFF;text-align:center;padding:16px;box-sizing:border-box">[Scene: {esc(p.get("moment", "their moment"))}]</div>')

    def render(self, n, total, p):
        b, L, s = self.b, self.L, self.s
        P, A, INK, G, LN, WARN = b["primary"], b["accent"], b["ink"], b["grey"], b["line"], b["warn"]
        conf = ''.join(f'<span style="width:34px;height:8px;background:{P if i < p.get("confidence", 1) else LN}"></span>' for i in range(4))
        legend = ''.join(self.tag(k) for k in s.get("legend", ["D", "S", "A"]))
        bul = lambda xs: ''.join(f'<li style="margin:0 0 6px;font:400 15px/21px {self.BODY};color:{INK}">{esc(t)}</li>' for t in xs)
        research = ''.join(
            f'<div style="display:flex;gap:10px;align-items:flex-start;background:#FFFFFF;border:1px solid {LN};padding:7px 12px">'
            f'<span style="flex:none;font:700 12px/20px {self.BODY};letter-spacing:0.5px;text-transform:uppercase;padding:0 7px;border:1px solid {P};color:{P}">{esc(r[2] if len(r) > 2 else "To do")}</span>'
            f'<div style="font:600 15px/20px {self.BODY};color:{INK}">{esc(r[0])} <span style="font-weight:400;color:{G}">· {esc(r[1])}</span></div></div>'
            for r in p.get("research", []))
        data = ''.join(
            f'<div style="display:flex;gap:10px;align-items:flex-start;background:#FFFFFF;border:1px solid {LN};padding:7px 12px">'
            f'<span style="flex:none;width:118px;font:700 11px/20px {self.BODY};letter-spacing:0.5px;text-transform:uppercase;color:#FFFFFF;background:{P};text-align:center">{esc(src)}</span>'
            f'<div style="font:600 15px/20px {self.BODY};color:{INK}">{esc(m)}</div></div>' for m, src in p.get("data", []))
        quote = ''
        if p.get("quote"):
            quote = (f'<div style="display:flex;gap:10px;margin-top:12px"><span style="font:700 54px/0.9 {self.HEAD};color:{A}">“</span><div>'
                     f'<div style="font:italic 600 17px/24px {self.BODY};color:{P}">{esc(p["quote"])}</div>'
                     f'<div style="font:400 12px/16px {self.BODY};color:{G};margin-top:4px">{esc(p.get("quote_note", L["quote_note"]))}</div></div></div>')
        return f'''<div style="width:{self.W}px;height:{self.H}px;position:relative;overflow:hidden;background:{b["bg"]};font-family:{self.BODY};color:{INK};display:flex;flex-direction:column">
<div style="background:{P};color:#FFFFFF;height:40px;padding:0 28px;display:flex;align-items:center;justify-content:space-between">
<span style="font:600 13px/1 {self.BODY};letter-spacing:2px;text-transform:uppercase">{esc(s.get("client", ""))} · proto-persona {n:02d} of {total:02d} · {esc(s.get("version", "v0.1"))}, {esc(s.get("date", ""))}</span>
<span style="font:600 13px/1 {self.BODY}">Sources: {legend}</span></div>
<div style="background:#FFFFFF;padding:16px 28px;display:flex;gap:24px;align-items:stretch;border-bottom:1px solid {LN}">
<div style="width:270px;flex:none;display:flex;flex-direction:column;gap:6px">{self.scene(p)}<div style="font:600 13px/17px {self.BODY};color:{G}">{esc(p.get("moment", ""))}</div></div>
<div style="width:500px;flex:none;display:flex;flex-direction:column;justify-content:center">
<div style="font:600 13px/1 {self.BODY};letter-spacing:2px;text-transform:uppercase;color:{G}">{esc(p.get("type", "Mindset"))} · {esc(p.get("often", ""))}</div>
<div style="font:700 46px/1 {self.HEAD};letter-spacing:0.5px;{self.UP}color:{P};margin-top:8px">{esc(p["name"])}</div>
<div style="font:400 16px/22px {self.BODY};color:{INK};margin-top:8px">{esc(p.get("who", ""))}</div>{quote}</div>
<div style="flex:1;display:flex;flex-direction:column;gap:12px">
<div style="flex:1;background:{A};padding:16px 20px;display:flex;flex-direction:column;justify-content:center">
{self.label(L["job"], b["accent_ink"])}
<div style="font:600 17px/24px {self.BODY};color:{b["accent_ink"]};margin-top:8px">{esc(p.get("job", ""))}</div></div>
<div style="display:flex;align-items:center;gap:12px">{self.label("Confidence", P)}<span style="display:flex;gap:4px">{conf}</span><span style="font:400 13px/17px {self.BODY};color:{G}">{esc(p.get("confidence_note", ""))}</span></div>
</div></div>
<div style="flex:1;padding:16px 28px 0;display:flex;gap:20px;min-height:0">
<div style="flex:1;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;align-items:center;gap:10px">{self.label(L["goal"], P)}<span style="flex:1;height:1px;background:{LN}"></span></div>
<div style="display:flex;gap:10px">{self.force(L["push"], p.get("push", []), P)}{self.arrow("r", P)}{self.force(L["pull"], p.get("pull", []), P)}{self.arrow("r", P)}
<div style="width:140px;box-sizing:border-box;flex:none;background:{P};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:10px"><span style="font:700 26px/1 {self.HEAD};{self.UP}color:{A}">Choose</span><span style="font:600 13px/18px {self.BODY};color:#FFFFFF;margin:4px 0">and</span><span style="font:700 26px/1 {self.HEAD};{self.UP}color:{A}">Commit</span></div></div>
<div style="display:flex;align-items:center;gap:10px">{self.label(L["back"], WARN)}<span style="flex:1;height:1px;background:{LN}"></span></div>
<div style="display:flex;gap:10px">{self.force(L["anxiety"], p.get("anxiety", []), WARN)}{self.arrow("l", WARN)}{self.force(L["habit"], p.get("habit", []), WARN)}{self.arrow("l", WARN)}<div style="width:140px;flex:none"></div></div>
</div>
<div style="width:330px;display:flex;flex-direction:column;gap:12px">
<div style="background:#FFFFFF;border:1px solid {LN};border-left:6px solid {A};padding:14px 16px">{self.label(L["tips"], P, 20)}<ul style="margin:10px 0 0;padding:0 0 0 18px">{bul(p.get("tips", []))}</ul></div>
<div style="background:#FFFFFF;border:1px solid {LN};border-left:6px solid {WARN};padding:14px 16px">{self.label(L["loses"], WARN, 20)}<ul style="margin:10px 0 0;padding:0 0 0 18px">{bul(p.get("loses", []))}</ul></div>
</div></div>
<div style="margin-top:14px;background:{b["band"]};padding:12px 28px 16px;display:flex;gap:20px">
<div style="flex:1;display:flex;flex-direction:column;gap:8px"><div style="display:flex;align-items:baseline;gap:12px">{self.label(L["research"], P, 20)}<span style="font:400 14px/1 {self.BODY};color:{G}">{esc(L["research_sub"])}</span></div>{research}</div>
<div style="flex:1;display:flex;flex-direction:column;gap:8px"><div style="display:flex;align-items:baseline;gap:12px">{self.label(L["data"], P, 20)}<span style="font:400 14px/1 {self.BODY};color:{G}">{esc(L["data_sub"])}</span></div>{data}</div>
</div></div>'''

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec"); ap.add_argument("--out", default="profiles"); ap.add_argument("--png", action="store_true")
    a = ap.parse_args()
    spec = json.load(open(a.spec, encoding="utf-8"))
    bd = Board(spec); os.makedirs(a.out, exist_ok=True)
    href = esc(bd.b["fonts_href"]); written = []
    profiles = spec["profiles"]
    for i, p in enumerate(profiles, 1):
        body = bd.render(i, len(profiles), p)
        name = f"{i:02d}-{slug(p['name'])}"
        page = (f'<!doctype html><html lang="{spec.get("lang", "en")}"><head><meta charset="utf-8"><title>{esc(p["name"])}</title>'
                f'<link rel="stylesheet" href="{href}"><style>body{{margin:0}}</style></head><body>{body}</body></html>')
        open(f"{a.out}/{name}.html", "w", encoding="utf-8").write(page)
        dc = f'''<!doctype html>
<html lang="{spec.get("lang", "en")}">
<head>
<meta charset="utf-8">
<title>Proto-persona {i:02d} · {esc(p["name"])}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="{href}">
<style>body{{margin:0;background:{bd.b["bg"]}}}</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{bd.W},"height":{bd.H}}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
        open(f"{a.out}/{name}.dc.html", "w", encoding="utf-8").write(dc)
        written.append(name)
    if a.png:
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            sys.exit("--png needs playwright: pip install playwright && playwright install chromium")
        with sync_playwright() as pw:
            br = pw.chromium.launch(); pg = br.new_page(viewport={"width": bd.W, "height": bd.H}, device_scale_factor=2)
            for name in written:
                pg.goto("file://" + os.path.abspath(f"{a.out}/{name}.html")); pg.wait_for_timeout(800)
                pg.screenshot(path=f"{a.out}/{name}.png")
            br.close()
    print("\n".join(f"{a.out}/{n}.*" for n in written))

if __name__ == "__main__":
    main()
