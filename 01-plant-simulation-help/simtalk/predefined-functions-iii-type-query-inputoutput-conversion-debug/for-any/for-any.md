# Query the Data Type of a Variable of Data Type any

SimTalk provides the functions listed below for querying the data type of a variable of data type `Any`.

The function expects a parameter whose data type Plant Simulation compares.

See also: Any [SimTalk] - data type

## getSimTalkTypename [SimTalk]

Returns the name of the data type of an arbitrary value.

- **Type:** Function
- **Syntax:** `getSimTalkTypename(Value:any) → string`
- **Return Value:** For the data types `table`/`stack`/`queue` returns the strings `"table"`, `"stack"`, `"queue"`. For local variables of data type `any` assigned a special object (e.g. a sensor), it returns `sensor`, `lane`, `storage place`, `3D object`, or `3D animation` depending on the type of the special object. If the passed value has an `Array` data type, returns `array`.

### Example

```simtalk
print getSimTalkTypename(Conveyor.sensorID(1))  // sensor
print getSimTalkTypename(Conveyor._3D)          // 3D object
print getSimTalkTypename(TwoLaneTrack.A)        // lane
print getSimTalkTypename(Store[1,1])            // storage place

// compute the character count
param value: any -> integer
switch getSimTalkTypename(value)
case "integer"
   if value > 0
      return log10(value) + 1
   elseif value < 0
      return log10(-value) + 2
   else
      return 1;
   end
case "string"
   return strlen(value)
case "object"
   return strlen(obj_to_str(value))
case "boolean"
   return when value then /*true*/4 else /*false*/5
else
   return -1  // error
end
```

## isAcceleration [SimTalk]

Returns if the designated argument is of data type Acceleration (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isAcceleration(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isAcceleration(arg)
   print "acceleration = ", arg
end
```

## isArray [SimTalk]

Returns if the designated argument has an Array data type (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isArray(Argument:Value) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
var a:any[] := [[1,2,3], 42]
print "a = ", a
print "a[1] = ", a[1]
print "a[2] = ", a[2]
print isArray(a)    // true
print isArray(a[1]) // true
print isArray(a[2]) // false
var j:json
j["a"] := [1,2,3]
print isArray(j["a"])  -- returns true
```

## isBoolean [SimTalk]

Returns if the designated argument is of data type Boolean (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isBoolean(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isBoolean(arg)
   print "Boolean = ", arg
end
```

## isDate [SimTalk]

Returns if the designated argument is of data type Date (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isDate(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isDate(arg)
   print "Date = ", arg
end
```

## isDatetime [SimTalk]

Returns if the argument designated is of data type DateTime (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isDatetime(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isDatetime(arg)
   print "Datetime = ", arg
end
```

## isInteger [SimTalk]

Returns if the designated argument is of data type Integer (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isInteger(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isInteger(arg)
   print "Integer = ", arg
end
```

## isJson [SimTalk]

Returns if the designated argument is of data type JSON (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isJson(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isJson(arg)
   print "json = ", arg
end
```

## isLength [SimTalk]

Returns if the designated argument is of data type Length (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isLength(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isLength(arg)
   print "Length = ", arg
end
```

## isList [SimTalk]

Returns if the designated argument is of data type List (`true`) or not (`false`).

- **Syntax:** `isList(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Note

The value `VOID` does not have a data type as local variables of data types `object`, `table`, and `list` can all take the value `void`. For this reason a local variable of data type `any` does not take a data type when you assign `void` to it.

### Example

```simtalk
var a: any := void
print isObject(a)  // prints false
print a = void     // prints true
var b : any := 123
print b = void     // prints false
```

## isListRange [SimTalk]

Returns if the designated argument is a list range (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isListRange(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isListRange(arg)           // something like {1,1}..{2,*}
   print "listRange = ", arg  // prints listRange = {1,1}..{2,*}
end
```

## isObject [SimTalk]

Returns if the designated argument is of data type Object (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isObject(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Note

For `isObject`, `isTable`, and `isList` this applies: The value `VOID` does not have a data type as local variables of data types `object`, `table`, and `list` can all take the value `void`. For this reason a local variable of data type `any` does not take a data type when you assign `void` to it. If the function `isObject` is called with such a variable, the function returns the result `false`.

### Example

```simtalk
var a: any := void
print isObject(a)  // prints false
print a = void     // prints true
var b : any := 123
print b = void     // prints false
```

## isQueue [SimTalk]

Returns if the designated argument is of data type Queue (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isQueue(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isQueue(arg)
   print "Queue = ", arg
end
```

## isReal [SimTalk]

Returns if the designated argument is of data type Real (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isReal(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isReal(arg)
   print "Real = ", arg
end
```

## isSpeed [SimTalk]

Returns if the designated argument is of data type Speed (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isSpeed(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isSpeed(arg)
   print "Speed = ", arg
end
```

## isStack [SimTalk]

Returns if the designated argument is of data type Stack (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isStack(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isStack(arg)
   print "Stack = ", arg
end
```

## isString [SimTalk]

Returns if the designated argument is of data type String (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isString(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isString(arg)
   print "String = ", arg
end
```

## isTable [SimTalk]

Returns if the designated argument is of data type Table (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isTable(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Note

The value `VOID` does not have a data type as local variables of data types `object`, `table`, and `list` can all take the value `void`. For this reason a local variable of data type `any` does not take a data type when you assign `void` to it.

### Example

```simtalk
param arg: any
if isTable(arg)
   print "Table = ", arg
end
```

## isTime [SimTalk]

Returns if the designated argument is of data type Time (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isTime(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isTime(arg)
   print "Time = ", arg
end
```

## isWeight [SimTalk]

Returns if the designated argument is of data type Weight (`true`) or not (`false`).

- **Type:** Function
- **Syntax:** `isWeight(Argument:any) → boolean`
- **Parameter:** `Argument` of data type `any` designates the argument to be checked.
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
param arg: any
if isWeight(arg)
   print "Weight = ", arg
end
```
