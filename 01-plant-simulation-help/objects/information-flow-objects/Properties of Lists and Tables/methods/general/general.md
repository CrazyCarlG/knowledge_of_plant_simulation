# Methods of Lists and Tables

The lists and tables share a number of methods. The different kinds — `DataStack`, `DataQueue`, `DataList`, `DataTable`, and `TimeSequence` — additionally provide object-specific methods.

To view all of the methods, read-only attributes, and attributes of an object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the attributes and methods of the selected Class.
- Press the **F8** key, or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show the attributes and methods of the selected Instance.

## Reading a Method Signature (Syntax Line)

An example of the Syntax line of an individual method:

```
<Path>.readFile(FileName:string[, NoDebugger:boolean:=false,
CodePage:string:="ANSI"]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method — the identifier and the data type of each parameter — is listed in parentheses. For example, `(Parameter:string)` designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.
- Optional parameters are listed within brackets. For example, `[,Parameter:boolean]` means you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter.
- If the method has a return value, the signature shows its data type after the arrow `->`.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

## Signature Abbreviations

| Argument | Data type | Range of values |
|---|---|---|
| integer | integer | integer greater than zero |
| any | all data types | depending on the data type |
| listrange | — | a range |
| direction | string | `"up"`, `"down"`, `" "` |
| attributes | string | name of an attribute |

## See also

- _Methods for Accessing Lists and Tables
- _Methods for the Order of Cells within Lists and Tables
- _Methods for the Format of Lists and Tables
- _Methods for Querying Statistics Values of Lists and Tables
- _Methods for Importing and Exporting Data in Text Format
- Instantiating Local Lists and Tables
- _Methods for Indirectly Accessing Lists and Tables
- Methods of the DataTable
- _Methods of the DataList
- _Methods of DataQueue and DataStack

## Methods for Accessing Lists and Tables

Lists and tables provide the methods listed in the table of contents (to the left) for accessing them. Read and write access depend on the object class and are described in the sub-chapters.

To view all of the methods, read-only attributes, and attributes of an object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the attributes and methods of the selected Class.
- Press the **F8** key, or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show the attributes and methods of the selected Instance.
