# Read-Only Attributes of the HtmlReport

The HtmlReport provides the _Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point in time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

## Querying a read-only attribute

```simtalk
print MyHtmlReport.UUID
```

## Viewing methods and attributes

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## Methods

### show

Shows the HtmlReport designated by `<Path>` as an HTML page.

- **Type:** Method
- **Syntax:** `<Path>.show([Anchor:string])`

#### Parameter

The optional parameter `Anchor` of data type string designates the anchor to which Plant Simulation navigates when it opens the HTML page.

#### Example

```simtalk
MyHtmlReport.show("DrainStat")
// jumps to the anchor defined by:
// << <a id="DrainStat"> </a> >>
// on the tab Content
```

## Attributes

The HtmlReport provides:

- The read-only attributes of all objects.
- The attributes of all objects.
