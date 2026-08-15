# Attributes of the DropDownList

## Overview

The DropDownList provides:

- The attributes listed in the table of contents.
- The [Attributes of All Objects].

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows or by assigning values to the respective attributes.

To set the value of an attribute:

```simtalk
MyDropdownList.UseIcon := false
```

To get the value of an attribute:

```simtalk
print MyDropdownList.UseIcon
```

To query the value of a read-only attribute:

```simtalk
print MyDropDownList.UUID
```

---

## Control [SimTalk] - DropDownList

Sets the Control which the DropDownList designated by `<Path>` executes when you select an item in the DropDownList in the Frame.

**Remarks**

The anonymous identifiers `?` and `@` are set to the DropDownList when the method is called.

**Type**

Attribute

**Syntax**

```
<Path>.Control:string
```

**Assignment Value**

You can assign a value of data type `string`.

**Examples**

```simtalk
MyDropdownList.Control := "myControl"
```

```simtalk
switch ?.Value
case 1 
   print "Item 1 selected"
case 2 
   print "Item 2 selected"
end
```

**See also**

Control [DropDownList]

---

## Item [SimTalk] - DropDownList

Sets which Item in the DropDownList designated by `<Path>` will be selected using its name.

**Remarks**

If you localize the items, you will usually use the attribute `Value` instead of the attribute `Item`. The value is a number which is language-independent, while the Item is a string which differs from language to language.

**Type**

Attribute

**Syntax**

```
<Path>.Item:string
```

**Assignment Value**

You can assign a value of data type `string`.

**Example**

```simtalk
MyDropdownList.Item := "My item text 1"
```

**See also**

Items [button] - DropDownList

---

## Items [SimTalk] - DropDownList

Sets or gets the Items which the DropDownList designated by `<Path>` shows.

**Remarks**

- If you want to use the index number to access an item in the list, use the attribute `Value`.
- If you want to use the name to access an item in the list, use the attribute `Item`.

**Type**

Attribute

**Syntax**

```
<Path>.Items:array
```

**Assignment Value**

You can assign a value of data type `array`.

**Example**

```simtalk
var a : string[] := ["Item 1", "Item 2", "Item 1"]
MyDropdownList.Items := a
```

**See also**

Items [button] - DropDownList

---

## ObjectHeight [SimTalk] - DropDownList

Sets the Height of the Drop-Down List designated by `<Path>` with which it is shown in the Frame.

**Type**

Attribute

**Syntax**

```
<Path>.ObjectHeight:integer
```

**Assignment Value**

You can assign a value of data type `integer`.

**Example**

```simtalk
MyDropDownList.ObjectHeight := 1 // meter
```

**See also**

Height [text box] - DropDownList

---

## ObjectWidth [SimTalk] - DropDownList

Sets the Width of the DropDownList designated by `<Path>` with which it is shown in the Frame.

**Remarks**

If you enter long identifiers for the Items, you have to adjust the width so that the label fits on the DropDownList without the text being cut off.

**Type**

Attribute

**Syntax**

```
<Path>.ObjectWidth:integer
```

**Assignment Value**

You can assign a value of data type `integer`.

**Example**

```simtalk
MyDropDownList.ObjectWidth := 4 // meters
```

**See also**

Width [text box] - Button, Items [button] - DropDownList

---

## Value [SimTalk] - DropDownList

Sets which item in the DropDownList designated by `<Path>` will be selected. Plant Simulation uses the index number of the item to do so.

**Remarks**

If you localize the items to other languages, you will usually use the attribute `Value` instead of the attribute `Item`. The value is a number which is language-independent, while the Item is a string which differs from language to language.

**Type**

Attribute

**Syntax**

```
<Path>.Value:integer
```

**Assignment Value**

You can assign a value of data type `integer`.

**Example**

```simtalk
MyDropdownList.Value := 3
```

**See also**

Value [text box] - DropDownList
