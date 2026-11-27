#!/usr/bin/env python3
"""Erzeugt die drei Startseiten-Varianten (DE + EN) fuer andair.ch.

Aufruf:  python3 build/build.py
Ausgabe: varianten/a-werkplan, varianten/b-bunker, varianten/c-editorial, index.html
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
A = "../../assets"


def t(de, en):
    return f'<span class="de" lang="de">{de}</span><span class="en" lang="en">{en}</span>'


# ---------- Inhalte (von andair.ch uebernommen) ----------
NAV = [
    ("#schutzraum", "Schutzraumtechnik", "Shelter technology"),
    ("#produkte", "Produkte", "Products"),
    ("#schall", "Schall und Schwingung", "Sound and vibration"),
    ("#lufttechnik", "Lufttechnik", "Ventilation"),
    ("#firma", "Firma", "Company"),
]
AREA_HREF = ["#schutzraum", "#schall", "#lufttechnik"]
H1 = ("Schutzraumtechnik aus der Schweiz. Seit 1968.", "Shelter technology from Switzerland. Since 1968.")
LEAD = (
    "Andair entwickelt und fertigt Explosionsschutzventile, ABC-Filter und Lüftungsanlagen für Schutzräume. "
    "Mehr als 3’000 geschützte Grossanlagen in über 55 Ländern sind damit ausgerüstet.",
    "Andair engineers and manufactures explosion protection valves, NBC filters and ventilation systems for shelters. "
    "More than 3,000 large protected installations in over 55 countries are equipped with them.",
)
FACTS = [
    ("1968", "1968", "Gegründet in der Schweiz", "Founded in Switzerland"),
    ("3’000+", "3,000+", "geschützte Grossanlagen", "large protected installations"),
    ("55+", "55+", "Länder weltweit", "countries worldwide"),
    ("ISO 9001", "ISO 9001", "zertifiziert nach 9001:2015", "certified to 9001:2015"),
]
AREAS = [
    ("Schutzraumtechnik", "Shelter technology",
     "In keinem Bereich ist kompromisslose Sicherheit wichtiger als hier. Geprüft, genehmigt, garantiert.",
     "No other area needs such uncompromising safety. Tested, approved, certified."),
    ("Schall- und Schwingungstechnik", "Sound and vibration damping",
     "Langjährige Erfahrung in modernster Schall- und Schwingungstechnik: innovative Lösungen mit Leistungsgarantie.",
     "Long experience in state-of-the-art sound and vibration protection: innovative, reliable solutions."),
    ("Lufttechnik Komponenten", "Ventilation components",
     "Belüftungstechnik stellt komplexe Anforderungen und verlangt Spezialisten. Wir garantieren Know-how und Top-Qualität.",
     "Ventilation makes high demands and requires specialists. We guarantee know-how and top quality."),
]
PRODUCTS = [
    ("ESV 4", "Explosionsschutzventile", "Explosion protection valves", "esv-red.jpg",
     "Druckfester Verschluss von Zu- und Abluftöffnungen in Schutzräumen, Raffinerien, Kontrollräumen und auf Bohrinseln.",
     "Pressure-resistant closure of air inlets and outlets in shelters, refineries, control rooms and oil rigs."),
    ("GF 600", "ABC-Gasfilter", "NBC gas filter", "gasfilter.jpg",
     "Schützt vor allen heute bekannten chemischen und biologischen Kampfstoffen. Baureihe von 20 bis 1500 m³/h.",
     "Protects against all chemical and biological warfare agents known today. Range from 20 to 1500 m³/h."),
    ("GAK-D", "Gasdichte Absperrklappe", "Gastight shut-off valve", "gak-d.jpg",
     "Sperrt den Luftstrom im Kanalsystem ab oder schaltet ihn um. Als Doppelklappe für Kanäle am Gasfilter vorbei.",
     "Shuts off or changes over the air flow in a ducting system. As a double valve for ducts that bypass the gas filter."),
    ("EMP", "EMP-Türen und Luken", "EMP doors and hatches", "emp-door.jpg",
     "Für Gebäude, Container und Räume, die gegen elektromagnetische Impulse abgeschirmt werden, inklusive HPM.",
     "For buildings, containers and rooms shielded against electromagnetic pulse, including HPM."),
]
APPS = [
    ("Zivile Schutzräume und Bunker", "Civil defence shelters"),
    ("Streit- und Verteidigungskräfte, Armee", "Air raid shelters"),
    ("Geschützte Produktionsstätten", "Hardened underground facilities"),
    ("C4ISTAR-Schutzräume", "C4ISTAR facilities"),
    ("NBC-geschützte Anlagen und Bio-Sicherheitslabors", "NBC protected facilities and bio safety labs"),
    ("Raffinerien und Ölfelder, Off-Shore-Plattformen", "Refineries, oil fields, offshore platforms"),
    ("Chemische und petrochemische Anlagen", "Chemical and petrochemical plants"),
    ("Kernkraftwerke", "Nuclear power plants"),
]
SPIEZ = (
    "Typengetestet und anerkannt durch das Labor Spiez vom Schweizerischen Bundesamt für Bevölkerungsschutz.",
    "Type tested and approved by the SPIEZ LABORATORY of the Swiss Federal Department of Defence.",
)
ABOUT = (
    "Andair wurde 1968 gegründet und ist der kompetente Spezialist für Schutzraumtechnik. "
    "Kleine und grosse Anlagen werden mit dem Andair-Produktsortiment erfolgreich vor vielen Bedrohungen und Gefahren geschützt und belüftet.",
    "Andair was founded in 1968 and is the competent specialist in shelter technology. "
    "With the Andair range of products, large and small shelters are ventilated and successfully protected against many threats.",
)
MOTTO = [("Sicher", "Safe"), ("Einfach", "Simple"), ("Robust", "Rugged")]
CLAIM = ("Wir übernehmen Verantwortung. Wir schützen Leben.", "We take responsibility. We ensure life protection.")
FLOW = [
    ("Bedrohungen", "Threats",
     [("Konventionelle Kriegsführung", "Conventional warfare"), ("Nukleare Kriegsführung", "Nuclear warfare"),
      ("Industrieunfälle", "Industrial accidents"), ("Sabotage und Terrorismus", "Sabotage and terrorism"),
      ("Erdbeben", "Earthquake"), ("Betriebsausfälle", "Breakdowns")]),
    ("Gefährdet sind", "Endangering of",
     [("Bevölkerung", "Population"), ("Anlagen und Infrastruktur", "Facilities and infrastructure"),
      ("Streitkräfte", "Armed and military forces"), ("Güter", "Goods"),
      ("Kulturgüter", "Cultural assets"), ("Versorgungssysteme", "Supply systems")]),
    ("Schutz für", "Shelter requirements for",
     [("Zivilschutzanlagen", "Civil defence shelters"), ("Kommandoposten", "Command posts"),
      ("Notspitäler", "Emergency hospitals"), ("Kommunikationszentralen", "Communication centers"),
      ("Kernkraftwerke", "Nuclear power stations"), ("Munition und Pyrotechnik", "Ammunition and pyrotechnics")]),
]
ALT = {
    "gak-d.jpg": ("Gasdichte Absperrklappe GAK-D mit Handhebel", "Gastight shut-off valve GAK-D with hand lever"),
    "esv-red.jpg": ("Explosionsschutzventil ESV 4", "Explosion protection valve ESV 4"),
    "gasfilter.jpg": ("ABC-Gasfilter GF 600", "NBC gas filter GF 600"),
    "emp-door.jpg": ("Rote EMP-Tür mit Stahlrahmen", "Red EMP door with steel frame"),
    "emp-dark.jpg": ("Rote EMP-Tür mit Stahlrahmen", "Red EMP door with steel frame"),
    "shelter.jpg": ("Rotes Panzertor am Eingang eines Schutzraums", "Red blast door at a shelter entrance"),
    "closures.jpg": ("Schutzraumabschluss mit Panzertür", "Shelter closure with blast door"),
    "pipes-strip.jpg": ("Lüftungsanlage mit Gasfiltern und grünen Rohrleitungen", "Ventilation plant with gas filters and green ducts"),
    "pipes.jpg": ("Grüne Lüftungsrohre einer Schutzanlage", "Green ventilation ducts of a protected installation"),
}
SIZE = {"gak-d.jpg": (900, 694), "esv-red.jpg": (400, 255), "gasfilter.jpg": (433, 650), "emp-door.jpg": (465, 650),
        "emp-dark.jpg": (312, 350), "shelter.jpg": (418, 350), "closures.jpg": (527, 600),
        "pipes-strip.jpg": (960, 172), "pipes.jpg": (440, 350)}


def img(name, cls="", eager=False):
    w, h = SIZE[name]
    de, _ = ALT[name]
    load = "" if eager else ' loading="lazy"'
    return f'<img src="{A}/img/{name}" width="{w}" height="{h}" alt="{de}"{load}{" class=" + chr(34) + cls + chr(34) if cls else ""}>'


ARROW = '<svg class="arr" viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'

BASE_CSS = """
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;font-family:var(--font-body);background:var(--bg);color:var(--ink);font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
img{display:block;max-width:100%;height:auto}
a{color:inherit;text-decoration:none}
h1,h2,h3,p,ul,ol,dl,dd,figure{margin:0}
ul,ol{padding:0;list-style:none}
button{font:inherit;color:inherit;background:none;border:0;padding:0;cursor:pointer}
html[data-lang=de] .en,html[data-lang=en] .de{display:none}
.wrap{width:100%;max-width:1320px;margin-inline:auto;padding-inline:clamp(20px,4vw,56px)}
.skip{position:absolute;left:16px;top:-60px;background:var(--ink);color:var(--bg);padding:10px 16px;z-index:100;transition:top .15s}
.skip:focus{top:12px}
:focus-visible{outline:2px solid var(--focus,var(--red));outline-offset:3px}
.arr{transition:transform .2s cubic-bezier(.2,.7,.2,1);flex:none}
a:hover .arr,button:hover .arr{transform:translateX(4px)}
.lang{display:inline-flex;gap:2px;font-size:13px;letter-spacing:.04em}
.lang button{padding:10px 8px;min-height:44px;opacity:.55;transition:opacity .15s}
.lang button:hover{opacity:1}
.lang button[aria-pressed=true]{opacity:1;text-decoration:underline;text-underline-offset:5px;text-decoration-thickness:2px;text-decoration-color:var(--red)}
.menu-btn{display:none;min-height:44px;padding:0 4px;font-size:15px}
@media (max-width:1080px){
  .menu-btn{display:inline-flex;align-items:center}
  header .nav-links{display:none;position:absolute;left:0;right:0;top:100%;flex-direction:column;align-items:stretch!important;gap:0!important;background:var(--bg);border-bottom:1px solid var(--line);padding:8px clamp(20px,4vw,56px) 20px}
  header .nav-links.open{display:flex}
  header .nav-links a{padding:14px 0;border-bottom:1px solid var(--line);font-size:18px}
}
h1,h2,h3{overflow-wrap:break-word}
@media (max-width:900px){h2,h3{hyphens:auto}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}html{scroll-behavior:auto}}
"""

JS = """
(function(){var h=document.documentElement,k='andair-lang',s=null;try{s=localStorage.getItem(k)}catch(e){}
function set(l){h.dataset.lang=l;h.lang=l;document.querySelectorAll('.lang button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.l===l)});
document.querySelectorAll('img[data-alt-'+l+']').forEach(function(i){i.alt=i.getAttribute('data-alt-'+l)});try{localStorage.setItem(k,l)}catch(e){}}
set(s==='en'?'en':'de');
document.querySelectorAll('.lang button').forEach(function(b){b.addEventListener('click',function(){set(b.dataset.l)})});
var pages=[].slice.call(document.querySelectorAll('[data-page]'));
function go(){var n=(location.hash||'#home').slice(1),p=document.getElementById(n);
if(!p||!p.hasAttribute('data-page')){if(document.querySelector('[data-page].on'))return;p=document.getElementById('home')}
pages.forEach(function(x){x.classList.toggle('on',x===p)});
document.querySelectorAll('.nav-links a').forEach(function(a){if(a.getAttribute('href')==='#'+p.id)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});
window.scrollTo(0,0)}
window.addEventListener('hashchange',go);go();
var m=document.querySelector('.menu-btn'),n=document.querySelector('.nav-links');
if(m){m.addEventListener('click',function(){var o=n.classList.toggle('open');m.setAttribute('aria-expanded',o)});
n.addEventListener('click',function(e){if(e.target.closest('a')){n.classList.remove('open');m.setAttribute('aria-expanded','false')}})}
})();
"""


def face(fam, file, weight, extra=""):
    return f"@font-face{{font-family:'{fam}';src:url({A}/fonts/{file}) format('woff2');font-weight:{weight};font-style:normal;font-display:swap;{extra}}}"


def lang_switch():
    return ('<div class="lang" role="group" aria-label="Sprache / Language">'
            '<button type="button" data-l="de" aria-pressed="true">DE</button>'
            '<button type="button" data-l="en" aria-pressed="false">EN</button></div>')


def nav_links():
    return "".join(f'<a href="{h}">{t(d, e)}</a>' for h, d, e in NAV)


def page(title, desc, fonts, css, body, theme, kick="eyebrow"):
    body = body.replace('<main id="main">', '<main id="main"><div data-page="home" id="home" class="on">').replace(
        "</main>", "</div>" + subpages(kick) + "</main>")
    return f"""<!DOCTYPE html>
<html lang="de" data-lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{theme}">
<style>
{fonts}
{BASE_CSS}
{css}
{SUB_CSS}
</style>
</head>
<body>
<a class="skip" href="#main">{t("Zum Inhalt", "Skip to content")}</a>
{body}
<script>{JS}</script>
</body>
</html>
"""


def with_alts(html):
    # img alt in beiden Sprachen hinterlegen
    for name, (de, en) in ALT.items():
        html = html.replace(f'alt="{de}"', f'alt="{de}" data-alt-de="{de}" data-alt-en="{en}"')
    return html


CONTACT = dict(
    street="Schaubenstrasse 4", city="CH-8450 Andelfingen", phone="+41 52 304 24 24",
    fax="+41 52 304 24 25", mail="info@andair.ch",
)

# =====================================================================
# Variante A  ·  Werkplan  (hell, technisch, Schweizer Raster)
# =====================================================================
def variant_a():
    fonts = "\n".join([
        face("Archivo", "archivo.woff2", "100 900", "font-stretch:62% 125%;"),
        face("Plex Mono", "plex-mono-400.woff2", 400), face("Plex Mono", "plex-mono-500.woff2", 500),
    ])
    css = """
:root{--bg:#F3F2EE;--paper:#FFFFFF;--ink:#14171A;--mute:#5C6166;--line:#D5D3CC;--red:#D7261E;--red-d:#B11C15;
--font-body:'Archivo',system-ui,sans-serif;--mono:'Plex Mono',ui-monospace,monospace}
.mono{font-family:var(--mono);font-size:12.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--mute)}
header{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.bar{display:flex;align-items:center;gap:32px;height:72px;position:relative}
.logo{background:var(--red);color:#fff;font-weight:800;font-stretch:112%;font-size:19px;letter-spacing:-.01em;padding:9px 16px 8px;line-height:1}
.nav-links{display:flex;gap:26px;margin-left:auto;align-items:center;font-size:15px;font-weight:500}
.nav-links a{position:relative;padding:12px 0}
.nav-links a::after{content:"";position:absolute;left:0;right:0;bottom:6px;height:2px;background:var(--red);transform:scaleX(0);transform-origin:left;transition:transform .25s cubic-bezier(.2,.7,.2,1)}
.nav-links a:hover::after{transform:scaleX(1)}
.btn{display:inline-flex;align-items:center;gap:10px;min-height:48px;padding:0 22px;font-weight:600;font-size:15.5px;border:1.5px solid var(--ink);transition:background .15s,color .15s,transform .1s,border-color .15s}
.btn:active{transform:translateY(1px)}
.btn.pri{background:var(--red);border-color:var(--red);color:#fff}
.btn.pri:hover{background:var(--red-d);border-color:var(--red-d)}
.btn.sec:hover{background:var(--ink);color:var(--bg)}
.bar .btn{min-height:44px;padding:0 18px}
h1,h2{font-stretch:84%;font-weight:640;letter-spacing:-.022em;line-height:1.0}
.hero{min-height:calc(100svh - 72px);display:flex;flex-direction:column}
.hero .wrap{flex:1;display:flex;flex-direction:column}
.hero-grid{flex:1;display:grid;grid-template-columns:7fr 5fr;gap:40px;align-items:center;padding-block:48px 32px}
h1{font-size:clamp(42px,6.1vw,94px);margin:22px 0 28px;max-width:11ch}
h1 .de,h1 .en{display:block}
html[data-lang=de] h1 .en,html[data-lang=en] h1 .de{display:none}
.lead{font-size:clamp(17px,1.35vw,20px);max-width:48ch;color:#2B2F33}
.acts{display:flex;gap:12px;flex-wrap:wrap;margin-top:34px}
.stage{position:relative}
.stage img{width:100%;mix-blend-mode:multiply;animation:in .9s cubic-bezier(.2,.7,.2,1) both}
@keyframes in{from{opacity:0;transform:translateY(14px) scale(.985)}to{opacity:1;transform:none}}
.tag{display:flex;justify-content:space-between;gap:16px;border-top:1px solid var(--ink);padding-top:10px;margin-top:6px}
.facts{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--ink)}
.facts div{padding:20px 20px 26px 0}
.facts div+div{padding-left:20px;border-left:1px solid var(--line)}
.facts b{display:block;font-stretch:84%;font-weight:640;font-size:clamp(28px,3vw,44px);letter-spacing:-.02em;line-height:1.1}
.facts span span,.facts>div>span{color:var(--mute);font-size:14.5px}
section{padding-block:clamp(72px,9vw,128px)}
.head{display:grid;grid-template-columns:3fr 9fr;gap:40px;margin-bottom:56px;align-items:start}
.head .mono{padding-top:14px;border-top:1px solid var(--ink)}
h2{font-size:clamp(32px,4vw,60px);max-width:18ch}
.areas{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--ink)}
.area{display:flex;flex-direction:column;padding:28px 32px 32px 0;position:relative;min-height:300px}
.area+.area{padding-left:32px;border-left:1px solid var(--line)}
.area::before{content:"";position:absolute;left:0;right:0;top:-1px;height:3px;background:var(--red);transform:scaleX(0);transform-origin:left;transition:transform .35s cubic-bezier(.2,.7,.2,1)}
.area:hover::before{transform:scaleX(1)}
.area h3{font-stretch:88%;font-weight:620;font-size:27px;line-height:1.12;letter-spacing:-.012em;margin:36px 0 14px}
.area p{color:#3A3F44;max-width:34ch}
.more{display:inline-flex;align-items:center;gap:8px;font-weight:600;font-size:15px;margin-top:auto;padding-top:28px;min-height:44px}
.prods{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.prod{background:var(--paper);display:flex;flex-direction:column;transition:transform .2s cubic-bezier(.2,.7,.2,1),box-shadow .2s}
.prod:hover{transform:translateY(-3px);box-shadow:0 14px 30px -18px rgba(20,23,26,.35)}
.prod .ph{aspect-ratio:1/1;display:grid;place-items:center;padding:26px;overflow:hidden}
.prod .ph img{max-height:100%;width:auto;object-fit:contain;transition:transform .5s cubic-bezier(.2,.7,.2,1)}
.prod:hover .ph img{transform:scale(1.035)}
.prod .ph.red{background:#C90A0A;padding:0}
.prod .ph.red img{width:100%;height:100%;object-fit:cover}
.prod .tx{padding:20px 22px 24px;border-top:1px solid var(--line)}
.prod h3{font-size:19px;font-weight:620;font-stretch:90%;line-height:1.2;margin:8px 0 8px}
.prod p{font-size:14.5px;color:var(--mute);line-height:1.5}
.dark{background:var(--ink);color:#F3F2EE}
.dark .mono{color:#9BA1A7}.dark .head .mono{border-color:#F3F2EE}
.apps{display:grid;grid-template-columns:5fr 7fr;gap:56px;align-items:start}
.apps p{color:#C5C9CD;max-width:40ch;font-size:18px}
.apps ol{columns:2;column-gap:40px;counter-reset:a}
.apps li{counter-increment:a;break-inside:avoid;display:flex;gap:14px;padding:14px 0;border-top:1px solid #353A40;font-size:16.5px;line-height:1.35}
.apps li::before{content:counter(a,decimal-leading-zero);font-family:var(--mono);font-size:12.5px;color:var(--red);padding-top:3px}
.strip{margin-top:72px;overflow:hidden}
.strip img{width:100%;aspect-ratio:960/172;object-fit:cover}
.motto{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--ink);border-bottom:1px solid var(--ink)}
.motto div{padding:36px 0 40px}
.motto div+div{padding-left:32px;border-left:1px solid var(--line)}
.motto b{display:block;font-stretch:80%;font-weight:680;font-size:clamp(44px,7vw,108px);letter-spacing:-.03em;line-height:.95}
.firma{display:grid;grid-template-columns:7fr 5fr;gap:56px;margin-top:56px;align-items:end}
.firma p{font-size:clamp(19px,1.7vw,25px);line-height:1.4;max-width:34ch;font-stretch:94%}
.kontakt{background:var(--red);color:#fff}
.kontakt .wrap{display:grid;grid-template-columns:7fr 5fr;gap:56px;align-items:end}
.kontakt h2{max-width:14ch}
.kontakt .mono{color:#FFD9D6}
.kontakt address{font-style:normal;font-size:18px;line-height:1.6}
.kontakt address a{text-decoration:underline;text-underline-offset:4px;text-decoration-thickness:1px}
.kontakt address a:hover{text-decoration-thickness:2px}
footer{background:var(--ink);color:#9BA1A7;font-size:14px;padding:26px 0}
footer .wrap{display:flex;gap:28px;flex-wrap:wrap;align-items:center}
footer a{padding:12px 0}footer a:hover{color:#fff}
footer .sp{margin-left:auto}
@media (max-width:1100px){.prods{grid-template-columns:repeat(2,1fr)}}
@media (max-width:1080px){.bar{gap:14px}.bar .lang{margin-left:auto}.bar>.btn{display:none}}
@media (max-width:900px){
 .bar{height:64px}
 .hero{min-height:0}.hero-grid,.head,.apps,.firma,.kontakt .wrap{grid-template-columns:1fr;gap:28px}
 .stage{max-width:420px}
 .facts{grid-template-columns:1fr 1fr}.facts div:nth-child(3){padding-left:0;border-left:0}.facts div:nth-child(n+3){border-top:1px solid var(--line)}
 .areas,.motto{grid-template-columns:1fr}.area{min-height:0;padding:24px 0 28px!important;border-left:0!important;border-top:1px solid var(--line)}
 .area h3{margin-top:14px}.motto div{padding:20px 0 24px!important;border-left:0!important;border-top:1px solid var(--line)}
 .apps ol{columns:1}.head{margin-bottom:36px}
}
@media (max-width:560px){.prods{grid-template-columns:1fr}.acts .btn{width:100%;justify-content:center}}
"""
    facts = "".join(f"<div><b>{t(d, e)}</b><span>{t(ld, le)}</span></div>" for d, e, ld, le in FACTS)
    areas = "".join(
        f'<a class="area" href="{AREA_HREF[i]}"><span class="mono">0{i + 1}</span><h3>{t(d, e)}</h3><p>{t(td, te)}</p>'
        f'<span class="more">{t("Mehr erfahren", "Read more")}{ARROW}</span></a>'
        for i, (d, e, td, te) in enumerate(AREAS))
    prods = "".join(
        f'<a class="prod" href="#produkte"><div class="ph{" red" if f == "esv-red.jpg" else ""}">{img(f)}</div>'
        f'<div class="tx"><span class="mono">{t("Typ", "Type")} {code}</span><h3>{t(d, e)}</h3><p>{t(td, te)}</p></div></a>'
        for code, d, e, f, td, te in PRODUCTS)
    apps = "".join(f"<li><span>{t(d, e)}</span></li>" for d, e in APPS)
    motto = "".join(f"<div><span class='mono'>0{i + 1}</span><b>{t(d, e)}</b></div>" for i, (d, e) in enumerate(MOTTO))
    c = CONTACT
    body = f"""
<header><div class="wrap bar">
 <a class="logo" href="#home" aria-label="Andair AG">Andair AG</a>
 <nav class="nav-links" id="nav" aria-label="Hauptnavigation">{nav_links()}</nav>
 {lang_switch()}
 <a class="btn pri" href="#kontakt">{t("Kontakt", "Contact")}</a>
 <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">{t("Menü", "Menu")}</button>
</div></header>
<main id="main">
<div class="hero"><div class="wrap">
 <div class="hero-grid">
  <div>
   <span class="mono">Andair AG · Andelfingen ZH</span>
   <h1>{t("Schutzraum&shy;technik aus der Schweiz. Seit 1968.", H1[1])}</h1>
   <p class="lead">{t(*LEAD)}</p>
   <div class="acts"><a class="btn pri" href="#produkte">{t("Produkte ansehen", "View products")}{ARROW}</a>
   <a class="btn sec" href="#kontakt">{t("Anfrage senden", "Send an enquiry")}</a></div>
  </div>
  <div class="stage">{img("gak-d.jpg", eager=True)}
   <div class="tag mono"><span>{t("Typ", "Type")} GAK-D</span><span>{t("Gasdichte Absperrklappe", "Gastight shut-off valve")}</span></div>
  </div>
 </div>
 <div class="facts">{facts}</div>
</div></div>

<section><div class="wrap">
 <div class="head"><span class="mono">{t("Bereiche", "Divisions")}</span><h2>{t("Drei Fachgebiete, ein Hersteller.", "Three disciplines, one manufacturer.")}</h2></div>
 <div class="areas">{areas}</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
 <div class="head"><span class="mono">{t("Produkte", "Products")}</span><h2>{t("Komponenten für jede Öffnung im Schutzbau.", "Components for every opening in a shelter.")}</h2></div>
 <div class="prods">{prods}</div>
</div></section>

<section class="dark"><div class="wrap">
 <div class="head"><span class="mono">{t("Einsatz", "Applications")}</span><h2>{t("Wo Andair-Komponenten Menschen und Anlagen schützen.", "Where Andair components protect people and plants.")}</h2></div>
 <div class="apps"><p>{t(*SPIEZ)}</p><ol>{apps}</ol></div>
 <div class="strip">{img("pipes-strip.jpg")}</div>
</div></section>

<section><div class="wrap">
 <div class="head"><span class="mono">{t("Firma", "Company")}</span><h2>{t("Der Massstab für jedes Andair-Produkt.", "The measure for every Andair product.")}</h2></div>
 <div class="motto">{motto}</div>
 <div class="firma"><p>{t(*ABOUT)}</p><p class="mono" style="max-width:none">{t(*CLAIM)}</p></div>
</div></section>

<section class="kontakt"><div class="wrap">
 <div><span class="mono">{t("Kontakt", "Contact")}</span><h2 style="margin-top:18px">{t("Sprechen Sie mit unseren Spezialisten.", "Talk to our specialists.")}</h2></div>
 <address>Andair AG<br>{c["street"]}<br>{c["city"]}<br><br>
 {t("Telefon", "Phone")} <a href="tel:+41523042424">{c["phone"]}</a><br><a href="mailto:{c["mail"]}">{c["mail"]}</a></address>
</div></section>
</main>
<footer><div class="wrap"><span>© Andair AG</span><a href="#datenschutz">{t("Datenschutz", "Privacy")}</a><a href="#impressum">{t("Impressum", "Imprint")}</a>
<span class="sp">{t("Entwurf A · Werkplan", "Draft A · Werkplan")}</span></div></footer>
"""
    return page("Andair AG · Schutzraumtechnik seit 1968", LEAD[0], fonts, css + SUB_A, body, "#F3F2EE", "mono")


# =====================================================================
# Variante B  ·  Bunker  (dunkel, Beton, grosse Versalien)
# =====================================================================
def variant_b():
    fonts = "\n".join([face("Barlow Condensed", f"barlow-condensed-{w}.woff2", w) for w in (500, 600, 700)]
                      + [face("Barlow", f"barlow-{w}.woff2", w) for w in (400, 500)])
    css = """
:root{--bg:#0E0F10;--panel:#191B1D;--ink:#F1EFEA;--mute:#A0A4A8;--line:#2C2F33;--red:#E1261C;--red-d:#B81D15;--focus:#fff;
--font-body:'Barlow',system-ui,sans-serif;--cond:'Barlow Condensed','Arial Narrow',sans-serif}
.cond{font-family:var(--cond);text-transform:uppercase;letter-spacing:.01em}
.eyebrow{font-family:var(--cond);font-weight:600;text-transform:uppercase;letter-spacing:.14em;font-size:15px;color:var(--red)}
header{position:sticky;top:0;z-index:20;background:rgba(14,15,16,.9);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.bar{display:flex;align-items:stretch;gap:32px;height:76px;position:relative}
.logo{background:var(--red);color:#fff;font-family:var(--cond);font-weight:700;font-size:26px;letter-spacing:.01em;display:flex;align-items:center;padding:0 24px;margin-left:calc(-1*clamp(20px,4vw,56px));padding-left:clamp(20px,4vw,56px)}
.nav-links{display:flex;gap:26px;margin-left:auto;align-items:center;font-family:var(--cond);font-weight:600;font-size:17px;text-transform:uppercase;letter-spacing:.08em}
.nav-links a{padding:12px 0;transition:color .15s}.nav-links a:hover{color:var(--red)}
.bar .lang,.bar .menu-btn,.bar .btn{align-self:center}
.btn{display:inline-flex;align-items:center;gap:12px;min-height:54px;padding:0 28px;font-family:var(--cond);font-weight:700;font-size:19px;text-transform:uppercase;letter-spacing:.08em;transition:background .15s,color .15s,transform .1s}
.btn:active{transform:translateY(1px)}
.btn.pri{background:var(--red);color:#fff}.btn.pri:hover{background:#fff;color:#0E0F10}
.btn.sec{box-shadow:inset 0 0 0 2px var(--ink)}.btn.sec:hover{background:var(--ink);color:var(--bg)}
.bar .btn{min-height:44px;padding:0 20px;font-size:17px}
.hero{min-height:calc(100svh - 76px);display:flex;flex-direction:column}
.hero-grid{flex:1;display:grid;grid-template-columns:7fr 5fr;gap:56px;align-items:center;padding-block:56px}
h1{font-family:var(--cond);font-weight:700;text-transform:uppercase;font-size:clamp(64px,10.4vw,168px);line-height:.86;letter-spacing:-.012em;margin:20px 0 30px}
h1 i{font-style:normal;display:block;animation:up .8s cubic-bezier(.2,.7,.2,1) both}
h1 i:nth-child(2){animation-delay:.08s}h1 i:nth-child(3){animation-delay:.16s;color:var(--red)}
@keyframes up{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
.lead{font-size:clamp(17px,1.4vw,21px);max-width:46ch;color:#D2D0CB}
.acts{display:flex;gap:14px;flex-wrap:wrap;margin-top:36px}
.shot{position:relative;margin-right:22px;margin-bottom:22px}
.shot::before{content:"";position:absolute;inset:22px -22px -22px 22px;background:var(--red)}
.shot img{position:relative;width:100%;aspect-ratio:418/350;object-fit:cover}
.band{background:var(--red);color:#fff}
.band .wrap{display:grid;grid-template-columns:repeat(4,1fr)}
.band .wrap>div{padding:22px 0 24px}.band .wrap>div+div{padding-left:28px;border-left:1px solid rgba(255,255,255,.28)}
.band b{display:block;font-family:var(--cond);font-weight:700;font-size:clamp(34px,3.6vw,54px);line-height:1}
.band .wrap>div>span{font-size:14.5px;opacity:.92}
section{padding-block:clamp(80px,10vw,140px)}
h2{font-family:var(--cond);font-weight:700;text-transform:uppercase;font-size:clamp(42px,6vw,92px);line-height:.92;letter-spacing:-.005em;margin:14px 0 56px;max-width:14ch}
.rows{border-top:1px solid var(--line)}
.row{display:grid;grid-template-columns:90px 5fr 5fr 60px;gap:32px;align-items:center;padding:34px 0;border-bottom:1px solid var(--line);position:relative;transition:padding .25s cubic-bezier(.2,.7,.2,1),color .2s}
.row::before{content:"";position:absolute;inset:0 calc(-1*clamp(20px,4vw,56px));background:var(--red);transform:scaleY(0);transform-origin:bottom;transition:transform .28s cubic-bezier(.2,.7,.2,1);z-index:-1}
.row:hover::before{transform:scaleY(1)}
.row .n{font-family:var(--cond);font-weight:600;font-size:22px;color:var(--red);transition:color .2s}.row:hover .n{color:#fff}
.row h3{font-family:var(--cond);font-weight:700;text-transform:uppercase;font-size:clamp(30px,3.6vw,54px);line-height:.98}
.row p{color:var(--mute);max-width:44ch;transition:color .2s}.row:hover p{color:#fff}
.row .arr{width:30px;height:30px;justify-self:end}
#produkte{background:var(--panel)}
.bento{display:grid;grid-template-columns:repeat(12,1fr);gap:16px}
.tile{position:relative;display:flex;flex-direction:column;justify-content:flex-end;min-height:440px;overflow:hidden;padding:28px;transition:transform .2s cubic-bezier(.2,.7,.2,1)}
.tile:hover{transform:translateY(-3px)}
.tile img{position:absolute;transition:transform .6s cubic-bezier(.2,.7,.2,1)}
.tile:hover img{transform:scale(1.04)}
.tile .tx{position:relative;z-index:1}
.tile h3{hyphens:auto;overflow-wrap:anywhere}
.tile .code{font-family:var(--cond);font-weight:700;font-size:18px;letter-spacing:.12em}
.tile h3{font-family:var(--cond);font-weight:700;text-transform:uppercase;font-size:clamp(28px,2.6vw,40px);line-height:1;margin:6px 0 10px}
.tile p{font-size:15px;line-height:1.45;max-width:36ch}
.t1{grid-column:span 7;background:#CB0000;color:#fff}
.t1 img{right:0;top:0;width:60%;height:auto;-webkit-mask-image:linear-gradient(to right,transparent,#000 32%),linear-gradient(to bottom,#000 72%,transparent);-webkit-mask-composite:source-in;mask-image:linear-gradient(to right,transparent,#000 32%),linear-gradient(to bottom,#000 72%,transparent);mask-composite:intersect}
.t1 .tx{max-width:62%}
.t2{grid-column:span 5;background:#000;color:#fff}
.t2 img{right:0;top:7%;height:86%;width:auto}
.t2 .tx{max-width:46%}
.t3,.t4{background:#fff;color:#14171A}
.t3{grid-column:span 5}.t3 img{right:8%;top:6%;height:58%;width:auto}
.t4{grid-column:span 7}.t4 img{right:2%;top:8%;height:78%;width:auto}
.t4 .tx{max-width:38%}
.t3 .code,.t4 .code{color:var(--red)}
.flow{display:grid;grid-template-columns:repeat(3,1fr);gap:0}
.col{padding:30px 36px 36px 0;border-top:4px solid var(--red);position:relative}
.col+.col{padding-left:44px}
.col+.col::before{content:"";position:absolute;left:-1px;top:26px;border:14px solid transparent;border-left-color:var(--red);border-right:0}
.col h3{font-family:var(--cond);font-weight:700;text-transform:uppercase;font-size:34px;line-height:1;margin-bottom:22px}
.col li{padding:11px 0;border-bottom:1px solid var(--line);color:#D2D0CB;font-size:16.5px}
.spiez{margin-top:56px;display:grid;grid-template-columns:5fr 7fr;gap:56px;align-items:center}
.spiez p{font-family:var(--cond);font-weight:500;font-size:clamp(24px,2.4vw,34px);line-height:1.15;text-transform:uppercase}
.spiez img{width:100%;aspect-ratio:960/172;object-fit:cover}
.firma{background:var(--ink);color:#0E0F10}
.firma .wrap{display:grid;grid-template-columns:6fr 6fr;gap:64px;align-items:center}
.firma h2{margin-bottom:0;max-width:none;font-size:clamp(54px,8.4vw,132px)}
.firma h2 i{font-style:normal;display:block}.firma h2 i:last-child{color:var(--red)}
.firma p{font-size:clamp(18px,1.5vw,22px);max-width:40ch}
.firma p+p{margin-top:22px;font-family:var(--cond);font-weight:700;text-transform:uppercase;font-size:24px;letter-spacing:.04em}
.kontakt .wrap{display:grid;grid-template-columns:7fr 5fr;gap:56px;align-items:end}
.kontakt h2{margin-bottom:0}
.kontakt address{font-style:normal;font-size:19px;line-height:1.65;color:#D2D0CB;border-left:4px solid var(--red);padding-left:24px}
.kontakt address b{color:#fff;font-family:var(--cond);font-size:26px;text-transform:uppercase;letter-spacing:.04em}
.kontakt address a{text-decoration:underline;text-underline-offset:4px;text-decoration-color:var(--red)}
.kontakt address a:hover{color:#fff}
footer{border-top:1px solid var(--line);color:var(--mute);font-size:14px;padding:24px 0}
footer .wrap{display:flex;gap:28px;flex-wrap:wrap;align-items:center}footer a{padding:12px 0}footer a:hover{color:#fff}footer .sp{margin-left:auto}
@media (max-width:1080px){.bar{gap:14px}.bar .lang{margin-left:auto}.bar>.btn{display:none}}
@media (max-width:900px){
 .bar{height:64px}.logo{font-size:22px}
 .hero{min-height:0}.hero-grid,.spiez,.firma .wrap,.kontakt .wrap{grid-template-columns:1fr;gap:32px}
 .hero-grid{padding-block:36px 48px}.shot{max-width:440px}
 .band .wrap{grid-template-columns:1fr 1fr}.band .wrap>div:nth-child(3){padding-left:0;border-left:0}.band .wrap>div:nth-child(n+3){border-top:1px solid rgba(255,255,255,.28)}
 .row{grid-template-columns:44px 1fr 30px;gap:14px;padding:24px 0}.row p{grid-column:2/4;grid-row:2}
 .bento{grid-template-columns:1fr}.tile{grid-column:auto!important;min-height:0;padding:0 22px 24px}
 .tile img{-webkit-mask-image:none!important;mask-image:none!important;position:static!important;width:auto!important;height:240px!important;max-width:100%;object-fit:contain;margin:22px auto}
 .tile .tx{max-width:none!important}
 .t1 img{width:calc(100% + 44px)!important;max-width:none;height:auto!important;margin:0 -22px 20px!important}
 .flow{grid-template-columns:1fr}.col{padding:24px 0 28px!important}.col+.col::before{display:none}
 h2{margin-bottom:36px}
}
@media (max-width:560px){.acts .btn{width:100%;justify-content:center}}
"""
    facts = "".join(f"<div><b>{t(d, e)}</b><span>{t(ld, le)}</span></div>" for d, e, ld, le in FACTS)
    rows = "".join(
        f'<a class="row" href="{AREA_HREF[i]}"><span class="n">0{i + 1}</span><h3>{t(d, e)}</h3><p>{t(td, te)}</p>{ARROW}</a>'
        for i, (d, e, td, te) in enumerate(AREAS))
    pmap = {"esv-red.jpg": "t1", "gasfilter.jpg": "t3", "gak-d.jpg": "t4", "emp-door.jpg": "t2"}
    order = [PRODUCTS[0], PRODUCTS[3], PRODUCTS[1], PRODUCTS[2]]
    tiles = "".join(
        f'<a class="tile {pmap[f]}" href="#produkte">{img("emp-dark.jpg" if f == "emp-door.jpg" else f)}'
        f'<div class="tx"><span class="code">{code}</span><h3>{t(d, e)}</h3><p>{t(td, te)}</p></div></a>'
        for code, d, e, f, td, te in order)
    flow = "".join(
        f'<div class="col"><h3>{t(d, e)}</h3><ul>{"".join(f"<li>{t(a, b)}</li>" for a, b in items)}</ul></div>'
        for d, e, items in FLOW)
    c = CONTACT
    body = f"""
<header><div class="wrap bar">
 <a class="logo" href="#home" aria-label="Andair AG">Andair AG</a>
 <nav class="nav-links" id="nav" aria-label="Hauptnavigation">{nav_links()}</nav>
 {lang_switch()}
 <a class="btn pri" href="#kontakt">{t("Kontakt", "Contact")}</a>
 <button class="menu-btn cond" type="button" aria-expanded="false" aria-controls="nav">{t("Menü", "Menu")}</button>
</div></header>
<main id="main">
<div class="hero">
 <div class="wrap hero-grid">
  <div>
   <span class="eyebrow">{t("Schutzraumtechnik aus der Schweiz · seit 1968", "Shelter technology from Switzerland · since 1968")}</span>
   <h1>{t("<i>Sicher.</i><i>Einfach.</i><i>Robust.</i>", "<i>Safe.</i><i>Simple.</i><i>Rugged.</i>")}</h1>
   <p class="lead">{t(*LEAD)}</p>
   <div class="acts"><a class="btn pri" href="#produkte">{t("Produkte ansehen", "View products")}{ARROW}</a>
   <a class="btn sec" href="#kontakt">{t("Anfrage senden", "Send an enquiry")}</a></div>
  </div>
  <div class="shot">{img("shelter.jpg", eager=True)}</div>
 </div>
 <div class="band"><div class="wrap">{facts}</div></div>
</div>

<section><div class="wrap">
 <span class="eyebrow">{t("Bereiche", "Divisions")}</span>
 <h2>{t("Drei Fachgebiete. Ein Hersteller.", "Three disciplines. One manufacturer.")}</h2>
 <div class="rows">{rows}</div>
</div></section>

<section><div class="wrap">
 <span class="eyebrow">{t("Produkte", "Products")}</span>
 <h2>{t("Gebaut für den Ernstfall.", "Built for the worst case.")}</h2>
 <div class="bento">{tiles}</div>
</div></section>

<section><div class="wrap">
 <span class="eyebrow">{t("Einsatz", "Applications")}</span>
 <h2>{t("Von der Bedrohung zum Schutz.", "From threat to protection.")}</h2>
 <div class="flow">{flow}</div>
 <div class="spiez"><p>{t(*SPIEZ)}</p>{img("pipes-strip.jpg")}</div>
</div></section>

<section class="firma"><div class="wrap">
 <h2>{t("<i>Wir schützen</i><i>Leben.</i>", "<i>We protect</i><i>lives.</i>")}</h2>
 <div><p>{t(*ABOUT)}</p><p>{t("Geprüft. Genehmigt. Garantiert.", "Tested. Approved. Certified.")}</p></div>
</div></section>

<section class="kontakt"><div class="wrap">
 <div><span class="eyebrow">{t("Kontakt", "Contact")}</span><h2>{t("Ihr Projekt. Unsere Spezialisten.", "Your project. Our specialists.")}</h2></div>
 <address><b>Andair AG</b><br>{c["street"]}<br>{c["city"]}<br><br>
 {t("Telefon", "Phone")} <a href="tel:+41523042424">{c["phone"]}</a><br><a href="mailto:{c["mail"]}">{c["mail"]}</a></address>
</div></section>
</main>
<footer><div class="wrap"><span>© Andair AG</span><a href="#datenschutz">{t("Datenschutz", "Privacy")}</a><a href="#impressum">{t("Impressum", "Imprint")}</a>
<span class="sp">{t("Entwurf B · Bunker", "Draft B · Bunker")}</span></div></footer>
"""
    return page("Andair AG · Sicher. Einfach. Robust.", LEAD[0], fonts, css + SUB_B, body, "#0E0F10")


# =====================================================================
# Variante C  ·  Editorial  (warm, Serifen, Vertrauen und Herkunft)
# =====================================================================
def variant_c():
    fonts = "\n".join([face("Fraunces", "fraunces.woff2", "100 900"), face("Instrument Sans", "instrument-sans.woff2", "400 700")])
    css = """
:root{--bg:#FAF7F1;--paper:#FFFFFF;--ink:#1C1A18;--mute:#6B655E;--line:#E2DCD1;--red:#C8201A;--red-d:#A31812;--sand:#EFE9DD;
--font-body:'Instrument Sans',system-ui,sans-serif;--serif:'Fraunces',Georgia,serif}
.serif{font-family:var(--serif);font-optical-sizing:auto}
.eyebrow{font-size:13px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--red)}
header{position:sticky;top:0;z-index:20;background:rgba(250,247,241,.93);backdrop-filter:blur(10px)}
.bar{display:flex;align-items:center;gap:32px;height:80px;position:relative;border-bottom:1px solid var(--line)}
.logo{display:flex;align-items:center;gap:12px;font-family:var(--serif);font-weight:600;font-size:24px;letter-spacing:-.01em}
.logo::before{content:"";width:0;height:0;border-left:11px solid transparent;border-right:11px solid transparent;border-bottom:19px solid var(--red)}
.nav-links{display:flex;gap:26px;margin-left:auto;align-items:center;font-size:15px;font-weight:500}
.nav-links a{padding:12px 0;background:linear-gradient(var(--red),var(--red)) 0 calc(100% - 8px)/0 1.5px no-repeat;transition:background-size .3s cubic-bezier(.2,.7,.2,1)}
.nav-links a:hover{background-size:100% 1.5px}
.btn{display:inline-flex;align-items:center;gap:10px;min-height:50px;padding:0 26px;border-radius:999px;font-weight:600;font-size:15.5px;transition:background .15s,color .15s,transform .1s,box-shadow .15s}
.btn:active{transform:translateY(1px)}
.btn.pri{background:var(--red);color:#fff}.btn.pri:hover{background:var(--red-d)}
.btn.sec{box-shadow:inset 0 0 0 1.5px var(--ink)}.btn.sec:hover{background:var(--ink);color:var(--bg)}
.bar .btn{min-height:44px;padding:0 20px}
.hero{min-height:calc(100svh - 80px);display:flex;flex-direction:column;justify-content:space-between;padding-top:clamp(40px,6vh,80px)}
.hero-top{text-align:center;max-width:980px;margin-inline:auto}
h1{font-family:var(--serif);font-weight:400;font-size:clamp(44px,6.6vw,104px);line-height:1.0;letter-spacing:-.028em;margin:22px 0 26px}
h1 em{font-style:italic;color:var(--red)}
.lead{font-size:clamp(17px,1.4vw,20.5px);max-width:56ch;margin-inline:auto;color:#3D3934}
.acts{display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-top:32px}
.trio{display:grid;grid-template-columns:5fr 4fr 5fr;gap:16px;margin-top:clamp(36px,5vh,64px);align-items:end}
.trio figure{overflow:hidden;border-radius:4px 4px 0 0;animation:rise .9s cubic-bezier(.2,.7,.2,1) both}
.trio figure:nth-child(2){animation-delay:.08s}.trio figure:nth-child(3){animation-delay:.16s}
@keyframes rise{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:none}}
.trio img{width:100%;height:clamp(200px,30vh,320px);object-fit:cover;transition:transform .7s cubic-bezier(.2,.7,.2,1)}
.trio figure:nth-child(2) img{height:clamp(240px,36vh,380px)}
.trio figure:hover img{transform:scale(1.03)}
section{padding-block:clamp(80px,10vw,144px)}
h2{font-family:var(--serif);font-weight:400;font-size:clamp(34px,4.4vw,66px);line-height:1.05;letter-spacing:-.022em;margin:16px 0 0;max-width:17ch}
.intro{display:grid;grid-template-columns:6fr 6fr;gap:72px;align-items:start}
.intro p{font-size:clamp(18px,1.5vw,21px);color:#3D3934;max-width:44ch;padding-top:44px}
.nums{display:grid;grid-template-columns:repeat(4,1fr);margin-top:72px;border-top:1px solid var(--ink)}
.nums div{padding:26px 24px 0 0}.nums div+div{padding-left:24px;border-left:1px solid var(--line)}
.nums b{display:block;white-space:nowrap;font-family:var(--serif);font-weight:300;font-size:clamp(34px,4.4vw,66px);letter-spacing:-.03em;line-height:1}
.nums div>span{display:block;margin-top:10px;color:var(--mute);font-size:15px}
.sand{background:var(--sand)}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:56px}
.card{background:var(--paper);border-radius:6px;padding:34px 32px 30px;display:flex;flex-direction:column;min-height:330px;transition:transform .22s cubic-bezier(.2,.7,.2,1),box-shadow .22s}
.card:hover{transform:translateY(-3px);box-shadow:0 20px 40px -26px rgba(60,40,20,.4)}
.card .tri{width:0;height:0;border-left:13px solid transparent;border-right:13px solid transparent;border-bottom:22px solid var(--red)}
.card:nth-child(2) .tri{border-bottom-color:#2E7F86}.card:nth-child(3) .tri{border-bottom-color:#2F62A8}
.card h3{font-family:var(--serif);font-weight:400;font-size:30px;line-height:1.1;letter-spacing:-.015em;margin:30px 0 14px}
.card p{color:#4A453F;font-size:16px}
.more{display:inline-flex;align-items:center;gap:8px;font-weight:600;font-size:15px;margin-top:auto;padding-top:26px;min-height:44px;color:var(--red)}
.plist{margin-top:56px;border-top:1px solid var(--ink)}
.pi{display:grid;grid-template-columns:150px 110px 4fr 5fr 40px;gap:32px;align-items:center;padding:22px 0;border-bottom:1px solid var(--line);transition:background .2s}
.pi:hover{background:var(--paper)}
.pi>*{min-width:0}
.pi .ph{height:130px;background:var(--paper);display:grid;place-items:center;border-radius:4px;overflow:hidden;padding:10px}
.pi .ph img{max-height:110px;width:auto;object-fit:contain;transition:transform .5s cubic-bezier(.2,.7,.2,1)}
.pi:hover .ph img{transform:scale(1.05)}
.pi .ph.red{background:#C90A0A;padding:0}.pi .ph.red img{max-height:none;width:100%;height:100%;object-fit:cover}
.pi .code{font-size:13px;font-weight:600;letter-spacing:.12em;color:var(--mute)}
.pi h3{font-family:var(--serif);font-weight:400;font-size:clamp(24px,2.2vw,32px);line-height:1.1;letter-spacing:-.015em}
.pi p{color:#4A453F;font-size:15.5px;max-width:48ch}
.pi .arr{color:var(--red);width:22px;height:22px}
.use{display:grid;grid-template-columns:5fr 7fr;gap:72px;align-items:start}
.use ul{columns:2;column-gap:40px;margin-top:8px}
.use li{break-inside:avoid;padding:15px 0;border-bottom:1px solid var(--line);font-size:17px;line-height:1.35}
.use .note{margin-top:28px;color:var(--mute);font-size:15.5px;max-width:40ch}
.claim{background:var(--red);color:#fff;text-align:center}
.claim p{font-family:var(--serif);font-weight:300;font-style:italic;font-size:clamp(34px,5vw,76px);line-height:1.08;letter-spacing:-.02em;max-width:18ch;margin-inline:auto}
.claim span.k{display:block;margin-top:32px;font-size:13px;font-weight:600;letter-spacing:.2em;text-transform:uppercase}
.kontakt .wrap{display:grid;grid-template-columns:7fr 5fr;gap:72px;align-items:end}
.kontakt address{font-style:normal;font-size:18px;line-height:1.7;border-top:1px solid var(--ink);padding-top:22px}
.kontakt address b{font-family:var(--serif);font-weight:500;font-size:24px}
.kontakt address a{text-decoration:underline;text-underline-offset:4px;text-decoration-color:var(--red)}
.kontakt address a:hover{color:var(--red)}
footer{border-top:1px solid var(--line);color:var(--mute);font-size:14px;padding:24px 0}
footer .wrap{display:flex;gap:28px;flex-wrap:wrap;align-items:center}footer a{padding:12px 0}footer a:hover{color:var(--ink)}footer .sp{margin-left:auto}
@media (max-width:1000px){.pi{grid-template-columns:110px 1fr 30px;gap:18px}.pi .code{grid-column:2;grid-row:1;align-self:end}.pi h3{grid-column:2;grid-row:2}.pi p{grid-column:2/4;grid-row:3}.pi .ph{grid-row:1/3;height:100px}.pi .ph img{max-height:84px}.pi .arr{grid-row:1/3}}
@media (max-width:1080px){.bar{gap:14px}.bar .lang{margin-left:auto}.bar>.btn{display:none}}
@media (max-width:900px){
 .bar{height:64px}
 .hero{min-height:0}.intro,.use,.kontakt .wrap{grid-template-columns:1fr;gap:24px}.intro p{padding-top:0}
 .trio{grid-template-columns:1fr 1fr}.trio figure:nth-child(3){display:none}.trio img{height:200px!important}
 .nums{grid-template-columns:1fr 1fr;margin-top:48px}.nums div{padding-bottom:22px}.nums div:nth-child(3){padding-left:0;border-left:0}.nums div:nth-child(n+3){border-top:1px solid var(--line)}
 .cards{grid-template-columns:1fr}.card{min-height:0}.use ul{columns:1}
}
@media (max-width:560px){.acts .btn{width:100%;justify-content:center}}
"""
    nums = "".join(f"<div><b>{t(d, e)}</b><span>{t(ld, le)}</span></div>" for d, e, ld, le in FACTS)
    cards = "".join(
        f'<a class="card" href="{AREA_HREF[i]}"><span class="tri" aria-hidden="true"></span><h3>{t(d, e)}</h3><p>{t(td, te)}</p>'
        f'<span class="more">{t("Mehr erfahren", "Read more")}{ARROW}</span></a>'
        for i, (d, e, td, te) in enumerate(AREAS))
    plist = "".join(
        f'<a class="pi" href="#produkte"><div class="ph{" red" if f == "esv-red.jpg" else ""}">{img(f)}</div>'
        f'<span class="code">{code}</span><h3>{t(d, e)}</h3><p>{t(td, te)}</p>{ARROW}</a>'
        for code, d, e, f, td, te in PRODUCTS)
    apps = "".join(f"<li>{t(d, e)}</li>" for d, e in APPS)
    c = CONTACT
    body = f"""
<header><div class="wrap"><div class="bar">
 <a class="logo" href="#home" aria-label="Andair AG">Andair AG</a>
 <nav class="nav-links" id="nav" aria-label="Hauptnavigation">{nav_links()}</nav>
 {lang_switch()}
 <a class="btn pri" href="#kontakt">{t("Kontakt", "Contact")}</a>
 <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">{t("Menü", "Menu")}</button>
</div></div></header>
<main id="main">
<div class="hero"><div class="wrap">
 <div class="hero-top">
  <span class="eyebrow">{t("Schutzraumtechnik aus Andelfingen · seit 1968", "Shelter technology from Andelfingen · since 1968")}</span>
  <h1>{t("Wir schützen die <em>Luft</em> für Sie.", "We protect the <em>air</em> for you.")}</h1>
  <p class="lead">{t(*LEAD)}</p>
  <div class="acts"><a class="btn pri" href="#produkte">{t("Produkte ansehen", "View products")}{ARROW}</a>
  <a class="btn sec" href="#kontakt">{t("Anfrage senden", "Send an enquiry")}</a></div>
 </div>
 <div class="trio"><figure>{img("shelter.jpg", eager=True)}</figure><figure>{img("closures.jpg", eager=True)}</figure><figure>{img("pipes.jpg", eager=True)}</figure></div>
</div></div>

<section><div class="wrap">
 <div class="intro"><div><span class="eyebrow">{t("Firma", "Company")}</span>
 <h2>{t("Ein Schweizer Spezialist mit über fünfzig Jahren Erfahrung.", "A Swiss specialist with more than fifty years of experience.")}</h2></div>
 <p>{t(*ABOUT)}</p></div>
 <div class="nums">{nums}</div>
</div></section>

<section class="sand"><div class="wrap">
 <span class="eyebrow">{t("Bereiche", "Divisions")}</span>
 <h2>{t("Drei Fachgebiete unter einem Dach.", "Three disciplines under one roof.")}</h2>
 <div class="cards">{cards}</div>
</div></section>

<section><div class="wrap">
 <span class="eyebrow">{t("Produkte", "Products")}</span>
 <h2>{t("Eine Auswahl aus dem Andair-Sortiment.", "A selection from the Andair range.")}</h2>
 <div class="plist">{plist}</div>
</div></section>

<section class="sand"><div class="wrap use">
 <div><span class="eyebrow">{t("Einsatz", "Applications")}</span>
 <h2>{t("Anlagen, die auf Andair vertrauen.", "Installations that rely on Andair.")}</h2>
 <p class="note">{t(*SPIEZ)}</p></div>
 <ul>{apps}</ul>
</div></section>

<section class="claim"><div class="wrap"><p>{t(*CLAIM)}</p>
 <span class="k">{t("Sicher · Einfach · Robust", "Safe · Simple · Rugged")}</span></div></section>

<section class="kontakt"><div class="wrap">
 <div><span class="eyebrow">{t("Kontakt", "Contact")}</span><h2>{t("Wir beraten Sie gern persönlich.", "We are happy to advise you in person.")}</h2></div>
 <address><b>Andair AG</b><br>{c["street"]}<br>{c["city"]}<br><br>
 {t("Telefon", "Phone")} <a href="tel:+41523042424">{c["phone"]}</a><br><a href="mailto:{c["mail"]}">{c["mail"]}</a></address>
</div></section>
</main>
<footer><div class="wrap"><span>© Andair AG</span><a href="#datenschutz">{t("Datenschutz", "Privacy")}</a><a href="#impressum">{t("Impressum", "Imprint")}</a>
<span class="sp">{t("Entwurf C · Editorial", "Draft C · Editorial")}</span></div></footer>
"""
    return page("Andair AG · Wir schützen die Luft für Sie", LEAD[0], fonts, css + SUB_C, body, "#FAF7F1")



# =====================================================================
# Unterseiten (in allen drei Varianten gleich aufgebaut, je Variante gestaltet)
# =====================================================================
import json
PRODS = json.loads((ROOT / "build" / "products.json").read_text(encoding="utf-8"))
FLOW_FULL = [
    ("Bedrohungen", "Threats",
     [("Konventionelle Kriegsführung", "Conventional warfare"), ("Nukleare Kriegsführung", "Nuclear warfare"),
      ("Industrieunfälle", "Industrial accidents"), ("Sabotage", "Sabotage"), ("Terrorismus", "Terrorism"),
      ("Erdbeben", "Earthquake"), ("Betriebsausfälle", "Breakdowns")]),
    ("Gefährdung von", "Endangering of",
     [("Bevölkerung", "Population"), ("Einrichtungen", "Facilities"),
      ("Bewaffneten und militärischen Streitkräften", "Armed and military forces"), ("Waren", "Goods"),
      ("Kulturgütern", "Cultural assets"), ("Infrastrukturen", "Infrastructure"), ("Zulieferungssystemen", "Supply systems")]),
    ("Schutzraum-Einrichtungen für", "Shelter requirements for",
     [("Schutzräume und Bunker", "Civil defence shelters"), ("Kommandoposten", "Command posts"),
      ("Petrochemische Einrichtungen", "Petro-chemical plants"), ("Kernkraftwerke", "Nuclear power stations"),
      ("Munition und Pyrotechnik", "Ammunition and pyrotechnics"), ("Streit- und Verteidigungskräfte, Armee", "Defence forces"),
      ("Kulturgüter", "Cultural assets"), ("Notfallspitäler", "Emergency hospitals"),
      ("Kommunikationszentren", "Communication centers")]),
]
SHOTS = [
    ("overview.jpg", 320, 190, "Beispiel einer typischen Schutzraumanlage", "Example of a typical shelter layout"),
    ("doors.jpg", 320, 221, "Explosionsgeschützter Schutzraumeingang", "Shelter entrance with blast doors"),
    ("filterbank.jpg", 320, 234, "EMP-geschütztes elektrisches Lüftungsgerät mit Handantrieb, im Hintergrund eine NBC-Filter-Reihe",
     "Ventilating unit with electro-motor and handcrank, large NBC filter bank"),
]

SUB_CSS = """
[data-page]{display:none}[data-page].on{display:block}
.nav-links a[aria-current=page]{color:var(--red)}
.phero{padding-block:clamp(44px,6vw,88px) clamp(40px,5vw,72px)}
.phero .wrap{display:grid;grid-template-columns:7fr 5fr;gap:56px;align-items:end}
.phero.solo .wrap{grid-template-columns:1fr}
.phero h1.pt{font-size:clamp(38px,5.6vw,84px);line-height:1;margin:16px 0 22px;max-width:16ch;hyphens:auto}
.plead{font-size:clamp(18px,1.5vw,22px);line-height:1.45;max-width:52ch}
.phero figure{overflow:hidden}.phero figure img{width:100%;aspect-ratio:4/3;object-fit:cover}
.sub{padding-block:0 clamp(64px,8vw,112px)}
.sub>.wrap>h2{font-size:clamp(30px,3.6vw,54px);margin:0 0 14px;max-width:20ch}
.sub .lede{font-size:19px;max-width:60ch;margin-bottom:36px;color:var(--soft)}
.rule{border-top:1px solid var(--rule,var(--ink));padding-top:clamp(40px,5vw,64px)}
.two{display:grid;grid-template-columns:5fr 7fr;gap:56px;align-items:start}
.two p+p{margin-top:16px}
.cols{columns:2;column-gap:40px}
.cols li{break-inside:avoid;padding:13px 0;border-bottom:1px solid var(--line);line-height:1.35}
.shots{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:48px}
.shots figure{overflow:hidden}.shots img{width:100%;aspect-ratio:4/3;object-fit:cover;transition:transform .6s cubic-bezier(.2,.7,.2,1)}
.shots figure:hover img{transform:scale(1.03)}
.shots figcaption{font-size:14px;line-height:1.4;color:var(--mute);margin-top:12px}
.m3{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--rule,var(--ink));border-bottom:1px solid var(--rule,var(--ink))}
.m3 div{padding:28px 0 32px}.m3 div+div{padding-left:28px;border-left:1px solid var(--line)}
.m3 b{display:block;font-size:clamp(40px,6vw,92px);line-height:.98}
.after{margin-top:28px;font-size:19px;max-width:60ch;color:var(--soft)}
.f3{display:grid;grid-template-columns:repeat(3,1fr);gap:40px}
.f3 .fc{border-top:4px solid var(--red);padding-top:22px}
.f3 h3{font-size:26px;line-height:1.1;margin-bottom:16px}
.f3 li{padding:10px 0;border-bottom:1px solid var(--line);font-size:16px;line-height:1.35}
.pgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px}
.pc{background:var(--card);display:flex;flex-direction:column;transition:transform .2s cubic-bezier(.2,.7,.2,1),box-shadow .2s}
.pc:hover{transform:translateY(-3px);box-shadow:0 14px 30px -18px rgba(0,0,0,.4)}
.pc .ph{aspect-ratio:4/3;background:#fff;padding:18px;overflow:hidden}
.pc .ph img{width:100%;height:100%;min-height:0;object-fit:contain;transition:transform .5s cubic-bezier(.2,.7,.2,1)}
.pc:hover .ph img{transform:scale(1.04)}
.pc .ph.none{background:var(--red)}
.pc .tx{padding:16px 18px 20px}
.pc h3{font-size:18px;line-height:1.2;hyphens:auto}
.pc .ty{display:block;margin-top:6px;font-size:14px;line-height:1.4;color:var(--mute)}
.cta{display:flex;justify-content:space-between;align-items:center;gap:32px;flex-wrap:wrap;background:var(--red);color:#fff;padding:clamp(28px,4vw,48px)}
.cta p{font-size:clamp(24px,2.8vw,40px);line-height:1.1;max-width:22ch}
.cta .btn{background:#fff!important;color:#14171A!important;border-color:#fff!important;box-shadow:none!important}
.cta .btn:hover{background:#14171A!important;color:#fff!important;border-color:#14171A!important}
.cgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.cb{background:var(--card);padding:28px 28px 30px;font-style:normal}
.cb .big{display:block;font-size:clamp(22px,2.2vw,30px);line-height:1.2;margin-top:14px;overflow-wrap:anywhere}
.cb a.big{text-decoration:underline;text-decoration-color:var(--red);text-underline-offset:6px;text-decoration-thickness:2px}
.cb a.big:hover{color:var(--red)}
.wide img{width:100%}
.legal{max-width:68ch}.legal h2{font-size:28px!important;margin:40px 0 12px!important}.legal p{margin-bottom:14px}
.legal a{text-decoration:underline;text-decoration-color:var(--red);text-underline-offset:4px}
@media (max-width:1100px){.pgrid{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:900px){
 .phero .wrap,.two{grid-template-columns:1fr;gap:28px}.cols{columns:1}
 .shots,.f3,.cgrid{grid-template-columns:1fr}.shots figure{max-width:420px}
 .m3{grid-template-columns:1fr}.m3 div{padding:18px 0 20px!important;border-left:0!important}.m3 div+div{border-top:1px solid var(--line)}
 .pgrid{grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
}
@media (max-width:420px){.pc .tx{padding:12px 12px 16px}.pc h3{font-size:16px}}
"""
SUB_A = """
:root{--card:#fff;--soft:#2B2F33}
.phero{border-bottom:1px solid var(--line);margin-bottom:clamp(48px,6vw,80px)}
.m3 b,.f3 h3,.pc h3,.cta p,.cb .big{font-stretch:84%;font-weight:640;letter-spacing:-.02em}
.pc h3,.f3 h3{font-stretch:90%;font-weight:620;letter-spacing:-.01em}
"""
SUB_B = """
:root{--card:#191B1D;--soft:#D2D0CB;--rule:#2C2F33}
.phero{border-bottom:1px solid var(--line);margin-bottom:clamp(48px,6vw,80px)}
.phero h1.pt{font-size:clamp(52px,8vw,128px);line-height:.88;max-width:13ch;margin:14px 0 26px}
.sub>.wrap>h2{font-size:clamp(38px,5vw,76px);line-height:.94;margin-bottom:22px;max-width:16ch}
.m3 b,.f3 h3,.pc h3,.cta p,.cb .big{font-family:var(--cond);font-weight:700;text-transform:uppercase;line-height:1}
.pc h3{font-size:22px}.f3 h3{font-size:32px}
.cols li,.f3 li{color:#D2D0CB}
.cta .btn{color:#0E0F10!important}
"""
SUB_C = """
:root{--card:#fff;--soft:#3D3934}
.phero{text-align:left}
.phero h1.pt{font-size:clamp(40px,5.8vw,88px);letter-spacing:-.025em}
.sub>.wrap>h2{margin-top:0}
.m3 b,.f3 h3,.pc h3,.cta p,.cb .big{font-family:var(--serif);font-weight:400;letter-spacing:-.02em}
.m3 b{font-weight:300}
.pc,.cb{border-radius:6px;overflow:hidden}.cta{border-radius:6px}
.phero figure,.shots figure{border-radius:4px}
.sub.sand{padding-top:clamp(56px,7vw,96px)}
"""


def subpages(K):
    def hero(pid_kick, title, lead, fig=None):
        kd, ke = pid_kick
        f = f"<figure>{img(fig, eager=True)}</figure>" if fig else ""
        return (f'<div class="phero{"" if fig else " solo"}"><div class="wrap"><div><span class="{K}">{t(kd, ke)}</span>'
                f'<h1 class="pt">{t(*title)}</h1><p class="plead">{t(*lead)}</p></div>{f}</div></div>')

    def motto(after=None):
        m = "".join(f"<div><b>{t(d, e)}</b></div>" for d, e in MOTTO)
        a = f'<p class="after">{t(*after)}</p>' if after else ""
        return f'<section class="sub"><div class="wrap"><div class="m3">{m}</div>{a}</div></section>'

    def cta(text, btn, href):
        return (f'<section class="sub"><div class="wrap"><div class="cta"><p>{t(*text)}</p>'
                f'<a class="btn pri" href="{href}">{t(*btn)}{ARROW}</a></div></div></section>')

    apps = "".join(f"<li>{t(d, e)}</li>" for d, e in APPS)
    shots = "".join(
        f'<figure><img src="{A}/img/{f}" width="{w}" height="{h}" alt="" loading="lazy"><figcaption>{t(d, e)}</figcaption></figure>'
        for f, w, h, d, e in SHOTS)
    flow = "".join(
        f'<div class="fc"><h3>{t(d, e)}</h3><ul>{"".join(f"<li>{t(a, b)}</li>" for a, b in items)}</ul></div>'
        for d, e, items in FLOW_FULL)
    pcs = ""
    for p in PRODS:
        ph = (f'<div class="ph"><img src="{A}/img/{p["img"]}" width="{p["w"]}" height="{p["h"]}" alt="" loading="lazy"></div>'
              if p["img"] else '<div class="ph none"></div>')
        ty = f'<span class="ty">{t(p["de2"], p["en2"])}</span>' if p["de2"] else ""
        pcs += f'<article class="pc">{ph}<div class="tx"><h3>{t(p["de"], p["en"])}</h3>{ty}</div></article>'
    c = CONTACT
    contact_blocks = f"""<div class="cgrid">
 <address class="cb"><span class="{K}">{t("Adresse", "Address")}</span><span class="big">Andair AG<br>{c["street"]}<br>{c["city"]}<br>{t("Schweiz", "Switzerland")}</span></address>
 <div class="cb"><span class="{K}">{t("Telefon", "Phone")}</span><a class="big" href="tel:+41523042424">{c["phone"]}</a>
 <span class="ty" style="display:block;margin-top:14px;color:var(--mute)">Fax {c["fax"]}</span></div>
 <div class="cb"><span class="{K}">E-Mail</span><a class="big" href="mailto:{c["mail"]}">{c["mail"]}</a></div>
</div>"""
    return f"""
<div data-page="schutzraum" id="schutzraum">
 {hero(("A wie absolute Verantwortung", "A for absolute responsibility"), ("Schutzraum&shy;technik", "Shelter technology"),
       ("In keinem Bereich ist kompromisslose Sicherheit wichtiger als hier. Absolute Funktionstüchtigkeit ist nicht nur Ziel, sondern Notwendigkeit. Hier zählt Technik, auf die man sich verlassen kann.",
        "No other area needs such uncompromising safety. Perfect operation reliability is not only a goal but a must. Reliable technique is required."), "shelter.jpg")}
 {motto(("Und geprüft, genehmigt, garantiert. Andair AG erbringt diese Spitzenleistung seit über 50 Jahren.",
         "And tested, approved, certified. Andair AG has been providing this outstanding performance for over 50 years."))}
 <section class="sub"><div class="wrap">
  <h2>{t("Führend in Schutzraum&shy;technologie", "Leading in shelter technology")}</h2>
  <p class="lede">{t("Andair-Systeme und -Komponenten werden in Luftschutz-, Sicherheits- und Kontrollräumen eingesetzt.",
                     "Andair components and systems are used in shelters, safety rooms and control rooms.")}</p>
  <div class="two"><div>
   <p>{t("Betreiberpersonal und andere Personen sowie sensibles Material dieser Anlagen müssen geschützt werden.",
         "Operating staff and other persons as well as sensitive equipment present in these installations need to be protected.")}</p>
   <p>{t("Fundiertes Know-how und ein umfassendes Sortiment an speziellen Produkten sind die Grundlage für die marktführende Stellung der Andair AG.",
         "Well founded know-how and a wide range of special products are the basis of Andair's leadership.")}</p>
   <p>{t("Über 50 Jahre Erfahrung bürgen für beste Qualität, typengetestet und anerkannt durch das Labor Spiez vom Schweizerischen Bundesamt für Bevölkerungsschutz.",
         "Over 50 years experience pledge for best quality, type tested and approved by the SPIEZ LABORATORY of the Swiss Federal Department of Defence.")}</p>
   <p>{t("Mehr als 3000 geschützte Grossanlagen in über 55 Ländern weltweit sind mit Andair-Komponenten ausgerüstet.",
         "More than 3000 large protected installations are equipped with Andair components in over 55 countries everywhere in the world.")}</p>
  </div><ul class="cols">{apps}</ul></div>
  <div class="shots">{shots}</div>
 </div></section>
 <section class="sub"><div class="wrap">
  <h2 style="margin-bottom:36px">{t("Von der Bedrohung zum Schutz", "From threat to protection")}</h2>
  <div class="f3">{flow}</div>
 </div></section>
 {cta(("Alle Komponenten für den Schutzraum.", "All components for the shelter."), ("Produkte ansehen", "View products"), "#produkte")}
</div>

<div data-page="produkte" id="produkte">
 {hero(("Sicher, einfach, robust", "Safe, simple, rugged"), ("Produkte", "Products"),
       ("Andair entwickelt und produziert alle für einen Schutzraum nötigen Produkte. Andair-Produkte entsprechen den Anforderungen des Schweizerischen Zivilschutzes und die Firma ist ISO 9001:2015 zertifiziert.",
        "Andair engineers, manufactures and offers a comprehensive range of all products required to equip shelters. Andair equipment meets the Swiss Civil Defence requirements, and the company is ISO 9001:2015 certified."))}
 <section class="sub"><div class="wrap"><div class="pgrid">{pcs}</div></div></section>
 {cta(("Fragen zu einem Produkt?", "Questions about a product?"), ("Kontakt aufnehmen", "Get in touch"), "#kontakt")}
</div>

<div data-page="schall" id="schall">
 {hero(("A wie Akustik", "A for acoustics"), ("Schall- und Schwingungs&shy;technik", "Sound and vibration damping"),
       ("Unsere langjährige Erfahrung in modernster Schall- und Schwingungstechnik gewährleistet innovative Lösungen mit Leistungsgarantie.",
        "Our long-lasting experience of state-of-the-art sound and vibration protection technique guarantees innovative and reliable solutions."))}
 {motto(("Wir übernehmen Verantwortung. Wir erhöhen Lebensqualität.", "We take responsibility. We ensure life protection."))}
 {cta(("Sprechen Sie mit unseren Spezialisten.", "Talk to our specialists."), ("Kontakt aufnehmen", "Get in touch"), "#kontakt")}
</div>

<div data-page="lufttechnik" id="lufttechnik">
 {hero(("A wie Atemluft", "A for aeration"), ("Lufttechnik Komponenten", "Ventilation components"),
       ("Belüftungstechnik stellt komplexe Anforderungen und verlangt Spezialisten, die Ihnen Luft verschaffen. Wir garantieren Know-how und Top-Qualität.",
        "Ventilation technique makes high demands and requires specialists to ensure fresh air. We guarantee know-how and top quality."), "pipes.jpg")}
 {motto(("Wir übernehmen Verantwortung. Wir sorgen für gute Luft.", "We take responsibility. We ensure life protection."))}
 <section class="sub"><div class="wrap wide">{img("pipes-strip.jpg")}</div></section>
 {cta(("Sprechen Sie mit unseren Spezialisten.", "Talk to our specialists."), ("Kontakt aufnehmen", "Get in touch"), "#kontakt")}
</div>

<div data-page="firma" id="firma">
 {hero(("Schützt die Luft für Sie", "Protects the air for you"), ("Über uns", "About us"),
       ("Andair wurde 1968 gegründet und ist der kompetente Spezialist für Schutzraumtechnik. Mehr als 3’000 geschützte Grossanlagen in über 55 Ländern weltweit sind mit Andair-Komponenten ausgerüstet.",
        "Andair was founded in 1968 and is the competent specialist in shelter technology. More than 3,000 large protected installations in over 55 countries worldwide have been equipped with Andair components."), "closures.jpg")}
 {motto(("Kleine und grosse Anlagen werden mit dem Andair-Produktsortiment erfolgreich vor vielen Bedrohungen und Gefahren geschützt und belüftet.",
         "With the Andair range of products large and small shelters are ventilated and successfully protected against many threats and endangerments."))}
 <section class="sub"><div class="wrap"><div class="cgrid">
  <div class="cb"><span class="{K}">Management</span><span class="big">Michael Riedo</span><span class="ty" style="display:block;margin-top:8px;color:var(--mute)">CEO</span></div>
  <div class="cb"><span class="{K}">{t("Gegründet", "Founded")}</span><span class="big">1968</span><span class="ty" style="display:block;margin-top:8px;color:var(--mute)">Andelfingen, {t("Schweiz", "Switzerland")}</span></div>
  <div class="cb"><span class="{K}">{t("Zertifizierung", "Certification")}</span><span class="big">ISO 9001:2015</span></div>
 </div></div></section>
 {cta(CLAIM, ("Kontakt aufnehmen", "Get in touch"), "#kontakt")}
</div>

<div data-page="kontakt" id="kontakt">
 {hero(("Schützt die Luft für Sie", "Protects the air for you"), ("Kontakt", "Contact"),
       ("Bei Fragen oder Anregungen zögern Sie nicht, mit uns Kontakt aufzunehmen.", "If you have any queries please do not hesitate to contact us."))}
 <section class="sub"><div class="wrap">{contact_blocks}</div></section>
</div>

<div data-page="impressum" id="impressum">
 {hero(("Andair AG", "Andair AG"), ("Impressum", "Imprint"), ("Andair AG, Schaubenstrasse 4, CH-8450 Andelfingen, Schweiz.", "Andair AG, Schaubenstrasse 4, CH-8450 Andelfingen, Switzerland."))}
 <section class="sub"><div class="wrap legal">
  <h2>Management</h2><p>Michael Riedo, CEO</p>
  <h2>{t("Kontakt", "Contact")}</h2><p>{t("Telefon", "Phone")} {c["phone"]}<br>Fax {c["fax"]}<br><a href="mailto:{c["mail"]}">{c["mail"]}</a></p>
  <h2>Copyright</h2><p>{t("Jegliche textliche Inhalte, das Logo und das Design der Website sind Eigentum der Andair AG. Texte oder Bilder dürfen ohne ausdrückliche Bewilligung der Andair AG nicht anderweitig verwendet oder vervielfältigt werden.",
   "All textual contents, the logo and design of the website are owned by Andair AG. Texts and pictures must not be used or reproduced without written consent of Andair AG.")}</p>
 </div></section>
</div>

<div data-page="datenschutz" id="datenschutz">
 {hero(("Andair AG", "Andair AG"), ("Datenschutz", "Privacy"), ("Die Datenschutzerklärung wird unverändert von der bestehenden Website übernommen.", "The privacy policy is carried over unchanged from the existing website."))}
 <section class="sub"><div class="wrap legal">
  <p>{t('Aktuelle Fassung: <a href="https://andair.ch/datenschutz_d.php">andair.ch/datenschutz_d.php</a>', 'Current version: <a href="https://andair.ch/datenschutz.php">andair.ch/datenschutz.php</a>')}</p>
 </div></section>
</div>
"""

OVERVIEW = """<!DOCTYPE html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Andair AG · Designvarianten</title>
<style>body{font:17px/1.5 system-ui,sans-serif;margin:0;background:#f3f2ee;color:#14171a}main{max-width:1100px;margin:auto;padding:56px 24px}
h1{font-size:40px;letter-spacing:-.02em;margin:0 0 8px}p{color:#5c6166;margin:0 0 36px}
ul{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px}
a{display:block;background:#fff;color:inherit;text-decoration:none;transition:transform .2s}a:hover{transform:translateY(-3px)}
img{display:block;width:100%;aspect-ratio:16/10;object-fit:cover;object-position:top;border-bottom:1px solid #d5d3cc}
b{display:block;padding:18px 20px 2px;font-size:20px}span{display:block;padding:0 20px 20px;color:#5c6166;font-size:15px}</style></head>
<body><main><h1>Andair AG · Website, drei Varianten</h1><p>Deutsch und Englisch, umschaltbar oben rechts.</p><ul>
<li><a href="varianten/a-werkplan/"><img src="varianten/a-werkplan/vorschau.png" alt=""><b>A · Werkplan</b><span>Hell, technisch, Schweizer Raster</span></a></li>
<li><a href="varianten/b-bunker/"><img src="varianten/b-bunker/vorschau.png" alt=""><b>B · Bunker</b><span>Dunkel, Beton, grosse Versalien</span></a></li>
<li><a href="varianten/c-editorial/"><img src="varianten/c-editorial/vorschau.png" alt=""><b>C · Editorial</b><span>Warm, Serifen, Herkunft und Vertrauen</span></a></li>
</ul>
<h1 style="margin-top:56px">Nur Schutzraumtechnik, mit neuem Logo</h1><p>Ohne Schall- und Schwingungstechnik und ohne Lufttechnik Komponenten.</p><ul>
<li><a href="varianten/a-werkplan-schutzraum/"><img src="varianten/a-werkplan-schutzraum/vorschau.png" alt=""><b>A · Werkplan · Schutzraum</b><span>Logo: A als Dach im roten Quadrat</span></a></li>
<li><a href="varianten/b-bunker-schutzraum/"><img src="varianten/b-bunker-schutzraum/vorschau.png" alt=""><b>B · Bunker · Schutzraum</b><span>Logo: Dreieck mit Eingang</span></a></li>
<li><a href="varianten/c-editorial-schutzraum/"><img src="varianten/c-editorial-schutzraum/vorschau.png" alt=""><b>C · Editorial · Schutzraum</b><span>Logo: Ring mit Dreieck im Kern</span></a></li>
</ul></main></body></html>
"""


# =====================================================================
# Schutzraum-Fassungen: nur Schutzraumtechnik, mit neuem Logo
# =====================================================================
GROUPS = [
    ("Explosionsschutz", "Explosion protection",
     "Explosionsschutzventile der Typen ESV, FC, KC-T und EGV für Zuluft, Abluft, Sanitärentlüftung und Abgase.",
     "Explosion protection valves of types ESV, FC, KC-T and EGV for air inlets, outlets, sanitary vents and exhaust gases."),
    ("NBC-Filtration und Belüftung", "NBC filtration and ventilation",
     "Gasfilter, Ventilationsinstallationen VA 150 bis VA 2400 und der NBC Survivor 40 für private Überlebensräume.",
     "Gas filters, ventilating installations VA 150 to VA 2400 and the NBC Survivor 40 for safe rooms."),
    ("Abschlüsse und EMP-Schutz", "Closures and EMP protection",
     "Panzertüren und Drucktüren, gasdichte Absperrklappen, EMP-Türen und EMP-Gitter.",
     "Blast doors and pressure doors, gastight shut-off valves, EMP doors and EMP grilles."),
]
NAV_SHELTER = [
    ("#schutzraum", "Schutzraumtechnik", "Shelter technology"),
    ("#produkte", "Produkte", "Products"),
    ("#firma", "Firma", "Company"),
]
OLD_LOGO = '<a class="logo" href="#home" aria-label="Andair AG">Andair AG</a>'
LOGOS = {
    # A: das A als Dach mit Querbalken, weiss im roten Quadrat
    "a-werkplan": ('<svg viewBox="0 0 40 40" width="36" height="36" aria-hidden="true"><rect width="40" height="40" fill="#D7261E"/>'
                   '<path fill="#fff" d="M20 7 34 33h-6.4L20 18.6 12.4 33H6z"/><rect x="14.6" y="26" width="10.8" height="3.2" fill="#fff"/></svg>'
                   '<span>ANDAIR</span>',
                   ".logo{background:none;color:var(--ink);padding:0;display:flex;align-items:center;gap:12px;font-weight:800;font-stretch:118%;font-size:21px;letter-spacing:.05em}"),
    # B: rotes Dreieck mit ausgespartem Eingang (Bunker und A zugleich)
    "b-bunker": ('<svg viewBox="0 0 40 40" width="40" height="40" aria-hidden="true"><path fill="#E1261C" d="M20 3 38 36H2z"/>'
                 '<rect x="16" y="23" width="8" height="13" fill="#0E0F10"/></svg><span>ANDAIR</span>',
                 ".logo{background:none;margin-left:0;padding:0;gap:12px;font-size:30px;letter-spacing:.07em}"),
    # C: Ring (Ventil, Luft) mit dem A als Dreieck im Kern
    "c-editorial": ('<svg viewBox="0 0 40 40" width="36" height="36" aria-hidden="true"><circle cx="20" cy="20" r="17.5" fill="none" stroke="#C8201A" stroke-width="2.6"/>'
                    '<path fill="#C8201A" d="M20 9.5 29.6 27H10.4z"/></svg><span>Andair</span>',
                    ".logo::before{display:none}.logo{gap:11px;font-size:27px;font-weight:500}.card:nth-child(n) .tri{border-bottom-color:var(--red)}"),
}
SWAPS = [
    (t("Bereiche", "Divisions"), t("Sortiment", "Range")),
    ("Drei Fachgebiete, ein Hersteller.", "Drei Produktgruppen, ein Hersteller."),
    ("Three disciplines, one manufacturer.", "Three product groups, one manufacturer."),
    ("Drei Fachgebiete. Ein Hersteller.", "Alles für den Schutzraum."),
    ("Three disciplines. One manufacturer.", "Everything for the shelter."),
    ("Drei Fachgebiete unter einem Dach.", "Alles für den Schutzraum unter einem Dach."),
    ("Three disciplines under one roof.", "Everything for the shelter under one roof."),
]


def shelter_version(slug, fn):
    import re
    global NAV, AREAS, AREA_HREF
    keep = (NAV, AREAS, AREA_HREF)
    NAV, AREAS, AREA_HREF = NAV_SHELTER, GROUPS, ["#produkte"] * 3
    try:
        h = fn()
    finally:
        NAV, AREAS, AREA_HREF = keep
    h = re.sub(r'<div data-page="schall" id="schall">.*?(?=<div data-page="firma")', "", h, flags=re.S)
    mark, css = LOGOS[slug]
    assert OLD_LOGO in h
    h = h.replace(OLD_LOGO, f'<a class="logo" href="#home" aria-label="Andair AG">{mark}</a>')
    h = h.replace("</style>", css + "\n</style>", 1)
    for a, b in SWAPS:
        h = h.replace(a, b)
    for a in ("Entwurf A · Werkplan", "Entwurf B · Bunker", "Entwurf C · Editorial", "Draft A · Werkplan", "Draft B · Bunker", "Draft C · Editorial"):
        h = h.replace(a, a + (" · Schutzraum" if a.startswith("Entwurf") else " · Shelter"))
    return h


if __name__ == "__main__":
    for slug, fn in (("a-werkplan", variant_a), ("b-bunker", variant_b), ("c-editorial", variant_c)):
        d = ROOT / "varianten" / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(with_alts(fn()), encoding="utf-8")
        print("ok", d / "index.html")
        d = ROOT / "varianten" / (slug + "-schutzraum")
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(with_alts(shelter_version(slug, fn)), encoding="utf-8")
        print("ok", d / "index.html")
    (ROOT / "index.html").write_text(OVERVIEW, encoding="utf-8")
