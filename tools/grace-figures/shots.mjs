import puppeteer from 'puppeteer-core';
const OUT = process.argv[2] || '.';
const only = process.argv[3];
const sleep = ms => new Promise(r => setTimeout(r, ms));
const browser = await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless:'new',
  args:['--use-angle=metal','--enable-gpu','--ignore-gpu-blocklist','--window-size=1440,900'], userDataDir: './.chrome-profile'});
const page = await browser.newPage();
await page.setViewport({width:1440, height:900, deviceScaleFactor:2});
page.on('console', m => { if (m.type()==='error') console.log('CONSOLE', m.text().slice(0,160)); });
const load = async () => { await page.goto('http://localhost:5199/', {waitUntil:'networkidle2', timeout:120000}); await sleep(6000); };
const shot = async (name, clip) => { await page.screenshot({path:`${OUT}/${name}.png`, clip}); console.log('saved', name); };
const clickRegion = async (name) => {
  await page.evaluate(n => { const el=[...document.querySelectorAll('#region-list *')].find(e=>e.children.length===0 && e.textContent.trim()===n); el.click(); }, name);
  await sleep(9000);
};
const rect = async (sel, pad=0) => page.evaluate((s,p) => { const r=document.querySelector(s).getBoundingClientRect(); return {x:Math.max(0,r.x-p), y:Math.max(0,r.y-p), width:r.width+2*p, height:r.height+2*p}; }, sel, pad);
const toEnd = async () => {
  await page.evaluate(() => { const r=document.querySelector('#time-control input[type=range]'); r.focus(); });
  await page.keyboard.press('End'); await sleep(3500);
};
const toMonth = async (label) => {
  for (let i=0;i<400;i++) {
    const cur = await page.evaluate(()=>document.getElementById('time-control').textContent);
    if (cur.includes(label)) break;
    await page.keyboard.press('ArrowLeft'); await sleep(60);
  }
  await sleep(3000);
};
const topPanel = async () => page.evaluate(() => { document.querySelectorAll('*').forEach(e => { if (e.scrollTop > 0 && !e.closest('#region-list')) e.scrollTop = 0; }); });
const want = n => !only || only.split(',').includes(n);

await load();
if (want('home')) await shot('app-home');
if (want('panel')) await shot('app-panel', {x:0, y:0, width:320, height:900});
if (want('region')) {
  await clickRegion('Iullemeden-Irhazer Aquifer System');
  await toEnd(); await toMonth('2024-09'); await topPanel(); await sleep(800);
  await shot('app-region');
  await shot('app-chart', await rect('#timeseries-plot'));
  // comparison curves
  await page.click('#series-toggles input[value="TWSa"], #series-toggles label:nth-child(2) input').catch(()=>{});
  await page.evaluate(() => { for (const v of ['TWSa','SMa']) { const i=[...document.querySelectorAll('#series-toggles input')].find(x=>x.closest('label')?.textContent.trim().startsWith(v)); if (i && !i.checked) i.click(); } });
  await sleep(4000);
  await shot('app-chart-compare', await rect('#timeseries-plot'));
  await page.evaluate(() => { for (const v of ['TWSa','SMa']) { const i=[...document.querySelectorAll('#series-toggles input')].find(x=>x.closest('label')?.textContent.trim().startsWith(v)); if (i && i.checked) i.click(); } });
  await sleep(1500);
  // cell + mascon boundaries
  await page.evaluate(() => { for (const id of ['border-toggle','mascon-toggle']) { const i=document.getElementById(id); if(!i.checked) i.click(); } });
  await sleep(4000);
  await shot('app-region-boundaries', {x:320, y:50, width:1120, height:580});
  await page.evaluate(() => { for (const id of ['border-toggle','mascon-toggle']) { const i=document.getElementById(id); if(i.checked) i.click(); } });
  await sleep(1000);
  await shot('app-header', {x:320, y:0, width:1120, height:50});
}
if (want('cv')) {
  await load();
  await clickRegion('California Central Valley');
  await toEnd(); await toMonth('2022-10'); await topPanel(); await sleep(800);
  await shot('app-central-valley');
}
if (want('global')) {
  await load();
  await page.click('#global-view-button'); await sleep(20000);
  await shot('app-global-trends');
  await page.click('#trends-button'); await sleep(5000);
  await toEnd(); await toMonth('2024-09');
  await shot('app-global');
  // click a cell in northern India
  const m = await rect('#region-map');
  await page.mouse.click(m.x + m.width*0.705, m.y + m.height*0.40); await sleep(6000);
  await shot('app-global-cell');
  await shot('app-time-control', await rect('#time-control', 4));
}
if (want('modals')) {
  await load();
  await page.click('#upload-button'); await sleep(1200);
  const fi = await page.$('#upload-file-input'); await fi.uploadFile('punjab.geojson');
  await page.$eval('#upload-region-name', e => { e.value = ''; }); await page.type('#upload-region-name', 'Punjab and Haryana'); await sleep(800);
  await shot('app-upload');
  await page.click('#upload-submit'); await sleep(12000);
  await toEnd(); await toMonth('2024-09'); await topPanel(); await sleep(800);
  await shot('app-upload-result');
  await load();
  await page.click('#settings-button'); await sleep(1200);
  await shot('app-settings');
  await page.click('#settings-close'); await sleep(800);
  await page.select('#region-set-select', await page.evaluate(()=>{ const o=[...document.querySelectorAll('#region-set-select option')].find(o=>/my regions/i.test(o.textContent)); return o?o.value:''; }));
  await sleep(3000);
  await shot('app-my-regions');
}
if (want('gapfill')) {
  await load();
  const setGapFill = async (v) => { await page.click(`#gap-fill-control input[value="${v}"]`); await sleep(2500); };
  await clickRegion('Northern Midwest Aquifer System');
  await toEnd(); await toMonth('2024-09'); await topPanel(); await sleep(800);
  // a taller chart panel than the default, so the seasonal swings read clearly
  const tallChart = async () => { await page.evaluate(() => { document.getElementById('timeseries-plot').style.flexBasis = '52%'; }); await sleep(2500); };
  await tallChart();
  // the trend line is dashed too; turn it off so only the fill is dashed
  if (await page.$eval('#trends-button', b => b.getAttribute('aria-pressed') === 'true')) { await page.click('#trends-button'); await sleep(3000); }
  for (const v of ['none', 'line', 'seasonal']) {
    await setGapFill(v);
    await page.mouse.move(5, 5); await sleep(500);
    await shot(`app-gap-fill-${v}`, await rect('#timeseries-plot'));
  }
  const c = await rect('#gap-fill-control', 12), l = await rect('#gap-fill-label', 12);
  await shot('app-gap-fill-control', {x: c.x, y: l.y, width: c.width, height: c.y + c.height - l.y});
}
await browser.close();
