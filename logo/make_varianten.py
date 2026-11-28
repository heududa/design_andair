#!/usr/bin/env python3
"""Varianten des ANDAIR-Logos (beide A als Zeichen) zum Vergleich. Aufruf: python3 logo/make_varianten.py"""
import re
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
HERE = Path(__file__).resolve().parent
OUT = HERE / 'varianten'
RED, INK = '#D7261E', '#141516'
FONTS = {}
def font(w):
    if w not in FONTS:
        f = instancer.instantiateVariableFont(TTFont(HERE.parent / 'assets/fonts/instrument-sans.woff2'), {'wght': w})
        FONTS[w] = (f.getGlyphSet(), f.getBestCmap(), f['head'].unitsPerEm, f['hmtx'], f['OS/2'].sCapHeight / f['head'].unitsPerEm)
    return FONTS[w]
def rnd(d):
    return re.sub(r'-?\d+\.\d+', lambda m: ('%.1f' % float(m.group())).rstrip('0').rstrip('.'), d)
def word(txt, size, x0, baseline, track, wght):
    gs, cmap, upm, hmtx, _ = font(wght); s = size / upm; x = x0; out = []
    for ch in txt:
        g = cmap[ord(ch)]; pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, baseline)))
        out.append(pen.getCommands()); x += hmtx[g][0] * s + track * size
    return rnd(' '.join(out)), x - x0 - track * size

def roof(B, w):
    """Dach auf 256er Raster, Hoehe 192 (y 32..224): B = halbe Fussbreite, w = Schenkelbreite."""
    slope = (B - w / 2) / 192; yin = 224 - (B - w) / slope; c = 128
    return f'M{c - w / 2:g} 32H{c + w / 2:g}L{c + B:g} 224H{c + B - w:g}L{c} {yin:.1f}L{c - B + w:g} 224H{c - B:g}Z', 2 * B

def logo(name, B=120, w=48, mark='dot', r=30, cy=194, roof_col=RED, mark_col=INK, ink=INK, wght=700, track=0.03, second='full'):
    d_roof, width = roof(B, w)
    SIZE, BASE, PAD = 220, 208, 28
    CAP = font(wght)[4]; K = SIZE * CAP / 192; sy = BASE - 224 * K
    def sym(x, with_mark=True):
        m = ''
        if with_mark:
            m = (f'<circle cx="128" cy="{cy}" r="{r}" fill="{mark_col}"/>' if mark == 'dot'
                 else f'<rect x="{128 - r}" y="{224 - 2 * r}" width="{2 * r}" height="{2 * r}" fill="{mark_col}"/>')
        return f'<g transform="translate({x - (128 - B) * K:g} {sy:g}) scale({K:g})"><path fill="{roof_col}" d="{d_roof}"/>{m}</g>'
    gap = SIZE * (0.035 + track * 0.5)
    x = PAD; parts = [sym(x)]; x += width * K + gap
    d1, w1 = word('ND', SIZE, x, BASE, track, wght); parts.append(f'<path fill="{ink}" d="{d1}"/>'); x += w1 + gap
    parts.append(sym(x, second == 'full')); x += width * K + gap
    d2, w2 = word('IR', SIZE, x, BASE, track, wght); parts.append(f'<path fill="{ink}" d="{d2}"/>'); x += w2
    W = round(x + PAD); top = BASE - SIZE * CAP - PAD
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {round(BASE + PAD - top)}" width="{W}" height="{round(BASE + PAD - top)}" role="img" aria-labelledby="t">'
           f'<title id="t">Andair</title><g transform="translate(0 {-top:g})">{"".join(parts)}</g></svg>\n')
    (OUT / f'{name}.svg').write_text(svg, encoding='utf-8')

logo('1-original')
logo('2-punkte-rot', roof_col=INK, mark_col=RED)
logo('3-schmal', B=94, w=46, r=22, cy=202)
logo('4-punkt-hoch', r=22, cy=150)
logo('5-tor', mark='tor', r=26)
logo('6-leicht', B=114, w=34, r=24, cy=200, wght=500, track=0.07)
logo('7-ein-punkt', second='roof')
logo('8-einfarbig-rot', roof_col=RED, mark_col=RED, ink=RED)
print(sorted(p.name for p in OUT.glob('*.svg')))
