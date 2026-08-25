# Common Attributes

This folder documents the attributes that are common to **all objects** in the Plant Simulation Class Library. It is the canonical reference for the general attributes, control-method attributes, and attributes of user-defined attributes, all addressable from SimTalk.

## Files

| File | Description |
|---|---|
| `common-attributes.md` | Structured summary of the source PDF, organized by topic, with all SimTalk code samples preserved. |
| `Plant-Simulation-Help2606_3678-3751.pdf` | Original PDF excerpt from the Plant Simulation Help. |
| `Plant-Simulation-Help2606_3678-3751.txtx` | Plain-text extraction of the PDF (input for the summary). |

## Content Map

The summary covers the following topics:

1. **UUID [SimTalk]** — read-only identifier of an object.
2. **Attributes of All Objects — Overview** — how to set/get attributes, the *Show Attributes and Methods* window, and read-only attribute filter.
3. **Data Held in Tabular Form in Attributes** — copy-on-get / assign-back semantics for table-typed attributes.
4. **General Attributes**:
   - `Coordinate3D`, `CreateIn3D`, `Label`, `Name`, `RootFolder`.
5. **Attributes of the Controls** (control-method bindings):
   - `AvailableCtrl`, `ChangePathCtrl`, `CloseCtrl`, `ConnectCtrl`, `ConstructorCtrl`, `DestructorCtrl`, `DragDropCtrl`, `FailCtrl`, `InitCtrl`, `MoveInFrameCtrl`, `MoveToFolderCtrl`, `NotAvailableCtrl`, `OpenCtrl`, `PauseCtrl`, `PermitDeleteCtrl`, `PlausibilityCtrl`, `RelabelCtrl`, `RenameCtrl`, `SelectCtrl`, `UnplannedCtrl`.
6. **Attributes of User-defined Attributes** (sub-attributes):
   - `Alignment`, `asString`, `BackgroundColor`, `Color`, `DataType`, `DecimalPlaces`, `Font`, `HasInitValue`, `InitValue`, `IntegerPlaces`, `Name`, `Position`, `Rotation`, `Scale`, `ShowDataType`, `ShowExternally`, `ShowIn3D`, `ShowInTooltip`, `ShowName`, `ShowUnit`, `StatisticsActive`, `Transparent`.
7. **Methods of the Material Flow Objects — Introduction** — signature conventions and how to read them.

## How to Read

- Each attribute entry lists its **type**, **syntax**, **assignment / return value**, and **example** code.
- Control-method entries also list the **parameters** Plant Simulation passes to the bound method, plus the typical use case.
- Search within `common-attributes.md` by the attribute name (e.g. `### PauseCtrl`) to jump straight to a specific entry.

---

*Source: Plant Simulation Help — "Objects — Common Attributes". Unpublished work. © 2026 Siemens.*
