// The hold-out test behind the RMSE tables on the Gaps and Gap Filling page.
//
// Observed months are hidden, the fill is refitted without them, and the filled
// values are compared with the real ones. Three fills are compared: the app's
// seasonal model, the same trend and seasonal cycle without the residual
// correction, and linear interpolation between the neighbouring observed
// months.
//
// It runs the app's own gapFill.js rather than a copy of it, so the table
// cannot drift away from what the app does.
//
//   node holdout.mjs <dir-of-app-csv-exports>
//
// where the directory holds one CSV per region as the app's Download CSV
// writes them (Date, GWSa, GWSa_upper, GWSa_lower, ...).

import {readFileSync} from "node:fs";
import {join} from "node:path";
import {seasonalFill} from "/Users/njones/python_projects/webapp-grace-groundwater/src/gapFill.js";

const REGIONS = [
  ["Northern Midwest Aquifer System", "northern_midwest.csv"],
  ["Volta Basin (GRDC)", "volta.csv"],
  ["Iullemeden-Irhazer Aquifer System", "iullemeden.csv"],
  ["California Central Valley", "central_valley.csv"],
];
const SINGLE_FRACTION = 0.10;   // share of observed months hidden, scattered
const BLOCK_MONTHS = 11;        // the gap between the missions
const BLOCKS = 6;               // blocks spread through the record
const SEED = 20261016;

// deterministic PRNG so the table is reproducible
let seed = SEED;
const rnd = () => (seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff;

const load = (path) => {
  const [header, ...lines] = readFileSync(path, "utf8").trim().split(/\r?\n/);
  const cols = header.split(",");
  const i = (n) => cols.indexOf(n);
  const rows = lines.map((l) => l.split(","));
  const num = (v) => (v === "" || v === undefined ? NaN : Number(v));
  return {
    months: rows.map((r) => {
      const [y, m] = r[i("Date")].slice(0, 7).split("-").map(Number);
      return y * 12 + (m - 1);
    }),
    values: rows.map((r) => num(r[i("GWSa")])),
    upper: rows.map((r) => num(r[i("GWSa_upper")])),
    lower: rows.map((r) => num(r[i("GWSa_lower")])),
  };
};

const rmse = (pairs) => {
  const v = pairs.filter(([a, b]) => Number.isFinite(a) && Number.isFinite(b));
  if (!v.length) return NaN;
  return Math.sqrt(v.reduce((s, [a, b]) => s + (a - b) ** 2, 0) / v.length);
};

// linear interpolation between the nearest observed months either side
const linear = (values, months, hidden) => {
  const out = values.slice();
  for (const h of hidden) {
    let a = h - 1, c = h + 1;
    while (a >= 0 && !Number.isFinite(values[a])) a--;
    while (c < values.length && !Number.isFinite(values[c])) c++;
    if (a < 0 || c >= values.length) { out[h] = NaN; continue; }
    const f = (months[h] - months[a]) / (months[c] - months[a]);
    out[h] = values[a] + f * (values[c] - values[a]);
  }
  return out;
};

const runOnce = (truth, months, hidden) => {
  const probe = truth.slice();
  for (const h of hidden) probe[h] = NaN;
  const fit = seasonalFill(probe, months, {requireGap: false});
  const lin = linear(probe, months, hidden);
  const pairs = (get) => hidden.map((h) => [get(h), truth[h]]);
  return {
    model: pairs((h) => fit.filled[h]),
    noResid: pairs((h) => fit.trend[h] + fit.seasonal[h]),
    linear: pairs((h) => lin[h]),
  };
};

const median = (a) => {
  const s = a.filter(Number.isFinite).sort((x, y) => x - y);
  return s.length ? s[Math.floor(s.length / 2)] : NaN;
};

console.log(`seed ${SEED}; single-month share ${SINGLE_FRACTION * 100}%; ` +
  `${BLOCKS} blocks of ${BLOCK_MONTHS} months\n`);

const dir = process.argv[2];
const rows = {single: [], block: []};
for (const [label, file] of REGIONS) {
  const {months, values, upper, lower} = load(join(dir, file));
  const observed = values.map((v, i) => (Number.isFinite(v) ? i : -1)).filter((i) => i >= 0);
  const sigma = median(observed.map((i) => (upper[i] - lower[i]) / 2));

  // --- scattered single months
  const n = Math.round(observed.length * SINGLE_FRACTION);
  const pool = observed.slice();
  const hidden = [];
  while (hidden.length < n && pool.length) hidden.push(pool.splice(Math.floor(rnd() * pool.length), 1)[0]);
  hidden.sort((a, b) => a - b);
  const s = runOnce(values, months, hidden);
  rows.single.push([label, sigma, rmse(s.noResid), rmse(s.model), rmse(s.linear), hidden.length]);

  // --- 11-month blocks, spread through the record
  const acc = {model: [], noResid: [], linear: []};
  let used = 0;
  for (let k = 0; k < BLOCKS; k++) {
    const start = Math.floor(((k + 0.5) / BLOCKS) * (values.length - BLOCK_MONTHS));
    const block = [];
    for (let j = start; j < start + BLOCK_MONTHS; j++) if (Number.isFinite(values[j])) block.push(j);
    if (block.length < BLOCK_MONTHS / 2) continue;
    used++;
    const b = runOnce(values, months, block);
    for (const k2 of ["model", "noResid", "linear"]) acc[k2].push(...b[k2]);
  }
  rows.block.push([label, sigma, rmse(acc.noResid), rmse(acc.model), rmse(acc.linear), used]);
}

const show = (title, data, lastLabel) => {
  console.log(title);
  console.log("| Region | ±1σ | Trend + seasonal | Seasonal model | Linear interpolation |");
  console.log("|---|---|---|---|---|");
  for (const [label, sigma, noResid, model, lin, n] of data) {
    console.log(`| ${label} | ${sigma.toFixed(1)} | ${noResid.toFixed(1)} | ${model.toFixed(1)} | ${lin.toFixed(1)} |   (${lastLabel} ${n})`);
  }
  console.log();
};
show("**Single months** (RMSE, cm):", rows.single, "months hidden");
show("**11-month blocks** (RMSE, cm):", rows.block, "blocks used");
