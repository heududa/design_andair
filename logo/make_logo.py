#!/usr/bin/env python3
"""Andair-Logo (Dach ueber Punkt als A): erzeugt alle SVG-Varianten.
Schriftzug: Instrument Sans Bold (SIL Open Font License), in Pfade umgewandelt.
Aufruf: python3 logo/make_logo.py   (braucht fonttools und brotli)"""
import re
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
HERE = Path(__file__).resolve().parent
OUT = HERE / 'svg'
RED, INK, WHITE = '#D7261E', '#141516', '#FFFFFF'
f = instancer.instantiateVariableFont(TTFont(HERE.parent / 'assets/fonts/instrument-sans.woff2'), {'wght': 700})
gs, cmap, upm, hmtx = f.getGlyphSet(), f.getBestCmap(), f['head'].unitsPerEm, f['hmtx']
CAP = f['OS/2'].sCapHeight / upm

def rnd(d):
    return re.sub(r'-?\d+\.\d+', lambda m: ('%.1f' % float(m.group())).rstrip('0').rstrip('.'), d)
def word(txt, size, x0, baseline, track=-0.02):
    s = size / upm; x = x0; out = []
    for ch in txt:
        g = cmap[ord(ch)]; pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, baseline)))
        out.append(pen.getCommands()); x += hmtx[g][0] * s + track * size
    return rnd(' '.join(out)), x - x0 - track * size

# Zeichen auf 256er Raster: Schenkel 48 breit, Steigung 1:2, Punkt r=30 auf der Grundlinie
ROOF = 'M104 32H152L248 224H200L128 80L56 224H8Z'
DOT = (128, 194, 30)
def symbol(roof, dot, dx=0, dy=0, k=1.0):
    t = f' transform="translate({dx:g} {dy:g}) scale({k:g})"' if (dx or dy or k != 1) else ''
    return (f'<g id="symbol"{t}><path fill="{roof}" d="{ROOF}"/>'
            f'<circle cx="{DOT[0]}" cy="{DOT[1]}" r="{DOT[2]}" fill="{dot}"/></g>')
def svg(inner, w, h, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" width="{w:g}" height="{h:g}" role="img" aria-labelledby="t">'
            f'<title id="t">{title}</title>{inner}</svg>\n')
def save(name, content):
    (OUT / name).write_text(content, encoding='utf-8')

SCHEMES = {  # name: (dach, punkt, schrift)
    'farbe': (RED, INK, INK), 'negativ': (RED, WHITE, WHITE),
    'schwarz': (INK, INK, INK), 'weiss': (WHITE, WHITE, WHITE), 'rot': (RED, RED, RED),
}
SIZE = 220                       # Schriftgroesse
CAPH = SIZE * CAP                # Versalhoehe
K = CAPH / 192                   # das Zeichen ersetzt das A: genau so hoch wie die Versalien
BASE = 208                       # Grundlinie
PAD = 28
for name, (roof, dot, ink) in SCHEMES.items():
    # nur Zeichen
    save(f'andair-zeichen-{name}.svg', svg(symbol(roof, dot), 256, 256, 'Andair Zeichen'))
    # Logo: das Zeichen steht als A vor "ndair", auf derselben Grundlinie
    sx = PAD - 8 * K; sy = BASE - 224 * K
    x_n = PAD + 240 * K + SIZE * 0.012          # das n rueckt nah an den rechten Schenkel
    d, w = word('ndair', SIZE, x_n, BASE)
    W = round(x_n + w + PAD); H = round(BASE + PAD + SIZE * 0.02)
    top = BASE - CAPH - SIZE * 0.06 - PAD        # Oberkante: Oberlaengen von d und i
    inner = f'<g transform="translate(0 {-top:g})">' + symbol(roof, dot, sx, sy, K) + f'<path id="wordmark" fill="{ink}" d="{d}"/></g>'
    save(f'andair-logo-{name}.svg', svg(inner, W, round(H - top), 'Andair'))
# App-Symbol und Favicon: weisses Zeichen im roten Feld, fuer kleine Groessen kraeftiger
def tile(rx, k, dot_r):
    c = f'<rect width="256" height="256" rx="{rx}" fill="{RED}"/>'
    c += (f'<g transform="translate({128 - 128 * k:g} {124 - 128 * k:g}) scale({k:g})"><path fill="#fff" d="{ROOF}"/>'
          f'<circle cx="128" cy="{224 - dot_r}" r="{dot_r}" fill="#fff"/></g>')
    return c
save('andair-app-symbol.svg', svg(tile(56, 0.62, 30), 256, 256, 'Andair'))
save('andair-favicon.svg', svg(tile(40, 0.74, 34), 256, 256, 'Andair'))
print(len(list(OUT.glob('*.svg'))), 'SVG; Versalhoehe', round(CAP, 3))
