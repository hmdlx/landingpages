#!/usr/bin/env node
// Rendert story.html als 1080x1920-Story (PNG + JPG) nach stories/.
//   node stories/src/blackweek-letzter-tag/render.js
const path = require('path');
const { execFileSync } = require('child_process');
const { chromium } = require('playwright');

(async () => {
  const out = path.resolve(__dirname, '../../HomeDeluxe_BlackWeek_LetzterTag_Story_1080x1920');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'story.html'));
  await page.evaluate(async () => {
    await Promise.all([400, 500, 600, 700].map(w => document.fonts.load(`${w} 40px Poppins`)));
    await document.fonts.ready;
    await document.querySelector('#logo').decode();
  });
  await page.screenshot({ path: out + '.png', type: 'png' });
  await browser.close();
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-i', out + '.png', '-q:v', '2', out + '.jpg']);
  console.log(out + '.png / .jpg');
})().catch(e => { console.error(e); process.exit(1); });
