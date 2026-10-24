# -*- coding: utf-8 -*-
"""A soft cyan-to-blue hairline used between README sections."""
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "rule.png"
W, H = 1200, 8

x = np.linspace(0, 1, W)
alpha = np.sin(np.pi * x) ** 1.6
rgb = np.zeros((H, W, 3), dtype=np.float32)
for i in range(W):
    t = x[i]
    rgb[:, i] = np.array([34, 211, 238]) * (1 - t) + np.array([59, 130, 246]) * t
arr = np.zeros((H, W, 4), dtype=np.uint8)
arr[..., :3] = np.clip(rgb, 0, 255).astype(np.uint8)
arr[..., 3] = (alpha * 120).astype(np.uint8)[None, :]

img = Image.fromarray(arr, "RGBA")
# A faint bloom under the hairline.
bloom = img.filter(ImageFilter.GaussianBlur(2))
out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
out.alpha_composite(bloom)
out.alpha_composite(img)
OUT.parent.mkdir(parents=True, exist_ok=True)
out.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
