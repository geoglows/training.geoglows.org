// Screenshots of Aquifer Analyst for docs/aquiferx. See README.md.
//   node shots.mjs <outdir> [name,name,...]
import puppeteer from 'puppeteer-core';

const APP = process.env.AQX_URL || 'http://localhost:5198/';
const OUT = process.argv[2] || 'raw';
const only = process.argv[3];
const want = n => !only || only.split(',').includes(n);
const sleep = ms => new Promise(r => setTimeout(r, ms));

const browser = await puppeteer.launch({
  executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: 'new',
  args: ['--window-size=1440,900'], userDataDir: './.chrome-profile',
});
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
page.on('console', m => { if (m.type() === 'error') console.log('CONSOLE', m.text().slice(0, 160)); });
page.on('pageerror', e => console.log('PAGEERROR', e.message.slice(0, 160)));

// Wait for every basemap tile in view, so no shot has grey squares
const tiles = () => page.waitForFunction(
  () => ![...document.querySelectorAll('.leaflet-tile')].some(t => !t.classList.contains('leaflet-tile-loaded')),
  { timeout: 30000 }).catch(() => console.log('tiles still loading'));
const shot = async (name, clip) => {
  await tiles(); await sleep(300);
  await page.screenshot({ path: `${OUT}/${name}.png`, clip, captureBeyondViewport: false }); console.log('saved', name);
};
const rect = (sel, pad = 0) => page.evaluate((s, p) => {
  const r = document.querySelector(s).getBoundingClientRect();
  return { x: Math.max(0, r.x - p), y: Math.max(0, r.y - p), width: r.width + 2 * p, height: r.height + 2 * p };
}, sel, pad);
const waitText = (text, ms = 60000) => page.waitForFunction(
  t => document.body.innerText.includes(t), { timeout: ms }, text);
const clickButton = async text => {
  await page.evaluate(t => {
    const b = [...document.querySelectorAll('button')].reverse().find(x => x.textContent.trim() === t);
    if (!b) throw new Error(`no button ${t}`);
    b.click();
  }, text);
  await sleep(800);
};
const treeItem = async name => {
  await page.waitForFunction(n => [...document.querySelectorAll('span.truncate')].some(x => x.textContent.trim() === n),
    { timeout: 60000 }, name);
  await page.evaluate(n => [...document.querySelectorAll('span.truncate')].find(x => x.textContent.trim() === n).click(), name);
  await sleep(2500);
};
const searchWell = async text => {
  await page.click('input[placeholder="Search wells..."]', { clickCount: 3 });
  await page.type('input[placeholder="Search wells..."]', text);
  await sleep(600);
  await page.keyboard.press('Enter');   // picks the highlighted match
  await sleep(3000);
};
const load = async () => {
  await page.goto(APP, { waitUntil: 'networkidle2', timeout: 120000 });
  await waitText('Regions'.toUpperCase()).catch(() => {});
  await sleep(1500);
  await clickButton('Sample Data');     // the app remembers which data set was open last
  await sleep(1000);
};
// The well filters are remembered too, so each shot that opens an aquifer starts from none
const clearFilters = async () => {
  await page.evaluate(() => {
    const el = document.querySelector('[title="Hide wells with fewer measurements than this"]');
    const box = el.tagName === 'INPUT' ? el : el.querySelector('input');
    const set = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
    set.call(box, '0'); box.dispatchEvent(new Event('input', { bubbles: true }));
    const measured = [...document.querySelectorAll('label')].find(l => l.textContent.trim().startsWith('Measured'))?.querySelector('input');
    if (measured?.checked) measured.click();
  });
  await sleep(800);
};

await load();
if (want('home')) {
  await shot('app-home');
}
if (want('region')) {
  await load();
  await treeItem('Utah');
  await treeItem('Cache Valley');
  await clearFilters();
  await shot('app-aquifer');
  await shot('app-panel', { x: 0, y: 0, width: 320, height: 900 });
  await searchWell('22bad');
  await page.mouse.move(5, 5); await sleep(2500);   // the chart animates its curves in
  await shot('app-well');
  await shot('app-chart', await rect('#map-container', 0).then(m => ({ x: m.x, y: m.y + m.height, width: m.width, height: 900 - m.y - m.height })));
}
if (want('menu')) {
  await load();
  await page.evaluate(() => {
    const row = [...document.querySelectorAll('span.truncate')].find(x => x.textContent.trim() === 'Utah');
    row.nextElementSibling.click();      // the ⋮ trigger beside the name
  });
  await sleep(800);
  await shot('app-region-menu', { x: 0, y: 280, width: 320, height: 260 });
  await page.keyboard.press('Escape');
}
if (want('multiwell')) {
  await load();
  await treeItem('Utah'); await treeItem('Cache Valley'); await clearFilters();
  await searchWell('22bad');
  // shift-click the nearest other well with 2+ measurements (blue markers)
  // The search centers the map on the selected well, so skip the marker at the center
  const pt = await page.evaluate(() => {
    const m = document.getElementById('map-container').getBoundingClientRect();
    const mid = { x: m.x + m.width / 2, y: m.y + m.height / 2 };
    const d = p => Math.hypot(p.x - mid.x, p.y - mid.y);
    return [...document.querySelectorAll('path[fill="#0000ff"]')].map(p => p.getBoundingClientRect())
      .map(r => ({ x: r.x + r.width / 2, y: r.y + r.height / 2 }))
      .filter(p => d(p) > 40).sort((p, q) => d(p) - d(q))[0];
  });
  await page.keyboard.down('Shift'); await sleep(400);
  await page.mouse.click(pt.x, pt.y); await sleep(200);
  await page.keyboard.up('Shift');
  await sleep(3000); await page.mouse.move(5, 5); await sleep(2500);
  await shot('app-two-wells');
}
if (want('filter')) {
  await load();
  await treeItem('Utah'); await treeItem('Cache Valley');
  const box = await page.evaluateHandle(() => {
    const el = document.querySelector('[title="Hide wells with fewer measurements than this"]');
    return el.tagName === 'INPUT' ? el : el.querySelector('input');
  });
  await box.evaluate(el => { el.focus(); el.select(); }); await box.type('20');
  await box.evaluate(el => el.blur());
  await sleep(2500);
  await shot('app-filter');
}
if (want('mydata')) {
  await load();
  await clickButton('My Data'); await sleep(4000);
  await shot('app-mydata');
}
if (want('settings')) {
  await load();
  await page.click('button[aria-label="Settings"]'); await sleep(1200);
  await shot('app-settings');
}

await browser.close();
