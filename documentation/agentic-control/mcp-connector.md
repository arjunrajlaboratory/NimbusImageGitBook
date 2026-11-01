---
description: >-
  Connect Claude (claude.ai or Claude Desktop) to NimbusImage so you can ask
  questions about your data in a chat
---

# Connect Claude to NimbusImage (MCP connector)

NimbusImage has an MCP connector at this address:

```
https://app.nimbusimage.com/mcp
```

Once it is connected, Claude can work with your NimbusImage data in a chat. It can find datasets, count and summarize annotations, look at images, read measurements, run analysis workers, and tag annotations.

* **Claude acts as you.** It sees exactly what your NimbusImage account can see, and nothing more.
* **You stay in control.** You approve the connection once, and you can [disconnect it](#see-and-disconnect-your-connections) at any time.
* **Claude asks before changing data.** Tools that change data (tagging annotations, computing a measurement, running a worker) are marked so that Claude asks you first.
* **Results are summaries by design.** Lists are capped (for example, 100 datasets or 200 annotations per request). Images come back downsampled. Claude waits up to about 2 minutes for a long job. For bulk work, see [Which option should I use?](#which-option-should-i-use)

## Which option should I use?

| You use | Use this |
| --- | --- |
| claude.ai (web) or the Claude Desktop app | The MCP connector (this page) |
| Claude Code or Codex (coding agents) | The [Python package and skill pack](python-package-and-skill-pack.md). It is much more capable: bulk changes, image arrays, custom analysis, and scripts. |

Coding agents can run code, so the Python package lets them do far more than the connector's fixed set of tools. The connector exists for apps that can't run code. You can also connect it in Claude Code ([see below](#claude-code-optional)), but you don't need to.

{% hint style="info" %}
Anthropic's menus change over time, so the steps below describe them in general terms. For the current details, see Anthropic's guide to [custom connectors](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp).
{% endhint %}

## Add the connector: Team and Enterprise organizations

An organization Owner adds the connector once for the whole organization. (On Enterprise, any role allowed to manage connectors can do this.)

1. In claude.ai, open your organization's connector settings and choose **Add custom connector**.
2. For **Name**, enter `NimbusImage`. For **URL**, enter `https://app.nimbusimage.com/mcp`.
3. For **Authentication**, choose **Sign in now**. Each member then signs in with their own NimbusImage account.
4. For **OAuth client**, choose **Use Claude's published identity**. claude.ai usually detects this automatically.
5. Leave **Request headers** empty and **Advanced** unchanged. Click **Save**.

{% hint style="warning" %}
Do **not** choose **No sign-in** with a shared API key in the request headers for an organization. Everyone in the organization would then act as the same NimbusImage user.
{% endhint %}

Then each member connects their own account:

1. In claude.ai, open your connector settings, find **NimbusImage**, and click **Connect**.
2. A NimbusImage page opens. Sign in if asked.
3. Review the consent page. It names the app that is asking for access. Click **Approve**. You return to Claude.
4. Try it out. Ask Claude: "List my NimbusImage datasets."

## Add the connector: individual Pro or Max plans

On a personal plan, you add the connector yourself.

1. In claude.ai, open your connector settings and choose **Add custom connector**.
2. For **Name**, enter `NimbusImage`. For **URL**, enter `https://app.nimbusimage.com/mcp`.
3. For **Authentication**, choose **Sign in now**.
4. For **OAuth client**, choose **Use Claude's published identity**.
5. Leave **Request headers** empty. Click **Save**.
6. Click **Connect**, sign in to NimbusImage if asked, and click **Approve**.

## Claude Desktop

Connectors you add on claude.ai belong to your Claude account. They appear in the Claude Desktop app automatically when you sign in with the same account. See Anthropic's [custom connectors guide](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp) for details.

## Claude Code (optional)

For Claude Code, we recommend the [Python package and skill pack](python-package-and-skill-pack.md) instead. To install them:

```bash
pip install nimbusimage
```

```bash
claude plugin marketplace add arjunrajlaboratory/NimbusImage
```

```bash
claude plugin install nimbusimage@NimbusImage
```

For Codex:

```bash
pip install nimbusimage
```

```bash
codex plugin marketplace add arjunrajlaboratory/NimbusImage
```

```bash
codex plugin add nimbusimage@NimbusImage
```

If you still want the connector in Claude Code (for example, for a quick look without keeping an API key on your computer):

1. Add it:

    ```bash
    claude mcp add --transport http nimbusimage https://app.nimbusimage.com/mcp
    ```
2. In Claude Code, type `/mcp`, choose `nimbusimage`, and choose **Authenticate**.
3. Your browser opens the NimbusImage consent page. Click **Approve**.

To remove it later, run the command below. Then also disconnect it in NimbusImage (see [See and disconnect your connections](#see-and-disconnect-your-connections)).

```bash
claude mcp remove nimbusimage
```

### Using an API key instead of signing in

You can also connect Claude Code with an [API key](python-package-and-skill-pack.md#step-1-get-an-api-key) instead of signing in. On app.nimbusimage.com, request a key from [support@cytopixel.com](mailto:support@cytopixel.com).

1. Save your key in a file that only you can read:

    ```bash
    chmod 600 ~/.nimbus_api_key
    ```
2. Add the connector with the key:

    ```bash
    claude mcp add --transport http nimbusimage https://app.nimbusimage.com/mcp \
      --header "Authorization: Bearer $(cat ~/.nimbus_api_key)"
    ```

Note that Claude Code stores the key in its own configuration file.

## What you can ask

Here are some examples. Replace the parts in angle brackets with your own names.

* "List my NimbusImage datasets."
* "What channels and z-slices does \<dataset> have?"
* "How many annotations are in \<dataset>, by tag and by shape?"
* "Show me channel 2 of \<dataset>."
* "Summarize the \<measurement> values for cells tagged 'nucleus'."
* "Which workers can segment nuclei? Run it on \<dataset> and tell me when it's done."
* "Tag every point annotation in \<dataset> with 'reviewed'." (Claude asks you first.)

The connector gives Claude these groups of tools:

| Group | What Claude can do |
| --- | --- |
| Datasets | List your datasets; get a dataset's size, channels, z-slices, time points, XY positions, and pixel size |
| Annotations | Count, summarize, and list annotations; add, remove, or replace tags |
| Images | Get the image as NimbusImage draws it (composite), or one channel in grayscale |
| Measurements | List measurements (properties), summarize their values, draw a histogram, and start computing a measurement |
| Workers and jobs | List workers, read a worker's parameters, run a worker, and wait for a job to finish |
| Help topics | Read NimbusImage's own documentation |

## See and disconnect your connections

1. In NimbusImage, open the account menu (top right) and find **Connected apps**.
2. Each connection is listed with:
   * the app (for example, Claude or Claude Code);
   * where it connects from (`claude.ai`, or `127.0.0.1` for Claude Code on your computer);
   * when it was connected;
   * when it was last used.
3. Click **Disconnect** to end a connection immediately. The app must sign in again to use NimbusImage. Disconnecting one connection doesn't affect the others.

A few things to know:

* "Last used" updates when the app signs in or renews its access, so it can lag by a few hours.
* Connections end on their own after 30 days without use.

## Troubleshooting

**Claude says it needs to sign in again, or "authentication required."**\
The connection was disconnected or has expired. Reconnect it. In claude.ai, click **Connect** again. In Claude Code, type `/mcp` and choose **Authenticate**.

**Claude can't find my dataset.**\
Claude only sees datasets your account can open. Check that you signed in as the right NimbusImage user.

**A worker job didn't finish.**\
Claude waits up to about 2 minutes. Ask it to check the job again, or watch the job in NimbusImage.

**I want Claude to do something bigger, like thousands of edits or a custom analysis.**\
Use the [Python package and skill pack](python-package-and-skill-pack.md) with Claude Code or Codex.

**Is this secure?**\
Claude acts with your permissions, and you can disconnect it at any time from **Connected apps**. NimbusImage never sees your Claude password, and Claude never sees your NimbusImage password.
