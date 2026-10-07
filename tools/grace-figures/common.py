"""Shared drawing helpers for the GRACE documentation diagrams."""
import math, subprocess, pathlib

FONT = "Helvetica, Arial, sans-serif"
C = dict(
    navy="#1f3a5f", blue="#2b6cb0", lightblue="#bee3f8", teal="#2c7a7b",
    orange="#dd6b20", red="#c53030", gray="#718096", darkgray="#4a5568",
    lightgray="#e2e8f0", ground="#e6dcc6", groundline="#a89474",
    gold="#d69e2e", sky="#f7fafc", green="#68a063",
)
OUT = pathlib.Path(__file__).resolve().parents[2] / "docs" / "static" / "images" / "grace"
INKSCAPE = "/Applications/Inkscape.app/Contents/MacOS/inkscape"


def text(x, y, s, size=14, anchor="middle", weight="normal", fill=None, style="", italic=False):
    fill = fill or C["darkgray"]
    fs = "italic" if italic else "normal"
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" font-style="{fs}" text-anchor="{anchor}" fill="{fill}" {style}>{s}</text>')


def arrow_defs():
    out = ["<defs>"]
    for name, col in C.items():
        out.append(
            f'<marker id="ah-{name}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker>')
    out.append("</defs>")
    return "\n".join(out)


def line(x1, y1, x2, y2, col="darkgray", w=1.5, dash=None, head=False, tail=False, opacity=1):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    h = f' marker-end="url(#ah-{col})"' if head else ""
    t = f' marker-start="url(#ah-{col})"' if tail else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{C[col]}" '
            f'stroke-width="{w}" stroke-linecap="round" opacity="{opacity}"{d}{h}{t}/>')


def svg_doc(w, h, body, title):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">\n'
            f'<title>{title}</title>\n{arrow_defs()}\n'
            f'<rect width="{w}" height="{h}" fill="white"/>\n{body}\n</svg>\n')


def save(name, svg):
    """Write the editable SVG to diagrams/ and a 2x PNG next to the pages' other images."""
    src = OUT / "diagrams" / f"{name}.svg"
    src.write_text(svg)
    png = OUT / f"{name}.png"
    subprocess.run([INKSCAPE, str(src), "--export-type=png", f"--export-filename={png}",
                    "--export-dpi=192", "--export-background=white"], check=True,
                   capture_output=True)
    return png
