# Methods of the Trigger

The Trigger provides:

- The methods listed in the table of contents to the left.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## Syntax line conventions

An example of the Syntax line of the individual methods might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. The expression `(Parameter:string)`, for example, designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. The expression `[,Parameter:boolean]`, for example, means that you can, but do not have to enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `→ boolean` in the example above.

---

## compute [SimTalk]

Generates a new value list for the Trigger designated by `<Path>` for the trigger type Combination.

**Remarks:** We advise to always call `compute` when the combination formula changed.

- **Type:** Method

**Syntax**

```
<Path>.compute
```

**Example**

```
MyTrigger.Formula := "K1 + K2 + K3"
MyTrigger.compute
```

**See also:** Trigger Type

---

## deleteTriggeredAttr [SimTalk]

Deletes the specified methods and attributes from the table **Triggered Attributes** of the Trigger designated by `<Path>`.

- **Type:** Method

**Syntax**

```
<Path>.deleteTriggeredAttr(Object:object, Attribute:string) -> boolean
```

**Parameters**

- The parameter `Object` of data type object designates the object.
- The parameter `Attribute` of data type string designates the attribute to be controlled.

**Return Value**

The return value has the data type boolean.

**Example**

```
MyTrigger.deleteTriggeredAttr(MyTrack,"pause")
```

**See also:** Attributes [Trigger], insertTriggeredAttr [SimTalk]

---

## deleteTriggeredMeth [SimTalk]

Deletes the specified Method from the list **Triggered Methods** of the Trigger designated by `<Path>`.

- **Type:** Method

**Syntax**

```
<Path>.deleteTriggeredMeth(Method:object) -> boolean
```

**Parameter**

The parameter `Method` of data type object designates the Method that is to be deleted.

**Return Value**

The return value has the data type boolean.

**Example**

```
MyTrigger.deleteTriggeredMeth(&shift1)
```

**See also:** Methods [Trigger], insertTriggeredMeth [SimTalk]

---

## insertTriggeredAttr [SimTalk]

Inserts the specified attribute of the specified object into the table **Triggered Attributes** of the Trigger designated by `<Path>`.

- **Type:** Method

**Syntax**

```
<Path>.insertTriggeredAttr(Object:object, Attribute:string)
```

**Parameters**

- The parameter `Object` of data type object designates the object.
- The parameter `Attribute` of data type string designates the attribute.

**Example**

```
MyTrigger.insertTriggeredAttr(MyTrack,"pause")
MyTrigger.insertTriggeredAttr(MyTrack,"length")
MyTrigger.insertTriggeredAttr(&MyVariable,"")
```

**See also:** Attributes [Trigger], deleteTriggeredAttr [SimTalk]

---

## insertTriggeredMeth [SimTalk]

Inserts the specified Method into the list **Triggered Methods** of the Trigger designated by `<Path>`.

- **Type:** Method

**Syntax**

```
<Path>.insertTriggeredMeth(Method:object)
```

**Parameter**

The parameter `Method` of data type object designates the Method that is to be inserted.

**Example**

```
MyTrigger.insertTriggeredMeth(&Shift3)
```

**See also:** Methods [Trigger], deleteTriggeredMeth [SimTalk]

---

# Read-Only Attributes of the Trigger

The Trigger provides:

- The read-only attribute `CurrentValue` [SimTalk].
- The Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```
print MyTrigger.CurrentValue
```
