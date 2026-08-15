# DataStack — Methods

## Methods

The DataStack provides the following methods:

- `createNestedList [SimTalk]` — DataQueue
- `pop [SimTalk]` — DataStack
- `push [SimTalk]` — Stack
- `pushList [SimTalk]`
- `top [SimTalk]`

In addition, it inherits:

- The Methods of Lists and Tables.
- The Methods of All Objects.

> To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.
>
> - Select **Show Attributes and Methods** on the context menu of the Class Library to show the attributes and methods of the selected *Class*.
> - Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the attributes and methods of the selected *Instance*.

## Syntax conventions

An example of the Syntax line of an individual method:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. For example, `(Parameter:string)` designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.
- Optional parameters are listed within brackets. For example, `[,Parameter:boolean]` means you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter.
- If the method has a return value, the signature shows its data type after the arrow `->`.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

### Abbreviations used in signatures

| Argument | Data type | Range of values |
|---|---|---|
| `integer` | integer | integer greater than zero |
| `any` | all data types | depending on the data type |
| `listrange` | — | a range |
| `direction` | string | `"up"`, `"down"`, `" "` |
| `attributes` | string | name of an attribute |

## Read-Only Attributes of DataQueue and DataStack

The DataStack and the DataQueue provide:

- The Read-Only Attributes of Lists and Tables.
- The Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (for example, on the **Statistics** tab).

Example of querying a read-only attribute:

```
print MyDataStack.Full
```

## Attributes of DataQueue and DataStack

The DataStack and the DataQueue provide:

- The Attributes of Lists and Tables.
- The Attributes of All Objects.

---

*Plant Simulation Help — Methods of the DataStack*
