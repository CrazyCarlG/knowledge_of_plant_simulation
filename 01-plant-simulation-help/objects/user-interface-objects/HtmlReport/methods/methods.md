# Methods of the HtmlReport

The `HtmlReport` provides:

- The methods listed in the table of contents.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the F8 key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## Reading the Syntax Line

An example of the Syntax line of the individual methods might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. The expression `(Parameter:string)`, for example, designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses (…). Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. The expression `[,Parameter:boolean]`, for example, means that you can, but do not have to enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `→ boolean` in the example above.

---

## append [SimTalk] — HtmlReport

Appends text to the Content of the `HtmlReport` designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.append(Text:string)`
- **Parameter:** The parameter `Text` of data type string designates the text that you want to append.

**Example**

```simtalk
MyReport.Content := "#Heading"
   for var i := 1 to numNodes 
   MyReport.append(strChr(10))
   MyReport.append("Name: ")
   MyReport.append(object(i).name)
next
```

**See also:** Tab Content [HtmlReport]

---

## appendLine [SimTalk]

Appends a line of text to the Content of the `HtmlReport` designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.appendLine(Text:string)`
- **Parameter:** The parameter `Text` of data type string designates the text of the line that you want to append.

**Example**

```simtalk
MyReport.Content := "#Heading" + strChr(10)
for var i := 1 to numNodes 
   MyReport.appendLine(object(i).name)
next
```

**See also:** Tab Content [HtmlReport]

---

## appendPlainText [SimTalk]

Appends a special character as plain text to the content of the `HtmlReport` designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.appendPlainText(PlainText:string)`
- **Parameter:** The parameter `PlainText` of data type string designates the special character that you want to append as plain text.

**Example**

```simtalk
MyReport.Content := "#Heading" + strChr(10)
MyReport.appendPlainText("##**")
```

**See also:** Tab Content [HtmlReport]

---

## close [SimTalk] — HtmlReport

Closes the window that you opened by clicking Show Report of the `HtmlReport` designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.close → boolean`
- **Return Value:** The return value has the data type `boolean`.

**Example**

```simtalk
MyReport.close
```

**See also:** show [SimTalk]

---

## getHTMLCode [SimTalk] — HtmlReport

Returns the HTML code of the `HtmlReport` designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.getHTMLCode([WithButtonsAndLinks:boolean:=false]) → string`
- **Parameter:** The optional parameter `WithButtonsAndLinks` of data type boolean sets if the returned string contains HTML-code for the buttons in the top left corner of the display window and links for the objects, for example in statistics tables of the material flow objects.
- **Default Value of the Parameter:** The default value is `false`.
- **Return Value:** The return value has the data type `string`.

**Example**

```simtalk
print MyHtmlReport.getHTMLCode
```

**See also:** Display a HtmlReport

---

## refresh [SimTalk]

Force-updates the displayed `HtmlReport` designated by `<Path>` with the current values.

- **Type:** Method
- **Syntax:** `<Path>.update -> boolean`
- **Return Value:** The return value has the data type `boolean`.
  - `true` if the HtmlReport was updated successfully.
  - `false` if it was not updated.

**Example**

```simtalk
MyHtmlReport.update
```

**See also:** Structure Pane of the Display Window > Refresh the report

---

## save [SimTalk] — HtmlReport

Saves the `HtmlReport` designated by `<Path>` as an HTML file.

- **Remarks:** You can also specify the location of the file on your hard drive.
- **Type:** Method
- **Syntax:** `<Path>.save(FileName:string)`
- **Parameter:** The parameter `FileName` of data type string designates the path to and the name of the HTML file you want to save.

**Example**

```simtalk
MyReport.save("C:\temp\MyReport.html")
```

---

## show [SimTalk]

Shows the `HtmlReport` designated by `<Path>` as an HTML page.

- **Type:** Method
- **Syntax:** `<Path>.show([Anchor:string])`
- **Parameter:** The optional parameter `Anchor` of data type string designates the anchor to which Plant Simulation navigates when it opens the HTML page.

**Example**

```simtalk
MyHtmlReport.show("DrainStat")
// jumps to the anchor defined by:
// << <a id="DrainStat"> </a> >>
// on the tab Content
```

**See also:** Show Report

---

## Read-Only Attributes of the HtmlReport

The `HtmlReport` provides the Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.
