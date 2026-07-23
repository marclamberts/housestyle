"""Line chart: one highlighted series + muted context lines + direct end labels.
Demonstrates the header/footer anatomy and the highlight-one convention."""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from housestyle import style, components
from housestyle.colors import LIGHT


def make(mode="light", outfile="output/line_highlight.png"):
    palette, _ = style.apply(mode)

    quarters = np.arange(2023.0, 2026.26, 0.25)
    rng = np.random.default_rng(7)
    meridian = 100 + np.cumsum(rng.normal(1.6, 1.1, len(quarters)))
    peer_a = 100 + np.cumsum(rng.normal(0.7, 1.0, len(quarters)))
    peer_b = 100 + np.cumsum(rng.normal(0.9, 1.3, len(quarters)))
    peer_c = 100 + np.cumsum(rng.normal(0.4, 0.9, len(quarters)))

    fig = plt.figure(figsize=(8, 5.2))
    ax = fig.add_axes([0.08, 0.16, 0.86, 0.58])  # leave room for header/footer

    for series in (peer_a, peer_b, peer_c, meridian):
        ax.plot(quarters, series)

    components.highlight_lines(ax, accent_index=3, palette=palette)

    for arr, label in ((peer_a, "Peer A"), (peer_b, "Peer B"), (peer_c, "Peer C")):
        ax.annotate(label, xy=(quarters[-1], arr[-1]), xytext=(6, 0),
                    textcoords="offset points", va="center", fontsize=8.5,
                    color=palette["ink_muted"])
    components.label_endpoint(ax, quarters[-1], meridian[-1], "Meridian",
                               palette["accent"], palette=palette)

    ax.set_ylabel("Indexed revenue (2023 Q1 = 100)")
    ax.set_xlim(quarters[0], quarters[-1] + 0.6)
    ax.margins(y=0.12)

    components.header(
        fig,
        kicker="Revenue",
        title="Growth cooled in Q3, but Meridian stayed ahead of peers",
        dek="Indexed quarterly revenue, 2023–2026",
        palette=palette,
    )
    components.footer(fig, source="Company filings; Meridian analysis", palette=palette)

    fig.savefig(Path(__file__).parent / outfile, facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__ == "__main__":
    make("light", "output/line_highlight_light.png")
    make("dark", "output/line_highlight_dark.png")
