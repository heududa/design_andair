// SVG -> PNG mit transparentem Grund: node render.mjs <svg> <png> <breite>
import puppeteer from '/tmp/sh/node_modules/puppeteer-core/lib/puppeteer/puppeteer-core.js';
import fs from 'fs';
const jobs = JSON.parse(process.argv[2]);
const b = await puppeteer.launch({ executablePath: '/usr/bin/google-chrome', args: ['--no-sandbox'] });
const p = await b.newPage();
for (const [src, out, w] of jobs) {
  const svg = fs.readFileSync(src, 'utf8'); const m = svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);
  const h = Math.round(w * m[2] / m[1]);
  await p.setViewport({ width: w, height: h });
  await p.setContent(`<body style="margin:0">${svg.replace(/width="[\d.]+" height="[\d.]+"/, `width="${w}" height="${h}"`)}`);
  await p.screenshot({ path: out, omitBackground: true });
}
await b.close();
