"""Bar chart: one highlighted category + muted context bars.
Demonstrates the header/footer anatomy on a categorical comparison."""
import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from housestyle import style, components


def make(mode="light", outfile="output/bar_highlight.png"):
    palette, _ = style.apply(mode)

    regions = ["North\nAmerica", "EMEA", "APAC", "LatAm", "Other"]
    growth = [4.2, 11.6, 6.8, 3.1, 2.4]
    accent_index = 1  # EMEA

    fig = plt.figure(figsize=(7.5, 5.0))
    ax = fig.add_axes([0.08, 0.16, 0.86, 0.58])

    container = ax.bar(regions, growth, width=0.6)
    components.highlight_bars(container, accent_index, palette=palette)

    for i, (rect, value) in enumerate(zip(container.patches, growth)):
        color = palette["accent"] if i == accent_index else palette["ink_secondary"]
        weight = "bold" if i == accent_index else "normal"
        ax.annotate(f"{value:.1f}%", xy=(rect.get_x() + rect.get_width() / 2, value),
                    xytext=(0, 4), textcoords="offset points", ha="center",
                    fontsize=9.5, color=color, fontweight=weight)

    ax.set_ylabel("YoY revenue growth")
    ax.set_ylim(0, max(growth) * 1.25)

    components.header(
        fig,
        kicker="Regions",
        title="EMEA is the standout region this quarter",
        dek="Year-over-year revenue growth by region, Q3 2026",
        palette=palette,
    )
    components.footer(fig, source="Company filings; Meridian analysis", palette=palette)

    fig.savefig(Path(__file__).parent / outfile, facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__ == "__main__":
    make("light", "output/bar_highlight_light.png")
    make("dark", "output/bar_highlight_dark.png")
