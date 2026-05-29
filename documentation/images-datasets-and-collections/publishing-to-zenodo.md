---
description: >-
  Archive an entire project—image files, annotations, and metadata—to Zenodo
  with a permanent DOI to satisfy data sharing and archiving requirements.
---

# Publishing to Zenodo

[Zenodo](https://zenodo.org/) is a free, open repository operated by CERN for archiving research data and minting permanent [DOIs](https://en.wikipedia.org/wiki/Digital_object_identifier). NimbusImage can upload an entire [project](README.md#projects)—the original image files, all of your annotations, and the project metadata—directly to Zenodo. This gives you a single, citable, permanently archived record of your imaging data so that you can comply with the data sharing and archiving policies required by journals and funding agencies.

Because NimbusImage uploads everything (raw images plus the analysis you layered on top), the Zenodo record is a complete, reproducible snapshot of your work rather than just a folder of files.

{% hint style="info" %}
Publishing to Zenodo is a **project-level** feature. Before you can publish, you'll need to gather your datasets and collections into a project and fill in its publication metadata. See [Projects](README.md#projects).
{% endhint %}

## What gets uploaded

When you upload a project, NimbusImage assembles a Zenodo deposition containing:

* **The original image files** for every dataset, in their original format (OME-TIFF, `.nd2`, etc.)
* **Annotation data** for each dataset, exported as JSON (the same format produced by [Importing and exporting objects and properties](../analyzing-image-data-with-objects-connections-and-properties/importing-and-exporting-objects-and-properties.md))
* **Collection configurations**, so the viewer and analysis setup can be reconstructed
* **A manifest** describing the structure and metadata of the whole project

## Step 1: Create a Zenodo API token

NimbusImage uploads on your behalf using a personal access token from your Zenodo account.

1. Log in to [Zenodo](https://zenodo.org/) (or [Zenodo Sandbox](https://sandbox.zenodo.org/) if you are testing—see the hint below).
2. Go to **Applications** in your account settings, and under **Personal access tokens** click **+ New Token**.
3. Give the token a name (for example, _NimbusImage_).
4. Grant the scopes `deposit:write`, `deposit:actions`, and `user:email` (or simply select **all**).
5. Click **Create**, then copy the token. **Zenodo only shows the token once**, so save a copy somewhere safe.

## Step 2: Configure the token in NimbusImage

1. Open your project and find the **Zenodo Publication** card on the project page.
2. Click **Configure Zenodo Token**.
3. Paste your token into the dialog and click **Save**. You can change or remove the token at any time from the same card.

Your token is stored encrypted on the NimbusImage server—it is never exposed in the browser.

{% hint style="info" %}
**Testing first?** Enable **Use Zenodo Sandbox** in the token dialog to practice the full workflow against [sandbox.zenodo.org](https://sandbox.zenodo.org/). The sandbox issues test-only DOIs and its data may be wiped periodically, so it's the safe place to rehearse before publishing for real. Note that the sandbox uses a separate account and a separate token from production Zenodo.
{% endhint %}

## Step 3: Upload the project

1. Make sure your project's publication metadata is filled in—**title, description, license, keywords, and authors**. NimbusImage maps these fields onto the Zenodo record.
2. On the **Zenodo Publication** card, click **Upload to Zenodo**.
3. A progress bar tracks the upload. Large projects can take several minutes; you can navigate away and come back, and the upload will continue in the background.

When the upload finishes, your project has a **draft** deposition on Zenodo. The card shows a link to open and review the draft on Zenodo's website.

{% hint style="info" %}
Zenodo limits a single record to **50 GB** and **100 files**. If your project is larger, you can request a quota increase (up to 200 GB) directly from Zenodo.
{% endhint %}

## Step 4: Review and publish

1. Click the link on the card to open the draft on Zenodo and confirm everything looks correct.
2. Back in NimbusImage, click **Publish (Mint DOI)** and confirm.

{% hint style="warning" %}
**Publishing is irreversible.** It mints a permanent DOI, and the published record can no longer be deleted—you can only add new versions. Review the draft carefully before publishing.
{% endhint %}

Once published, the card displays the project's DOI. This is the identifier you cite in your paper and report to your funding agency.

If you uploaded a draft but decide not to publish it, click **Discard Draft** to remove it.

## Updating a published project

If your data or analysis changes after publishing, you don't start over. Open the project and click **Upload New Version**. NimbusImage uploads the current state of the project as a new version of the existing Zenodo record. Each version gets its own version-specific DOI, while a single _concept DOI_ continues to point at the latest version—so citations remain valid as your work evolves.
