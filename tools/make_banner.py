# -*- coding: utf-8 -*-
"""Generate the profile hero banner: deep-navy network topology, bilingual."""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "banner.png"

# Logical design canvas; render at 2x for crisp text and thin lines.
W, H = 1280, 340
S = 2
RW, RH = W * S, H * S

FONT_DIR = Path("C:/Windows/Fonts")
FONT_LATIN_BOLD = FONT_DIR / "segoeuib.ttf"
FONT_LATIN = FONT_DIR / "segoeui.ttf"
FONT_MONO = FONT_DIR / "consola.ttf"
FONT_MONO_BOLD = FONT_DIR / "consolab.ttf"
FONT_CN_BOLD = FONT_DIR / "msyhbd.ttc"
FONT_CN = FONT_DIR / "msyh.ttc"

CYAN = (34, 211, 238)
SKY = (56, 189, 248)
BLUE = (59, 130, 246)
WHITE = (248, 250, 252)
SLATE = (148, 163, 184)
MUTED = (100, 116, 139)


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size * S)


def radial_glow(xx: np.ndarray, yy: np.ndarray, cx: float, cy: float, sigma: float) -> np.ndarray:
    d2 = (xx - cx) ** 2 + (yy - cy) ** 2
    return np.exp(-d2 / (2.0 * sigma * sigma))


def make_background() -> Image.Image:
    yy, xx = np.mgrid[0:RH, 0:RW].astype(np.float32)
    xn = xx / (RW - 1)
    yn = yy / (RH - 1)

    # Diagonal gradient: near-black -> petrol blue.
    t = np.clip(0.58 * xn + 0.42 * yn, 0.0, 1.0)
    c0 = np.array([4, 7, 13], dtype=np.float32)
    c1 = np.array([7, 24, 40], dtype=np.float32)
    c2 = np.array([9, 38, 58], dtype=np.float32)
    arr = np.zeros((RH, RW, 3), dtype=np.float32)
    m = t < 0.62
    u = (t[m] / 0.62)[:, None]
    arr[m] = c0 * (1 - u) + c1 * u
    u = ((t[~m] - 0.62) / 0.38)[:, None]
    arr[~m] = c1 * (1 - u) + c2 * u

    # Cyan bloom on the right, faint blue bloom lower-left.
    g1 = radial_glow(xx, yy, 0.80 * RW, 0.36 * RH, 0.20 * RW)
    arr += g1[..., None] * np.array([10, 62, 76], dtype=np.float32)
    g2 = radial_glow(xx, yy, 0.55 * RW, 0.95 * RH, 0.28 * RW)
    arr += g2[..., None] * np.array([8, 22, 60], dtype=np.float32)

    # Vignette.
    vx = (xx - RW / 2) / (RW / 2)
    vy = (yy - RH / 2) / (RH / 2)
    vig = np.clip(1.0 - 0.30 * (vx * vx + vy * vy), 0.55, 1.0)
    arr *= vig[..., None]

    # Fine noise keeps the large gradient from banding.
    rng = np.random.default_rng(7)
    arr += rng.normal(0.0, 2.0, (RH, RW, 1))
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, "RGB").convert("RGBA")


def draw_grid(img: Image.Image) -> None:
    grid = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid)
    step = 64 * S
    for x in range(0, RW, step):
        gd.line([(x, 0), (x, RH)], fill=(125, 211, 252, 255), width=1)
    for y in range(0, RH, step):
        gd.line([(0, y), (RW, y)], fill=(125, 211, 252, 255), width=1)

    yy, xx = np.mgrid[0:RH, 0:RW].astype(np.float32)
    # Fade grid out on the left so the type stays clean.
    mask = np.clip((xx / RW - 0.06) / 0.55, 0, 1)
    mask = (mask * 20).astype(np.uint8)
    grid.putalpha(Image.fromarray(mask, "L"))
    img.alpha_composite(grid)


def draw_network(img: Image.Image) -> None:
    n = lambda x, y: (x * S, y * S)  # noqa: E731
    nodes = {
        "a": (820, 78),
        "b": (930, 48),
        "c": (1040, 92),
        "d": (1160, 58),
        "e": (1222, 140),
        "f": (1100, 178),
        "g": (980, 148),
        "h": (860, 190),
        "i": (900, 268),
        "j": (1030, 282),
        "k": (1150, 250),
        "l": (1232, 300),
        "m": (786, 290),
        "n": (960, 220),
        "o": (1080, 118),
        "p": (1200, 210),
        "q": (1008, 38),
        "r": (880, 130),
    }
    edges = [
        ("a", "b"), ("a", "h"), ("a", "r"),
        ("b", "q"), ("b", "c"), ("b", "g"),
        ("c", "d"), ("c", "o"), ("c", "q"),
        ("d", "e"), ("d", "o"), ("d", "p"),
        ("e", "f"), ("e", "p"), ("e", "k"),
        ("f", "g"), ("f", "j"), ("f", "k"), ("f", "o"),
        ("g", "h"), ("g", "n"), ("g", "o"),
        ("h", "i"), ("h", "m"), ("h", "r"),
        ("i", "j"), ("i", "m"),
        ("j", "k"), ("j", "n"),
        ("k", "l"), ("k", "p"),
        ("n", "f"), ("n", "j"),
        ("o", "p"),
    ]

    line_layer = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    ld = ImageDraw.Draw(line_layer)
    for idx, (u, v) in enumerate(edges):
        p1, p2 = n(*nodes[u]), n(*nodes[v])
        # Alternate cool hues; a couple of brighter backbone links.
        col = (34, 211, 238) if idx % 3 else (56, 189, 248)
        alpha = 95 if idx % 4 else 135
        width = 2 if idx % 5 else 3
        ld.line([p1, p2], fill=col + (alpha,), width=width * S)

    glow = line_layer.filter(ImageFilter.GaussianBlur(7 * S))
    img.alpha_composite(glow)
    img.alpha_composite(line_layer)

    # Node halos.
    halo = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    hd = ImageDraw.Draw(halo)
    hubs = {"g", "f", "o", "k"}
    for key, (x, y) in nodes.items():
        p = n(x, y)
        r = (10 if key in hubs else 6) * S
        col = CYAN if key in hubs else SKY
        hd.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=col + (120,))
    img.alpha_composite(halo.filter(ImageFilter.GaussianBlur(10 * S)))

    nd = ImageDraw.Draw(img)
    for key, (x, y) in nodes.items():
        p = n(x, y)
        core_r = (4.2 if key in hubs else 2.8) * S
        col = (236, 254, 255) if key in hubs else (186, 230, 253)
        nd.ellipse([p[0] - core_r, p[1] - core_r, p[0] + core_r, p[1] + core_r], fill=col + (255,))
        if key in hubs:
            ring_r = 15 * S
            nd.ellipse(
                [p[0] - ring_r, p[1] - ring_r, p[0] + ring_r, p[1] + ring_r],
                outline=CYAN + (95,),
                width=max(1, S),
            )
            nd.ellipse(
                [p[0] - 23 * S, p[1] - 23 * S, p[0] + 23 * S, p[1] + 23 * S],
                outline=CYAN + (32,),
                width=max(1, S),
            )

    # Small coordinate ticks near two hubs: a subtle instrument-panel cue.
    for key, dx, dy, label in (("d", 16, -30, "AS 100"), ("k", 18, 22, "AS 200")):
        x, y = nodes[key]
        px, py = n(x + dx, y + dy)
        f = font(FONT_MONO, 9)
        nd.text((px, py), label, font=f, fill=(103, 232, 249, 110))


def tracked(draw: ImageDraw.ImageDraw, xy, text, fnt, fill, tracking=0):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking * S
    return x


def draw_text(img: Image.Image) -> None:
    layer = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)

    # Accent rule.
    bar_x = 78 * S
    for i in range(150 * S):
        t = i / max(1, 150 * S - 1)
        col = (
            int(CYAN[0] * (1 - t) + BLUE[0] * t),
            int(CYAN[1] * (1 - t) + BLUE[1] * t),
            int(CYAN[2] * (1 - t) + BLUE[2] * t),
            255,
        )
        d.line([(bar_x, (92 * S) + i), (bar_x + 3 * S, (92 * S) + i)], fill=col)

    # Eyebrow.
    f_label = font(FONT_MONO, 12)
    d.ellipse(
        [108 * S, 64 * S, 115 * S, 71 * S],
        fill=CYAN + (255,),
    )
    tracked(d, (124 * S, 58 * S), "GITHUB PROFILE  /  NETWORK & CODE", f_label, (103, 232, 249, 235), 2.0)

    # Name on its own layer so only the name gets a controlled cyan bloom.
    name_layer = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    nd = ImageDraw.Draw(name_layer)
    f_name = font(FONT_LATIN_BOLD, 66)
    nd.text((105 * S, 87 * S), "FENG WANYI", font=f_name, fill=WHITE + (255,))

    # Chinese positioning line.
    f_cn = font(FONT_CN_BOLD, 23)
    d.text((107 * S, 190 * S), "网络工程  ·  全栈开发  ·  交互式仿真", font=f_cn, fill=(226, 232, 240, 255))

    # English positioning line.
    f_en = font(FONT_LATIN, 14)
    d.text(
        (107 * S, 231 * S),
        "Network Engineering   ·   Full-stack Development   ·   Interactive Simulation",
        font=f_en,
        fill=(148, 163, 184, 255),
    )

    # Hairline.
    d.line([(107 * S, 272 * S), (700 * S, 272 * S)], fill=(56, 189, 248, 80), width=S)

    # Footer line.
    f_small = font(FONT_MONO, 11)
    d.text((107 * S, 288 * S), "Xi'an Shiyou University", font=f_small, fill=(148, 163, 184, 220))
    d.ellipse([352 * S, 294 * S, 356 * S, 298 * S], fill=CYAN + (210,))
    d.text((366 * S, 288 * S), "github.com/alicefw1", font=f_small, fill=(148, 163, 184, 220))

    # Coordinates, bottom right.
    f_tiny = font(FONT_MONO, 9)
    d.text((1120 * S, 306 * S), "34.34N  108.94E", font=f_tiny, fill=(100, 116, 139, 150))

    # Cyan bloom behind the name only, then the crisp type.
    name_alpha = name_layer.split()[3].point(lambda v: int(v * 0.50))
    bloom = Image.new("RGBA", (RW, RH), CYAN + (0,))
    bloom.putalpha(name_alpha)
    img.alpha_composite(bloom.filter(ImageFilter.GaussianBlur(8 * S)))
    img.alpha_composite(layer)
    img.alpha_composite(name_layer)

    # Corner brackets.
    od = ImageDraw.Draw(img)
    o = 26 * S
    ln = 22 * S
    col = (34, 211, 238, 95)
    od.line([(o, o), (o + ln, o)], fill=col, width=S)
    od.line([(o, o), (o, o + ln)], fill=col, width=S)
    od.line([(RW - o, RH - o), (RW - o - ln, RH - o)], fill=col, width=S)
    od.line([(RW - o, RH - o), (RW - o, RH - o - ln)], fill=col, width=S)


def main() -> None:
    img = make_background()
    draw_grid(img)
    draw_network(img)
    draw_text(img)
    img = img.convert("RGB").resize((W, H), Image.Resampling.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} ({OUT.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
