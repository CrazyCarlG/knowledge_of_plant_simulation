# Common Read-Only Attributes

This folder documents the **read-only attributes** that are common to all Plant Simulation objects (Class Library objects). Read-only attributes can be queried but not set — Plant Simulation computes the value at query time. In most cases they correspond to an unavailable dialog item on one of the object's tabs (e.g. **Statistics**).

## Files

| File | Description |
|---|---|
| `common-read-only-attributes.md` | Structured summary of the source PDF, organized by topic, with all SimTalk code samples preserved. |
| `Plant-Simulation-Help2606_3662-3678.txtx` | Plain-text extraction of the PDF (input for the summary). |

## Content Map

The summary covers the following topics:

1. **Overview** — what read-only attributes are, how to query them, and the *Show Attributes and Methods* window.
2. **Read-Only Attributes**:
   - `~` (tilde) — material-flow-object location (also exposed as `Location`).
   - `Class` — origin class of an instance.
   - `InternalClassType` — built-in English object name (full English / German mapping table preserved).
   - `Location` — alias of `~` for material-flow objects.
   - `NumAttr` — count of user-defined attributes.
   - `NumChildren` — count of inheriting children.
   - `Origin` — most recent origin object in the inheritance chain.
   - `OriginRoot` — root object of the inheritance chain.
   - `RootFrame` — root frame in the Frame hierarchy.
   - `UUID` — universally unique identifier.

## How to Read

- Each entry lists its **syntax** and **return value**, with SimTalk examples.
- `~` and `Location` are interchangeable aliases for material-flow objects.
- `InternalClassType` returns the English name regardless of UI language; the full English ↔ German table is preserved verbatim.
- Search within `common-read-only-attributes.md` by attribute name (e.g. `### NumAttr`) to jump straight to a specific entry.

---

*Source: Plant Simulation Help — "Objects — Read-Only Attributes of All Objects". Unpublished work. © 2026 Siemens.*