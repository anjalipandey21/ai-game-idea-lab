#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const mechDir = path.join(root, "mechanics");

if (!fs.existsSync(mechDir)) {
  fs.mkdirSync(mechDir, { recursive: true });
}

const themes = [
  "neural forest",
  "floating islands",
  "glitched arcade",
  "underwater data center",
];

const genres = [
  "deckbuilder",
  "arena brawler",
  "grid puzzle",
  "stealth platformer",
];

const actions = [
  "splice enemy behaviors",
  "rewind only projectiles",
  "swap health with enemies",
  "compress time into bursts",
];

const constraints = [
  "input latency randomly spikes",
  "vision cone is very narrow",
  "only one resource can be maxed at a time",
  "any upgrade also buffs enemies",
];

const aiTwists = [
  "log player mistakes and replay them as ghost enemies",
  "cluster player paths and surface the rarest ones as bonus routes",
  "use a simple score model to decide when to trigger harder waves",
  "track player hesitation time and adapt difficulty in real-time",
];

function pick(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function slugify(text) {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function main() {
  const theme = pick(themes);
  const genre = pick(genres);
  const action = pick(actions);
  const constraint = pick(constraints);
  const twist = pick(aiTwists);

  const title = `${action} ${genre}`;
  const now = new Date();
  const dateStr = now.toISOString().slice(0, 10);
  const slug = slugify(title);
  const filename = `${dateStr}-${slug}-js-note.md`;
  const mechPath = path.join(mechDir, filename);

  const body = `# ${title}
  
**Date:** ${dateStr}  
**Engine idea:** JS / browser / canvas

## Sketch

- Theme: ${theme}
- Core action: **${action}**
- Constraint: **${constraint}**
- AI twist: **${twist}**

### JS prototype thoughts

- Start with a minimal canvas loop.
- Represent entities as plain objects, keep systems small.
- Log a few key events to localStorage to simulate “learning”.
`;

  if (!fs.existsSync(mechPath)) {
    fs.writeFileSync(mechPath, body.trim() + "\n", "utf8");
  }
}

main();
