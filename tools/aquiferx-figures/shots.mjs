// Screenshots of Aquifer Analyst for docs/aquiferx. See README.md.
//   node shots.mjs <outdir> [name,name,...]
import puppeteer from 'puppeteer-core';

const APP = process.env.AQX_URL || 'http://localhost:5198/';
const OUT = process.argv[2] || 'raw';
const only = process.argv[3];
const want = n => !only || only.split(',').includes(n);
const sleep = ms => new Promise(r => setTimeout(r, ms));

// The examples: an aquifer in the Utah sample, and two wells in it with long, steady records
const REGION = 'Utah';
const AQUIFER = 'Escalante Valley-Beryl-Enterprise';
const WELL = { name: '(C-36-16)29daa- 1', lat: 37.6263635, lng: -113.6613536 };
const WELL2 = { name: '(C-35-16)33bcc- 1', lat: 37.71441685, lng: -113.655799 };

const browser = await puppeteer.launch({
  executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: 'new',
  args: ['--window-size=1440,900'], userDataDir: './.chrome-profile',
});
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
page.on('console', m => { if (m.type() === 'error') console.log('CONSOLE', m.text().slice(0, 160)); });
page.on('pageerror', e => console.log('PAGEERROR', e.message.slice(0, 160)));

// Wait until the map has stopped moving and every basemap tile it asked for has loaded. Checking
// only for loaded tiles is not enough: mid-flight, the tiles for the new view are not requested yet.
const tiles = async () => {
  let last = '', since = Date.now();
  for (let i = 0; i < 150; i++) {
    const state = await page.evaluate(() => {
      const t = [...document.querySelectorAll('.leaflet-tile')];
      return t.map(x => x.src).sort().join('|') + (t.every(x => x.classList.contains('leaflet-tile-loaded')) ? '#ok' : '#wait');
    });
    if (state !== last) { last = state; since = Date.now(); }
    else if (state.endsWith('#ok') && Date.now() - since > 1200) return;
    await sleep(300);
  }
  console.log('tiles did not settle');
};
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
// Screen position of a point, from the position of a basemap tile (z/x/y in its URL)
const toScreen = ({ lat, lng }) => page.evaluate((lat, lng) => {
  const tile = [...document.querySelectorAll('.leaflet-tile-loaded')].find(t => /\/\d+\/\d+\/\d+\.png/.test(t.src));
  const [z, x, y] = tile.src.match(/\/(\d+)\/(\d+)\/(\d+)\.png/).slice(1).map(Number);
  const r = tile.getBoundingClientRect(), n = 2 ** z, rad = lat * Math.PI / 180;
  const tx = (lng + 180) / 360 * n, ty = (1 - Math.log(Math.tan(rad) + 1 / Math.cos(rad)) / Math.PI) / 2 * n;
  return { x: r.left + (tx - x) * r.width, y: r.top + (ty - y) * r.height };
}, lat, lng);
const searchWell = async well => {
  await page.click('input[placeholder="Search wells..."]');
  await page.type('input[placeholder="Search wells..."]', well.name);
  await sleep(600);
  await page.keyboard.press('Enter');   // picks the highlighted match; the map flies to zoom 14
  await sleep(2500);
};
const zoomOut = async clicks => {      // each click is half a zoom level
  for (let i = 0; i < clicks; i++) { await page.click('.leaflet-control-zoom-out'); await sleep(450); }
  await sleep(1000);
};
const setMinMeasurements = async n => {
  const box = await page.evaluateHandle(() => {
    const el = document.querySelector('[title="Hide wells with fewer measurements than this"]');
    return el.tagName === 'INPUT' ? el : el.querySelector('input');
  });
  await box.evaluate(el => { el.focus(); el.select(); }); await box.type(String(n));
  await box.evaluate(el => el.blur());
  await sleep(2000);
};
const clickWell = async (well, shift = false) => {
  await tiles();
  let pt = await toScreen(well);
  for (let i = 0; i < 6; i++) {        // zoom out until the well is comfortably inside the map
    const m = await rect('#map-container');
    if (pt.x > m.x + 60 && pt.x < m.x + m.width - 60 && pt.y > m.y + 60 && pt.y < m.y + m.height - 60) break;
    await zoomOut(1); await tiles(); pt = await toScreen(well);
  }
  if (shift) { await page.keyboard.down('Shift'); await sleep(400); }
  await page.mouse.click(pt.x, pt.y); await sleep(200);
  if (shift) await page.keyboard.up('Shift');
  await sleep(2500); await page.mouse.move(5, 5);
  await sleep(2500);   // the chart animates its curves in
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
if (want('overview')) {
  await load();
  await treeItem(REGION); await treeItem(AQUIFER); await setMinMeasurements(20);
  await treeItem('wte_kriging'); await sleep(4000);
  await page.focus('input[type=range]'); await page.keyboard.press('End');   // the last year of the map
  await sleep(3000); await page.mouse.move(5, 5);
  await shot('app-overview');
}
if (want('region')) {
  await load();
  await treeItem(REGION);
  await treeItem(AQUIFER);
  await clearFilters();
  await shot('app-aquifer');
  await shot('app-panel', { x: 0, y: 0, width: 320, height: 900 });
  await searchWell(WELL); await zoomOut(4);
  await page.mouse.move(5, 5); await sleep(2000);   // the chart animates its curves in
  await shot('app-chart', await rect('#map-container', 0).then(m => ({ x: m.x, y: m.y + m.height, width: m.width, height: 900 - m.y - m.height })));
}
if (want('menu')) {
  await load();
  await page.evaluate(r => {
    const row = [...document.querySelectorAll('span.truncate')].find(x => x.textContent.trim() === r);
    row.nextElementSibling.click();      // the ⋮ trigger beside the name
  }, REGION);
  await sleep(800);
  await shot('app-region-menu', { x: 0, y: 280, width: 320, height: 260 });
  await page.keyboard.press('Escape');
}
if (want('multiwell')) {
  await load();
  await treeItem(REGION); await treeItem(AQUIFER); await clearFilters();
  await searchWell(WELL); await zoomOut(4);
  await clickWell(WELL2, true);
  await shot('app-two-wells');
}
if (want('filter')) {
  await load();
  await treeItem(REGION); await treeItem(AQUIFER);
  await setMinMeasurements(20);
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
