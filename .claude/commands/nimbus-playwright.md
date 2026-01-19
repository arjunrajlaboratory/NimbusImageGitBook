# NimbusImage Screenshot Automation

Take screenshots of NimbusImage for documentation using Playwright MCP.

## Usage

When asked to take screenshots for documentation, use this workflow with the Playwright MCP tools (`mcp__plugin_playwright_playwright__*`).

## Basic Workflow

### 1. Navigate to the Page

```
browser_navigate → url: "http://localhost:5173/#/your-route"
```

### 2. Wait for Content to Load

```
browser_wait_for → time: 2
```

### 3. Take a Snapshot (to see available elements)

```
browser_snapshot
```

Returns a YAML-like structure showing all interactive elements with `ref` IDs.

### 4. Take a Screenshot

```
browser_take_screenshot → filename: "my-screenshot.png"
```

Screenshots are saved to `.playwright-mcp/` in the project directory.

## Highlighting Elements

### Simple Red Outline

```javascript
browser_evaluate → function: "() => {
  const el = document.querySelector('#your-selector');
  if (el) {
    el.style.outline = '4px solid red';
    el.style.outlineOffset = '6px';
  }
}"
```

### Outline with Glow Effect

```javascript
browser_evaluate → function: "() => {
  const el = document.querySelector('#your-selector');
  if (el) {
    el.style.outline = '4px solid red';
    el.style.outlineOffset = '6px';
    el.style.boxShadow = '0 0 20px 8px rgba(255, 0, 0, 0.6)';
  }
}"
```

### Circle Overlay

```javascript
browser_evaluate → function: "() => {
  const el = document.querySelector('#your-selector');
  if (el) {
    const rect = el.getBoundingClientRect();
    const circle = document.createElement('div');
    circle.style.cssText = `
      position: fixed;
      left: ${rect.x - 20}px;
      top: ${rect.y - 20}px;
      width: ${rect.width + 40}px;
      height: ${rect.height + 40}px;
      border: 3px solid red;
      border-radius: 50%;
      pointer-events: none;
      z-index: 99999;
    `;
    document.body.appendChild(circle);
  }
}"
```

## Adding Red Arrows

### Straight Arrow (SVG injection)

```javascript
browser_evaluate → function: "() => {
  const el = document.querySelector('#your-selector');
  if (el) {
    const rect = el.getBoundingClientRect();
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 99999;
    `;

    const startX = rect.x - 60;
    const startY = rect.y - 60;
    const endX = rect.x + rect.width / 2;
    const endY = rect.y;

    svg.innerHTML = `
      <defs>
        <marker id='arrowhead' markerWidth='10' markerHeight='7'
                refX='9' refY='3.5' orient='auto'>
          <polygon points='0 0, 10 3.5, 0 7' fill='red'/>
        </marker>
      </defs>
      <line x1='${startX}' y1='${startY}' x2='${endX}' y2='${endY}'
            stroke='red' stroke-width='3' marker-end='url(#arrowhead)'/>
    `;

    document.body.appendChild(svg);
  }
}"
```

### Curved Arrow

```javascript
browser_evaluate → function: "() => {
  const el = document.querySelector('#your-selector');
  if (el) {
    const rect = el.getBoundingClientRect();
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 99999;
    `;

    const startX = rect.x - 60;
    const startY = rect.y - 60;
    const endX = rect.x + rect.width / 2;
    const endY = rect.y;

    svg.innerHTML = `
      <defs>
        <marker id='arrowhead' markerWidth='10' markerHeight='7'
                refX='9' refY='3.5' orient='auto'>
          <polygon points='0 0, 10 3.5, 0 7' fill='red'/>
        </marker>
      </defs>
      <path d='M ${startX} ${startY} Q ${startX + 40} ${endY - 20} ${endX} ${endY}'
            stroke='red' stroke-width='3' fill='none' marker-end='url(#arrowhead)'/>
    `;

    document.body.appendChild(svg);
  }
}"
```

## Cropping Screenshots

### Screenshot a Specific Element

```javascript
browser_run_code → code: "async (page) => {
  const element = await page.locator('#important-area');
  await element.screenshot({ path: '.playwright-mcp/cropped.png' });
}"
```

### Clip to a Rectangular Region

```javascript
browser_run_code → code: "async (page) => {
  await page.screenshot({
    path: '.playwright-mcp/cropped.png',
    clip: { x: 100, y: 200, width: 400, height: 300 }
  });
}"
```

### Element with Padding

```javascript
browser_run_code → code: "async (page) => {
  const box = await page.locator('#target').boundingBox();
  const padding = 50;
  await page.screenshot({
    path: '.playwright-mcp/cropped.png',
    clip: {
      x: box.x - padding,
      y: box.y - padding,
      width: box.width + padding * 2,
      height: box.height + padding * 2
    }
  });
}"
```

## Highlight Style Options

| Style | CSS | Best For |
|-------|-----|----------|
| Simple outline | `outline: 3px solid red` | Clean, minimal highlight |
| Outline with offset | `outline: 4px solid red; outline-offset: 6px` | Button/input highlighting |
| Glow effect | `box-shadow: 0 0 20px 8px rgba(255,0,0,0.6)` | Drawing attention |
| Background highlight | `background-color: rgba(255,255,0,0.3)` | Text/area highlighting |

### Color Variations

- Red: `rgba(255, 0, 0, 0.6)` - Errors, important actions
- Green: `rgba(0, 255, 0, 0.6)` - Success, recommended actions
- Yellow: `rgba(255, 255, 0, 0.6)` - Warnings, notes
- Blue: `rgba(0, 100, 255, 0.6)` - Information, links

## Handling Animated Elements

Animated/pulsing elements cause Playwright timeout errors. Use JavaScript click instead:

```javascript
browser_evaluate → function: "() => { document.querySelector('#my-button-id').click(); }"
```

## Complete Example

Take a screenshot of a button with a red arrow and glow, cropped with padding:

```javascript
// 1. Navigate
browser_navigate(url="http://localhost:5173/#/dataset/123")

// 2. Wait for load
browser_wait_for(time=2)

// 3. Add highlight and arrow
browser_evaluate(function=`() => {
  const el = document.querySelector('#view-dataset-button');
  if (el) {
    // Add glow
    el.style.outline = '4px solid red';
    el.style.outlineOffset = '6px';
    el.style.boxShadow = '0 0 20px 8px rgba(255, 0, 0, 0.6)';

    // Add arrow
    const rect = el.getBoundingClientRect();
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:99999;';
    const startX = rect.x - 60, startY = rect.y - 60;
    const endX = rect.x + rect.width/2, endY = rect.y;
    svg.innerHTML = \`<defs><marker id='ah' markerWidth='10' markerHeight='7' refX='9' refY='3.5' orient='auto'><polygon points='0 0,10 3.5,0 7' fill='red'/></marker></defs><line x1='\${startX}' y1='\${startY}' x2='\${endX}' y2='\${endY}' stroke='red' stroke-width='3' marker-end='url(#ah)'/>\`;
    document.body.appendChild(svg);
  }
}`)

// 4. Take cropped screenshot with padding
browser_run_code(code=`async (page) => {
  const box = await page.locator('#view-dataset-button').boundingBox();
  const padding = 80;
  await page.screenshot({
    path: '.playwright-mcp/view-button-highlighted.png',
    clip: { x: box.x - padding, y: box.y - padding, width: box.width + padding*2, height: box.height + padding*2 }
  });
}`)
```

## Troubleshooting

### "Failed to launch browser"
Chrome is already running. Close all Chrome windows or use Claude in Chrome MCP instead.

### Element Not Found
Increase wait time or use `browser_snapshot` to see available elements.

### Click Timeout on Animated Elements
Use JavaScript click: `browser_evaluate → function: "() => { document.querySelector('#id').click(); }"`

## File Locations

- Screenshots: `.playwright-mcp/*.png` (in project root)
- For GitBook: Copy to `.gitbook/assets/` and reference in markdown

## Copying to GitBook

After taking a screenshot, copy it to the GitBook assets folder:

```bash
cp .playwright-mcp/my-screenshot.png .gitbook/assets/
```

Then reference in markdown:
```markdown
<figure><img src="../.gitbook/assets/my-screenshot.png" alt=""><figcaption></figcaption></figure>
```
