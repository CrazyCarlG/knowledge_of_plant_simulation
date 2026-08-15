# Attributes of the HtmlReport

The HtmlReport provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.

## Viewing attributes

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

To query the value of a read-only attribute, you might, for example, type:

```
print MyHtmlReport.UUID
```

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```
MyReport.TocLevels := 3
```

- To get the value of an attribute, you might, for example, type:

```
print MyReport.TocLevel
```

---

## Content [SimTalk] - HtmlReport

Sets the Content which the HtmlReport designated by `<Path>` displays.

**Type:** Attribute

**Syntax:**

```
<Path>.Content:string
```

**Assignment Value:** You can assign a value of data type string.

**Example:**

```
HtmlReport.Content := "[!self, Header, *]\
# General Information\
[Receiving, \"Statistics of the Source named 'Receiving' and the station 
named 'MyStation'\"]\
[MyStation]\
Created on [=day(sysdate)].[=month(sysdate)].[=year(sysdate)+1900]"
```

**See also:** Tab Content [HtmlReport]

---

## IsShown [SimTalk] - HtmlReport

Sets if the HtmlReport designated by `<Path>` is displayed in the Frame window into which it is inserted (true) or not (false).

**Type:** Method

**Syntax:**

```
<Path>.IsShown:boolean
```

**Assignment Value:** You can assign a value of data type boolean.

**Example:**

```
MyReport.IsShown := true
```

**See also:** Show Report

---

## TocLevels [SimTalk]

Sets the number of levels of the table of contents which the HtmlReport designated by `<Path>` shows.

**Type:** Attribute

**Syntax:**

```
<Path>.TocLevels:integer
```

**Assignment Value:** You can assign a value of data type integer.

Specify a value between 1 and 4. If you specify a value greater than 4, Plant Simulation treats this value as 4.

**Example:**

```
MyReport.TocLevels := 4
```

**See also:** Study the HtmlReport

---

## WindowHeight [SimTalk]

Sets the height in pixels with which Plant Simulation opens the display window of the HtmlReport designated by `<Path>`.

**Syntax:**

```
<Path>.WindowHeight:integer
```

**Assignment Value:** You can assign a value of data type integer.

**Example:**

```
MyHtmlReport.WindowHeight := 600 // pixels
```

**See also:** Show Report

---

## WindowWidth [SimTalk]

Sets the width in pixels with which Plant Simulation opens the display window of the HtmlReport designated by `<Path>`.

**Syntax:**

```
<Path>.WindowWidth:integer
```

**Assignment Value:** You can assign a value of data type integer.

**Example:**

```
MyHtmlReport.WindowWidth :=  800 // pixels
```

**See also:** Show Report
