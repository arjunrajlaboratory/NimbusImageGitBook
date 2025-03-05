---
description: How to track and analyze objects across time using Time lapse mode
---

# Time lapse mode

Time lapse mode in NimbusImage provides powerful capabilities for tracking and analyzing objects across time points. This feature is particularly useful for cell tracking, movement analysis, and other time-dependent studies.

## Enabling Time lapse mode

When working with time lapse datasets, the Time lapse mode option automatically becomes available in the interface:

1. Look for the "Time lapse mode" checkbox in the variable navigation panel
2. Check the box to enable tracking visualization and special time lapse features

When enabled, Time lapse mode shows additional options:

## Understanding tracks and connections

In Time lapse mode, objects are connected across time points to form "tracks" that represent the same biological entity (like a cell) over time.

### Visualizing tracks

Tracks appear as connected lines between objects across different time points:

Key features of track visualization:
- **Current time point**: The current time point is highlighted with "Curr T=X" label and typically appears larger
- **Connected objects**: All objects connected to the current object are shown as a track
- **Time labels**: Each object shows its time point (T=1, T=7, etc.)
- **Connection colors**:
  - **Colored connections**: Normal connections between consecutive time points. Each color represents a different track.
  - **Red connections**: Connections that skip time points (gaps in tracking)
  - **Line thickness**: Forward-in-time connections are thicker than backward-in-time connections

### Track window setting

The "Track window" slider controls how many time points before and after the current time point are shown in the track visualization:

- Higher values show more of the track's history and future
- Lower values focus on just the immediate connections
- Adjust based on the density of your data and analysis needs

## Creating and editing tracks

### Using Connect timelapse tool

NimbusImage provides a dedicated tool for connecting objects across time:

Key settings:
- **Object to connect tag**: Select which type of objects to connect (based on their tags)
- **Connect across gaps**: Allows connecting objects even when there are missing time points
- **Max distance**: Maximum pixel distance between objects in consecutive frames to be considered for connection

To use the tool:
1. Configure the settings
2. Click "COMPUTE" to automatically connect objects based on proximity and settings

### Using Lasso connect for manual tracking

One of the most powerful features is the ability to use a lasso tool to manually define tracks:

1. Create a lasso connect tool from the toolset menu
2. Draw a lasso around the objects you want to connect across time
3. NimbusImage will **automatically connect them sequentially by time point**

This feature is particularly helpful for:
- Connecting "orphaned" objects to existing tracks
- Creating new tracks from scratch
- Fixing tracking errors where automatic tracking failed

## Navigating time with tracks

Tracks provide an intuitive way to navigate through time:

- **Click on any point in a track** to jump directly to that time point
- Use this to quickly inspect the history or future of a specific object
- Especially useful when analyzing division events or complex behaviors

## Best practices for time lapse analysis

1. **Start with automatic connections** using the Connect timelapse tool
2. **Review and fix tracks** using the lasso connect tool for any errors
3. **Use track window setting** to adjust visualization density
4. **Enable "Show labels"** to see time point information directly on objects
5. **Create properties** to analyze track information (velocity, displacement, etc.)

## Exporting time lapse data

Once you've established tracks, you can:
1. Create properties to measure changes over time
2. Export track data to CSV for further analysis in Python/R
3. Create snapshots to document specific tracking events
4. Download time lapse movies showing your tracks (see [Snapshots](snapshots.md) for more details)

## Common applications

Time lapse mode is particularly useful for:
- Cell migration tracking
- Mitotic event analysis
- Particle movement studies
- Growth measurements over time
- Interaction analysis between objects

By combining NimbusImage's flexible object tagging system with Time lapse mode, you can create sophisticated tracking analyses that capture the dynamic nature of your biological systems.