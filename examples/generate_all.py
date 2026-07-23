"""Regenerate every example chart under examples/output/."""
import line_highlight
import bar_highlight

if __name__ == "__main__":
    line_highlight.make("light", "output/line_highlight_light.png")
    line_highlight.make("dark", "output/line_highlight_dark.png")
    bar_highlight.make("light", "output/bar_highlight_light.png")
    bar_highlight.make("dark", "output/bar_highlight_dark.png")
    print("Rendered 4 example charts to examples/output/")
