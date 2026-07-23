# housestyle

**Meridian** — a distinctive, editorial house style for data visuals in
Python (matplotlib). Warm paper surfaces, one reserved signature accent, a
kicker–headline–dek header, and a validated colorblind-safe palette.

Read **[STYLEGUIDE.md](STYLEGUIDE.md)** for the full identity rationale,
palette tables, typography, and chart-anatomy rules.

## Quickstart

```bash
pip install -r requirements.txt
python examples/generate_all.py   # renders examples/output/*.png
```

```python
from housestyle import style, components
import matplotlib.pyplot as plt

palette, cats = style.apply("light")

fig = plt.figure(figsize=(8, 5.2))
ax = fig.add_axes([0.08, 0.16, 0.86, 0.58])
ax.plot(x, y)
components.header(fig, kicker="…", title="…", dek="…", palette=palette)
components.footer(fig, source="…", palette=palette)
fig.savefig("out.png", facecolor=fig.get_facecolor())
```

## Layout

```
housestyle/
  colors.py       validated palette — categorical, sequential, diverging, status, chrome
  style.py        style.apply("light" | "dark") — sets matplotlib rcParams
  components.py   header(), footer(), highlight_lines(), highlight_bars(), label_endpoint()
examples/
  line_highlight.py   line chart, one highlighted series, direct end labels
  bar_highlight.py    bar chart, one highlighted category
  generate_all.py     regenerate every example PNG
  output/              rendered reference PNGs (light + dark)
STYLEGUIDE.md      full house-style documentation
```
