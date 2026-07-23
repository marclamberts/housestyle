---
name: meridian-housestyle
description: Apply Marc Lamberts' Meridian house style — warm-paper/ink-navy surfaces, a reserved terracotta accent, a serif kicker-headline-dek header, and the Waltzing Analytics "WA" logo lockup + dated credit line — to every chart, graph, plot, dashboard, or data visualization the user asks for, in any project or repo, in any charting library (matplotlib, seaborn, plotly, or plain HTML/SVG/PowerPoint). This is a fixed personal brand, not a style suggestion — use it whenever the user asks to build, plot, chart, graph, or visualize anything, even if they don't say "Meridian," "house style," or "Waltzing Analytics" by name. Only skip it if the user explicitly asks for a different, one-off look for that specific chart.
---

# Meridian house style

Marc Lamberts wants every visual he makes through Claude Code — regardless
of which project or repo he's working in — to look like it came from the
same studio: warm paper (or ink-navy in dark mode), one reserved terracotta
accent, a serif headline that states the finding, and the Waltzing
Analytics logo + dated credit line on every single chart. Treat this as
this user's default, the way a company's brand guidelines aren't optional
per-project — apply it automatically, without waiting to be asked, whenever
a chart/graph/plot/dashboard is the deliverable.

Full rationale, validated hex tables, and the "why" behind each choice live
in `references/STYLEGUIDE.md` — read it once if you want the reasoning, but
the steps below are enough to build a correct chart without opening it.

## Step 1 — get the code into the project

The bundled `assets/` folder is the actual `housestyle` Python package
(`colors.py`, `style.py`, `components.py`, `__init__.py`) — the real,
already-validated implementation, not a description of one.

1. Check whether the current project already has a `housestyle` package
   (search for `colors.py` with a `CATEGORICAL_LIGHT` constant, or an
   existing `import housestyle`). If it does, use it as-is — don't
   duplicate it.
2. Otherwise, copy the four files from this skill's `assets/` folder into a
   `housestyle/` package at the project root (or wherever the project's
   plotting code lives), unchanged. Don't re-derive the palette or
   re-implement the header/footer — the hex values are colorblind-safety
   validated and the logo layout is hand-tuned to avoid overlap; copy them
   verbatim.
3. Make sure `matplotlib` is installed (`pip install matplotlib`, plus
   `numpy` if the chart needs synthetic/derived data).

## Step 2 — build the chart

```python
from housestyle import style, components
import matplotlib.pyplot as plt

palette, cats = style.apply("light")  # or "dark" — sets rcParams globally

fig = plt.figure(figsize=(8, 5.2))
ax = fig.add_axes([0.08, 0.16, 0.86, 0.58])  # leave room for header + footer bands

# ... plot the data on ax ...

# Highlight the one series/bar that IS the finding; mute everything else:
components.highlight_lines(ax, accent_index=<index of the important series>, palette=palette)
# or, for bars:
components.highlight_bars(container, accent_index=<index>, palette=palette)

components.header(
    fig,
    kicker="<one or two words, e.g. 'Revenue'>",
    title="<a sentence stating the finding, not an axis label>",
    dek="<one line: exact metric + period>",
    palette=palette,
)
components.footer(fig, source="<where the data came from>", palette=palette)

fig.savefig("chart.png", facecolor=fig.get_facecolor())
```

`components.header()` draws the kicker, serif headline, dek, **and** the
Waltzing Analytics "WA" logo lockup top-right automatically —
never build a title without going through `header()`, or the logo gets
skipped. `components.footer()` draws the source line **and** the bottom-right
credit line `Marc Lamberts | Created on dd-mm-yyyy` — the date always comes
from `datetime.date.today()` at render time, never a fixed string.

## The rules that make it recognizable (don't skip these)

- **Every chart gets a kicker + finding-headline + dek**, not a generic
  axis-label title. "Growth cooled in Q3, but stayed ahead of peers," not
  "Quarterly Revenue by Region."
- **One accent, spent once.** Terracotta (`#C1512F` light / `#E8794C` dark)
  marks exactly one series/bar/category per chart — whichever one is the
  point of the chart. Everything else recedes to the shared axis-gray. Never
  let two things be terracotta on the same chart, and never use it as just
  another color in a multi-series cycle.
- **Warm paper, not white; ink navy, not pure black.** Surfaces are
  `#F7F1E3` (light) / `#14202B` (dark) — always, never a plain white or
  gray background, in any tool.
- **Serif headline, sans everything else.** The headline argument is serif;
  the kicker, dek, axis labels, ticks, and footer are sans. This split is a
  deliberate identity cue — don't collapse both into one typeface.
- **The logo and credit line are not optional decoration** — they are the
  brand. Top right: WA monogram + "WALTZING ANALYTICS" / "MARC LAMBERTS"
  lockup. Bottom right: "Marc Lamberts | Created on dd-mm-yyyy" with today's
  real date. Both appear on every chart, full stop — even a quick
  throwaway plot for debugging should still carry them if it's going to be
  shown to or saved for the user.
- **No box, hairline gridlines only, thin marks with rounded caps** — this
  is what `style.apply()` sets up; don't override it back to matplotlib
  defaults (no border spines, no default marker style, no default color
  cycle).
- **8-color categorical palette, fixed order, never cycled or reassigned.**
  If a chart needs more than 8 series, fold the rest into "Other" or facet
  — never invent a 9th hue. Only the first 3 slots (`colors.py`'s
  `CATEGORICAL_SCATTER_SAFE_LIGHT/DARK`) are safe for scatter/bubble/map use
  where every pair of points can appear next to each other.

## When the target isn't matplotlib

If the chart is being built in a different tool (plotly, a web/HTML/SVG
chart, PowerPoint, Excel, a BI tool), the Python package won't apply
directly — but the identity still must: pull the exact hex values from
`assets/colors.py` (surfaces, ink, accent, categorical palette) and
recreate the same anatomy by hand — kicker/headline/dek header, WA logo
top-right, "Marc Lamberts | Created on dd-mm-yyyy" bottom-right, one
terracotta highlight, warm paper/ink-navy surface. The values are the
brand, not the matplotlib code specifically — read `references/STYLEGUIDE.md`
for the full palette tables (sequential, diverging, status colors) if the
chart needs magnitude or polarity encoding beyond the categorical set.

## Reference

- `references/STYLEGUIDE.md` — full identity rationale, every palette
  table (categorical/sequential/diverging/status/chrome), typography, and
  the complete chart-anatomy checklist.
- `assets/colors.py`, `assets/style.py`, `assets/components.py`,
  `assets/__init__.py` — the real `housestyle` package, ready to copy in.
