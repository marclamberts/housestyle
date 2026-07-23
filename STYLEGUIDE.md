# Meridian — a house style for data visuals

Meridian is a distinctive, editorial house style for charts: a warm paper
surface, one signature accent color reserved for the finding, a
kicker–headline–dek header borrowed from data journalism, and a
highlight-one/mute-the-rest convention for series emphasis. It's built for
Python (matplotlib), validated for colorblind safety, and designed to be
recognizable at a glance — even with no logo in frame.

## Identity, in one paragraph

Every Meridian chart opens with a small terracotta tick (`▪`) and an
uppercase kicker, a serif headline that states the finding as a sentence
(not an axis label), and a muted one-line dek for context. The plot itself
sits on a warm paper background, never white, with only a baseline and
faint horizontal gridlines — no box, no border. One series or bar carries
the signature terracotta; everything else recedes to a shared warm gray.
A hairline footer closes every chart with a source line and the wordmark.
That combination — paper surface, terracotta flag, serif headline, one
color doing the talking — is the recognizable signature, independent of
chart type.

## Why these choices

- **Warm paper, not white.** Off-white/cream surfaces are rare in dashboard
  and BI defaults (nearly all default to pure white or dark gray), so this
  alone makes a Meridian chart identifiable before you read a single label.
- **One signature accent, used sparingly.** Terracotta appears only on the
  kicker mark and on whichever single series/category is "the finding."
  Reserving it (never spending it on every series) is what makes it read as
  a signal instead of decoration — the same trick FT's salmon and The
  Economist's red rely on.
- **Serif headline over sans data.** The headline is the argument; the data
  is the evidence. Splitting typefaces between them is a deliberate,
  old-media-editorial cue that most software dashboards don't use, which is
  part of what makes this recognizable rather than generic-corporate.
- **Highlight one, mute the rest.** Rather than a rainbow legend, Meridian
  charts pick the one series that matters and let everything else fall back
  to a shared gray — readers always know where to look first.

## Palette

All hex values live in `housestyle/colors.py` and are validated with the
dataviz skill's `validate_palette.js` (OKLab CVD separation, normal-vision
floor, chroma floor, lightness band, contrast). Do not reorder the
categorical lists — order is the CVD-safety mechanism.

### Categorical (fixed order — never cycle, never reassign by rank)

| Slot | Hue | Light | Dark | Notes |
|---|---|---|---|---|
| 1 | ink blue | `#2A5C99` | `#5B8AC9` | primary series / "us" |
| 2 | terracotta | `#C1512F` | `#D9663A` | **signature accent — reserve for emphasis** |
| 3 | teal | `#0C8A76` | `#1FA88C` | |
| 4 | ochre | `#C6932B` | `#B37F1E` | sub-3:1 on paper — pair with a direct label |
| 5 | plum | `#9C3E82` | `#C168A8` | |
| 6 | moss | `#74881F` | `#7C9A2E` | |
| 7 | violet | `#6A4C9C` | `#9A82CE` | |
| 8 | crimson | `#B23A55` | `#D9637F` | |

Validated: adjacent-pair CVD ΔE ≥ 8 and normal-vision floor ≥ 15 in **both**
modes, against surfaces `#F7F1E3` (light) / `#14202B` (dark). **Only the
first three slots** additionally clear the `--pairs all` gate — that's the
series cap for scatter, bubble, choropleth, or small-multiples use. Past
three, fold extra series into "Other" or facet instead of extending the
cycle.

### Sequential — single hue (blue), for magnitude

7 steps light→dark (`SEQUENTIAL_BLUE_LIGHT` / `_DARK` in `colors.py`),
anchored on categorical slot 1 at step 500.

### Diverging — blue ↔ terracotta

Cool (blue) and warm (terracotta) arms, 4 steps each, meeting at a neutral
paper-gray midpoint (`#E3DDCC` light / `#33404A` dark). Equal step count per
arm; never a hue at the midpoint.

### Status (fixed — never themed, never reused for a series)

| Role | Light | Dark |
|---|---|---|
| good | `#2E7D46` | `#3FAE64` |
| warning | `#D9A31B` | `#E6B94A` |
| serious | `#D9682E` | `#E67D3E` |
| critical | `#B2242E` | `#D9434B` |

Status colors sit close to some categorical hues by design (warm family
overlaps ochre/terracotta/crimson) — the mitigation is the same one the
dataviz skill always requires: status always ships with an icon + label,
never color alone.

### Chrome & ink

| Role | Light | Dark |
|---|---|---|
| Surface | `#F7F1E3` | `#14202B` |
| Page plane | `#FBF7EC` | `#0C1219` |
| Primary ink | `#1B1B18` | `#F2EFE6` |
| Secondary ink | `#6B6558` | `#B7B0A0` |
| Muted ink (ticks/footer) | `#8C8570` | `#8A8778` |
| Gridline | `#E4DCC8` | `#263440` |
| Axis/baseline | `#C9BFA5` | `#3C4A57` |

## Typography

- **Headline / kicker:** serif — `Source Serif 4`, falling back through
  `PT Serif` → `Georgia` → `DejaVu Serif` (matplotlib-bundled, always
  available). Kicker is the serif stack's bold sans companion in practice
  (see `components.header`) — small caps, terracotta, with the `▪` mark.
- **Everything else** (dek, axis, ticks, legend, footer): sans —
  `IBM Plex Sans` → `Inter` → `Arial` → `DejaVu Sans`.
- Install `Source Serif 4` and `IBM Plex Sans` (both free, Google Fonts) for
  the full effect; the style degrades cleanly to bundled fonts without them.

## Chart anatomy (every chart, every time)

1. **Header** — `▪ KICKER` in terracotta small caps, then a serif headline
   phrased as a finding ("Growth cooled in Q3"), then an optional sans dek
   with the exact metric/period. The **Waltzing Analytics** wordmark (bold
   italic serif) sits top right, always — `components.header()` draws it
   automatically; call `components.brand_mark()` directly for any chart
   that skips `header()`.
2. **Plot** — warm paper surface, no border box, baseline only, hairline
   horizontal gridlines behind the data, thin 2px marks with rounded caps.
3. **Emphasis** — one series/category in terracotta (or ink blue if
   terracotta is reserved elsewhere on the same page); everything else in
   shared axis-gray. Direct-label the emphasized mark instead of a legend
   box when there are ≤ 3 lines.
4. **Footer** — hairline rule, `Source: …` in muted ink (bottom left),
   and `Marc Lamberts | Created on dd-mm-yyyy` (bottom right, today's date
   filled in automatically at render time) — always, on every chart.
5. **Dark mode** is a selected alternative, not an automatic invert — use
   `style.apply("dark")`, which swaps to the validated dark steps and the
   dark surface, never a CSS-filter-style flip.

## Branding (fixed, on every chart)

- **Top right:** `Waltzing Analytics` wordmark — `components.brand_mark()`,
  called automatically by `components.header()`.
- **Bottom right:** `Marc Lamberts | Created on dd-mm-yyyy` —
  `components.footer()`, date computed from the system clock at render
  time (`datetime.date.today()`), never hardcoded.

## Usage

```python
from housestyle import style, components

palette, cats = style.apply("light")  # or "dark" — sets rcParams globally

fig = plt.figure(figsize=(8, 5.2))
ax = fig.add_axes([0.08, 0.16, 0.86, 0.58])  # reserve header/footer bands
ax.plot(x, y1)
ax.plot(x, y2)
components.highlight_lines(ax, accent_index=1, palette=palette)
components.header(fig, kicker="Revenue", title="…", dek="…", palette=palette)
components.footer(fig, source="…", palette=palette)
fig.savefig("chart.png", facecolor=fig.get_facecolor())
```

See `examples/line_highlight.py` and `examples/bar_highlight.py` for
complete, runnable charts. Run `python examples/generate_all.py` to
regenerate all four reference PNGs in `examples/output/`.

## Rules that don't change per chart type

- One y-axis, always. Two measures of different scale get two charts, small
  multiples, or a common index — never a second axis.
- Categorical color follows the entity, never its sort rank; a filter that
  drops a series must not repaint the survivors.
- A legend box is optional for ≤ 3 direct-labeled series; required for more.
- Never fabricate a 9th categorical color — fold into "Other" or facet.
- Re-run `validate_palette.js` before adding or reordering any categorical
  hex (see the docstring in `housestyle/colors.py` for the exact commands).
