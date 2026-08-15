# Importing and Exporting Data in Text Format

Lists and tables provide methods for working with them in **text format**, instead of table format (`.pslist`).

To view all methods, read-only attributes, and attributes of an object, open the **Show Attributes and Methods** window (example shown for the object *Station*):

- Select **Show Attributes and Methods** on the context menu of the Class Library to show attributes/methods of the selected **Class**.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame containing an inserted instance to show attributes/methods of the selected **Instance**.

All methods in this section apply to the objects **DataStack, DataQueue, DataList, DataTable, and TimeSequence**.

---

## readExcelFile [SimTalk]

Imports data from the designated Excel file (`*.xls`) into the list/table designated by `<Path>`.

**Remarks**

- Plant Simulation overwrites any existing data.
- Plant Simulation does **not** overwrite the column index and/or row index of a DataTable if the respective Excel cells are empty. To overwrite that content, delete it before importing.
- Plant Simulation uses Excel as a COM server when reading/writing MS Excel files, so MS Excel must be installed. To use the previous (no longer supported) Excel interface, use the start option `-NativeExcel`.

**Syntax**

```
<Path>.readExcelFile(FileName:string[, Sheet:string,
NoDebugger:boolean:=false, Password:string]) → boolean
```

**Parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| `FileName` | string | Path to and name of the Excel file (`*.xls`). |
| `Sheet` (optional) | string | The worksheet. If omitted and the file has multiple worksheets, a dialog opens to select one. |
| `NoDebugger` (optional) | boolean | Whether the Method Debugger opens after unsuccessful access (`false`) or not (`true`). Default `false`. When `true`, returns `false` on error instead of opening the debugger. |
| `Password` (optional) | string | The password. |

**Return value:** boolean

**Example**

```
MyDataList.readExcelFile("C:\users\johnE\times.xls")
MyDataTable.readExcelFile("C:\temp\product_plan.xls","plant xy anytown")
if MyDataStack.readExcelFile("C:\temp\data.xls", true) = false
   // could not read file
end
```

**See also:** Import File; Specifying Start Options, `-NativeExcel`

---

## readFile [SimTalk] - lists

Imports data from the designated file into the list/table designated by `<Path>`. Plant Simulation overwrites any existing data.

**Remarks**

- Can import text files exported with `writeFile`, as well as object files exported with `writeObjectFile`.

**Syntax**

```
<Path>.readFile(FileName:string[, NoDebugger:boolean:=false,
CodePage:string:="ANSI"]) → boolean
```

**Parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| `FileName` | string | Path to and name of the text file (`*.txt`). |
| `NoDebugger` (optional) | boolean | Whether the Method Debugger opens after unsuccessful access (`false`) or not (`true`). Default `false`. |
| `CodePage` (optional) | string | Encoding: `"ANSI"` or `"System"`, `"UTF-8"`, or `"Unicode"`. Default `"ANSI"`. |

**Return value:** boolean

**Example**

```
MyDataList.readFile("C:\users\johnE\times.txt")
MyDataTable.readFile("C:\temp\product_plan.psobj")
if MyDataStack.readFile("C:\temp\data.txt", true) = false
   // could not read file
end
```

**See also:** Import File; `writeFile`, `writeObjectFile`

---

## readXMLFile [SimTalk]

Imports data from the designated XML file (`*.xml`) into the list/table designated by `<Path>`. Plant Simulation overwrites any existing data.

**Remarks**

- When reading an XML file that does **not** use Plant Simulation's proprietary format, Plant Simulation tries to construct a list/table from any XML data. For complex XML files some data might not be entirely imported. Use the **XMLInterface** to read complex XML files instead.

**Syntax**

```
<Path>.readXMLFile(FileName:string[, NoDebugger:boolean:=false]) → boolean
```

**Parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| `FileName` | string | Path to and name of the XML file (`*.xml`). |
| `NoDebugger` (optional) | boolean | Whether the Method Debugger opens after unsuccessful access (`false`) or not (`true`). Default `false`. |

**Return value:** boolean

**Example**

```
MyDataTable.readXMLFile("D:\MyName\Public\xmltest.xml")
```

**See also:** Import File; XMLInterface; `writeXMLFile`

---

## readXMLString [SimTalk]

Imports the designated string, which contains valid XML syntax, into the list/table designated by `<Path>`.

**Remarks**

- Plant Simulation overwrites any existing data.

**Syntax**

```
<Path>.readXMLString(XML:string[, NoDebugger:boolean:=false]) → boolean
```

**Parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| `XML` | string | The text of the XML content. |
| `NoDebugger` (optional) | boolean | Whether the Debugger opens after unsuccessful access (`false`) or not (`true`). Default `false`. |

**Return value:** boolean

**See also:** Import File; `writeXMLFile`

---

## writeExcelFile [SimTalk]

Exports the contents of the list/table designated by `<Path>` to the designated Excel file.

**Remarks**

- Plant Simulation overwrites any existing content **and** the format of the Excel file.
- Uses Excel as a COM server (MS Excel must be installed). Use start option `-NativeExcel` for the previous interface.
- If a background color is defined in the Plant Simulation DataTable, it is written to the Excel file. Otherwise, an existing Excel file's background color is not altered.

**Syntax**

```
<Path>.writeExcelFile(FileName:string[, Sheet:string,
NoDebugger:boolean=false]) → boolean
```

**Parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| `FileName` | string | Excel file to export into. Extension must be `.xls`, `.xlsx`, `.xlsm`, or `.xlsb`; the extension determines the written format. |
| `Sheet` (optional) | string | The worksheet. If omitted, the list is saved with the worksheet name `Table1`. |
| `NoDebugger` (optional) | boolean | Whether the Method Debugger opens after unsuccessful access (`false`) or not (`true`). Default `false`. |

**Return value:** boolean

**Example**

```
MyDataStack.writeExcelFile("C:\users\nelly\factory_a.xls")
MyDataTable.writeExcelFile("C:\temp\factory_a.xls","Engines",true)
if MyDataList.writeExcelFile("C:\temp\data.xls")
   // data written successfully
else // take appropriate measures
end
```

**See also:** Export Excel File; Specifying Start Options, `-NativeExcel`; `readExcelFile`, `writeExcelXMLFile`

---

## writeExcelXMLFile [SimTalk]

Exports the contents of the list/table designated by `<Path>` to the designated Excel file in **Microsoft Excel Spreadsheet 2003** format.

**Remarks**

- Plant Simulation overwrites any existing content of the file.
- Unlike `writeExcelFile`, this method does **not** require a Microsoft Excel installation, so it is considerably faster.
- If a background color is defined in the Plant Simulation DataTable, it is written to the Excel file. Otherwise, an existing Excel file's background color is not altered.

**Syntax**

```
<Path>.writeExcelXMLFile(FileName:string[, Sheet:string,
NoDebugger:boolean:=false]) → boolean
```

**Parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| `FileName` | string | Excel file to export into. The file name must have the extension `.xml`. |
| `Sheet` (optional) | string | The worksheet. If omitted, the list is saved with the worksheet name `Table1`. |
| `NoDebugger` (optional) | boolean | Whether the Method Debugger opens after unsuccessful access (`false`) or not (`true`). Default `false`. |

**Return value:** boolean

**Example**

```
MyDataStack.writeExcelXMLFile("C:\users\nelly\factory_a.xml")
MyDataTable.writeExcelXMLFile("C:\temp\factory_a.xml","Engines",true)
if MyDataList.writeExcelXMLFile("C:\temp\data.xml")
   // data written successfully
else // take appropriate measures
end
```

**See also:** Export Excel File; `readExcelFile`, `writeExcelFile`

---

## writeFile [SimTalk] - lists

Exports the contents of the list/table designated by `<Path>` to the designated text file.

**Remarks**

- Plant Simulation overwrites any data that the file might already contain.

**Syntax**

```
<Path>.writeFile(FileName:string[, NoDebugger:boolean:=false,
CodePage:string:="UTF-8"]) → boolean
```

**Parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| `FileName` | string | Name of the text file to export into. |
| `NoDebugger` (optional) | boolean | Whether the Method Debugger opens after unsuccessful access (`false`) or not (`true`). Default `false`. |
| `CodePage` (optional) | string | Encoding: `"ANSI"` or `"System"`, `"UTF-8"`, or `"Unicode"`. Default `"ANSI"`. |

**Return value:** boolean

**Example**

```
MyDataStack.writeFile("C:\users\nelly\times.txt")
MyDataTable.writeFile("C:\temp\run1.txt")
if MyDataList.writeFile("C:\temp\data.txt", true)
   // data written successfully
else // take appropriate measures
end
```

**See also:** Export to File [lists]; `readFile` [lists]

---

## writeObjectFile [SimTalk]

Exports data of the list/table designated by `<Path>` to the designated file of type `.pslist`.

**Remarks**

- Plant Simulation overwrites any data that the file might already contain.

**Syntax**

```
<Path>.writeObjectFile(FileName:string[, NoDebugger:boolean:=false]) → boolean
```

**Parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| `FileName` | string | Name of the object file (`.pslist`) to export into. Saved to the current folder (see `setCurrentDirectory`) or to the folder passed as an absolute path. |
| `NoDebugger` (optional) | boolean | Whether the Method Debugger opens after unsuccessful access (`false`) or not (`true`). Default `false`. |

**Return value:** boolean

**Example**

```
MyDataStack.writeObjectFile("C:\users\johnE\times.pslist")
MyDataTable.writeObjectFile("C:\temp\run1.pslist")
if MyDataList.writeObjectFile("C:\temp\data.pslist", true)
   // data written successfully
else // take appropriate measures
end
```

**See also:** Export Object File; `readFile` [lists], `setCurrentDirectory`

---

## writeXMLFile [SimTalk]

Exports the contents of the list/table designated by `<Path>` to the designated XML file. Plant Simulation overwrites any data that the file might already contain.

**Remarks**

- When writing an XML file, Plant Simulation always uses its proprietary format.

**Syntax**

```
<Path>.writeXMLFile(FileName:string[, NoDebugger:boolean:=false]) → boolean
```

**Parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| `FileName` | string | Name of the XML file to export into. |
| `NoDebugger` (optional) | boolean | Whether the Debugger opens after unsuccessful access (`false`) or not (`true`). Default `false`. |

**Return value:** boolean

**Example**

```
MyDataTable.writeXMLFile("D:\MyName\Public\xmltest.xml")
```

**See also:** Export XML File; `readXMLFile`

---

## Methods for Indirectly Accessing Lists and Tables

Lists and tables also provide methods for **indirectly accessing** them. These methods only apply to ranges of data type **object** — the contents of the cells are references to objects whose attributes are to be processed.

To view all methods, read-only attributes, and attributes of an object, open the **Show Attributes and Methods** window (example shown for the object *Station*):

- Select **Show Attributes and Methods** on the context menu of the Class Library to show attributes/methods of the selected **Class**.
