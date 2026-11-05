#!/usr/bin/env python3
"""Build a Code effort estimate (.xlsx, live formulas) from a JSON spec.

Usage: python build_estimate.py spec.json output.xlsx
Prints check warnings and the totals. Run the xlsx skill's recalc.py afterwards.
Spec shape: references/spec-format.md
"""
import json
import re
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

NAVY, LIME, PANEL, BLUE_IN, MUTED = "000050", "B0F467", "ECF1F4", "0000FF", "5A5F8A"
FONT = "Arial"
HAIR = Border(bottom=Side(style="hair", color="B8BCD6"))


def f(bold=False, color=NAVY, size=10, italic=False):
    return Font(name=FONT, bold=bold, color=color, size=size, italic=italic)


def fill(c):
    return PatternFill("solid", start_color=c, end_color=c)


def g(x):
    return f"{x:g}"


# ---------------------------------------------------------------- multipliers
STANDARDS = {
    # method: label, unit, units, setup label, setup days, [(step, days)], analysis label, analysis days
    "customer_groups": ("Customer groups", "group", "groups", "Discussion guide and screener", 2,
                        [("prep", 0.5), ("running and notes", 3.5)], "Customer group analysis", 1),
    "customer_interviews": ("Customer interviews", "interview", "interviews", "Discussion guide and screener", 1.5,
                            [("prep", 0.1), ("running and notes", 0.4)], "Customer interview analysis", 0.25),
    "stakeholder_interviews": ("Stakeholder interviews", "interview", "interviews", "Interview guide", 1,
                               [("prep", 0.1), ("running, paired (5 a day x 2 people)", 0.4)], "Stakeholder interview analysis", 0.2),
    "user_testing": ("User testing", "test group", "test groups", "Test plan and script", 2,
                     [("prep and set-up", 0.5), ("running sessions", 2.5)], "User testing analysis", 2),
    "workshops": ("Internal mapping workshops", "session", "sessions", "Workshop design", 1,
                  [("prep", 0.25), ("running", 0.25)], "Workshop write-up", 0.25),
    "field_visits": ("Field visits", "visit", "visits", "Field guide and visit planning", 1.5,
                     [("prep", 0.25), ("visit and notes", 1)], "Field visit analysis", 0.5),
    "complex_journeys": ("Complex journey design", "complex journey", "complex journeys", "", 0,
                         [("design sprint", 6), ("content design", 4), ("hi-fidelity design", 4),
                          ("usability testing", 4), ("amends", 2)], "", 0),
}
ANALYSIS_SECTION = "Synthesis and analysis"
EXTERNAL_SECTION = "External costs"
# Methods where Code talks to customers/users, so recruitment must be asked about.
PARTICIPANT_METHODS = {"customer_groups", "customer_interviews", "user_testing"}


def add_external_costs(spec):
    """Stage-level external_costs (supplier tools, AI tokens, venues…) become an expense section."""
    cur = spec.get("currency", "£")
    for stage in spec["stages"]:
        items = stage.pop("external_costs", None)
        if items is None and len(spec["stages"]) == 1:
            items = spec.pop("external_costs", None)
        if not items:
            continue
        lines = []
        for it in items:
            q = float(it.get("qty", 1))
            unit = it.get("unit", "")
            unit_cost = float(it.get("unit_cost", it.get("cost", 0)))
            sup = it.get("supplier")
            note = it.get("notes") or ", ".join(x for x in [
                sup, f"{cur}{unit_cost:,.0f}{' per ' + unit if unit else ''}" + (f" x {g(q)}" if q != 1 else "")] if x)
            lines.append({"activity": it["item"], "type": "expense", "qty": q, "unit_cost": unit_cost, "notes": note})
        stage["sections"].append({"name": EXTERNAL_SECTION, "lines": lines})
    return spec


def normalise(spec):
    """Accept the simple form (top-level phases + management) or the staged form."""
    if "stages" not in spec:
        spec["stages"] = [{"name": None, "sections": spec.pop("phases")}]
    # Top-level management (incl. AI tokens) is charged once on the whole project's effort.
    # Stage-level management stays available for clients priced phase by phase.
    spec["project_management"] = spec.pop("management", [])
    return spec


def expand_methods(spec):
    std = dict(STANDARDS)
    for k, v in spec.get("standards", {}).items():
        base = list(std.get(k, ("", "unit", "units", "Setup", 0, [], "Analysis", 0)))
        for field, idx in (("label", 0), ("setup_days", 4), ("steps", 5), ("analysis_days", 7)):
            if field in v:
                base[idx] = [tuple(s) for s in v[field]] if field == "steps" else v[field]
        std[k] = tuple(base)
    cur = spec.get("currency", "£")
    for stage in spec["stages"]:
        analysis = []
        for sec in stage["sections"]:
            new = []
            for ln in sec["lines"]:
                m = ln.get("method")
                if not m:
                    new.append(ln)
                    continue
                if m not in std:
                    raise SystemExit(f"Unknown method '{m}'. Known: {', '.join(std)}")
                if "qty" not in ln:
                    raise SystemExit(f"'{m}' needs a qty. Ask the person how many {std[m][2]}.")
                if m in PARTICIPANT_METHODS and not ln.get("recruit_cost_per_unit") and ln.get("recruitment") != "none":
                    spec.setdefault("_warnings", []).append(
                        f"'{ln.get('activity', std[m][0])}': talks to people but has no recruitment cost. "
                        "Ask who recruits and the cost per group/participant, or set recruitment: \"none\" (e.g. client supplies).")
                label, unit, units, s_label, s_days, steps, a_label, a_days = std[m]
                label = ln.get("activity", label)
                q, grade = float(ln["qty"]), ln.get("grade", "Standard")
                noun = unit if q == 1 else units
                if s_days:
                    new.append({"activity": f"{label}: {s_label.lower()}", "grade": grade, "days": s_days,
                                "notes": ln.get("setup_notes", f"Done once, whatever the number of {units}")})
                if ln.get("split_steps"):
                    for s, d in steps:
                        new.append({"activity": f"{s.capitalize()} – {g(q)} {noun}", "grade": grade, "days": q * d,
                                    "notes": f"{g(q)} {noun} x {g(d)} days"})
                else:
                    per = sum(d for _, d in steps)
                    breakdown = " + ".join(f"{g(d)} {s}" for s, d in steps)
                    new.append({"activity": f"{label} x{g(q)} {noun}", "grade": grade, "days": q * per,
                                "notes": (ln["notes"] + " " if ln.get("notes") else "") +
                                f"{g(q)} {noun} x {g(per)} days ({breakdown})"})
                for key, what in (("recruit_cost_per_unit", "recruitment"), ("incentive_per_unit", "incentives")):
                    if ln.get(key):
                        new.append({"activity": f"{label}: {what}", "type": "expense", "qty": q,
                                    "unit_cost": ln[key],
                                    "notes": f"{ln.get('recruiter', 'Recruitment partner') + ' at ' if what == 'recruitment' else ''}{cur}{ln[key]:,.0f} per {unit}, {g(q)} {noun}"})
                if a_days:
                    analysis.append({"activity": f"{a_label} x{g(q)} {noun}", "grade": grade,
                                     "days": q * a_days, "notes": f"{g(q)} {noun} x {g(a_days)} days"})
            sec["lines"] = new
        if analysis:
            target = next((s for s in stage["sections"] if s["name"].lower() == ANALYSIS_SECTION.lower()), None)
            if target is None:
                target = {"name": ANALYSIS_SECTION, "lines": []}
                idx = next((i for i, s in enumerate(stage["sections"]) if "strateg" in s["name"].lower()),
                           len(stage["sections"]))
                stage["sections"].insert(idx, target)
            target["lines"] = analysis + target["lines"]
    return spec


# ---------------------------------------------------------------- line maths
def ltype(ln):
    return ln.get("type", "effort")


def line_days(ln):
    if ltype(ln) != "effort":
        return None
    if ln.get("days") is not None:
        return float(ln["days"])
    if "qty" in ln and "unit_days" in ln:
        return float(ln["qty"]) * float(ln["unit_days"])
    return 0.0


def line_cost_input(ln):
    if "cost" in ln:
        return float(ln["cost"])
    return float(ln.get("qty", 0)) * float(ln.get("unit_cost", 0))


def checks(spec):
    warns = []
    for stage in spec["stages"]:
        for sec in stage["sections"]:
            for ln in sec["lines"]:
                name, notes = ln["activity"], ln.get("notes", "") or ""
                if ltype(ln) == "effort":
                    d = line_days(ln)
                    if not d:
                        warns.append(f"'{name}': no days. Size it, or move it to assumptions/exclusions.")
                    if re.search(r"(£|\$|€)\s?[\d,]+\s*(per|/|each)", notes, re.I):
                        warns.append(f"'{name}': note gives a fee per unit. Probably an expense, not days.")
                    for a, b in re.findall(r"(\d+(?:\.\d+)?)\s*(?:x|×)\s*(\d+(?:\.\d+)?)\s*days?", notes, re.I):
                        if d and abs(float(a) * float(b) - d) > 0.01:
                            warns.append(f"'{name}': note says {a} x {b} = {float(a)*float(b):g} days but the line has {d:g}.")
                    m_act = re.search(r"x\s*(\d+)", name, re.I)
                    m_note = re.search(r"(\d+)\s*(groups|sessions|interviews|workshops)", notes, re.I)
                    if m_act and m_note and m_act.group(1) != m_note.group(1):
                        warns.append(f"'{name}': activity says x{m_act.group(1)} but note says {m_note.group(1)} {m_note.group(2)}.")
                    if re.search(r"\bper (group|journey|session|interview|workshop)\b", name, re.I) and not re.search(r"\d", name + notes):
                        warns.append(f"'{name}': says 'per …' but gives no quantity. Ask how many.")
                elif ltype(ln) == "fixed" and "carries_management" not in ln:
                    warns.append(f"'{name}': fixed-price line. Confirm whether it carries management (default: yes).")
    if "contingency" not in spec:
        warns.append("Contingency not stated. Set it, even if 0%.")
    has_external = any(s["name"] == EXTERNAL_SECTION for st in spec["stages"] for s in st["sections"])
    if not has_external and not spec.get("external_costs_confirmed_none"):
        warns.append("No external costs. Ask about equipment (devices, recording or test kit), supplier tools "
                     "(prototyping, research platforms) and travel, or set external_costs_confirmed_none: true.")
    has_pm_token = any("token" in m["activity"].lower() for m in spec.get("project_management", []))
    for st in ([] if has_pm_token else spec["stages"][:1]):
        if not any("token" in m["activity"].lower() for s2 in spec["stages"] for m in s2.get("management", [])):
            warns.append("No AI token cost line. Default is 2% of effort cost in the project management block "
                         "({\"activity\": \"AI token costs\", \"percent\": 0.02, \"basis\": \"cost\", \"applies_to\": [\"effort\"]}).")
    return spec.pop("_warnings", []) + warns


# ---------------------------------------------------------------- build
def build(spec, out):
    cur = spec.get("currency", "£")
    money = f'"{cur}"#,##0;("{cur}"#,##0);"-"' if spec.get("cost_rounding") == "whole" \
        else f'"{cur}"#,##0.00;("{cur}"#,##0.00);"-"'
    days_fmt = '0.0;-0.0;"-"' if spec.get("days_decimals", True) else '0;-0;"-"'
    rounding = spec.get("rounding", "half")
    whole_cost = spec.get("cost_rounding") == "whole"
    hpd = spec.get("hours_per_day")
    layout = spec.get("layout", "full")

    if layout == "client":
        cols = ["activity", "days", "cost", "grade", "rate", "key", "type"]
        heads = {"activity": "Activity", "days": "Time (days)", "cost": f"Cost ({cur})"}
        hidden = {"grade", "rate", "key", "type"}
        widths = {"activity": 52, "days": 13, "cost": 15}
    else:
        cols = ["activity", "grade", "days", "hours", "rate", "cost", "notes", "key", "type"]
        heads = {"activity": "Activity", "grade": "Grade", "days": "Days", "hours": "Hours",
                 "rate": "Day rate", "cost": "Cost", "notes": "Notes"}
        hidden = {"key", "type"}
        widths = {"activity": 46, "grade": 11, "days": 9, "hours": 9, "rate": 12, "cost": 15, "notes": 70}
    C = {k: get_column_letter(i + 1) for i, k in enumerate(cols)}
    ci = {k: i + 1 for i, k in enumerate(cols)}
    ncol_vis = len([c for c in cols if c not in hidden])

    wb = Workbook()
    ws = wb.active
    ws.title = "Estimate"
    st = wb.create_sheet("Settings")
    sm = wb.create_sheet("Summary")
    asm = wb.create_sheet("Assumptions")

    # Settings
    st["A1"], st["A1"].font = "Settings", f(True, size=14)
    st["A2"], st["A2"].font = "Blue cells are inputs. Change them here and the estimate recalculates.", f(color=MUTED, italic=True)
    for c, h in (("A4", "Grade"), ("B4", f"Day rate ({cur})")):
        st[c], st[c].font, st[c].fill = h, f(True, "FFFFFF"), fill(NAVY)
    r = 5
    for grade, rate in spec["rates"].items():
        st.cell(r, 1, grade).font = f(color=BLUE_IN)
        c = st.cell(r, 2, rate)
        c.font, c.number_format = f(color=BLUE_IN), f'"{cur}"#,##0.00'
        r += 1
    rl = r - 1
    RATE_A, RATE_B = f"Settings!$A$5:$A${rl}", f"Settings!$B$5:$B${rl}"
    r += 1
    S = {}
    srows = [("hpd", "Hours per day", hpd or 7.5, "0.0")]
    for si, stage in enumerate(spec["stages"]):
        for mi, m in enumerate(stage.get("management", [])):
            label = f"{stage['name'] + ': ' if stage['name'] else ''}{m['activity']} % (of {m.get('basis', 'days')})"
            srows.append((f"m{si}_{mi}", label, m["percent"], "0.0%"))
    for mi, m in enumerate(spec.get("project_management", [])):
        srows.append((f"pm{mi}", f"{m['activity']} % (of {m.get('basis', 'days')}, whole project)", m["percent"], "0.0%"))
    srows += [("cont", "Contingency %", spec.get("contingency", 0), "0.0%"),
              ("vat", "VAT %", spec.get("vat_rate", 0.2), "0.0%")]
    for key, label, val, fmt in srows:
        st.cell(r, 1, label).font = f()
        c = st.cell(r, 2, val)
        c.font, c.number_format = f(color=BLUE_IN), fmt
        if key == "cont":
            c.fill = fill("FFFF00")
        S[key] = f"Settings!$B${r}"
        r += 1
    st.column_dimensions["A"].width, st.column_dimensions["B"].width = 52, 16

    def rnd_cost(expr):
        return f"ROUND({expr},0)" if whole_cost else expr

    def rnd_days(expr):
        return {"half": f"ROUND({expr}*2,0)/2", "whole": f"ROUND({expr},0)"}.get(rounding, expr)

    # Estimate header
    ws["A1"], ws["A1"].font = spec.get("project", "Effort estimate"), f(True, size=16)
    ws["A2"] = "  ·  ".join(x for x in [spec.get("client"), spec.get("version"), spec.get("date"),
                                         f"Prepared by {spec['prepared_by']}" if spec.get("prepared_by") else None] if x)
    ws["A2"].font = f(color=MUTED)
    ws["A3"], ws["A3"].font = "INTERNAL DRAFT", Font(name=FONT, bold=True, size=9, color="3F4FE0")
    pmgmt = spec.get("project_management", [])
    multi = len(spec["stages"]) > 1 or spec["stages"][0]["name"]
    tot_items = len(spec["stages"]) if multi else len(spec["stages"][0]["sections"])
    TB = 5  # totals block starts here
    tb_rows = 1 + tot_items + (1 if pmgmt else 0) + 2 + (2 if spec.get("show_vat", True) else 0)
    HR = TB + tb_rows + 2
    for k in cols:
        c = ws.cell(HR, ci[k], heads.get(k, k))
        c.font, c.fill = f(True, "FFFFFF"), fill(NAVY)
        c.alignment = Alignment(vertical="center", horizontal="left" if k in ("activity", "grade", "notes") else "right")
    ws.row_dimensions[HR].height = 22

    def band(row, text, size=11, colour=PANEL):
        ws.cell(row, 1, text).font = f(True, size=size)
        for col in range(1, ncol_vis + 1):
            ws.cell(row, col).fill = fill(colour)

    def put(row, ln, key, days_formula=None, cost_formula=None):
        t = ltype(ln)
        ws.cell(row, ci["activity"], ln["activity"]).font = f()
        ws.cell(row, ci["key"], key)
        ws.cell(row, ci["type"], "mgmt" if (days_formula or cost_formula) else t)
        if "notes" in ci:
            n = ws.cell(row, ci["notes"], ln.get("notes", ""))
            n.font, n.alignment = f(color=MUTED), Alignment(wrap_text=True, vertical="top")
        if t in ("expense", "fixed") and not cost_formula:
            if "grade" in ci:
                ws.cell(row, ci["grade"], "Expense" if t == "expense" else "Fixed").font = f(color=MUTED)
            c = ws.cell(row, ci["cost"], line_cost_input(ln))
            c.font, c.number_format = f(color=BLUE_IN), money
        elif cost_formula:
            if "grade" in ci:
                ws.cell(row, ci["grade"], "—").font = f(color=MUTED)
            c = ws.cell(row, ci["cost"], cost_formula)
            c.font, c.number_format = f(), money
        else:
            gcell = ws.cell(row, ci["grade"], ln.get("grade", "Standard"))
            gcell.font = f(color=BLUE_IN)
            d = ws.cell(row, ci["days"], days_formula if days_formula else line_days(ln))
            d.font, d.number_format = f(color=NAVY if days_formula else BLUE_IN), days_fmt
            if "hours" in ci and hpd:
                h = ws.cell(row, ci["hours"], f"={C['days']}{row}*{S['hpd']}")
                h.font, h.number_format = f(), '0.0;-0.0;"-"'
            rt = ws.cell(row, ci["rate"], f"=INDEX({RATE_B},MATCH({C['grade']}{row},{RATE_A},0))")
            rt.font, rt.number_format = f(), money
            c = ws.cell(row, ci["cost"], "=" + rnd_cost(f"{C['days']}{row}*{C['rate']}{row}"))
            c.font, c.number_format = f(), money
        for col in range(1, ncol_vis + 1):
            ws.cell(row, col).border = HAIR

    r = HR + 1
    stage_totals = []
    summary_keys = []
    all_rows = {"effort": [], "fixed": [], "fixed_nomgmt": [], "expense": []}
    for si, stage in enumerate(spec["stages"]):
        if stage["name"]:
            band(r, stage["name"], 12, "D6DCF5")
            r += 1
        s_first = r
        rows_by = {"effort": [], "fixed": [], "expense": []}
        for sec in stage["sections"]:
            band(r, sec["name"])
            r += 1
            key = f"{stage['name'] + ' | ' if stage['name'] else ''}{sec['name']}"
            summary_keys.append(key)
            for ln in sec["lines"]:
                put(r, ln, key)
                bucket = ltype(ln)
                if bucket == "fixed" and ln.get("carries_management") is False:
                    bucket = "fixed_nomgmt"
                rows_by.setdefault(bucket, []).append(r)
                r += 1
        for b, xs in rows_by.items():
            all_rows.setdefault(b, []).extend(xs)
        eff_days = "+".join(f"{C['days']}{x}" for x in rows_by["effort"]) or "0"
        mgmt = stage.get("management", [])
        if mgmt:
            if not stage.get("management_inline", False):
                band(r, "Management and AI tokens" if any("token" in m["activity"].lower() for m in mgmt) else "Management")
                r += 1
            key = f"{stage['name'] + ' | ' if stage['name'] else ''}Management"
            summary_keys.append(key)
            for mi, m in enumerate(mgmt):
                pct = S[f"m{si}_{mi}"]
                basis = m.get("basis", "days")
                note = m.get("notes")
                if basis == "cost":
                    applies = m.get("applies_to", ["effort", "fixed"])
                    base_rows = [x for b in applies for x in rows_by.get(b, [])]
                    base = "+".join(f"{C['cost']}{x}" for x in base_rows) or "0"
                    note = note or f"Calculated at {m['percent']*100:g}% of {' and '.join(applies)} costs"
                    put(r, {"activity": m["activity"], "notes": note}, key,
                        cost_formula="=" + rnd_cost(f"{pct}*({base})"))
                else:
                    note = note or f"Calculated at {m['percent']*100:g}% of total effort days"
                    put(r, {"activity": m["activity"], "grade": m.get("grade", "Standard"), "notes": note}, key,
                        days_formula="=" + rnd_days(f"{pct}*({eff_days})"))
                r += 1
        s_last = r - 1
        if multi:
            label = stage.get("subtotal_label") or f"{stage['name']} subtotal"
            ws.cell(r, 1, label).font = f(True)
            dsum = ws.cell(r, ci["days"], f"=SUM({C['days']}{s_first}:{C['days']}{s_last})")
            dsum.number_format, dsum.font = days_fmt, f(True)
            csum = ws.cell(r, ci["cost"], f"=SUM({C['cost']}{s_first}:{C['cost']}{s_last})")
            csum.number_format, csum.font = money, f(True)
            for col in range(1, ncol_vis + 1):
                ws.cell(r, col).border = Border(top=Side(style="thin", color=NAVY))
            stage_totals.append(r)
            r += 2

    # Project-level management and AI tokens, on the whole project's effort
    pm_rows = []
    if pmgmt:
        band(r, "Management and AI tokens (whole project)" if any("token" in m["activity"].lower() for m in pmgmt)
             else "Management (whole project)")
        r += 1
        all_eff_days = "+".join(f"{C['days']}{x}" for x in all_rows["effort"]) or "0"
        summary_keys.append("Management and AI tokens")
        for mi, m in enumerate(pmgmt):
            pct = S[f"pm{mi}"]
            note = m.get("notes")
            if m.get("basis", "days") == "cost":
                applies = m.get("applies_to", ["effort", "fixed"])
                base = "+".join(f"{C['cost']}{x}" for b in applies for x in all_rows.get(b, [])) or "0"
                note = note or f"Calculated at {m['percent']*100:g}% of the project's {' and '.join(applies)} costs"
                put(r, {"activity": m["activity"], "notes": note}, "Management and AI tokens",
                    cost_formula="=" + rnd_cost(f"{pct}*({base})"))
            else:
                note = note or f"Calculated at {m['percent']*100:g}% of the project's total effort days"
                put(r, {"activity": m["activity"], "grade": m.get("grade", "Standard"), "notes": note},
                    "Management and AI tokens", days_formula="=" + rnd_days(f"{pct}*({all_eff_days})"))
            pm_rows.append(r)
            r += 1
        r += 1

    # Totals
    if multi:
        sub_r = r
        parts = stage_totals + pm_rows
        ws.cell(r, 1, "Total (all phases" + (", management and AI tokens)" if pm_rows else ")")).font = f(True)
        ws.cell(r, ci["days"], "=" + "+".join(f"{C['days']}{x}" for x in parts)).number_format = days_fmt
        ws.cell(r, ci["cost"], "=" + "+".join(f"{C['cost']}{x}" for x in parts)).number_format = money
    else:
        if not pm_rows:
            r += 1
        sub_r = r
        ws.cell(r, 1, "Sub total").font = f(True)
        ws.cell(r, ci["days"], f"=SUM({C['days']}{HR+1}:{C['days']}{r-1})").number_format = days_fmt
        ws.cell(r, ci["cost"], f"=SUM({C['cost']}{HR+1}:{C['cost']}{r-1})").number_format = money
    for k in ("days", "cost"):
        ws.cell(sub_r, ci[k]).font = f(True)
    r += 1
    ws.cell(r, 1, "Contingency").font = f()
    if "grade" in ci:
        pc = ws.cell(r, ci["grade"], f"={S['cont']}")
        pc.number_format, pc.font = "0%", f()
    ws.cell(r, ci["cost"], "=" + rnd_cost(f"{C['cost']}{sub_r}*{S['cont']}")).number_format = money
    if "notes" in ci:
        ws.cell(r, ci["notes"], "Allowance for unknowns and variation").font = f(color=MUTED)
    cont_r = r
    r += 1
    tot_r = r
    ws.cell(r, 1, "TOTAL (ex VAT)")
    ws.cell(r, ci["cost"], f"={C['cost']}{sub_r}+{C['cost']}{cont_r}").number_format = money
    ws.cell(r, ci["days"], f"={C['days']}{sub_r}").number_format = days_fmt
    for col in range(1, ncol_vis + 1):
        ws.cell(r, col).fill, ws.cell(r, col).font = fill(LIME), f(True, size=11)
    r += 1
    if spec.get("show_vat", True):
        ws.cell(r, 1, "VAT").font = f()
        ws.cell(r, ci["cost"], "=" + rnd_cost(f"{C['cost']}{tot_r}*{S['vat']}")).number_format = money
        r += 1
        ws.cell(r, 1, "TOTAL (inc VAT)").font = f(True)
        c = ws.cell(r, ci["cost"], f"={C['cost']}{tot_r}+{C['cost']}{r-1}")
        c.number_format, c.font = money, f(True)
        r += 1
    last_line = r
    vat_r = tot_r + 1 if spec.get("show_vat", True) else None

    # Totals block at the top of the sheet: the answer, before the detail
    rng_e = lambda k: f"${C[k]}${HR+1}:${C[k]}${last_line}"
    t = TB
    ws.cell(t, 1, "TOTALS")
    for k in ("activity", "days", "cost"):
        c = ws.cell(t, ci[k], {"activity": "TOTALS", "days": heads["days"], "cost": heads["cost"]}[k])
        c.font, c.fill = f(True, "FFFFFF"), fill(NAVY)
        c.alignment = Alignment(horizontal="left" if k == "activity" else "right")
    for col in range(1, ncol_vis + 1):
        ws.cell(t, col).fill = fill(NAVY)
    t += 1
    if multi:
        for st_, sr in zip(spec["stages"], stage_totals):
            ws.cell(t, 1, st_["name"]).font = f()
            ws.cell(t, ci["days"], f"={C['days']}{sr}").number_format = days_fmt
            ws.cell(t, ci["cost"], f"={C['cost']}{sr}").number_format = money
            t += 1
    else:
        for sec in spec["stages"][0]["sections"]:
            ws.cell(t, 1, sec["name"]).font = f()
            ws.cell(t, ci["days"], f"=SUMIF({rng_e('key')},\"{sec['name']}\",{rng_e('days')})").number_format = days_fmt
            ws.cell(t, ci["cost"], f"=SUMIF({rng_e('key')},\"{sec['name']}\",{rng_e('cost')})").number_format = money
            t += 1
    if pmgmt:
        ws.cell(t, 1, "Management and AI tokens (whole project)").font = f()
        ws.cell(t, ci["days"], "=" + "+".join(f"{C['days']}{x}" for x in pm_rows)).number_format = days_fmt
        ws.cell(t, ci["cost"], "=" + "+".join(f"{C['cost']}{x}" for x in pm_rows)).number_format = money
        t += 1
    ws.cell(t, 1, "Contingency").font = f()
    ws.cell(t, ci["cost"], f"={C['cost']}{cont_r}").number_format = money
    t += 1
    ws.cell(t, 1, "TOTAL (ex VAT)")
    ws.cell(t, ci["days"], f"={C['days']}{tot_r}").number_format = days_fmt
    ws.cell(t, ci["cost"], f"={C['cost']}{tot_r}").number_format = money
    for col in range(1, ncol_vis + 1):
        ws.cell(t, col).fill, ws.cell(t, col).font = fill(LIME), f(True, size=11)
    t += 1
    if vat_r:
        ws.cell(t, 1, "VAT").font = f()
        ws.cell(t, ci["cost"], f"={C['cost']}{vat_r}").number_format = money
        t += 1
        ws.cell(t, 1, "TOTAL (inc VAT)").font = f(True)
        c = ws.cell(t, ci["cost"], f"={C['cost']}{vat_r + 1}")
        c.number_format, c.font = money, f(True)
        t += 1
    for rr_ in range(TB + 1, t):
        for k in ("days", "cost"):
            if ws.cell(rr_, ci[k]).font.b is False:
                ws.cell(rr_, ci[k]).font = f()
        for col in range(1, ncol_vis + 1):
            if ws.cell(rr_, col).fill.fgColor.rgb in (None, "00000000"):
                ws.cell(rr_, col).border = HAIR

    for k in cols:
        col = ws.column_dimensions[C[k]]
        if k in hidden:
            col.hidden = True
        else:
            col.width = widths.get(k, 12)
    ws.freeze_panes = ws.cell(HR + 1, 1)
    ws.sheet_view.showGridLines = False
    ws.print_title_rows = f"{HR}:{HR}"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1

    # Summary
    sm["A1"], sm["A1"].font = "Summary", f(True, size=14)
    for i, h in enumerate(["Section", "Days", f"Cost ({cur})", "% of total"], 1):
        c = sm.cell(3, i, h)
        c.font, c.fill = f(True, "FFFFFF"), fill(NAVY)
    rng = lambda k: f"Estimate!${C[k]}${HR+1}:${C[k]}${last_line}"
    rr = 4
    for k in summary_keys:
        sm.cell(rr, 1, k).font = f()
        sm.cell(rr, 2, f"=SUMIF({rng('key')},A{rr},{rng('days')})").number_format = days_fmt
        sm.cell(rr, 3, f"=SUMIF({rng('key')},A{rr},{rng('cost')})").number_format = money
        sm.cell(rr, 4, f"=IF(Estimate!${C['cost']}${sub_r}=0,0,C{rr}/Estimate!${C['cost']}${sub_r})").number_format = "0.0%"
        rr += 1
    sm.cell(rr, 1, "Total").font = f(True)
    sm.cell(rr, 2, f"=SUM(B4:B{rr-1})").number_format = days_fmt
    sm.cell(rr, 3, f"=SUM(C4:C{rr-1})").number_format = money
    rr += 2
    for label, t in (("Effort", "effort"), ("Fixed-price items", "fixed"), ("Expenses (pass-through)", "expense"), ("Management", "mgmt")):
        sm.cell(rr, 1, label).font = f()
        if t in ("effort", "mgmt"):
            sm.cell(rr, 2, f"=SUMIF({rng('type')},\"{t}\",{rng('days')})").number_format = days_fmt
        sm.cell(rr, 3, f"=SUMIF({rng('type')},\"{t}\",{rng('cost')})").number_format = money
        rr += 1
    for col, w in zip("ABCD", (48, 10, 16, 12)):
        sm.column_dimensions[col].width = w

    # Assumptions
    asm["A1"], asm["A1"].font = "Assumptions & exclusions", f(True, size=14)
    items = list(spec.get("assumptions", []))
    items.append(f"All costs are days x day rate ({', '.join(f'{k} {cur}{v:,.2f}' for k, v in spec['rates'].items())}).")
    for stage in spec["stages"]:
        for m in stage.get("management", []):
            scope = f"{stage['name']}: " if stage["name"] else ""
            if m.get("basis", "days") == "cost":
                items.append(f"{scope}{m['activity']} is {m['percent']*100:g}% of {' and '.join(m.get('applies_to', ['effort', 'fixed']))} costs.")
            else:
                items.append(f"{scope}{m['activity']} is {m['percent']*100:g}% of effort days, rounded to the nearest {'half day' if rounding == 'half' else 'day' if rounding == 'whole' else 'fraction'}.")
    for m in spec.get("project_management", []):
        if m.get("basis", "days") == "cost":
            items.append(f"{m['activity']} is {m['percent']*100:g}% of the whole project's {' and '.join(m.get('applies_to', ['effort', 'fixed']))} costs, charged once.")
        else:
            items.append(f"{m['activity']} is {m['percent']*100:g}% of the whole project's effort days, charged once, rounded to the nearest {'half day' if rounding == 'half' else 'day' if rounding == 'whole' else 'fraction'}.")
    items.append("Expenses (recruitment, incentives, equipment, travel) are passed through at cost.")
    for i, t in enumerate(items, 3):
        asm.cell(i, 1, f"• {t}").font = f()
        asm.cell(i, 1).alignment = Alignment(wrap_text=True)
    asm.column_dimensions["A"].width = 110
    wb.save(out)

    # Python mirror of the totals, for the console report
    report = {"stages": []}
    grand = 0.0
    import math
    xl_round = lambda x: math.floor(x + 0.5)  # Excel ROUND (half away from zero), not Python's banker's rounding
    rnd = xl_round if whole_cost else (lambda x: x)
    rdays = {"half": lambda x: xl_round(x * 2) / 2, "whole": xl_round}.get(rounding, lambda x: x)
    for stage in spec["stages"]:
        costs = {"effort": 0.0, "fixed": 0.0, "fixed_nomgmt": 0.0, "expense": 0.0}
        ed = 0.0
        for sec in stage["sections"]:
            for ln in sec["lines"]:
                t = ltype(ln)
                if t == "effort":
                    d = line_days(ln) or 0
                    ed += d
                    costs["effort"] += rnd(d * spec["rates"][ln.get("grade", "Standard")])
                else:
                    if t == "fixed" and ln.get("carries_management") is False:
                        t = "fixed_nomgmt"
                    costs[t] += line_cost_input(ln)
        md, mc = 0.0, 0.0
        for m in stage.get("management", []):
            if m.get("basis", "days") == "cost":
                mc += rnd(m["percent"] * sum(costs[b] for b in m.get("applies_to", ["effort", "fixed"])))
            else:
                d = rdays(m["percent"] * ed)
                md += d
                mc += rnd(d * spec["rates"][m.get("grade", "Standard")])
        sub = sum(costs.values()) + mc
        grand += sub
        report["stages"].append({"stage": stage["name"], "effort_days": ed, "management_days": md,
                                 "days": ed + md, "management_cost": mc, "subtotal": sub})
    tot_eff_days = sum(s_["effort_days"] for s_ in report["stages"])
    tot_costs = {"effort": 0.0, "fixed": 0.0}
    for stage in spec["stages"]:
        for sec in stage["sections"]:
            for ln in sec["lines"]:
                if ltype(ln) == "effort":
                    tot_costs["effort"] += rnd((line_days(ln) or 0) * spec["rates"][ln.get("grade", "Standard")])
                elif ltype(ln) == "fixed" and ln.get("carries_management") is not False:
                    tot_costs["fixed"] += line_cost_input(ln)
    pm = []
    for m in spec.get("project_management", []):
        if m.get("basis", "days") == "cost":
            pm.append({"line": m["activity"], "days": None,
                       "cost": rnd(m["percent"] * sum(tot_costs.get(b, 0) for b in m.get("applies_to", ["effort", "fixed"])))})
        else:
            d = rdays(m["percent"] * tot_eff_days)
            pm.append({"line": m["activity"], "days": d, "cost": rnd(d * spec["rates"][m.get("grade", "Standard")])})
    report["project_management"] = pm
    grand += sum(x["cost"] for x in pm)
    report["total_days"] = tot_eff_days + sum(s_["management_days"] for s_ in report["stages"]) + sum(x["days"] or 0 for x in pm)
    report["total_ex_vat"] = grand + rnd(grand * spec.get("contingency", 0))
    return report


if __name__ == "__main__":
    spec = add_external_costs(expand_methods(normalise(json.load(open(sys.argv[1])))))
    for w in checks(spec):
        print("CHECK:", w)
    print(json.dumps(build(spec, sys.argv[2]), indent=2))
