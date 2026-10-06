---
description: >-
  Use Nimbus AI, a conversational assistant that can drive the NimbusImage
  interface, run analyses, and answer questions about how the app works
---

# Nimbus AI

Nimbus AI is a conversational assistant built into NimbusImage. You describe what you want in plain language — "go to the third time point and show only the DAPI channel", "find the nuclei and measure their area" — and the assistant carries it out in your own viewer while you watch. It can also look at your image, summarize and plot your measurements, and explain how to do things in the interface. Nimbus AI currently runs on Claude Sonnet 5.5.

Nimbus AI can only do what you could do yourself by clicking, and it works with your own account and permissions.

## Opening Nimbus AI

You need to be logged in to use Nimbus AI. Open the panel in either of these ways:

* **Robot button.** Click the robot icon at the right end of the top app bar.
* **Command palette.** Press ⌘K (Mac) or Ctrl+K (Windows/Linux), type "AI" or "assistant", and choose **Open Nimbus AI panel**. See [Command palette](viewing-your-data.md#command-palette).

Type your request in the box at the bottom and press Enter to send it (Shift+Enter starts a new line). Each step the assistant takes appears in the panel as a short card (for example, "Move to Z=4") with a running, done, or failed status, followed by a brief summary of the result.

The buttons at the top of the panel let you:

* **Revert** (circular-arrow icon) the view changes from the last message. This appears after a message that changed the view.
* **Start over** (refresh icon) by clearing the conversation.
* **Close** the panel.

While the assistant is working, the send button becomes a red **stop** button that you can use to interrupt it. Your conversation, including any plots, is kept in your browser between sessions until you clear it.

## What Nimbus AI can do

### Looking at your data

* **Check where you are.** The assistant always knows your current dataset, collection, location (XY/Z/time), layers, selected tool, active filters, and object counts.
* **See the image.** When it needs to judge what's actually in the image (for example, what kind of staining or sample is visible), it takes a screenshot of the viewer and looks at it.
* **Count and summarize objects.** It can break down your objects by tag, shape, and channel, or look at a few specific objects.

### Navigating and changing the view

* **Move around.** Go to a different XY position, Z slice, or time point; pan and zoom; or fit the view to all objects, the selected objects, or the full image.
* **Adjust layers.** Change a layer's color, contrast, name, or visibility; show only certain layers; switch between single, multiple, and unrolled layer modes.
* **Display options.** Show or hide objects and connection lines, change object opacity, toggle the scale bar, change the background color, and switch between 2D and 3D views.
* **Select and filter objects.** Select objects by tag, shape, or channel; filter what's shown by tag, by current frame, or by a measurement range (for example, area above 100).

### Tools, workers, and measurements

* **Set up tools.** Create a manual blob, point, or line tool, or an automated worker tool such as Cellpose-SAM or Piscis, with tags and parameters chosen for your channels. It can also activate a tool for you.
* **Run workers.** Run a worker tool on your dataset, then wait for the job to finish and continue with the result.
* **Measure objects.** Set up and compute properties (such as intensity or morphology) for a set of objects, then report summary statistics.
* **Set the physical scale.** Record pixel size, Z step, and time step so that measurements use real units.

### Coloring and tagging objects

* **Color objects.** Give selected objects, or objects matching a tag or shape, a single color or random colors.
* **Color by a property.** Color every object in the dataset by a computed property, with a legend in the viewer — a color ramp for continuous values, or distinct colors for categories such as cluster IDs. See [Coloring objects by a property value](analyzing-image-data-with-objects-connections-and-properties/interacting-with-objects.md#coloring-objects-by-a-property-value).
* **Tag objects.** Add, remove, or replace tags on selected objects or on objects matching a query.

### Analyzing measurements

* **Statistics and distributions.** Ask for the mean, median, spread, or a histogram of any property, optionally for just one subset of objects.
* **Plots in the panel.** Ask for a scatter plot, histogram, or box plot (including one box per tag). The interactive plot appears right in the panel.
* **Analysis plots and gates.** Add a plot to the Analysis panel with a rectangular gate that filters objects everywhere in the app. See [Analysis plots and gating](analyzing-image-data-with-objects-connections-and-properties/analysis-plots-and-gating.md).

### Answering questions

* **How-to help.** Ask how a feature works or how to do something yourself. The assistant draws on built-in NimbusImage help covering the interface, visualization, object tools, connections, measurements, import/export, and troubleshooting.
* **Explaining what you see.** For example, why some objects are missing (it checks for filters and analysis gates) or why objects have the colors they do.

### Example prompts

* "What am I looking at?"
* "Hide everything except DAPI and brighten it a bit."
* "Set up a Cellpose-SAM tool for nuclei on the DAPI channel and run it."
* "Measure the area of all my nucleus objects and show me a histogram."
* "Make a scatter plot of area versus mean intensity, colored by tag."
* "Color my cells by area."
* "Only show spots with intensity above 500."
* "Why do I see fewer objects than I expected?"

## Approving actions

Changes to the view — location, camera, layer settings, display options, filters, selection — happen immediately without asking, because you can see them and revert them. Actions that start computations or change things shared with everyone using the collection ask for your confirmation first. The assistant shows a card describing what it is about to do, with **Run** and **Cancel** buttons. Actions that need approval are:

* **Running a worker** — it can take minutes and may create many objects.
* **Computing a property** — it starts a compute job.
* **Creating a tool or a property, or setting the scale** — these change the shared collection.
* **Coloring the whole dataset by a property** — it replaces every object's color and is not undoable.
* **Removing analysis plots** — the plots and their gates belong to the shared collection and can't be rebuilt.

If you click **Cancel**, the assistant is told you declined and will adjust its plan or ask what you'd like instead.

The **Auto-approve all actions** switch below the text box skips these confirmations. Use it with care, especially for coloring by a property, which can't be undone.

### Undoing changes

* **View changes** from your last message can be reverted with the revert button at the top of the panel. If you've switched to a different dataset since then, revert isn't available.
* **Object edits** such as coloring or tagging specific objects are on the normal undo history, so you can ask the assistant to undo them or undo them yourself.
* **Coloring by a property** is not undoable; to change it, re-apply a different coloring or remove the coloring.

{% hint style="info" %}
If you switch to a different dataset while the assistant is working, it stops rather than applying changes to the wrong dataset.
{% endhint %}

## What Nimbus AI can't do

Some things are outside what the assistant can do directly. In these cases it will guide you to do them yourself:

* **Connections.** It can't create, filter, or delete connections. It will point you to the connection tools and the Connections tab of the Object list. See [Tools for connecting objects](analyzing-image-data-with-objects-connections-and-properties/tools-for-connecting-objects.md).
* **Organizing tools.** It can't pin or reorder tools in the Tools palette.
* **Command palette.** It can't open the command palette for you, but it often suggests what to type there.
* **Drawing gates.** It can only make rectangular gates. For an irregular population, it creates the plot and asks you to draw the region.
* **Creating or deleting objects directly.** It can't draw or delete objects one by one, or switch to a different dataset or collection. It can create objects by running a worker.

## AI-suggested tools

Separately from the chat panel, NimbusImage can suggest a starting set of tools for a new collection based on your image and its channel names. Suggestions appear automatically the first time you open a new, empty collection, and you can ask for them at any time with the lightbulb button in the Tools palette or **Suggest tools with AI** in the command palette. Nothing is added until you accept it. See [AI-suggested tools](analyzing-image-data-with-objects-connections-and-properties/tools-for-making-objects.md#ai-suggested-tools).

## What is shared with the AI model

Nimbus AI sends your requests through the NimbusImage server to Anthropic's Claude API. Along with each message, it sends a text summary of your current interface state (dataset and collection names, location, layers, filters, object counts, and so on). It sends screenshots of the viewer only when it decides it needs to see the image content. AI-suggested tools similarly send a screenshot of the viewer along with your channel names.

## Tips for getting good results

1. **Use channel and tag names.** "Run Cellpose-SAM on the DAPI channel and tag the results nucleus" works better than "find the cells".
2. **Ask for one workflow at a time.** The assistant takes up to 30 steps per message; if it stops partway through a long task, send another message to continue.
3. **Ask for plots and summaries, not lists.** It reports counts and statistics rather than pasting long lists, since you can see the objects in the interface.
4. **Check worker settings before approving.** The approval card summarizes what will run. If a parameter looks wrong, cancel and tell the assistant what to change.
5. **Treat image descriptions with care.** The assistant sees a lower-resolution screenshot, so verify its observations about image content yourself.
6. **Start over when changing topics.** Clearing the conversation with the refresh button gives the assistant a clean slate.
