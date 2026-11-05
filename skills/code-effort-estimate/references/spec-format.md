# Spec format

Two shapes. **Simple** (one priced block): top-level `phases` (used as sections). **Phased** (separate subtotals per phase): `stages`, each with `sections` and its own `external_costs`.

**Top-level `management` is charged once on the whole project** (all phases' effort) in a "Management and AI tokens (whole project)" block after the phases. That's the default. A stage's own `management` is only for clients priced phase by phase.

```json
{
  "client": "Client name",
  "project": "Discovery and CX strategy",
  "prepared_by": "Name",
  "version": "v1",
  "date": "2026-11-05",
  "currency": "£",                    // ask; "$", "€" fine
  "rates": {"Standard": 1000},        // dummy; always ask the person, one per grade
  "cost_rounding": "pence",           // "pence" | "whole" (round each line to whole units)
  "layout": "full",                   // "full" | "client" (Activity | Time (days) | Cost)
  "hours_per_day": 7.5,               // optional; full layout only
  "rounding": "half",                 // days-basis management: "half" | "whole" | "none"

  "stages": [
    {"name": "Phase 1", "subtotal_label": "Phase 1 Subtotal",
     "sections": [
       {"name": "Immersion and Discovery", "lines": [
         {"activity": "Day 0", "days": 5, "notes": "..."},
         {"method": "customer_groups", "qty": 4,                 // ALWAYS ask the quantity
          "recruit_cost_per_unit": 1500, "recruiter": "Recruitment partner",
          "incentive_per_unit": 0},
         {"method": "user_testing", "qty": 2, "recruitment": "none",   // client supplies participants
          "notes": "..."},
         {"activity": "Supporter segments", "type": "fixed", "cost": 25000,
          "carries_management": true},
         {"activity": "Venue hire", "type": "expense", "cost": 600}
       ]}
     ],
     // "management": [...] here only if this client is priced phase by phase
     "external_costs": [
       {"item": "Prototyping tool licence", "supplier": "Supplier", "unit": "month", "qty": 3, "unit_cost": 300},
       {"item": "Test devices", "supplier": "Supplier", "qty": 2, "unit_cost": 150}
     ]}
  ],

  "management": [                                    // once, on the whole project (default)
    {"activity": "Delivery Management", "percent": 0.20},            // basis "days" by default
    {"activity": "Product Consultancy", "percent": 0.05},
    {"activity": "AI token costs", "percent": 0.02, "basis": "cost", "applies_to": ["effort"]}
  ],
  "standards": {"user_testing": {"setup_days": 3}},  // optional per-estimate overrides
  "contingency": 0.0,
  "show_vat": true,
  "vat_rate": 0.20,
  "external_costs_confirmed_none": false,            // true only when the person says there are none
  "assumptions": ["Shown on the Assumptions sheet"]
}
```

## Line types

- `effort` (default): `days`, or `qty` × `unit_days`. Cost = days × rate for its `grade`.
- `fixed`: a lump-sum item with `cost` and no days. Carries management unless `carries_management: false`.
- `expense`: a pass-through with `cost`, or `qty` × `unit_cost`. Never carries management.
- `method`: a quantity-driven line that expands into setup, per-unit and analysis lines plus recruitment and incentive expenses. Keys: `customer_groups`, `customer_interviews`, `stakeholder_interviews`, `user_testing`, `workshops`, `field_visits`, `complex_journeys`. Options: `activity` (label), `notes`, `split_steps: true` (one line per step instead of one combined line), `recruit_cost_per_unit`, `recruiter`, `incentive_per_unit`, `recruitment: "none"`.

## Management

- `basis: "days"`: days = percent × effort days (the whole project's, or the phase's for stage-level management), rounded as set (Excel rounding, half up). Cost = days × rate.
- `basis: "cost"`: cost = percent × the costs of the line types in `applies_to` (default effort and fixed). No days.

## External costs

`external_costs` (top-level for the simple shape, per stage for phased) becomes an "External costs" section of expense lines. Each item has `item`, optional `supplier`, `unit`, `qty`, and `unit_cost`.

The Estimate sheet opens with a TOTALS table (each phase, management and AI tokens, contingency, total ex VAT, VAT, total inc VAT) linked to the detail below it.

Every figure in the sheet is a formula off the Settings sheet and the line inputs (blue text).
