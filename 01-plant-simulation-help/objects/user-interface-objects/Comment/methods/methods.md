# Methods of the Comment

The Comment object provides:

- The methods listed in this document.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the members of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show the members of the selected Instance.

## Syntax line example

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature lists the identifier and data type of each parameter in parentheses. `(Parameter:string)` designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required type.
- Optional parameters are listed in brackets, e.g. `[,Parameter:boolean]`.
- If a parameter has a default value, the signature shows it after the parameter, e.g. `:= false`.
- If the method has a return value, the signature shows its data type after the arrow `→`, e.g. `→ boolean`.

> **Note:** Make sure to enter parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

---

## appendToContent [SimTalk]

Appends the passed text to the existing text on the tab **Comment** which the Comment designated by `<Path>` shows.

- **Type:** Method

**Remarks**

Plant Simulation requests memory in larger blocks from the operating system so that memory does not have to be increased with each call. This makes putting a message together from many text blocks faster.

**Syntax**

```
<Path>.appendToContent(Text:string)
```

**Parameter**

- `Text` (string) — the text which you want to add.

**Example**

```
MyComment.appendToContent("my added text")
```

**See also:** Tab Comment [Comment]

---

## openComment [SimTalk]

Opens a window that only shows the comment you entered into the Comment designated by `<Path>`, without any formatting options.

- **Type:** Method

**Syntax**

```
<Path>.openComment → boolean
```

**Return Value**

The return value has the data type boolean.

**Example**

```
MyComment.openComment
```

**See also:** Tab Comment [Comment]

---

## Read-Only Attributes of the Comment

The Comment provides the _Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.
