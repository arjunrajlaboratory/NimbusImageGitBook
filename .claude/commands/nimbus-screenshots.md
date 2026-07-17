# NimbusImage Screenshot Automation (chrome-devtools MCP)

Take documentation screenshots of NimbusImage using the **chrome-devtools MCP**
(`mcp__plugin_chrome-devtools-mcp_chrome-devtools__*`). This is the recommended
approach for NimbusImage because the viewer renders images with **WebGL**, which
needs a real, visible browser window to paint.

## Why chrome-devtools MCP (and not claude-in-chrome)

- **claude-in-chrome drives the user's normal Chrome tab.** When that tab is not
  the focused/visible tab, Chrome throttles WebGL, so the **main image canvas
  screenshots as solid black** while the 2D minimap thumbnail still shows. Its
  screenshots also don't reliably write files to disk you can read.
- **chrome-devtools MCP launches its own visible browser window.** It renders
  WebGL correctly, is already **authenticated to `localhost:5173`** (local dev
  server), and **writes real retina-resolution PNG files** (`devicePixelRatio: 2`,
  e.g. a 1440-wide window → 2880-px-wide PNG) that you can crop and commit.

Net: use chrome-devtools MCP. The Playwright command (`/nimbus-playwright`) has
tool-agnostic tips (highlighting, arrows, crop math) but a fresh Playwright
context is **not logged in**, so datasets won't load there.

## One-time setup

Load the tools in one `ToolSearch` call:

```
select:mcp__plugin_chrome-devtools-mcp_chrome-devtools__list_pages,
mcp__plugin_chrome-devtools-mcp_chrome-devtools__navigate_page,
mcp__plugin_chrome-devtools-mcp_chrome-devtools__take_screenshot,
mcp__plugin_chrome-devtools-mcp_chrome-devtools__take_snapshot,
mcp__plugin_chrome-devtools-mcp_chrome-devtools__click,
mcp__plugin_chrome-devtools-mcp_chrome-devtools__hover,
mcp__plugin_chrome-devtools-mcp_chrome-devtools__fill,
mcp__plugin_chrome-devtools-mcp_chrome-devtools__press_key,
mcp__plugin_chrome-devtools-mcp_chrome-devtools__evaluate_script,
mcp__plugin_chrome-devtools-mcp_chrome-devtools__wait_for,
mcp__plugin_chrome-devtools-mcp_chrome-devtools__resize_page
```

**File output goes to a workspace root only.** chrome-devtools refuses paths
outside its configured roots (e.g. the `/tmp` scratchpad). Write full screenshots
to a gitignored temp dir inside the repo, then copy finished crops to
`.gitbook/assets/`:

```bash
mkdir -p .tmp-shots && echo ".tmp-shots/" >> .gitignore
```

## Core workflow

1. **Resize the window** for consistent output: `resize_page → 1440 x 880`
   (use a taller height like `1260` for tall modal dialogs).
2. **Navigate.** `navigate_page → type: "url"`. NimbusImage uses hash routes, so
   switching datasets by only changing the `#/datasetView/<id>` hash often does
   **not** reload the app. **Bounce through `about:blank` first**, then navigate
   to the target URL.
3. **Wait** for content: `wait_for → text: ["NAVIGATOR", "Add new tool", ...]`.
4. **Find elements:** `take_snapshot` (optionally `filePath` to save the a11y
   tree) returns `uid`s. Interact by uid: `click`, `hover`, `fill`, `press_key`.
   Pass `includeSnapshot: true` on a click to get the fresh tree back in one call.
5. **Capture:**
   - Full viewport → `take_screenshot → filePath: ".tmp-shots/<name>-full.png"`.
   - A single element (panel/dialog) → `take_screenshot → uid: "<uid>", filePath: …`
     (cleanest crop; but if the element scrolls internally, only the visible part
     is captured — see gotchas).
6. **Crop / downscale with PIL** (retina = multiply CSS coords by 2). Read the
   `[Image: original WxH, displayed at …, multiply by N]` hint the Read tool
   prints to map displayed coords back to PNG pixels. Downscale large full-frame
   shots to ~1600 px wide to keep file size reasonable.
7. **Commit** finished crops to `.gitbook/assets/` with **descriptive filenames**
   (e.g. `viewer-minimap.png`, matching the `3d-volume-visualization.png`
   convention), then update the markdown `src=` and open a PR.

### Zooming the WebGL viewer

There is no scroll tool. Dispatch wheel events on the canvas via `evaluate_script`
(negative `deltaY` zooms in):

```js
() => {
  const c = document.querySelector('canvas.webgl-canvas');
  for (let i=0;i<3;i++) c.dispatchEvent(new WheelEvent('wheel',
    {deltaY:-120, clientX:900, clientY:440, bubbles:true, cancelable:true}));
}
```

Zoom so image content fills the frame (avoid black margins where the field of
view extends past the scanned area).

## Gotchas

- **Local vs production datasets.** Only datasets that exist on `localhost:5173`
  load. Dataset IDs from `app.nimbusimage.com` URLs will 404 locally — ask for a
  local equivalent.
- **Right user.** The devtools browser has its own profile. If folders look empty
  or it's the wrong account, ask the user to log in **in that window**, then
  `navigate_page → type: "reload"` to pick up the session.
- **Tall dialogs.** Some modals exceed the window and scroll internally. Resize
  the window taller, or `evaluate_script` an `el.scrollIntoView()` on the target
  section before capturing.
- **Menus are portalled.** Vuetify menus/dropdowns render in `.v-overlay__content`
  at `<body>` level, not inside the panel that opened them — locate them there.
- **Semi-transparent panels** let the image bleed through (e.g. a reddish tint
  over red annotations). Usually fine; otherwise navigate to a neutral region first.
- **Clear tooltips** before capturing a panel by `hover`-ing a neutral element
  (e.g. another panel's heading).
- **Uploads / destructive dialogs.** You can open the Create Dataset / Export
  dialogs to screenshot them, but **Cancel** (don't click Download/Import/Upload)
  so nothing is created or downloaded. To populate the Create Dataset dialog, ask
  the user to drop a file onto the drop zone in the devtools window, or use
  `mcp__plugin_chrome-devtools-mcp_chrome-devtools__upload_file` with a file input `uid`.

## Highlighting (optional)

Match the existing docs, which use clean, un-annotated screenshots. If you do need
a callout, inject it with `evaluate_script` (red outline / SVG arrow) before
capturing — see `/nimbus-playwright` for ready-made snippets.
