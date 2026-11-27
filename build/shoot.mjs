// Screenshots der Varianten: node build/shoot.mjs <url> <out.png> <breite> <hoehe> [full] [lang]
import puppeteer from 'puppeteer-core';
const [url, out, w = '1440', h = '900', full = '', lang = 'de'] = process.argv.slice(2);
const b = await puppeteer.launch({ executablePath: '/usr/bin/google-chrome', args: ['--no-sandbox', '--allow-file-access-from-files'] });
const p = await b.newPage();
await p.setViewport({ width: +w, height: +h });
await p.evaluateOnNewDocument(l => { try { localStorage.setItem('andair-lang', l); } catch (e) {} }, lang);
await p.goto(url, { waitUntil: 'networkidle0' });
await p.evaluate(async () => {
  await document.fonts.ready;
  document.querySelectorAll('img').forEach(i => (i.loading = 'eager'));
  for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); }
  window.scrollTo(0, 0);
});
await new Promise(r => setTimeout(r, 1200));
const ov = await p.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
const broken = await p.evaluate(() => [...document.images].filter(i => !i.naturalWidth).map(i => i.src));
console.log(out, 'overflow-x:', ov, 'broken:', broken.length, 'height:', await p.evaluate(() => document.body.scrollHeight));
await p.screenshot({ path: out, fullPage: full === 'full' });
await b.close();
