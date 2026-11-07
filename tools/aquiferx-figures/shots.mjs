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
// Part 2's, in the Monterey County practice region: a well in the East Side Aquifer with a record from
// 1944, found by its ID, since other wells' names contain its name, 901
const PRACTICE_AQUIFER = 'East Side Aquifer';
const PRACTICE_WELL = { name: '367386N1216740W001', lat: 36.73863, lng: -121.67404 };

const browser = await puppeteer.launch({
  executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: 'new',
  args: ['--window-size=1440,900'], userDataDir: './.chrome-profile', protocolTimeout: 600000,
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
      const pane = document.querySelector('.leaflet-map-pane')?.style.transform;   // changes while the map moves
      return pane + t.map(x => x.src).sort().join('|') + (t.every(x => x.classList.contains('leaflet-tile-loaded')) ? '#ok' : '#wait');
    });
    if (state !== last) { last = state; since = Date.now(); }
    else if (state.endsWith('#ok') && Date.now() - since > 1200) break;
    await sleep(300);
  }
  // Every point of the map should sit on a loaded tile; a gap means tiles were never requested
  const gaps = await page.evaluate(() => {
    const m = document.getElementById('map-container')?.getBoundingClientRect();
    if (!m) return 0;
    // Only the current zoom level's tiles count: Leaflet keeps the previous level's underneath, which can hide a gap
    const level = [...document.querySelectorAll('.leaflet-tile-container')]
      .sort((a, b) => (+b.style.zIndex || 0) - (+a.style.zIndex || 0))[0];
    const rects = [...(level?.querySelectorAll('.leaflet-tile-loaded') ?? [])].map(t => t.getBoundingClientRect());
    let missing = 0;
    for (let i = 1; i < 12; i++) for (let j = 1; j < 12; j++) {
      const x = m.x + m.width * i / 12, y = m.y + m.height * j / 12;
      if (!rects.some(r => x >= r.left && x <= r.right && y >= r.top && y <= r.bottom)) missing++;
    }
    return missing;
  });
  if (gaps) console.log(`MAP GAPS: ${gaps} of 121 sample points have no tile`);
};
const shot = async (name, clip) => {
  // Twice, a second apart: once it caught an in-between state where the tiles had not been placed yet
  await tiles(); await sleep(1000); await tiles(); await sleep(300);
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
// Screen position of a point, from the position of a basemap tile. Esri tile URLs end /tile/z/y/x,
// OpenStreetMap's /z/x/y.png.
const toScreen = ({ lat, lng }) => page.evaluate((lat, lng) => {
  const parse = src => {
    let m = src.match(/\/tile\/(\d+)\/(\d+)\/(\d+)/);
    if (m) return [+m[1], +m[3], +m[2]];
    m = src.match(/\/(\d+)\/(\d+)\/(\d+)\.png/);
    return m && [+m[1], +m[2], +m[3]];
  };
  const tile = [...document.querySelectorAll('.leaflet-tile-loaded')].find(t => parse(t.src));
  const [z, x, y] = parse(tile.src);
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
// Zoom out and pan until the open aquifer's outline (stroke #6366f1) sits whole in the map, clear of
// the cards over it: the time slider at the bottom, the legends at the sides
const fitAquifer = async () => {
  for (let i = 0; i < 6; i++) {
    await tiles();
    const g = await page.evaluate(() => {
      const r = el => el.getBoundingClientRect();
      const a = [...document.querySelectorAll('path[stroke="#6366f1"]')].map(r);
      const m = r(document.getElementById('map-container'));
      const slider = document.querySelector('input[type=range]')?.closest('.rfs-card');
      const box = { left: m.left + 270, right: m.right - 260, top: m.top + 20, bottom: (slider ? r(slider).top : m.bottom) - 20 };
      const aq = { left: Math.min(...a.map(x => x.left)), right: Math.max(...a.map(x => x.right)),
                   top: Math.min(...a.map(x => x.top)), bottom: Math.max(...a.map(x => x.bottom)) };
      return { box, aq, grab: { x: m.left + 200, y: m.top + m.height * 0.6 } };
    });
    const { box, aq, grab } = g;
    if (aq.bottom - aq.top > box.bottom - box.top || aq.right - aq.left > box.right - box.left) { await zoomOut(1); continue; }
    const dx = (box.left + box.right) / 2 - (aq.left + aq.right) / 2, dy = (box.top + box.bottom) / 2 - (aq.top + aq.bottom) / 2;
    if (Math.abs(dx) < 8 && Math.abs(dy) < 8) return;
    await page.mouse.move(grab.x, grab.y); await page.mouse.down();
    for (let k = 1; k <= 10; k++) { await page.mouse.move(grab.x + dx * k / 10, grab.y + dy * k / 10); await sleep(30); }
    await page.mouse.up(); await sleep(2500);   // the drag coasts before the map requests new tiles
  }
};
// My Data holding one region, a fresh copy of the Oregon sample. Whatever an earlier run left in
// My Data is deleted first, so copies do not pile up.
const clearMyData = async () => {
  await load();
  await page.click('button[aria-label="Settings"]'); await sleep(1000);
  const canDelete = await page.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find(x => x.textContent.trim() === 'Delete all My Data');
    return !!b && !b.disabled;
  });
  if (canDelete) { await clickButton('Delete all My Data'); await clickButton('Delete everything'); await sleep(2000); }
  await clickButton('Close');
};
const myDataWithOregon = async () => {
  await clearMyData();
  await page.evaluate(() => {
    const row = [...document.querySelectorAll('span.truncate')].find(x => x.textContent.trim() === 'Oregon');
    row.nextElementSibling.click();
  });
  await sleep(600);
  await clickButton('Copy to My Data'); await sleep(5000);   // the app switches to My Data and opens the copy
  await treeItem('Williamson');
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
  // A taller window keeps the map one zoom level closer, where the basemap shows terrain
  await page.setViewport({ width: 1440, height: 1000, deviceScaleFactor: 2 });
  await load();
  await treeItem(REGION); await treeItem(AQUIFER); await setMinMeasurements(1);
  await treeItem('wte_kriging'); await sleep(4000);
  await fitAquifer();   // the chart panel shortens the map, which then clips the aquifer's southern tail
  await page.mouse.move(5, 5);
  await shot('app-overview');
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
}
if (want('panel')) {
  // Oregon has two aquifers and several data types, so the panel is short and shows the Data type list
  await page.setViewport({ width: 1440, height: 800, deviceScaleFactor: 2 });
  await load();
  await treeItem('Oregon'); await treeItem('Williamson'); await clearFilters();
  await page.mouse.move(5, 5);
  await shot('app-panel', { x: 0, y: 0, width: 320, height: 800 });
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
}
if (want('region')) {
  await load();
  await treeItem(REGION);
  await treeItem(AQUIFER);
  await clearFilters();
  await shot('app-aquifer');
  await searchWell(WELL); await zoomOut(4);
  await page.mouse.move(5, 5); await sleep(2000);   // the chart animates its curves in
  await shot('app-chart', await rect('#map-container', 0).then(m => ({ x: m.x, y: m.y + m.height, width: m.width, height: 900 - m.y - m.height })));
}
if (want('mapparts')) {
  // Small crops of the map's controls for the Map section of The App Interface
  await load();
  await treeItem(REGION); await treeItem(AQUIFER); await clearFilters();
  await searchWell(WELL); await zoomOut(4); await page.mouse.move(5, 5); await sleep(1500);
  const box = (r, pad = 6) => ({ x: r.x - pad, y: r.y - pad, width: r.width + 2 * pad, height: r.height + 2 * pad });
  const union = sel => page.evaluate(sel => {
    const els = [...document.querySelectorAll(sel)].flatMap(e => [e, ...e.querySelectorAll('*')]).map(e => e.getBoundingClientRect()).filter(r => r.width && r.height);
    const l = Math.min(...els.map(r => r.left)), t = Math.min(...els.map(r => r.top));
    return { x: l, y: t, width: Math.max(...els.map(r => r.right)) - l, height: Math.max(...els.map(r => r.bottom)) - t };
  }, sel);
  // The location bar: Home, the region, the aquifer and the selected well
  const crumbs = await page.evaluate(() => {
    const home = [...document.querySelectorAll('button')].find(b => b.textContent.trim() === 'Home');
    const els = [...home.parentElement.querySelectorAll('*')].map(e => e.getBoundingClientRect()).filter(r => r.width && r.height);
    const l = Math.min(...els.map(r => r.left)), t = Math.min(...els.map(r => r.top));
    return { x: l, y: t, width: Math.max(...els.map(r => r.right)) - l, height: Math.max(...els.map(r => r.bottom)) - t };
  });
  await shot('map-breadcrumb', box(crumbs, 8));
  await shot('map-zoom', box(await union('.leaflet-top.leaflet-left')));   // + and -, and the frame button under them
  for (const [label, name] of [['Analyze Trends', 'button-trends'], ['Spatial Analysis', 'button-spatial'], ['Impute Gaps', 'button-impute']]) {
    await shot(name, box(await union(`button[aria-label="${label}"]`), 4));
  }
  const legend = await page.evaluate(() => {
    const h = [...document.querySelectorAll('.rfs-card')].find(c => c.textContent.trim().startsWith('Wells'));
    const r = h.getBoundingClientRect(); return { x: r.x, y: r.y, width: r.width, height: r.height };
  });
  await shot('map-legend', box(legend));
  await page.click('button[aria-label="Basemap"]'); await page.mouse.move(700, 600); await sleep(1200);   // off the button, so no tooltip
  const basemap = await page.evaluate(() => {
    const wrap = document.querySelector('button[aria-label="Basemap"]').closest('div.absolute');
    const els = [wrap, ...wrap.querySelectorAll('*')].map(e => e.getBoundingClientRect()).filter(r => r.width && r.height);
    const l = Math.min(...els.map(r => r.left)), t = Math.min(...els.map(r => r.top));
    return { x: l, y: t, width: Math.max(...els.map(r => r.right)) - l, height: Math.max(...els.map(r => r.bottom)) - t };
  });
  await shot('map-basemap', box(basemap));
  await page.click('button[aria-label="Basemap"]'); await sleep(600);
  // Hide the wells legend, which sits under the matches and would peek out at the crop's edge
  await page.evaluate(() => { [...document.querySelectorAll('.rfs-card')].find(c => c.textContent.trim().startsWith('Wells')).style.visibility = 'hidden'; });
  await page.click('input[placeholder="Search wells..."]'); await page.type('input[placeholder="Search wells..."]', '(C-36-16)2'); await sleep(1000);
  const search = await page.evaluate(() => {
    // The box and its list of matches; the list scrolls, so its contents run past what shows
    const r = document.querySelector('input[placeholder="Search wells..."]').closest('div.absolute').getBoundingClientRect();
    return { x: r.x, y: r.y, width: r.width, height: r.height };
  });
  await shot('map-search', box(search));
  console.log('sizes (CSS px):', JSON.stringify({ crumbs, legend, basemap, search }));
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
if (want('datatype')) {
  // Oregon has water levels and water quality, so the panel shows the Data type list
  await load();
  await treeItem('Oregon'); await sleep(1500);
  const box = await page.evaluate(() => {
    const a = document.querySelector('label[for="data-type-select"]').getBoundingClientRect();
    const b = document.querySelector('#data-type-select').getBoundingClientRect();
    const p = 12, x = Math.min(a.left, b.left) - p, y = a.top - p;
    return { x, y, width: Math.max(a.right, b.right) + p - x, height: b.bottom + p - y };
  });
  await shot('panel-datatype', box);
}
if (want('mydata') || want('settings')) {
  await myDataWithOregon();
  await page.mouse.move(5, 5);
  if (want('mydata')) await shot('app-mydata');
  await page.click('button[aria-label="Settings"]'); await sleep(1500);
  // Only the dialog, with a little of the dimmed app around it: the whole window shrunk to fit the page leaves it unreadable
  if (want('settings')) await shot('app-settings', await rect('div.fixed.inset-0 > div', 16));
  await clickButton('Close');
}

// Part 2: the Add Data window and its importers, fed the files make-practice.py writes
const PRACTICE = new URL('./practice/', import.meta.url).pathname;
// The topmost dialog, with a little of the dimmed window around it
const topCard = (pad = 16) => page.evaluate(p => {
  const cards = [...document.querySelectorAll('div.fixed.inset-0 > div.bg-white')];
  const r = cards[cards.length - 1].getBoundingClientRect();
  return { x: Math.max(0, r.x - p), y: Math.max(0, r.y - p), width: r.width + 2 * p, height: r.height + 2 * p };
}, pad);
const upload = async file => {
  const inputs = await page.$$('input[type=file]');
  await inputs[inputs.length - 1].uploadFile(PRACTICE + file);
  await sleep(2500);
};
const clickLabel = async text => {
  await page.evaluate(t => {
    const l = [...document.querySelectorAll('label')].reverse().find(x => x.textContent.trim().startsWith(t));
    if (!l) throw new Error(`no label ${t}`);
    (l.querySelector('input') || l).click();
  }, text);
  await sleep(600);
};
const cardButton = async (title, button) => {     // a button on one of the Add Data window's cards
  await page.evaluate((t, b) => {
    const card = [...document.querySelectorAll('h4')].find(h => h.textContent.trim() === t).closest('.border');
    [...card.querySelectorAll('button')].find(x => x.textContent.trim() === b).click();
  }, title, button);
  await sleep(1200);
};
const newRegion = async (name, file, singleUnit) => {
  await clickButton('Add Region');
  await page.type('input[placeholder="e.g., California Central Valley"]', name);
  if (!singleUnit) await clickLabel('Single-unit region');
  await sleep(400);
  return async () => {             // the rest, after any screenshot of the first step
    await clickButton('Next'); await upload(file);
    await clickButton('Create Region'); await sleep(3000);
  };
};
const waitText2 = (text, ms) => page.waitForFunction(t => document.body.innerText.includes(t), { timeout: ms }, text);
// One panel of the topmost dialog: the bordered box around a heading, or (up = n) the heading's nth parent
const panelOf = (text, up = 0, pad = 10) => page.evaluate((t, u, p) => {
  const el = [...document.querySelectorAll('p, span, label, h4, option')].reverse().find(x => x.textContent.trim() === t);
  if (!el) throw new Error(`no ${t}`);
  let box = el.closest(u ? 'body' : '.rounded-lg');
  if (u) { box = el; for (let i = 0; i < u; i++) box = box.parentElement; }
  const r = box.getBoundingClientRect();
  return { x: r.x - p, y: r.y - p, width: r.width + 2 * p, height: r.height + 2 * p };
}, text, up, pad);
// The top of the topmost dialog, down to the file chooser
const dialogTop = (pad = 16) => page.evaluate(p => {
  const cards = [...document.querySelectorAll('div.fixed.inset-0 > div.bg-white')];
  const c = cards[cards.length - 1].getBoundingClientRect();
  const inputs = [...document.querySelectorAll('input[type=file]')];
  const f = inputs[inputs.length - 1].getBoundingClientRect();
  return { x: c.x - p, y: c.y - p, width: c.width + 2 * p, height: f.bottom + 20 - c.y + p };
}, pad);

if (want('adddata') || want('wq')) {
  // Tall enough that the longer importers fit without scrolling inside the dialog
  await page.setViewport({ width: 1440, height: 2000, deviceScaleFactor: 2 });
}
if (want('adddata')) {
  await clearMyData();
  await clickButton('My Data'); await sleep(800);
  await clickButton('Add Data');
  const finish = await newRegion('Monterey County', 'monterey-region.geojson', false);
  await shot('data-new-region', await topCard());
  await finish();
  await shot('data-hub-new', await topCard());

  await cardButton('Aquifers', 'Add Aquifers');
  await upload('monterey-aquifers.geojson');         // opens the column mapper
  await shot('data-aquifer-columns', await topCard());
  await clickButton('Done'); await clickButton('Save Aquifers'); await sleep(2500);

  await cardButton('Wells', 'Add Wells');
  await clickButton('USGS Download');
  await shot('data-wells-usgs', await topCard());
  await clickButton('Upload CSV');
  await clickLabel('Use aquifer_id column');
  await upload('monterey-wells.csv');
  await clickButton('Done'); await sleep(1500);
  await shot('data-wells', await topCard());
  await clickButton('Save Wells'); await sleep(3000);

  await cardButton('Measurements', 'Add Measurements');
  await upload('monterey-water-levels.csv');
  // The whole dialog is too tall to read on a page, so its parts
  await shot('meas-top', await dialogTop());
  await shot('meas-columns-ids', await panelOf('Columns'));
  await shot('meas-duplicates', await panelOf('Average duplicates'));
  await clickButton('Save Measurements');
  await waitText2('Import complete', 600000);
  await sleep(800);
  await shot('data-levels-done', await topCard());
  await clickButton('Done'); await sleep(2500);
  await clickButton('Done'); await sleep(1500);
}
if (want('wq')) {
  // The Pajaro Valley, a single-unit region with no wells, then its water quality file, whose rows
  // make the wells from their names and coordinates
  await load();
  await clickButton('My Data'); await sleep(800);
  await clickButton('Add Data');
  await (await newRegion('Pajaro Valley', 'pajaro-region.geojson', true))();
  await cardButton('Measurements', 'Add Measurements');
  await upload('pajaro-water-quality.csv');
  await waitText2('by proximity', 60000);
  await sleep(800);
  await shot('meas-columns-wells', await panelOf('Columns'));
  await shot('meas-matching', await panelOf('Well matching'));
  await shot('meas-datacolumns', await panelOf('Map data columns'));
  await clickButton('Save Measurements');
  await waitText2('Import complete', 600000);
  await sleep(800);
  await clickButton('Done'); await sleep(2500);

  // A laptop-sized window, where the parameter list scrolls instead of filling a tall picture
  await page.setViewport({ width: 1440, height: 1000, deviceScaleFactor: 2 }); await sleep(800);
  await cardButton('Measurements', 'Add Measurements');
  await clickButton('Water Quality (WQP)');
  await clickButton('Pick parameters');
  for (const name of ['Nitrate', 'Arsenic']) {
    await page.evaluate(n => {
      const row = [...document.querySelectorAll('tr')].find(r => r.textContent.includes(n) && r.querySelector('input[type=checkbox]'));
      row.querySelector('input[type=checkbox]').click();
    }, name);
    await sleep(300);
  }
  await shot('data-wqp-picker', await topCard());
  await clickButton('Apply');
  await clickButton('Estimate');
  await waitText2('Estimated:', 60000).catch(() => {});
  await sleep(800);
  await shot('data-wqp', await topCard());
}
if (want('edit')) {
  // Monterey County, as the adddata step leaves it in My Data
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
  await load();
  await clickButton('My Data'); await sleep(1500);
  await page.evaluate(() => {
    const row = [...document.querySelectorAll('span.truncate')].find(x => x.textContent.trim() === 'Monterey County');
    row.nextElementSibling.click();
  });
  await sleep(600);
  await clickButton('Edit'); await sleep(800);
  await shot('data-edit-region', await topCard());
  await clickButton('Cancel');

  await treeItem('Monterey County'); await treeItem(PRACTICE_AQUIFER); await clearFilters();
  await searchWell(PRACTICE_WELL); await sleep(3000);
  await clickButton('View/Edit'); await sleep(1500);
  // The table opens at the earliest values; bring the first flagged one into view
  await page.evaluate(() => {
    const row = [...document.querySelectorAll('tbody tr')].find(r => r.classList.contains('bg-red-50') && !r.classList.contains('line-through'));
    row?.scrollIntoView({ block: 'center' });
  });
  await sleep(600);
  await shot('edit-table', await topCard());
  await clickButton('Cancel'); await sleep(800);

  // Right-click a measurement on the chart for its menu
  const dot = await page.evaluate(() => {
    const cs = [...document.querySelectorAll('.recharts-wrapper circle')].map(c => c.getBoundingClientRect()).filter(r => r.width > 0);
    const r = cs[Math.floor(cs.length * 0.6)];
    return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
  });
  await page.mouse.click(dot.x, dot.y, { button: 'right' }); await sleep(800);
  const box = await page.evaluate(d => {
    const m = document.querySelector('.rfs-menu').getBoundingClientRect();
    const x = Math.min(d.x, m.left) - 70, y = Math.min(d.y, m.top) - 50;
    return { x, y, width: Math.max(d.x, m.right) + 70 - x, height: Math.max(d.y, m.bottom) + 50 - y };
  }, dot);
  await shot('edit-point-menu', box);
  await page.keyboard.press('Escape');
}

await browser.close();
