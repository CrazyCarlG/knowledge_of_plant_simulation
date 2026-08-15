# Attributes of the AttributeExplorer

This document summarizes the attributes of the **AttributeExplorer** object.

## General Information

- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.
- To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.
- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.

### Getting and Setting Attribute Values

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

To query the value of a read-only attribute:

```simtalk
print MyAttributeExplorer.UUID
```

To set the value of an attribute:

```simtalk
MyAttributeExplorer.Comment := "Processing time changes globally"
```

To get the value of an attribute:

```simtalk
print MyAttributeExplorer.AttributeRepresentation
posit := Station.Cont.XPos
```

---

## AttributeRepresentation

Shows the attributes with their **Name** or with their **Alias** in the Explorer window of the AttributeExplorer designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.AttributeRepresentation:string`
- **Assignment Value:** You can assign a value of data type string. You can specify `"Name"` or `"Alias"`.

```simtalk
MyAttributeExplorer.AttributeRepresentation := "Alias"
```

**See also:** Show Attributes With

---

## AttributeTable

Sets the attribute table of the AttributeExplorer designated by `<Path>` for object attributes.

- **Remarks:** This table contains the attributes you enter on the tab **Attributes**.
- **Type:** Attribute
- **Syntax:** `<Path>.AttributeTable:table`
- **Assignment Value:** You can assign a value of data type table.

```simtalk
MyAttributeExplorer.AttributeTable := tableAttributes
```

**See also:** Tab Attributes [AttributeExplorer]

---

## Comment

Sets the comment, which the AttributeExplorer designated by `<Path>` displays above the list box.

- **Type:** Attribute
- **Syntax:** `<Path>.Comment:string`
- **Assignment Value:** You can assign a value of data type string.

```simtalk
MyAttributeExplorer.Comment := "Processing time changes globally"
```

**See also:** Comment [AttributeExplorer], Show Comment [AttributeExplorer]

---

## ExplorerTable

Sets the table which the AttributeExplorer designated by `<Path>` shows.

- **Remarks:**
  - The AttributeExplorer enters the attributes you type into row 0 of the table into the Attribute Table.
  - The AttributeExplorer enters the objects you type into column 0 of the table into the Object Table.
  - The AttributeExplorer enters the attributes you type into any of the columns of the table into the Explorer table.
- **Type:** Attribute
- **Syntax:** `<Path>.ExplorerTable:table`
- **Assignment Value:** You can assign a value of data type table.

```simtalk
MyAttributeExplorer.ExplorerTable := MyExplorerTable
```

**See also:** Show Explorer, AttributeTable [SimTalk], ObjectTable [SimTalk]

---

## IncludeMUs

Makes the AttributeExplorer designated by `<Path>` also search MUs located within the active Frame (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.IncludeMUs:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

```simtalk
MyAttributeExplorer.IncludeMUs := true
```

**See also:** Include MUs [AttributeExplorer], Frame [find attribute in]

---

## IncludeSubframes

Makes the AttributeExplorer designated by `<Path>` also search Frames located within the active Frame (`true`), or not (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.IncludeSubframes:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

```simtalk
MyAttributeExplorer.IncludeSubframes := true
```

**See also:** Include Subframes [AttributeExplorer], Frame [find attribute in]

---

## IsShown

Shows (`true`) or hides (`false`) the attribute table of the AttributeExplorer designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.IsShown:boolean`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** You can assign a value of data type boolean.

```simtalk
MyAttributeExplorer.IsShown := false
```

**See also:** ExplorerTable [SimTalk], Show Explorer

---

## Mode

Sets the mode that the AttributeExplorer designated by `<Path>` uses.

- **Type:** Attribute
- **Syntax:** `<Path>.Mode:string`
- **Assignment Value:** You can assign a value of data type string. You can specify `"Watch"`, `"Edit"`, or `"Read"`.

```simtalk
MyAttributeExplorer.Mode := "Edit"
```

**See also:** Watch [AttributeExplorer], Edit [AttributeExplorer], Read Only [AttributeExplorer]

---

## ObjectRepresentation

Shows the objects of the AttributeExplorer designated by `<Path>` with their entire **Path**, their **Name**, or their **Label** in the Explorer window.

- **Type:** Attribute
- **Syntax:** `<Path>.ObjectRepresentation:string`
- **Assignment Value:** You can assign a value of data type string. You can specify `"Path"`, `"Name"`, or `"Label"`.

```simtalk
MyAttributeExplorer.ObjectRepresentation := "Label"
```

**See also:** Show Objects With

---

## ObjectTable

Sets the table containing the Plant Simulation objects of the AttributeExplorer designated by `<Path>`.

- **Remarks:** The objects table contains the objects which you type in on the tab **Objects**.
- **Type:** Attribute
- **Syntax:** `<Path>.ObjectTable:table`
- **Assignment Value:** You can assign a value of data type table.

```simtalk
MyAttributeExplorer.ObjectTable := tableObjects
```

**See also:** Tab Objects [AttributeExplorer]

---

## QueryTable

Sets the query table of the AttributeExplorer designated by `<Path>`.

- **Remarks:** The query table contains the settings which you enter on the tab **Query**.
- **Type:** Attribute
- **Syntax:** `<Path>.QueryTable:table`
- **Assignment Value:** You can assign a value of data type table.

```simtalk
MyAttributeExplorer.QueryTable := myQueryTable
```

**See also:** Tab Query

---

## ShowComment

Shows the text box for specifying a comment above the list field of the AttributeExplorer designated by `<Path>` (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.ShowComment:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

```simtalk
MyAttributeExplorer.ShowComment := true
```

**See also:** Show Comment [AttributeExplorer], Comment [AttributeExplorer]

---

## StartNode

Sets the Frame in which the AttributeExplorer designated by `<Path>` starts finding the attributes of the objects.

- **Type:** Attribute
- **Syntax:** `<Path>.StartNode:object`
- **Assignment Value:** You can assign a value of data type object.

```simtalk
MyAttributeExplorer.StartNode := MyPlant.MyFrame
```

**See also:** Frame [find attribute in], FileLink
