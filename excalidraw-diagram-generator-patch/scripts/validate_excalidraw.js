#!/usr/bin/env node
const fs = require("fs");

const file = process.argv[2];
if (!file) {
  console.log("FAIL: missing file path");
  process.exit(1);
}

let data;
try {
  data = JSON.parse(fs.readFileSync(file, "utf8"));
} catch (e) {
  console.log("FAIL: invalid JSON");
  process.exit(1);
}

const elements = (data.elements || []).filter(e => !e.isDeleted);
const texts = elements.filter(e => e.type === "text");
const rects = elements.filter(e => e.type === "rectangle");
const rectMap = new Map(rects.map(r => [r.id, r]));

function insideRect(t, r, pad = 3) {
  return t.x >= r.x - pad &&
    t.x + t.width <= r.x + r.width + pad &&
    t.y >= r.y - pad &&
    t.y + t.height <= r.y + r.height + pad;
}

function rectContainsRect(outer, inner, pad = 2) {
  if (outer.id === inner.id) return false;
  return inner.x >= outer.x + pad &&
    inner.x + inner.width <= outer.x + outer.width - pad &&
    inner.y >= outer.y + pad &&
    inner.y + inner.height <= outer.y + outer.height - pad;
}

function textCenter(t) {
  return { x: t.x + t.width / 2, y: t.y + t.height / 2 };
}

function hasChildRects(r) {
  return rects.some(c => rectContainsRect(r, c, 2));
}

function isLargeContainer(r) {
  return r.width >= 260 && r.height >= 180;
}

// Conservative title inference:
// A text is title-like ONLY when it's bound to a large container that itself contains child rectangles,
// and the text center is in the top band of that same container.
function isTitleLikeBoundText(t) {
  if (!t.containerId) return false;
  const r = rectMap.get(t.containerId);
  if (!r) return false;
  if (!isLargeContainer(r)) return false;
  if (!hasChildRects(r)) return false;
  const c = textCenter(t);
  const topBandY = r.y + r.height * 0.28;
  return c.y <= topBandY;
}

const fails = [];

// 0) title-like text must remain unbound
for (const t of texts) {
  if (isTitleLikeBoundText(t)) {
    fails.push(`title must be unbound: ${t.text}`);
  }
}

// 1) second-level text binding
for (const t of texts) {
  // Skip title-like labels (they are checked above)
  if (isTitleLikeBoundText(t)) continue;

  if (!t.containerId) {
    // only flag as unbound when text clearly sits in a structural rectangle
    const holder = rects.find(r => insideRect(t, r, 3));
    if (holder) {
      // Ignore if holder itself is a large container (could be free annotation/title)
      if (!isLargeContainer(holder)) {
        fails.push(`unbound text: ${t.text}`);
      }
    }
    continue;
  }

  const r = rectMap.get(t.containerId);
  if (!r) {
    fails.push(`missing container rect for text: ${t.text}`);
    continue;
  }

  const back = Array.isArray(r.boundElements) &&
    r.boundElements.some(b => b.id === t.id && b.type === "text");
  if (!back) fails.push(`missing backlink boundElements for text: ${t.text}`);

  if (t.textAlign !== "center" || t.verticalAlign !== "middle") {
    fails.push(`alignment mismatch: ${t.text}`);
  }
}

// 2) empty boxes (non-outer)
for (const r of rects) {
  const hasText = texts.some(t => insideRect(t, r));
  const isOuter = isLargeContainer(r);
  if (!isOuter && !hasText) fails.push(`empty structural box: ${r.id}`);
}

// 3) duplicate boxes
const seen = new Map();
for (const r of rects) {
  const key = `${r.x}|${r.y}|${r.width}|${r.height}`;
  if (seen.has(key)) fails.push(`duplicate box geometry: ${key}`);
  else seen.set(key, r.id);
}

if (fails.length) {
  console.log("FAIL");
  for (const f of fails) console.log(`- ${f}`);
  process.exit(2);
}
console.log("PASS");
