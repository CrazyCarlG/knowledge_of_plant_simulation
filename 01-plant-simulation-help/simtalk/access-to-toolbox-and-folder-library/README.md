# Access to Toolbox and Folder Library (SimTalk)

This directory covers SimTalk interfaces for the **Toolbox (toolbars)** and the
**Folder in the Class Library**.

| File | Description |
|------|-------------|
| `access-to-toolbox-and-folder-library.md` | Full reference for Toolbox + Class Library folder methods/attributes, plus the Console. |
| `access-to-toolbox-and-folder-library.txtx` | Raw text extraction of the original Plant Simulation Help pages (with page headers). |

## Summary

### Part 1 — Toolbox (Toolbars)

Manage toolbar visibility and icons:

| Member | Kind | Purpose |
|--------|------|---------|
| `Visible [toolbar]` | Attribute | Show/hide the selected toolbar in the Toolbox. |
| `addObject` | Method | Append an object's icon to a toolbar (optional position). |
| `delObject` | Method | Remove an object's icon from a toolbar. |
| `redraw` | Method | Refresh a toolbar — useful after `setPixel` edits. |
| `Visible [SimTalk]` | Attribute | Programmatic show/hide of a toolbar in the Toolbox. |

### Part 2 — Folder in the Class Library

Create, query, lock, license, and enumerate folders, plus clipboard paste.

| Member | Kind | Purpose |
|--------|------|---------|
| `createFolder` | Method | Create a folder at root or inside `<Folder-Path>`. |
| `createToolbar` | Method | Create a toolbar at root or inside `<Folder-Path>`. |
| `getLibraryInfo` | Method | Read library metadata (name, version, description, file path, prohibited flag, alternative paths). |
| `HiddenWhenInLockedFolder` | Attribute | Hide a folder inside a locked folder. |
| `IsLocked` | Read-only | Whether a folder is a locked library. |
| `loadObjectAs` | Method | Load a `.psobj` into a folder, with optional auto-merge / replace / password. |
| `lockFolder` | Method | Lock / unlock a folder with a password; optionally encrypt methods. |
| `node` | Method | Return an object inside a folder by index or name. |
| `numNodes` | Method | Return the number of objects directly contained in a folder (sub-folders count as 1, their contents do not). |
| `pasteClipboard` | Method | Paste the clipboard into a folder, optionally collecting pasted objects into a table. |
| `setLibraryInfo` | Method | Mark a folder as a library, set version, description, prohibited flag. |
| `setRequiredLicense` | Method | Require a user-defined license for the library (feature / version / password / free-tier / update password). |
| `ShowToolbar` | Attribute | Show/hide the folder's toolbar in the Toolbox. |

### Part 3 — Console

The Console window reports actions Plant Simulation executes. Configure its
verbosity under **File > Preferences > User Interface > Console Filter**.
Context menu supports **Copy**, **Clear**, **Select All**, **Show Print
Output**, and **Show Info Output**.

## Code Samples Preserved

- `addObject` — adding an icon at a specific position.
- `delObject` — removing an icon.
- `redraw` — full example that derives a station, adds it to a toolbar, paints a
  gradient icon with `setPixel` / `makeRGBValue`, then calls `redraw`.
- `Visible` — toggling toolbar visibility.
- `createFolder` / `createToolbar` — creating and renaming folders/toolbars.
- `getLibraryInfo` — reading library name + version into local variables.
- `HiddenWhenInLockedFolder` — hiding a folder in a locked parent.
- `IsLocked` — querying the lock state.
- `loadObjectAs` — loading a `.psobj` with auto-merge.
- `lockFolder` — locking with new password, and locking with no new password.
- `node` — printing the 5th object in a folder.
- `numNodes` — printing the object count.
- `pasteClipboard` — capturing pasted objects into a table and iterating.
- `ShowToolbar` — hiding a folder's toolbar.
- `setRequiredLicense` — registering a user-defined license for a library.

*Source: Plant Simulation Help — "SimTalk Access to the Toolbox and Folder
Library". Unpublished work. © 2026 Siemens.*