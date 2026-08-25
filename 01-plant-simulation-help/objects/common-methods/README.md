# Common Methods

This folder documents the methods that are common to **all objects** in the Plant Simulation Class Library, addressable from SimTalk. It is the canonical reference for the general methods, object-icon methods, location/predecessor/successor methods, inheritance methods, attribute-management methods, user-defined-attribute methods, and miscellaneous user-defined-attribute methods.

## Files

| File | Description |
|---|---|
| `common-methods.md` | Structured summary of the source PDF, organized by topic, with all SimTalk code samples preserved. |
| `Plant-Simulation-Help2606_3561-3662.txtx` | Plain-text extraction of the PDF (input for the summary). |

## Content Map

The summary covers the following topics:

1. **Methods of All Objects — Overview** — syntax conventions, optional parameters, default values, return values, and the *Show Attributes and Methods* window.
2. **General Methods**:
   - `addObserver`, `attributeWatchable`, `closeDialog`, `deleteObject`, `derive`, `duplicate`, `extendPath`, `getHTMLCode`, `getObservers`, `getXYWH`, `isNameUnique`, `memUsage`, `moveToFolder`, `openDialog`, `removeAllObservers`, `removeObserver`, `replace`, `setName`, `setPosition`, `setXYWH`, `showObject`, `updateDialog`, `writeObject`.
3. **Methods for Object Icons**:
   - `createIcon`, `deleteIcon`, `existsIcon`, `getIconSize`, `getPixel`, `putIconToClipboard`, `saveIconToFile`, `setCurrIconFromClipboard`, `setIconFromFile`, `setIconSize`, `setPixel`.
4. **Methods for the Location, Predecessor, and Successor**:
   - `pred`, `predConnector`, `succ`, `succConnector`.
5. **Methods for Managing Inheritance Relations**:
   - `childNo`, `hasAttribute`, `inheritAttribute` (object), `typeOf`.
6. **Methods for Managing Attributes**:
   - `getAttribute` (object), `getSubAttribute`, `putAttributeNamesIntoTable`, `setAttribute` (object), `setSubAttribute`.
7. **Methods for Managing User-defined Attributes**:
   - `createAttr`, `deleteAttr`, `getAttribute` (UDA), `getAttrName`, `getAttrNo`, `getAttrType`, `getAttrValue`, `inheritAttribute` (UDA), `setAttribute` (UDA), `setAttrType`, `setAttrValue`, `unshare`.
8. **Miscellaneous Methods of User-defined Attributes**:
   - `getStatisticsTable`, `increment`.
9. **Read-Only Attributes of All Objects — Introduction** — how to query, why they aren't settable.

## How to Read

- Each method entry lists its **syntax** (with default values and optional parameters), **parameters**, **return value**, and **example** code.
- User-defined-attribute methods use the path pattern `<Path>.<UserDefinedAttribute>.methodName(...)`.
- The complete list of `getHTMLCode` statistics type identifiers (English / German) and column-identifier syntax is preserved as a table.
- Search within `common-methods.md` by method name (e.g. `### addObserver`) to jump straight to a specific entry.

---

*Source: Plant Simulation Help — "Objects — Methods of All Objects". Unpublished work. © 2026 Siemens.*