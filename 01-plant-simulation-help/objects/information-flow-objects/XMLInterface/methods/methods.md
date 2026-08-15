# Methods of the XML Interface

The XML Interface provides:

- The methods listed in the table of contents.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance.

## Understanding the Syntax Line

An example syntax line:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature (identifier and data type of each parameter) is listed in parentheses. `(Parameter:string)` designates a parameter of data type string. Instead of a constant, you can use a variable or a method that returns the required type.

**Note:** Always enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets: `[,Parameter:boolean]`.
- If a parameter has a default value, the signature shows it after the parameter, e.g. `:= false`.
- If the method has a return value, the signature shows its data type after the arrow `->`, e.g. `→ boolean`.

---

## addAttribute [SimTalk]

Adds a new attribute to the XML file of the XMLInterface designated by `<Path>`. Applies when you sequentially access data.

**Type:** Method

**Syntax:**
```
<Path>.addAttribute(Name:string, Value:string) → boolean
```

**Parameters:**
- `Name` (string): the name of the attribute.
- `Value` (string): the value of the attribute.

**Return Value:** boolean

**Example:**
```simtalk
MyXMLInterface.addAttribute("xmlns", "myBooks")
MyXMLInterface.addAttribute("xmlns:aa", "specAth")
```

---

## close [SimTalk] — XML Interface

Closes the XML file of the XMLInterface designated by `<Path>`.

**Type:** Method

**Syntax:**
```
<Path>.close → boolean
```

**Return Value:** boolean

**Example:**
```simtalk
MyXMLInterface.filename := "C:\users\johnE\myfile.xml"
MyXMLInterface.openRead
MyXMLInterface.close
```

---

## closeChildren [SimTalk]

Closes the active level of the respective children and returns to the next higher level in the structure of the XMLInterface designated by `<Path>`. Applies when you randomly traverse data.

**Type:** Method

**Syntax:**
```
<Path>.closeChildren → boolean
```

**Return Value:** boolean

**Example:**
```simtalk
// This method selects the children of a node and prints name and value of
// each child. It will be started recursively for the selected child.
// Selects the children of the current node
MyXMLInterface.selectChildren
// this is the loop traversing the children
while MyXMLInterface.getNextNode = true 
   // prints the name and the value of each child
   print MyXMLInterface.getNodeName+ ": " + MyXMLInterface.getNodeValue
   // checks for children of this child
   VisitChildren
end
// returns to the parent node
MyXMLInterface.closeChildren
```

---

## deleteNodes [SimTalk]

Deletes all nodes that you selected with an XPath instruction in the XMLInterface designated by `<Path>`. Applies when you randomly access data.

**Type:** Method

**Syntax:**
```
<Path>.deleteNodes(Instruction:string) → boolean
```

**Parameter:**
- `Instruction` (string): the nodes selected with an XPath instruction.

**Return Value:** boolean

**Example:**
```simtalk
// delete all nodes specified by XPath instructions
MyXMLInterface.filename := "D:\MSXML 4.0\books.xml"
// load the XML document to be randomly accessed into RAM
MyXMLInterface.openDocument
// delete all 'book' nodes of genre 'Fantasy'
MyXMLInterface.deleteNodes("book[genre = 'Fantasy']")
MyXMLInterface.filename := "D:\MSXML 4.0\tmp.xml"
// write the document to a file
MyXMLInterface.write
// remove the document from RAM
MyXMLInterface.close
```

---

## endElement [SimTalk]

Terminates an item of the XMLInterface designated by `<Path>` that you started with the method `startElement`. Applies when you sequentially access data.

**Type:** Method

**Syntax:**
```
<Path>.endElement → boolean
```

**Return Value:** boolean

**Example:**
```simtalk
MyXMLInterface.endElement
```

---

## getAttributeName [SimTalk]

Returns the name of the attribute of the XMLInterface designated by `<Path>` at the designated position. Applies when you randomly traverse data.

**Type:** Method

**Syntax:**
```
<Path>.getAttributeName(Position:integer) → string
```

**Parameter:**
- `Position` (integer): the position of the attribute.

**Return Value:** string

**Example:**
```simtalk
MyXMLInterface.getAttributeName(i)+":" + MyXMLInterface.getAttributeValue(i)
```

---

## getAttributeValue [SimTalk]

Returns the value of the designated attribute of the XMLInterface designated by `<Path>`. Applies when you randomly traverse data.

**Type:** Method

**Syntax:**
```
<Path>.getAttributeValue(Parameter:any) → string
```

**Parameter:**
- `Parameter` (any): the attribute.

**Return Value:** string

**Example:**
```simtalk
MyXMLInterface.getAttributeName(i)+":" + MyXMLInterface.getAttributeValue(i)
```

---

## getContainer [SimTalk]

Returns a pre-formatted table that provides the container for accepting the data, which the XMLInterface designated by `<Path>` is to write. Applies when you randomly access data.

**Type:** Method

**Syntax:**
```
<Path>.getContainer(Depth:integer) → table
```

**Parameter:**
- `Depth` (integer): the depth of the data to be written.

**Return Value:** table

**Example:**
```simtalk
// insert new data into a XML document
var tbl:table
MyXMLInterface.filename := "D:\MSXML 4.0\books.xml"
// load the XML document
MyXMLInterface.openDocument
// get an Empty table to write the data to
// depth = 1 means that we want to write nodes with children
tbl := MyXMLInterface.getContainer(1)
// set the parent node for the new data
MyXMLInterface.setContext("/catalog")
// first the node to append to the 'catalog' nodes
tbl[1,1] := "book"
// then the attributes of the 'book' node
tbl.createNestedList(4,1)
// explicit namespace
tbl[4,1][1,1] := "xmlns:aa"
tbl[4,1][2,1] := "specAth"
// additional attributes
tbl[4,1][1,2] := "id"
tbl[4,1][2,2] := "bk113"
// child nodes
tbl.createNestedList(5,1)
tbl[5,1][1,1] := "aa:author"
tbl[5,1][2,1] := "specAth"
tbl[5,1][3,1] := "XYZ"
tbl[5,1][1,2] := "title"
tbl[5,1][3,2] := "UNKNOWN"
tbl[5,1][1,3] := "genre"
tbl[5,1][3,3] := "also"
tbl[5,1][1,4] := "price"
tbl[5,1][3,4] := "12,45"
tbl[5,1][1,5] := "publish_date"
tbl[5,1][3,5] := "12.1.02"
tbl[5,1][1,6] := "description"
tbl[5,1][3,6] := "xx0011"
MyXMLInterface.insertNodes(tbl)
// saves the changed document
MyXMLInterface.filename := "D:\MSXML 4.0\tmp.xml"
MyXMLInterface.write
// closes the document 
MyXMLInterface.close
```

---

## getNextNode [SimTalk]

Returns the next node after the one you selected with the method `selectChildren` located on the active level of the structure of the XMLInterface designated by `<Path>`. Applies when you randomly traverse data.

**Type:** Method

**Syntax:**
```
<Path>.getNextNode → boolean
```

**Return Value:** boolean

**Example:**
```simtalk
// select the children of a node and prints name and value of
// each child. It will be started recursively for the selected child.
// select the children of the current node
MyXMLInterface.selectChildren
// this is the loop traversing the children
while MyXMLInterface.getNextNode = true 
   // print the name and the value of each child
   print MyXMLInterface.getNodeName+ ": " + MyXMLInterface.getNodeValue
   // check for children of this child
   VisitChildren
end
// return to the parent node
MyXMLInterface.closeChildren
```

---

## getNodeName [SimTalk]

Returns the name of the node located on the active level of the structure of the XMLInterface designated by `<Path>`. Applies when you randomly traverse data.

**Type:** Method

**Syntax:**
```
<Path>.getNodeName → string
```

**Return Value:** string

**Example:**
```simtalk
print MyXMLInterface.getNodeName+ ": " + MyXMLInterface.getNodeValue
```

---

## getNodes [SimTalk]

Returns all nodes of the XPath instruction of the XMLInterface designated by `<Path>`. Applies when you randomly access data.

**Type:** Method

**Syntax:**
```
<Path>.getNodes(Instruction:string, NumberOfLevels:integer) → table
```

**Parameters:**
- `Instruction` (string): the name of the XPath instruction.
- `NumberOfLevels` (integer): the levels of the structure to which this applies.

**Return Value:** table

**Example:**
```simtalk
MyXMLInterface.getNodes("book[title='MidnightRain']",1)
```

---

## getNodeValue [SimTalk]

Returns the value of the node located on the active level of the structure of the XMLInterface designated by `<Path>`. Applies when you randomly traverse data.

**Type:** Method

**Syntax:**
```
<Path>.getNodeValue → string
```

**Return Value:** string

**Example:**
```simtalk
print MyXMLInterface.getNodeName+ ": " + MyXMLInterface.getNodeValue
```

---

## insertNodes [SimTalk]

Inserts the nodes contained in a table into the XMLInterface designated by `<Path>`. Applies when you randomly access data.

**Type:** Method

**Syntax:**
```
<Path>.insertNodes(NodesTable:list) → boolean
```

**Parameter:**
- `NodesTable` (list): the name of the table.

**Return Value:** boolean

**Example:**
```simtalk
MyXMLInterface.insertNodes(tbl)
```

---

## newDocument [SimTalk]

Creates a new, empty XML document in RAM into which you insert data for the XMLInterface designated by `<Path>`. Applies when you randomly access data.

**Type:** Method

**Syntax:**
```
<Path>.newDocument(Name:string) → boolean
```

**Parameter:**
- `Name` (string): the name of the new XML document.

**Return Value:** boolean

**Example:**
```simtalk
// create a new document using the method newDocument
var tbl:table
MyXMLInterface.newDocument("catalog")
tbl := MyXMLInterface.getContainer(1)
MyXMLInterface.setContext("/catalog")
// parent node
tbl[1,1] := "book"
// default namespace
tbl[2,1] := "MyBooks"
// attributes
tbl.createNestedList(4,1)
// explicit namespace
tbl[4,1][1,1] := "xmlns:aa"
tbl[4,1][2,1] := "specAth"
// additional attributes
tbl[4,1][1,2] := "id"
tbl[4,1][2,2] := "bk113"
// child nodes
tbl.createNestedList(5,1)
tbl[5,1][1,1] := "aa:author"
tbl[5,1][2,1] := "specAth"
tbl[5,1][3,1] := "XYZ"
tbl[5,1][1,2] := "title"
tbl[5,1][3,2] := "UNKNOWN"
tbl[5,1][1,3] := "genre"
tbl[5,1][3,3] := "also"
tbl[5,1][1,4] := "price"
tbl[5,1][3,4] := "12,45"
tbl[5,1][1,5] := "publish_date"
tbl[5,1][3,5] := "12.1.02"
tbl[5,1][1,6] := "description"
tbl[5,1][3,6] := "xx0011"
MyXMLInterface.insertNodes(tbl)
MyXMLInterface.filename := "D:\MSXML 4.0\tmp.xml"
MyXMLInterface.write
```

---

## openDocument [SimTalk]

Opens an XML file of the XMLInterface designated by `<Path>`, reads the data contained within, and places it into RAM. Applies when you randomly access data.

**Type:** Method

**Syntax:**
```
<Path>.openDocument → boolean
```

**Return Value:** boolean

**Example:**
```simtalk
// random access using XPath instructions
var tbl: table
MyXMLInterface.filename := "D:\MSXML 4.0\books.xml"
// load the XML document to be randomly accessed into RAM
MyXMLInterface.openDocument
// select nodes using an XPath instruction. Selection starts with
// the context node you entered into the MyXMLInterface.
// The second parameter defines the selection depth for each node
// 0 means no children. The result is passed to a table.
tbl := MyXMLInterface.getNodes("book[title='Midnight Rain']", 1)
MyXMLInterface.close
```

---

## openRead [SimTalk]

Opens the XML file, which you want to read sequentially of the XMLInterface designated by `<Path>`. Applies when you randomly access data.

The import method is called by the method `openRead` for all objects, which are contained in the XML file.

**Type:** Method

**Syntax:**
```
<Path>.openRead → boolean
```

**Return Value:** boolean

**Example:**
```simtalk
MyXMLInterface.filename := "C:\users\johnE\myfile.xml"
MyXMLInterface.openRead
MyXMLInterface.close
```

**See also:** Import Method [XML Interface]

---

## openWrite [SimTalk]

Opens the XML file, whose content you want to sequentially write to the XMLInterface designated by `<Path>`. Applies when you randomly access data.

**Note:** `openWrite` encodes the XML file in UTF-8 format. This enables the XML files to be treated as ASCII files provided only characters from the ASCII character set are used.

**Type:** Method

**Syntax:**
```
<Path>.openWrite → boolean
```

**Return Value:** boolean

**Example:**
```simtalk
MyXMLInterface.filename := "D:\MSXML 4.0\writeSequ.xml"
// opens the XML document for sequential writing
MyXMLInterface.openWrite
MyXMLInterface.startElement("catalog")
MyXMLInterface.startElement("book")
```

---

## remove [SimTalk] — XML Interface

Deletes the XML file of the XMLInterface designated by `<Path>`.

**Type:** Method

**Syntax:**
```
<Path>.remove → boolean
```

**Return Value:** boolean

**Example:**
```simtalk
MyXMLInterface.remove
```

**See also:** Delete File [XML Interface]

---

## selectChildren [SimTalk]

Selects all children of the active node of the XMLInterface designated by `<Path>`. Applies when you randomly traverse data.

**Type:** Method

**Syntax:**
```
<Path>.selectChildren → boolean
```

**Return Value:** boolean

**Example:**
```simtalk
// select the children of a node and print name and value of
// each child. It will be started recursively for the selected child.
// Select the children of the current node
MyXMLInterface.selectChildren
// this is the loop traversing the children
while MyXMLInterface.getNextNode = true 
// print the name and the value of each child
   print MyXMLInterface.getNodeName+ ": " + MyXMLInterface.getNodeValue
   // check for children of this node
   VisitChildren
end
// returns to the parent node
MyXMLInterface.closeChildren
```

---

## selectNodes [SimTalk]

Selects the designated nodes of the XPath instruction of the XMLInterface designated by `<Path>`. Applies when you randomly traverse data.

**Type:** Method

**Syntax:**
```
<Path>.selectNodes(Instruction:string) → boolean
```

**Parameter:**
- `Instruction` (string): the nodes of the XPath instruction.

**Return Value:** boolean

**Example:**
```simtalk
MyXMLInterface.selectNodes("book[genre = 'Computer']")
```

---

## setContext [SimTalk]

Sets the context of the XMLInterface designated by `<Path>`. Applies when you randomly access data.

By setting the context you can restrict the data to be read. As a rule you will enter a context if you do not need to work with all of the data contained in the XML file. If you do not specify a context, the XMLInterface imports the entire file, which may contain a large amount of data, some of which you do not need. This might take some time to import and use up a large amount of your computer's RAM.

**Type:** Method

**Syntax:**
```
<Path>.setContext(Node:string) → boolean
```

**Parameter:**
- `Node` (string): the node of the structure of the XML document at which the XMLInterface starts reading data.

**Return Value:** boolean

**Example:**
```simtalk
// create a new document by calling the methods openDocument and setContext
var tbl:table
// load no file
MyXMLInterface.filename := ""
MyXMLInterface.openDocument
// set the context to the root node
MyXMLInterface.setContext("/")
// set the document item
tbl := MyXMLInterface.getContainer(0)
tbl[1,1] := "catalog"
MyXMLInterface.insertNodes(tbl)
// set the context to the document item
MyXMLInterface.setContext("/catalog")
// returns a container for a subtree
tbl := MyXMLInterface.getContainer(1)
// parent node
tbl[1,1] := "book"
// default namespace
tbl[2,1] := "MyBooks"
// attributes
tbl.createNestedList(4,1)
// explicit namespace
tbl[4,1][1,1] := "xmlns:aa"
tbl[4,1][2,1] := "specAth"
// additional attributes
tbl[4,1][1,2] := "id"
tbl[4,1][2,2] := "bk113"
// child nodes
tbl.createNestedList(5,1)
tbl[5,1][1,1] := "aa:author"
tbl[5,1][2,1] := "specAth"
tbl[5,1][3,1] := "XYZ"
tbl[5,1][1,2] := "title"
tbl[5,1][3,2] := "UNKNOWN"
tbl[5,1][1,3] := "genre"
tbl[5,1][3,3] := "also"
tbl[5,1][1,4] := "price"
tbl[5,1][3,4] := "12,45"
tbl[5,1][1,5] := "publish_date"
tbl[5,1][3,5] := "12.1.02"
tbl[5,1][1,6] := "description"
tbl[5,1][3,6] := "xx0011"
MyXMLInterface.insertNodes(tbl) 
// set the filename to save the file with
MyXMLInterface.filename := "D:\MSXML 4.0\tmp.xml"
// write the document
MyXMLInterface.write
```

---

## startElement [SimTalk]

Designates the start of the designated item of the XMLInterface designated by `<Path>`. Applies when you randomly access data.

**Type:** Method

**Syntax:**
```
<Path>.startElement(Element:string) → boolean
```

**Parameter:**
- `Element` (string): the item.

**Return Value:** boolean

**Example:**
```simtalk
MyXMLInterface.startElement("catalog")
   MyXMLInterface.startElement("book")
```

---

## updateNodes [SimTalk]

Updates the nodes you selected with the method `getNodes` of the XMLInterface designated by `<Path>`, and writes them into a table. Applies when you randomly access data.

**Type:** Method

**Syntax:**
```
<Path>.updateNodes(NodesTable:list) → boolean
```

**Parameter:**
- `NodesTable` (table): the name of the table.

You can then manipulate the contents of the resulting table, and finally update the selected nodes.

**Return Value:** boolean

**Example:**
```simtalk
// update the selected nodes of the document
var tbl: table
MyXMLInterface.filename := "D:\MSXML 4.0\books.xml"
MyXMLInterface.openDocument
// select the nodes to be changed
tbl := MyXMLInterface.getNodes("/catalog/book[title='Midnight Rain']", 1)
// update the value
tbl[5,1][3,3] := "TEST"
// write the changed data
MyXMLInterface.updateNodes(tbl)
MyXMLInterface.filename := "D:\MSXML 4.0\tmp.xml"
MyXMLInterface.write
MyXMLInterface.close
```

**See also:** getNodes [SimTalk]

---

## write [SimTalk] — XML Interface

Writes the XML data of the XMLInterface designated by `<Path>` from your computer's RAM into a file on your hard drive.

**Type:** Method

**Syntax:**
```
<Path>.write → boolean
```

**Return Value:** boolean

**Example:**
```simtalk
// delete all nodes specified by XPath
MyXMLInterface.filename := "D:\MSXML 4.0\books.xml"
// load the XML document to be randomly accessed into memory
MyXMLInterface.openDocument
// delete all 'book' nodes of genre 'Fantasy'
MyXMLInterface.deleteNodes("book[genre = 'Fantasy']")
MyXMLInterface.filename := "D:\MSXML 4.0\tmp.xml"
// write the document to a file
MyXMLInterface.write
// remove the document from memory
MyXMLInterface.close
```

---

## writeElement [SimTalk]

Writes the item of the XMLInterface designated by `<Path>` and closes it at the same time. Applies when you sequentially access data.

**Type:** Method

**Syntax:**
```
<Path>.writeElement(Name:string, Value:string) → boolean
```

**Parameters:**
- `Name` (string): the name of the item.
- `Value` (string): the value of the item.

**Return Value:** boolean

**Example:**
```simtalk
// demonstrate how to sequentially write an XML file
MyXMLInterface.filename := "D:\MSXML 4.0\writeSequ.xml"
// open the XML document for sequential writing
MyXMLInterface.openWrite
MyXMLInterface.startElement("catalog")
     MyXMLInterface.startElement("book")
     // add attributes to the 'book' item'
     MyXMLInterface.addAttribute("id", "bk01")
     MyXMLInterface.addAttribute("xmlns", "myBooks")
     MyXMLInterface.addAttribute("xmlns:aa", "specAth")
// these are the children of the 'book' item
     MyXMLInterface.writeElement("aa:author", "Gambardella, Matthew")
           // add an attribute to the 'author' item
       MyXMLInterface.addAttribute("age", "16")
       MyXMLInterface.writeElement("title", "XML Developer's Guide")
       MyXMLInterface.writeElement("genre", "Computer")
           MyXMLInterface.writeElement("price", "44.95")
           MyXMLInterface.writeElement("publish_date", "2000-10-01")
           MyXMLInterface.writeElement("description", "An in-depth ...")
      // terminate the item 'book'
      MyXMLInterface.endElement
// terminate the item named 'catalog'
MyXMLInterface.endElement
MyXMLInterface.close
```

---

# Read-Only Attributes of the XMLInterface

The XMLInterface provides:

- The read-only attribute `GetNumberAttributes` [SimTalk].
- The Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value at the point-in-time at which you query it.

To query the value of a read-only attribute:

```simtalk
print MyXMLInterface.GetNumberAttributes
```
