---
description: >-
  Let AI agents such as Claude Code, Codex, and claude.ai work with your
  NimbusImage data on your behalf
---

# Agentic control

NimbusImage can be driven by AI agents. You describe what you want in plain language, and the agent finds your datasets, looks at your images, runs analyses, and reports back. The agent always acts as you: it can see and change only what your own account can.

There are three ways to do this. They differ in where the agent runs and how much it can do.

| You use | Use this | What it can do |
| --- | --- | --- |
| The NimbusImage app itself | [Nimbus AI](../nimbus-ai.md) | Drives your viewer while you watch: navigation, layers, tools, workers, measurements, plots. |
| Claude Code or Codex (coding agents) | [The Python package and skill pack](python-package-and-skill-pack.md) | The most capable option: bulk changes, image arrays, custom analysis, and reusable scripts. |
| claude.ai (web) or the Claude Desktop app | [The MCP connector](mcp-connector.md) | Lookups and summaries in a chat: find datasets, count annotations, view images, read measurements, run workers, and tag annotations. |

## Which option should I use?

**If you can use a coding agent, use the Python package and skill pack.** Coding agents such as Claude Code and Codex can write and run code. With the `nimbusimage` Python package, they can do anything the API allows, on as much data as you need. The skill pack teaches the agent how to use the package well.

**If you work in claude.ai or the Claude Desktop app, use the MCP connector.** These apps can't run code, so the connector gives Claude a fixed set of tools instead. It is ideal for quick questions about your data, but it returns summaries and isn't meant for bulk work.

**If you want help inside the viewer, use Nimbus AI.** It is built into NimbusImage and changes what you see on screen as it works.

## In this section

* [Python package and skill pack](python-package-and-skill-pack.md) — install the `nimbusimage` package, get an API key, and add the skills to Claude Code or Codex.
* [Connect Claude to NimbusImage (MCP connector)](mcp-connector.md) — add NimbusImage to claude.ai or Claude Desktop, see what you can ask, and manage your connections.
