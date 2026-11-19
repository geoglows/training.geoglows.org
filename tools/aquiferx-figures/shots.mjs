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
// Part 2's, in the Monterey County practice region: a well in the Langley Area measured each winter
// since 1960, 13783, found by its ID
const PRACTICE_AQUIFER = 'Langley Area';
const PRACTICE_WELL = { name: '367886N1216748W001', lat: 36.7886, lng: -121.67483 };

const browser = await puppeteer.launch({
  executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: 'new',
  // Without the GPU, which left loaded basemap tiles unpainted more often (shot() checks for them)
  args: ['--window-size=1440,900', '--disable-gpu'], userDataDir: './.chrome-profile', protocolTimeout: 600000,
});
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
page.on('console', m => { if (m.type() === 'error') console.log('CONSOLE', m.text().slice(0, 160)); });
page.on('pageerror', e => console.log('PAGEERROR', e.message.slice(0, 160)));
// A basemap tile that fails still counts as loaded to Leaflet, so tiles() can't see it: report it
page.on('requestfailed', r => { if (r.resourceType() === 'image') console.log('TILE FAILED', r.failure()?.errorText, r.url().slice(-60)); });
page.on('response', r => { if (r.request().resourceType() === 'image' && r.status() >= 400) console.log('TILE', r.status(), r.url().slice(-60)); });
// Leaflet's grey background shows wherever the basemap is not painted, and Chrome sometimes leaves tiles unpainted that the page
// has loaded and placed. Magenta instead, so shot() can find any such gap in the picture itself.
// Each page load also starts from the app's default map display (wells shown, no labels, no filters): the app remembers it,
// and a run that stopped part way left it changed for the next.
await page.evaluateOnNewDocument(() => { try { localStorage.removeItem('aqx-map-display'); } catch { /* none */ } });
await page.evaluateOnNewDocument(() => document.addEventListener('DOMContentLoaded', () => {
  const s = document.createElement('style');
  s.textContent = '.leaflet-container { background: #ff00ff !important; }';
  document.head.appendChild(s);
}));

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
// The share of a picture's pixels that are magenta, or magenta under a dialog's dimming: the map's background (above)
const blankShare = buf => page.evaluate(async b64 => {
  const img = new Image(); img.src = 'data:image/png;base64,' + b64; await img.decode();
  const c = new OffscreenCanvas(img.width, img.height), g = c.getContext('2d');
  g.drawImage(img, 0, 0);
  const d = g.getImageData(0, 0, img.width, img.height).data;
  let n = 0, sx = 0, sy = 0;
  for (let i = 0; i < d.length; i += 4) if (d[i] - d[i + 1] > 60 && d[i + 2] - d[i + 1] > 60) { n++; sx += (i / 4) % img.width; sy += Math.floor(i / 4 / img.width); }
  return { share: n / (d.length / 4), x: n ? sx / n / devicePixelRatio : 0, y: n ? sy / n / devicePixelRatio : 0 };
}, Buffer.from(buf).toString('base64'));
const shot = async (name, clip) => {
  // Twice, a second apart: once it caught an in-between state where the tiles had not been placed yet
  await tiles(); await sleep(1000); await tiles(); await sleep(300);
  for (let attempt = 0; ; attempt++) {
    const buf = await page.screenshot({ clip, captureBeyondViewport: false });
    const { share: blank, x: bx, y: by } = await blankShare(buf);
    if (blank < 0.0005) {
      (await import('fs')).writeFileSync(`${OUT}/${name}.png`, buf);
      console.log('saved', name, attempt ? `(after ${attempt} retries)` : '');
      return;
    }
    console.log(`BLANK MAP in ${name}: ${(100 * blank).toFixed(1)}% of the picture`);
    // The basemap tiles over the middle of the blank area (tiles take no pointer events, so elementsFromPoint misses them)
    console.log(JSON.stringify(await page.evaluate((x, y) => ({ at: [x, y].map(Math.round),
      levels: [...document.querySelectorAll('.leaflet-tile-container')].map(c => ({ z: c.style.zIndex, n: c.children.length, t: c.style.transform })),
      over: [...document.querySelectorAll('.leaflet-tile')].filter(e => { const r = e.getBoundingClientRect(); return x >= r.left && x <= r.right && y >= r.top && y <= r.bottom; })
        .map(e => { const c = getComputedStyle(e); return { cls: e.className, src: e.src.slice(-30), op: c.opacity, vis: c.visibility, disp: c.display, done: e.complete, w: e.naturalWidth, z: e.parentElement.style.zIndex, t: e.style.transform, wh: [e.style.width, e.style.height] }; }),
    }), (clip?.x ?? 0) + bx, (clip?.y ?? 0) + by)));
    (await import('fs')).writeFileSync(`${OUT}/${name}-BLANK${attempt}.png`, buf);
    if (attempt === 3) throw new Error(`${name}: the basemap would not paint`);
    // Make Chrome paint the map again: the tiles were loaded, placed and opaque, yet unpainted
    await page.evaluate(() => Promise.all([...document.querySelectorAll('.leaflet-tile')].map(t => t.decode().catch(() => {}))));
    await tiles(); await sleep(1500);
  }
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
// Drag the bar between the map and the chart panel until the panel is h CSS px tall. It opens at 250, short for a picture of
// the chart alone.
const taller = async h => {
  const g = await page.evaluate(() => {
    const bar = document.querySelector('div.cursor-row-resize'), r = bar.getBoundingClientRect();
    return { x: r.x + r.width / 2, y: r.y + r.height / 2, panel: bar.nextElementSibling.getBoundingClientRect().height };
  });
  await page.mouse.move(g.x, g.y); await page.mouse.down();
  for (let k = 1; k <= 10; k++) { await page.mouse.move(g.x, g.y - (h - g.panel) * k / 10); await sleep(30); }
  await page.mouse.up(); await sleep(1500);
  await page.mouse.move(5, 5);
};
// Crops: the map with the chart panel under it, and the chart panel alone
const lower = () => rect('#map-container', 0).then(m => ({ x: m.x, y: m.y, width: m.width, height: page.viewport().height - m.y }));
const chartOnly = () => rect('div.cursor-row-resize + div', 0);   // the chart panel, under the bar that resizes it
// Drag across the chart from one year to another to zoom in. The x axis's tick labels (a year, or month/year when the chart
// spans less than two years) give the screen position of a date.
const zoomChart = async (fromYear, toYear) => {
  const g = await page.evaluate((y0, y1) => {
    const labels = [...document.querySelectorAll('g.recharts-xAxis-tick-labels')].sort((a, b) => b.getBoundingClientRect().width - a.getBoundingClientRect().width)[0];
    const r = labels.closest('svg').getBoundingClientRect();
    const ticks = [...labels.querySelectorAll('.recharts-cartesian-axis-tick-value')].map(t => {
      const p = t.textContent.trim().split('/').map(Number), b = t.getBoundingClientRect();
      return { year: p.length === 1 ? p[0] : p[1] + (p[0] - 1) / 12, x: b.x + b.width / 2 };
    });
    const a = ticks[0], z = ticks[ticks.length - 1], px = yr => a.x + (yr - a.year) / (z.year - a.year) * (z.x - a.x);
    return { from: px(y0), to: px(y1), y: r.y + r.height / 2 };
  }, fromYear, toYear);
  await page.mouse.move(g.from, g.y);
  await page.mouse.down();
  for (let i = 1; i <= 10; i++) { await page.mouse.move(g.from + (g.to - g.from) * i / 10, g.y); await sleep(40); }
  await page.mouse.up(); await sleep(1500);
  await page.evaluate(() => document.activeElement?.blur());    // no focus outline around the chart
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
  await searchWell(WELL); await zoomOut(4); await taller(450);
  await page.mouse.move(5, 5); await sleep(2000);   // the chart animates its curves in
  await shot('app-chart', await chartOnly());
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
if (want('nested')) {
  // Three wells of one nest, finished at 180, 264 and 302 ft, share a spot in the example aquifer: a click there opens the list
  const NEST = { name: '(C-35-15)28bdc- 3', lat: 37.72886216, lng: -113.5407957 };
  await load();
  await treeItem(REGION); await treeItem(AQUIFER); await clearFilters();
  await searchWell(NEST); await tiles();
  const p = await toScreen(NEST);
  await page.mouse.click(p.x, p.y); await sleep(1200);
  await page.mouse.move(p.x - 200, p.y + 150); await sleep(600);   // off the marker, so its popup closes
  await page.evaluate(() => document.activeElement?.blur());           // and no focus outline on it
  const box = await page.evaluate(pt => {
    const d = [...document.querySelectorAll('div.absolute')].find(x => /wells here/.test(x.innerText) && x.querySelector('ul'));
    const r = d.getBoundingClientRect();
    const x = Math.min(pt.x, r.left) - 80, y = Math.min(pt.y, r.top) - 70;
    return { x, y, width: Math.max(pt.x, r.right) + 80 - x, height: Math.max(pt.y, r.bottom) + 70 - y };
  }, p);
  await shot('app-nested', box);
}
if (want('chart')) {
  // Part 3: the example well's chart with its ground surface elevation, then with a 12-month moving average
  await load();
  await treeItem(REGION); await treeItem(AQUIFER); await clearFilters();
  await searchWell(WELL); await zoomOut(4); await taller(450);
  const chartBox = chartOnly;
  const check = async label => {
    await page.evaluate(l => [...document.querySelectorAll('label')].find(x => x.textContent.trim() === l).querySelector('input').click(), label);
    await sleep(1500);
  };
  await check('GSE'); await page.mouse.move(5, 5); await sleep(2000);
  await shot('chart-gse', await chartBox());
  await check('GSE'); await check('MAvg');
  await page.evaluate(() => {
    const el = [...document.querySelectorAll('label')].find(x => x.textContent.trim().startsWith('months:')).querySelector('input');
    const set = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
    set.call(el, '12'); el.dispatchEvent(new Event('input', { bubbles: true }));
  });
  await page.mouse.move(5, 5); await sleep(2500);
  // Zoom to 1985 to 2005, where the readings are dense
  await zoomChart(1985, 2005);
  await page.mouse.move(5, 5); await page.evaluate(() => document.activeElement?.blur()); await sleep(1500);
  await shot('chart-mavg', await chartBox());
  await clickButton('Reset Zoom');
  await check('MAvg');
}
if (want('trends')) {
  // Part 3: Analyze Trends with its 30-year window, first over the region's aquifers, then over the example aquifer's
  // wells with the two example wells selected, so the chart shows their trend lines
  await load();
  await treeItem(REGION);
  await page.click('button[aria-label="Analyze Trends"]'); await sleep(3000);
  await page.mouse.move(5, 5); await sleep(1000);
  await shot('trends-aquifers');
  await treeItem(AQUIFER); await clearFilters();
  await searchWell(WELL); await zoomOut(4);
  await clickWell(WELL2, true);
  // Zoom the chart to the window, where the trend lines are fitted
  await zoomChart(new Date().getFullYear() - 30, new Date().getFullYear() + 1);
  await page.mouse.move(5, 5); await sleep(1500);
  await shot('trends-wells');
}
if (want('impute')) {
  // Part 4: the Escalante model saved in Sample Data, on a well with a ten-year gap, first with MC+LNN's estimate beside the
  // readings (the chart's default), then combined; then the Impute Gaps wizard on a My Data copy of Utah, in a taller window
  // so the whole first step shows
  const GAP_WELL = { name: '(C-36-16) 3ddc- 1', lat: 37.67802916, lng: -113.6271865 };
  await load();
  await treeItem(REGION); await treeItem(AQUIFER); await clearFilters();
  await treeItem('mc_lnn');
  await searchWell(GAP_WELL); await zoomOut(4); await taller(450);
  const chartBox = chartOnly;
  await page.mouse.move(5, 5); await sleep(2500);
  await shot('impute-separate', await chartBox());
  await page.evaluate(() => [...document.querySelectorAll('label')].find(x => x.textContent.trim() === 'Combined').querySelector('input').click());
  await page.mouse.move(5, 5); await sleep(2500);
  await shot('impute-combined', await chartBox());

  await clearMyData();
  await page.evaluate(n => [...document.querySelectorAll('span.truncate')].find(x => x.textContent.trim() === n).nextElementSibling.click(), REGION);
  await sleep(600);
  await clickButton('Copy to My Data'); await sleep(15000);   // the app switches to My Data and opens the copy
  await treeItem(AQUIFER);
  await page.setViewport({ width: 1440, height: 1250, deviceScaleFactor: 2 }); await sleep(1500);
  await page.click('button[aria-label="Impute Gaps"]');
  await waitText('wells will be filled'); await sleep(2500);
  await shot('impute-wizard', await rect('div.fixed.inset-0 > div', 16));
  await clickButton('Cancel');
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 }); await sleep(1500);
}
// Leaflet sometimes misses the map's last change of size and leaves part of it without basemap tiles; a resize makes it look again
const resized = async () => { await page.evaluate(() => window.dispatchEvent(new Event('resize'))); await sleep(1500); };
if (want('maps')) {
  // Part 5: the Escalante maps of the Sample Data in March 1960 with their storage change curve, their statistics, and a cross section
  // across the valley through the area of the largest fall, in March 1941 (the chart alone) and March 1999. A 1200 px window with
  // the chart panel at 450 px leaves the map as tall as the 1000 px window's did.
  const SECTION = [{ lat: 37.740, lng: -113.808 }, { lat: 37.856, lng: -113.408 }];
  const setYear = async year => {
    await page.evaluate(y => {
      const s = document.querySelector('input[type=range].rfs-range');
      const label = () => s.parentElement.querySelector('span.tabular-nums').textContent;
      const set = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
      set.call(s, '0'); s.dispatchEvent(new Event('input', { bubbles: true }));
      const first = +label().slice(0, 4);
      set.call(s, String(y - first)); s.dispatchEvent(new Event('input', { bubbles: true }));   // one map a year
    }, year);
    await sleep(2000);
  };
  // The panel's Show on map > Wells checkbox, set rather than toggled: the app remembers it, also from a run that stopped
  const showWells = on => page.evaluate(on => {
    const head = [...document.querySelectorAll('p.rfs-label')].find(p => p.textContent.trim() === 'Show on map');
    const box = [...head.parentElement.querySelectorAll('label')].find(l => l.textContent.trim() === 'Wells').querySelector('input');
    if (box.checked !== on) box.click();
  }, on).then(() => sleep(1500));
  await page.setViewport({ width: 1440, height: 1200, deviceScaleFactor: 2 });
  await load();
  await treeItem(REGION); await treeItem(AQUIFER); await clearFilters(); await showWells(true);
  await setMinMeasurements(5);    // the 364 wells with 5 readings or more, so the colors show between them
  await treeItem('wte_kriging'); await sleep(4000);
  await taller(450);
  await fitAquifer();
  await setYear(1960); await page.mouse.move(5, 5); await sleep(1500);
  await resized();
  await shot('map-view', await lower());
  await clickButton('Raster Statistics'); await page.mouse.move(5, 5); await sleep(1500);
  await shot('map-stats', await chartOnly());
  await setYear(1999);
  await showWells(false);         // the line and its labels, clear of the markers
  await clickButton('Cross Section'); await sleep(800);
  for (const p of SECTION) { const s = await toScreen(p); await page.mouse.click(s.x, s.y); await sleep(1200); }
  await page.mouse.move(5, 5); await sleep(3000);
  // The ground surface along the line, fetched from the elevation tiles
  await page.evaluate(() => [...document.querySelectorAll('label')].find(l => l.textContent.trim() === 'GSE').querySelector('input').click());
  await page.waitForFunction(() => !document.body.innerText.includes('Loading ground surface'), { timeout: 60000 }); await sleep(1500);
  if (await page.evaluate(() => document.body.innerText.includes('Ground surface unavailable'))) throw new Error('no ground surface');
  await setYear(1941); await page.mouse.move(5, 5); await sleep(1500);
  await shot('map-section-1941', await chartOnly());
  await setYear(1999); await page.mouse.move(5, 5); await sleep(1500);
  await resized();
  await shot('map-section', await lower());
  await clickButton('Clear Cross Section');
  await showWells(true); await clearFilters();
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
}
if (want('mapwizard')) {
  // Part 5, in a My Data copy of Utah: the wizard's first step, then a second set of Escalante maps from the gap-filling model,
  // compared with the first on the storage chart (mapstorage). The second set's file is saved beside the pictures for the text.
  await clearMyData();
  await page.evaluate(n => [...document.querySelectorAll('span.truncate')].find(x => x.textContent.trim() === n).nextElementSibling.click(), REGION);
  await sleep(600);
  await clickButton('Copy to My Data'); await sleep(15000);   // the app switches to My Data and opens the copy
  await treeItem(AQUIFER);
  await page.setViewport({ width: 1440, height: 1300, deviceScaleFactor: 2 }); await sleep(1500);
  await page.click('button[aria-label="Spatial Analysis"]');
  await waitText('wells qualify'); await sleep(2500);
  await shot('map-wizard', await rect('div.fixed.inset-0 > div', 16));
  await clickButton('Imputed Data'); await sleep(3000);
  for (let k = 0; k < 4 && !(await page.$('input[placeholder="e.g. Annual Analysis 2024"]')); k++) { await clickButton('Next'); await sleep(4000); }
  await page.evaluate(() => {
    const el = document.querySelector('input[placeholder="e.g. Annual Analysis 2024"]');
    Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set.call(el, 'kriging_mc_lnn');
    el.dispatchEvent(new Event('input', { bubbles: true }));
  });
  await sleep(500);
  await clickButton('Run Analysis');
  await waitText('Analysis Complete', 900000); await sleep(1000);
  await clickButton('View Results'); await sleep(4000);
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
}
if (want('mapwizard') || want('mapstorage')) {
  // The two Escalante sets the mapwizard step leaves in My Data, on one storage chart
  await page.setViewport({ width: 1440, height: 1200, deviceScaleFactor: 2 });
  await load();
  await clickButton('My Data'); await sleep(1500);
  await treeItem(REGION); await treeItem(AQUIFER);
  await treeItem('wte_kriging_mc_lnn'); await sleep(4000);
  // Shift-click the set from the measurements to add its curve
  const other = await page.evaluateHandle(() => [...document.querySelectorAll('span.truncate')].find(x => x.textContent.trim() === 'wte_kriging'));
  await page.keyboard.down('Shift'); await other.click(); await page.keyboard.up('Shift'); await sleep(3000);
  await taller(450);
  await shot('map-storage', await chartOnly());
  const file = await page.evaluate(() => new Promise((res, rej) => {
    const r = indexedDB.open('aquifer-analyst-my-data');
    r.onsuccess = () => {
      const q = r.result.transaction('files').objectStore('files').getAll();
      q.onsuccess = () => res(q.result.find(x => /escalante_valley_beryl_enterprise\/raster_wte_kriging_mc_lnn\.json$/.test(x.path))?.text);
      q.onerror = rej;
    };
    r.onerror = rej;
  }));
  if (file) { (await import('fs')).writeFileSync(`${OUT}/escalante_raster_wte_kriging_mc_lnn.json`, file); console.log('saved the model maps'); }
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
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
  await myDataWithOregon(); await clearFilters();   // the filter step leaves At least 20
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
  // The import looks up the elevations of the 161 new wells first
  await waitText2('Import complete', 600000);
  await sleep(800);
  await clickButton('Done'); await sleep(2500);

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
  // A short window, where the parameter list shows its first rows and scrolls, so the picture is short
  // enough for the page to show it at full size
  await page.setViewport({ width: 1440, height: 760, deviceScaleFactor: 2 }); await sleep(800);
  await shot('data-wqp-picker', await topCard());
  await page.setViewport({ width: 1440, height: 1000, deviceScaleFactor: 2 }); await sleep(800);
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
  // A short window, so the table shows six or so rows and the picture is short enough for the page to
  // show it at full size. The table opens at the earliest values; bring the first flagged one into view
  await page.setViewport({ width: 1440, height: 650, deviceScaleFactor: 2 }); await sleep(800);
  await page.evaluate(() => {
    const row = [...document.querySelectorAll('tbody tr')].find(r => r.classList.contains('bg-red-50') && !r.classList.contains('line-through'));
    row?.scrollIntoView({ block: 'center' });
  });
  await sleep(600);
  await shot('edit-table', await topCard());
  await clickButton('Cancel'); await sleep(800);
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 }); await sleep(1500);

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

if (want('places')) {
  // Spatial Analysis' Wells at One Place step, for the 180/400 Foot Aquifer of the Monterey County region the adddata step leaves in
  // My Data. A tall window, so the list shows every place without scrolling
  await page.setViewport({ width: 1440, height: 1500, deviceScaleFactor: 2 });
  await load();
  await clickButton('My Data'); await sleep(1500);
  await treeItem('Monterey County'); await treeItem('180/400 Foot Aquifer'); await clearFilters(); await sleep(2000);
  await page.click('button[aria-label="Spatial Analysis"]'); await sleep(2000);
  await clickButton('Next'); await sleep(3000);
  await shot('map-places', await topCard());
  await clickButton('Cancel'); await sleep(800);
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
}

// Part 6: the case study's region, Monterey County as the adddata step leaves it, downloaded with its menu's Download so readers can
// load it with Restore
const CASE_ZIP_DIR = new URL('../../docs/static/files/aquiferx/', import.meta.url).pathname;
const CASE_ZIP = CASE_ZIP_DIR + 'monterey-county.zip';
const myFiles = () => page.evaluate(() => new Promise((res, rej) => {
  const r = indexedDB.open('aquifer-analyst-my-data');
  r.onsuccess = () => { const q = r.result.transaction('files').objectStore('files').getAllKeys(); q.onsuccess = () => res(q.result); q.onerror = rej; };
  r.onerror = rej;
}));
if (want('casedata')) {
  await load();
  await clickButton('My Data'); await sleep(1500);
  const files = (await myFiles()).filter(p => p.startsWith('monterey-county/'));
  if (!files.includes('monterey-county/data_wte.csv') || files.some(p => /\/(raster|model)_/.test(p))) {
    throw new Error('casedata: run adddata first, so Monterey County holds the imported files and nothing else');
  }
  const fs = await import('fs');
  fs.rmSync(CASE_ZIP, { force: true });
  const cdp = await page.createCDPSession();
  await cdp.send('Browser.setDownloadBehavior', { behavior: 'allow', downloadPath: CASE_ZIP_DIR });
  await page.evaluate(() => [...document.querySelectorAll('span.truncate')].find(x => x.textContent.trim() === 'Monterey County').nextElementSibling.click());
  await sleep(600);
  await clickButton('Download');
  for (let i = 0; i < 60 && !fs.existsSync(CASE_ZIP); i++) await sleep(500);
  await sleep(1500);
  console.log('saved', CASE_ZIP, fs.statSync(CASE_ZIP).size, 'bytes,', files.length, 'files');
}

if (want('casestudy')) {
  // Part 6: the East Side Aquifer, Salinas Valley, in the Monterey County region restored from the casedata zip into an empty My Data:
  // two wells and their trends, maps from the measurements, Impute Gaps, maps from the model, the two storage curves, a cross section
  const AQ = 'East Side Aquifer';
  const W901 = { name: '367386N1216740W001', lat: 36.73863, lng: -121.67404 };     // 901, in the pumping low near Salinas
  const W10410 = { name: '365351N1214389W001', lat: 36.53513, lng: -121.43898 };   // 10410, at the aquifer's southeast end
  const W1825 = { name: '367155N1216595W001', lat: 36.71552, lng: -121.6595 };     // 1825, read in August and December since 1990
  // Southeast end to the low, along the valley, 150 m or more inside the outline where it narrows at Chualar (a sample
  // whose cells touch the outline has no value, and the line breaks there)
  const SECTION = [{ lat: 36.515, lng: -121.41 }, { lat: 36.745, lng: -121.676 }];
  const setYear = async year => {
    await page.evaluate(y => {
      const s = document.querySelector('input[type=range].rfs-range');
      const label = () => s.parentElement.querySelector('span.tabular-nums').textContent;
      const set = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
      set.call(s, '0'); s.dispatchEvent(new Event('input', { bubbles: true }));
      const first = +label().match(/\d{4}/)[0];
      set.call(s, String(y - first)); s.dispatchEvent(new Event('input', { bubbles: true }));   // one map a year
    }, year);
    await sleep(2000);
  };
  const setTitle = async (t, placeholder) => {
    await page.evaluate((t, ph) => {
      const el = document.querySelector(`input[placeholder="${ph}"]`);
      Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set.call(el, t);
      el.dispatchEvent(new Event('input', { bubbles: true }));
    }, t, placeholder);
    await sleep(500);
  };
  const spatial = async (imputed, title) => {
    await page.click('button[aria-label="Spatial Analysis"]');
    await waitText('wells qualify'); await sleep(2500);
    if (imputed) { await clickButton('Imputed Data'); await sleep(3000); }
    for (let k = 0; k < 4 && !(await page.$('input[placeholder="e.g. Annual Analysis 2024"]')); k++) { await clickButton('Next'); await sleep(3000); }
    await setTitle(title, 'e.g. Annual Analysis 2024');
    await clickButton('Run Analysis');
    await waitText('Analysis Complete', 900000); await sleep(1000);
    console.log((await page.evaluate(() => document.querySelector('div.fixed.inset-0').innerText)).replace(/\s+/g, ' ').slice(0, 300));
    await clickButton('View Results'); await sleep(4000);
  };
  const toggleTrends = async () => { await page.click('button[aria-label="Analyze Trends"]'); await sleep(3000); };
  // fitAquifer only zooms out, and selecting the far well left the map zoomed out further than the aquifer needs: zoom in while the
  // outline would still fit at the next half level, then centre it
  const closeFit = async () => {
    for (let i = 0; i < 6; i++) {
      await tiles();
      const fits = await page.evaluate(() => {
        const r = el => el.getBoundingClientRect();
        const a = [...document.querySelectorAll('path[stroke="#6366f1"]')].map(r);
        const m = r(document.getElementById('map-container'));
        const slider = document.querySelector('input[type=range]')?.closest('.rfs-card');
        const w = m.width - 530, h = (slider ? r(slider).top : m.bottom) - m.top - 40;
        const aw = Math.max(...a.map(x => x.right)) - Math.min(...a.map(x => x.left));
        const ah = Math.max(...a.map(x => x.bottom)) - Math.min(...a.map(x => x.top));
        return aw * Math.SQRT2 < w && ah * Math.SQRT2 < h;
      });
      if (!fits) break;
      await page.click('.leaflet-control-zoom-in'); await sleep(1200);
    }
    await fitAquifer();
  };

  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
  await clearMyData();
  await clickButton('My Data'); await sleep(1000);
  await (await page.$('input[type=file][accept=".zip"]')).uploadFile(CASE_ZIP);
  await waitText('Restore backup'); await sleep(800);
  await clickButton('Restore');
  await waitText('restored to My Data', 120000); await sleep(800);
  await clickButton('Done'); await sleep(2000);
  await treeItem('Monterey County'); await treeItem(AQ); await clearFilters();

  // Two wells: one in the low, one at the far end
  await searchWell(W901); await zoomOut(4);
  await clickWell(W10410, true);
  await closeFit(); await page.mouse.move(5, 5); await sleep(1500);
  await shot('case-wells');
  // Their trends over 30 years, then over 10
  await toggleTrends(); await page.mouse.move(5, 5); await sleep(1500);
  await shot('case-trends-30');
  for (let i = 0; i < 4; i++) { await page.evaluate(() => [...document.querySelectorAll('button')].find(b => b.textContent.trim() === '−' && b.nextElementSibling?.textContent.includes('yr')).click()); await sleep(1200); }
  await page.mouse.move(5, 5); await sleep(1500);
  await shot('case-trends-10');
  await toggleTrends();

  // Maps from the measurements, with the defaults
  await page.setViewport({ width: 1440, height: 1200, deviceScaleFactor: 2 }); await sleep(1500);
  await spatial(false, 'kriging');
  await taller(450); await closeFit();
  await setYear(1992); await page.mouse.move(5, 5); await sleep(1500);
  await resized();
  await shot('case-map-1992', await lower());
  // The seven wells that join the maps in December 1980
  await clickButton('Active Wells'); await sleep(1500);
  const mapOnly = () => rect('#map-container', 0);
  await setYear(1979); await page.mouse.move(5, 5); await sleep(1500);
  await shot('case-active-1979', await mapOnly());
  await setYear(1980); await page.mouse.move(5, 5); await sleep(1500);
  await shot('case-active-1980', await mapOnly());
  await clickButton('Active Wells'); await sleep(1000);

  // Impute Gaps with the defaults, then the model's series at 1825 across its 1996-2005 gap
  await page.click('button[aria-label="Impute Gaps"]');
  await waitText('wells will be filled'); await sleep(2500);
  await clickButton('Next'); await sleep(1500);
  await clickButton('Run Imputation');
  await waitText('Imputation Complete', 900000); await sleep(1500);
  console.log((await page.evaluate(() => document.querySelector('div.fixed.inset-0').innerText)).replace(/\s+/g, ' ').slice(0, 400));
  await clickButton('View Results'); await sleep(4000);
  await searchWell(W1825); await zoomOut(4); await taller(450);
  await page.evaluate(() => [...document.querySelectorAll('label')].find(x => x.textContent.trim() === 'Combined').querySelector('input').click());
  await page.mouse.move(5, 5); await sleep(2500);
  await shot('case-impute', await chartOnly());

  // Maps from the model, and the two storage curves
  await spatial(true, 'kriging_mc_lnn');
  const other = await page.evaluateHandle(() => [...document.querySelectorAll('span.truncate')].find(x => x.textContent.trim() === 'wte_kriging'));
  await page.keyboard.down('Shift'); await other.click(); await page.keyboard.up('Shift'); await sleep(3000);
  await taller(450);
  await page.mouse.move(5, 5); await sleep(1500);
  await shot('case-storage', await chartOnly());

  // A cross section of the model's maps along the valley, from the southeast end into the low, with the ground surface
  await load();
  await clickButton('My Data'); await sleep(1500);
  await treeItem('Monterey County'); await treeItem(AQ); await clearFilters();
  await treeItem('wte_kriging_mc_lnn'); await sleep(4000);
  await taller(450); await closeFit();
  await setYear(1992);
  await page.evaluate(() => {
    const head = [...document.querySelectorAll('p.rfs-label')].find(p => p.textContent.trim() === 'Show on map');
    const box = [...head.parentElement.querySelectorAll('label')].find(l => l.textContent.trim() === 'Wells').querySelector('input');
    if (box.checked) box.click();
  });
  await sleep(1500);
  await clickButton('Cross Section'); await sleep(800);
  for (const p of SECTION) { const s = await toScreen(p); await page.mouse.click(s.x, s.y); await sleep(1200); }
  await page.mouse.move(5, 5); await sleep(3000);
  await page.evaluate(() => [...document.querySelectorAll('label')].find(l => l.textContent.trim() === 'GSE').querySelector('input').click());
  await page.waitForFunction(() => !document.body.innerText.includes('Loading ground surface'), { timeout: 60000 }); await sleep(1500);
  if (await page.evaluate(() => document.body.innerText.includes('Ground surface unavailable'))) throw new Error('no ground surface');
  await page.mouse.move(5, 5); await sleep(1500);
  await resized();
  await shot('case-section', await lower());
  await clickButton('Clear Cross Section');
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
}

await browser.close();
