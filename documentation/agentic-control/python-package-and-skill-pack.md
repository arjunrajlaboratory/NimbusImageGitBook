---
description: >-
  Use the nimbusimage Python package and the NimbusImage skill pack to let
  Claude Code or Codex work with your data
---

# Python package and skill pack

The `nimbusimage` Python package gives you programmatic access to NimbusImage. You can fetch images as arrays, create and edit annotations, run workers, compute measurements, and export results, all from code.

The NimbusImage skill pack teaches coding agents such as Claude Code and Codex how to use this package. Once it is installed, you can ask the agent to do things like "segment the nuclei in every dataset in this collection and export their areas to a CSV," and it writes and runs the code for you.

{% hint style="info" %}
**Using Claude Code or Codex?** This page is the recommended setup. It can do far more than the [MCP connector](mcp-connector.md), which is meant for claude.ai and Claude Desktop.
{% endhint %}

## Step 1: Get an API key

The package signs in with an API key. The key doesn't expire, so you only need to set it up once.

* **On app.nimbusimage.com:** email [support@cytopixel.com](mailto:support@cytopixel.com) from your account's email address and ask for an API key.
* **On your own server:** in the Girder admin interface, open **Users**, select your user, and choose **Edit User** > **API Keys** to create a key. Or ask your server's administrator. See [Installation](../../installation.md) for more about running your own server.

Keep your key private. Anyone who has it can act as you in NimbusImage.

## Step 2: Install the package

```bash
pip install nimbusimage
```

Then tell the package where your server is and what your key is. Add these lines to your shell profile (for example, `~/.zshrc` or `~/.bashrc`):

```bash
export NI_API_URL="https://app.nimbusimage.com/girder/api/v1"
export NI_API_KEY="your-api-key-here"
```

Open a new terminal and check that it works:

```python
import nimbusimage as ni

client = ni.connect()
for d in client.list_datasets():
    print(d["name"])
```

## Step 3: Install the skill pack

### Claude Code

```bash
claude plugin marketplace add arjunrajlaboratory/NimbusImage
```

```bash
claude plugin install nimbusimage@NimbusImage
```

### Codex

```bash
codex plugin marketplace add arjunrajlaboratory/NimbusImage
```

```bash
codex plugin add nimbusimage@NimbusImage
```

You only need to add the marketplace once. After that, start a new session and ask the agent about your NimbusImage data.

## What the skills cover

The agent loads the right skill automatically based on what you ask. You can also call one by name.

| Skill | What it covers |
| --- | --- |
| Core (`nimbusimage`) | Connecting, finding datasets, dataset metadata, projects |
| Images | Single frames, composites, z-stacks, and crops as arrays |
| Annotations | Creating, filtering, editing, and deleting objects; bulk operations; converting to shapes and masks |
| Workers | Finding and running analysis workers, and tracking their jobs |
| Analyze | Measurements (properties), export to CSV, JSON, and GeoJSON, connections, and sharing |
| Xenium ingest | Loading a 10x Xenium bundle (images, cells, genes, clusters) into NimbusImage |
| Spatial Genomics ingest | Loading a Spatial Genomics (GenePS) export into NimbusImage |

## What you can ask

* "List my NimbusImage datasets and how many objects each one has."
* "Run Cellpose-SAM on the DAPI channel of every dataset in this project."
* "For each cell, count the spots inside it and save the counts as a property."
* "Delete all the point objects tagged 'test' in this dataset."
* "Get the z-stack for channel 2 at XY position 3 and make a max projection."
* "Export area and mean intensity for all nuclei to a CSV."
* "Load this Xenium bundle into NimbusImage."

Depending on your agent's settings, it may ask before running code. For anything that deletes or changes many objects, ask the agent to explain its plan first, and check it before you let it run.

## Using the package without an agent

You can also use the package directly in your own Python scripts and notebooks. A short example:

```python
import nimbusimage as ni

client = ni.connect()
ds = client.dataset(name="My Experiment")

img = ds.images.get(channel=0, z=0)          # a numpy array
nuclei = ds.annotations.list(shape="polygon", tags=["nucleus"])
ds.export.to_csv(property_paths=[["prop_id", "Area"]], path="results.csv")
```

See the [API reference](https://arjunrajlaboratory.github.io/NimbusImage/) for the full set of functions.

## Connecting the MCP connector in Claude Code too

You don't need the [MCP connector](mcp-connector.md) in Claude Code if you have the skill pack. If you add both, the skill pack tells Claude to use the Python package for anything beyond a quick lookup. See [Claude Code (optional)](mcp-connector.md#claude-code-optional).
