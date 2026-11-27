#!/usr/bin/env python3
"""Macht aus jeder Variante eine einzige, eigenstaendige HTML-Datei (Schriften und Bilder eingebettet).
Aufruf: python3 build/inline.py  ->  dist/<variante>.html"""
import base64, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
MIME = {".jpg": "image/jpeg", ".png": "image/png", ".woff2": "font/woff2"}
(ROOT / "dist").mkdir(exist_ok=True)
for v in ("a-werkplan", "b-bunker", "c-editorial"):
    html = (ROOT / "varianten" / v / "index.html").read_text(encoding="utf-8")
    def data(m):
        f = ROOT / "assets" / m.group(1)
        return f"data:{MIME[f.suffix]};base64," + base64.b64encode(f.read_bytes()).decode()
    out = re.sub(r"\.\./\.\./assets/([\w./-]+)", data, html)
    (ROOT / "dist" / f"{v}.html").write_text(out, encoding="utf-8")
    print(v, len(out) // 1024, "KB", "rest:", out.count("../../assets"))
