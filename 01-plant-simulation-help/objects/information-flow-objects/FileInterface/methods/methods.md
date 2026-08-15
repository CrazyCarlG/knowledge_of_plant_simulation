# Methods of the FileInterface

This document summarizes the methods and read-only attributes of the **FileInterface** object, as described in the Plant Simulation Help.

The FileInterface provides:
- The methods listed below.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes of an object, open the window **Show Attributes and Methods** (select it on the context menu of the Class Library for a Class, or press **F8** / click it on the Home ribbon tab of the Frame for an Instance).

## Understanding the syntax line

An example of a syntax line looks like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature (identifier and data type of each parameter) is listed in parentheses. `(Parameter:string)` designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required type.
- Optional parameters are listed within brackets. `[,Parameter:boolean]` means you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, e.g. `:= false`.
- If the method has a return value, the signature shows its data type after the arrow `->`, e.g. `→ boolean`.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

---

## Methods

### close [SimTalk] - FileInterface

Saves all unsaved data of the FileInterface designated by `<Path>` and then closes the file.

- **Type:** Method
- **Syntax:** `<Path>.close → boolean`
- **Return Value:** data type `boolean`

**Example**

```
MyFileInterface.close
```

**See also:** open [SimTalk] - FileInterface

---

### formFeed [SimTalk]

Adds a FormFeed character to the end of the file of the FileInterface designated by `<Path>` and places the cursor at the end of the entry.

**Remarks**

- When printing a file, the printer starts a new page after this character.
- If the file is not open, the FileInterface opens it and leaves it open after accessing it.

- **Type:** Method
- **Syntax:** `<Path>.formFeed → boolean`
- **Return Value:** data type `boolean`

**Example**

```
MyFileInterface.formFeed
```

---

### goBottom [SimTalk]

Moves the cursor to the end of the last line of the file of the FileInterface designated by `<Path>`.

**Remarks**

- After reaching the end of the last line of the file, no more data will be read.
- If the file is not open, the FileInterface opens it and leaves it open after accessing it.

- **Type:** Method
- **Syntax:** `<Path>.goBottom → boolean`
- **Return Value:** data type `boolean`

**Example**

```
MyFileInterface.goBottom
```

**See also:** goTop [SimTalk]

---

### goToLine [SimTalk]

Moves the cursor in the file of the FileInterface designated by `<Path>` to the start of the designated line.

**Remarks**

- The FileInterface processes the file starting at this line. It returns `false` if the file contains fewer lines than you enter.
- If the file is not open, the FileInterface opens it and leaves it open after accessing it.

- **Type:** Method
- **Syntax:** `<Path>.goToLine(LineNumber:integer) → boolean`
- **Parameter:** `LineNumber` of data type `integer` designates the line.
- **Return Value:** data type `boolean`

**Example**

```
MyFileInterface.goToLine(2)
```

---

### goTop [SimTalk]

Moves the cursor to the start of the first line of the file of the FileInterface designated by `<Path>`.

**Remarks**

- If the file is not open, the FileInterface opens it and leaves it open after accessing it.

- **Type:** Method
- **Syntax:** `<Path>.goTop → boolean`
- **Return Value:** data type `boolean`

**Example**

```
MyFileInterface.goTop
```

**See also:** goBottom [SimTalk]

---

### newLine [SimTalk]

Adds a carriage return to the end of the file of the FileInterface designated by `<Path>` and sets the cursor to the end of the entry.

**Remarks**

- The FileInterface inserts new entries into a new line. You can format the protocol file like this.
- If the file is not open, the FileInterface opens it and leaves it open after accessing it.

- **Type:** Method
- **Syntax:** `<Path>.newLine → boolean`
- **Return Value:** data type `boolean`

**Example**

```
// evaluate the DataTable Tab. Insert an empty line into the table Tab
// every ten lines
var y: integer
for var y := 1 to Tab.YDim
   MyFileInterface.writeLn(Tab[1,y], Tab[2,y])
   if index mod 10 = 0
      MyFileInterface.newLine
   end
next
```

---

### open [SimTalk] - FileInterface

Opens the file of the FileInterface designated by `<Path>`.

**Remarks**

- The FileInterface leaves the file open until you close it again with the method `close`.
- To execute several operations one after the other, open the file beforehand to increase access speed. Close the file afterward, as data will not be saved to the file if Plant Simulation terminates unexpectedly. You can also increase access speed of an open file significantly if you collect the data beforehand and save it.

> **Note:** Plant Simulation can only open 10 files at a time. We advise to close files you do not need any more.

- **Type:** Method
- **Syntax:** `<Path>.open([ReadOnly:boolean:=false]) → boolean`
- **Parameter:** The optional parameter `ReadOnly` of data type `boolean` sets if the user has read-only permission only (`true`) or read and write permission (`false`).
- **Default Value of the Parameter:** `false`
- **Return Value:** data type `boolean`

**Example**

```
MyFileInterface.open
```

**See also:** close [SimTalk] - FileInterface

---

### read [SimTalk] - FileInterface

Reads the entire file starting at the current position into the FileInterface designated by `<Path>`.

**Remarks**

- If the file was just opened, Plant Simulation also recognizes the encoding according to the byte order marks and uses this encoding.
- If Plant Simulation does not recognize the encoding, it uses the specified encoding.

- **Type:** Method
- **Syntax:** `<Path>.read → string`
- **Return Value:** data type `string`

**Example**

```
var fileContent:string := FileInterface.read
```

**See also:** open [SimTalk] - FileInterface

---

### readLn [SimTalk]

Reads the line, in which the file cursor is located, into the file of the FileInterface designated by `<Path>` and increases the counter by one.

**Remarks**

- `readLn` passes the entire line as a string. You might have to use one of the conversion functions, such as `str_to_num`, to convert the string into another data type.
- If the file is not open for write, the FileInterface opens it and reads the line. If the file cannot be opened, for example because the path to the file is invalid, the function fails with an error. To avoid this error, you can explicitly call the method `open`, which returns `false` if the file cannot be opened.

- **Type:** Method
- **Syntax:** `<Path>.readLn → string`
- **Return Value:** data type `string`

**Example**

```
// A file contains numbers in several lines. These will be read
// into the second column of a DataTable
var y: integer, line: string
y := 1
while not MyFileInterface.EoF      // until end of file reached
   line := MyFileInterface.readLn  // get next line
   MyDataTable[2,y] := line
   y += 1
end
```

**See also:** writeLn [SimTalk], open [SimTalk] - FileInterface

---

### remove [SimTalk] - FileInterface

Closes the file of the FileInterface designated by `<Path>` if it was open and deletes it for good.

- **Type:** Method
- **Syntax:** `<Path>.remove → boolean`
- **Return Value:** data type `boolean`
  - `true` if deleting the file succeeded.
  - `false` if deleting fails. Then, check if the file exists and make sure that it is not read-only.

**Example**

```
MyFileInterface.remove
```

**See also:** Delete File [FileInterface]

---

### write [SimTalk] - FileInterface

Adds the designated data to the end of the file of the FileInterface designated by `<Path>`, without starting a new line.

**Remarks**

- The FileInterface places the cursor at the end of the entry. If the file does not exist, the FileInterface creates it. If the file is not open for write, the FileInterface opens it, writes the data, and closes it afterwards.
- If the file cannot be opened, for example because the path to the file is invalid, the function fails with an error. To avoid this error, you can explicitly call the method `open`, which returns `false` if the file cannot be opened.

- **Type:** Method
- **Syntax:** `<Path>.write(Data:any) → boolean`
- **Parameter:** `Data` of data type `any` designates the data that is appended to the end of the file.
- **Return Value:** data type `boolean`

**Example**

```
var FIF : object
FIF := FileInterface
FIF.write("ProcTime: ")
FIF.write(.machine.ProcTime,"[s]")
```

**See also:** open [SimTalk] - FileInterface

---

### writeLn [SimTalk]

Adds the data designated by the parameter of data type `any` and a carriage return character and a line feed character to the file, i.e., any data added after this will be written to a new line.

**Remarks**

- If the file is not open for write, the FileInterface opens it and closes it afterward. If you write many lines, it is therefore faster if you open the file once before you are calling `writeLn`.
- If the file cannot be opened, for example because the path to the file is invalid, the function fails with an error. To avoid this error, you can explicitly call the method `open`, which returns `false` if the file cannot be opened.

- **Type:** Method
- **Syntax:** `<Path>.writeLn(Data:any, ...) → boolean`
- **Parameter:** `Data` of data type `any` designates the data that is appended to the end of the file.
- **Return Value:** data type `boolean`

**Example**

```
var FIF : object
FIF := FileInterface
FIF.writeLn("length of track:")
FIF.writeLn(.Track.length,"meters")
FIF.writeLn(3.1415,true,"text",3+4)
```

**See also:** readLn [SimTalk], open [SimTalk] - FileInterface

---

## Read-Only Attributes of the FileInterface

The FileInterface provides:
- The read-only attributes listed in the table of contents to the left.
- The Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To query the value of a read-only attribute, you might, for example, type:

```
print MyFileInterface.IsOpen
```
