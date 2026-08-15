# Functions for Converting Data Types

SimTalk provides these functions for converting data types:

- Converting Numerical Values
- Converting Physical Data Types
- Converting Physical Data Types with Units into Data Types without Units
- Converting Values without Units into Physical Data Types with Units
- Converting References
- Converting Time and Date Values
- Converting Arrays

> **Note:** You can use the function `to_str` to convert any value to a string.

---

## Converting Numerical Values

### bool_to_num

Converts the specified boolean value into a number of data type `integer`.

- **Type:** Function
- **Syntax:** `bool_to_num(Value:boolean) → integer`
- **Parameter:** `Value` has the data type `boolean`.
- **Return Value:** data type `integer` — `true` returns `1`, `false` returns `0`.

```simtalk
var gross: real
var inclVAT: boolean
print bool_to_num(true)
print "Price:"
print gross + 0.16*gross*bool_to_num(inclVAT)
```

### bool_to_str

Converts the specified boolean value into a string.

- **Type:** Function
- **Syntax:** `bool_to_str(Value:boolean) → string`
- **Parameter:** `Value` has the data type `boolean`.
- **Return Value:** data type `string`.

```simtalk
var s: string
var b: boolean
s := bool_to_str(b)
```

### num_to_bool

Converts the specified number into a boolean value.

- **Type:** Function
- **Syntax:** `num_to_bool(Value:real) → boolean`
- **Parameter:** `Value` has the data type `real`.
- **Return Value:** data type `boolean` — `true` if the parameter is not zero, `false` if the parameter is zero.

```simtalk
var s: stack[boolean]
var number: real
stack.create
stack.insert(num_to_bool(number))
```

### num_to_hex

Converts the specified integer number into a string value.

> **Remarks:** `num_to_hex` only shows the integer value as a hexadecimal value.

- **Type:** Function
- **Syntax:** `num_to_hex(Value:integer[, Is64Bit:boolean:=false]) → string`
- **Parameters:**
  - `Value` (integer) — the value to convert.
  - `Is64Bit` (boolean, optional) — `true` creates a 64-Bit hexadecimal number, `false` a 32-Bit hexadecimal number. To remain compatible with previous versions, it creates a 32-Bit hexadecimal number if you do not specify the parameter. **Default value:** `false`.
- **Return Value:** data type `string`.

```simtalk
print num_to_hex(-1)                // "ffffffff"
print num_to_hex(-1, true)          // "ffffffffffffffff"
print num_to_hex(2343432205, true)  // "8badf00d"
```

### num_to_str

Converts the specified real number into a string.

- **Type:** Function
- **Syntax:** `num_to_str(Number:real[, Precision:integer, Width:integer]) → string`
- **Parameters:**
  - `Number` (real) — the number to convert.
  - `Precision` (integer, optional) — for numerical data types, the number of significant digits the resulting string has at most. If `Number` is `integer` or `time`, `Precision` has no function. A negative value uses its absolute number as the desired number of decimal places.
  - `Width` (integer, optional) — the desired number of characters. If not reached, Plant Simulation adds zeros (`0`) at the start of the string.
- **Return Value:** data type `string`.

```simtalk
print num_to_str(3, 0, 4)    // returns 0003
print num_to_str(pi, -2, 6)  // returns 003.14
```

### str_to_bool

Converts the specified string into a value of data type `boolean`.

> **Remarks:** The spelling of the string is not case-sensitive.

- **Type:** Function
- **Syntax:** `str_to_bool(Value:string) → boolean`
- **Parameter:** `Value` has the data type `string`.
- **Return Value:** data type `boolean` — `true` if the value `true` was passed, `false` for any other value.

```simtalk
table[1,1] := str_to_bool("true")
```

### str_to_num

Converts the specified string value into a floating-point value of data type `real`.

> **Remarks:** Apart from digits the string can optionally contain leading white spaces, a sign, a decimal point and an `e` (lower case) or `E` (upper case) for the exponent. If the string begins with `0x`, the following string is interpreted as a hexadecimal integer number. If the string contains an invalid character, the function only converts all preceding characters into a number.

- **Type:** Function
- **Syntax:** `str_to_num(Value:string) → real`
- **Parameter:** `Value` (string) — the data to convert.
- **Return Value:** data type `real`.

```simtalk
x := str_to_num("   -7")              // minus seven
y := str_to_num("3.141xyz")           // 3.141
w := str_to_num("-1e6")               // minus one million
var n: integer := str_to_num("0x10a") // hexadecimal number 10a
print n                               // outputs 266
```

### time_to_str

Converts the specified time value into a string.

- **Type:** Function
- **Syntax:** `time_to_str(Value:time[, FormatLikeDialogs:boolean]) → string`
- **Parameters:**
  - `Time` (time) — the time to convert.
  - `FormatLikeDialogs` (boolean, optional) — `true` uses the same time format as in text boxes of the dialogs. If omitted or `false`, Plant Simulation uses the same time format as in tables (four decimal places).
- **Return Value:** data type `string`.

```simtalk
var t: time
t := 60
Dialog.setCaption("myProcTime", time_to_str(t, true))
```

### to_str

Converts all of the specified parameters into a string each, concatenates the resulting strings into a single string, and returns it.

- **Type:** Function
- **Syntax:** `to_str(Parameter1:any[, Parameter2:any, …]) → string`
- **Parameters:** parameters have data type `any`.
- **Return Value:** data type `string`.

```simtalk
var s: string
var x: real
s := to_str(true)                     // assigns "true"
x := 1.5
s := to_str("length: ", x, " meters") // assigns "length: 1.5 meters"
var a : real[]
var s : string := to_str(a)  // s := "[ ]"
var a : string["Kent, Clark", ""]
var s : string := to_str(a)  -- assigns ["Kent, Clark", ""]
```

---

## Converting Physical Data Types

SimTalk provides the following functions for converting strings to physical data types. You can also enter a unit which the function then uses.

### str_to_acceleration

Converts the specified data into a number of data type `acceleration`.

> **Remarks:** You can specify one of these units: `"mm/s²"`, `"cm/s²"`, `"m/s²"`, `"km/h²"`, `"m/min²"`, `"in/s²"`, `"ft/s²"`, or `"yd/s²"`. If you do not specify a unit, Plant Simulation outputs the acceleration according to the settings under **File > Model Settings/Preferences > Units > Acceleration**.

- **Type:** Function
- **Syntax:** `str_to_acceleration(Data:string) → acceleration`
- **Parameter:** `Data` (string) — the data to convert.
- **Return Value:** data type `acceleration`.

```simtalk
// reads values in dialog box
var entry: string
entry := dialog.getValue("acceleration")
print str_to_acceleration(entry)
str_to_acceleration("20")
// interprets 20 according to the acceleration setting you selected under Preferences
str_to_length("20m/ss")
// interprets 20 as meters per square second
```

### str_to_length

Converts the specified data into a number of data type `length`.

> **Remarks:** You can specify one of these units: `"mm"`, `"m"`, `"cm"`, `"km"`, `"in"`, `"ft"`, `"yd"`, or `"mi"`. If you do not specify a unit, Plant Simulation outputs the length according to the settings under **File > Model Settings/Preferences > Units > Length**.

- **Type:** Function
- **Syntax:** `str_to_length(Data:string) → length`
- **Parameter:** `Data` (string) — the data to convert.
- **Return Value:** data type `length`.

```simtalk
// reads the values in the dialog box
var entry: string
entry := dialog.getValue("length")
print str_to_length(entry)
entry := dialog.getValue("width")
print str_to_length(entry)
str_to_length("1.23")
// interprets 1.23 according to the length setting you selected under Preferences
str_to_length("1.23ft")
// interprets 1.23 as feet
```

### str_to_speed

Converts the specified data into a number of data type `speed`.

> **Remarks:** You can specify one of these units: `"mm/s"`, `"cm/s"`, `"m/s"`, `"km/h"`, `"m/min"`, `"in/s"`, `"ft/s"`, `"yd/s"`, or `"mph"`. If you do not specify a unit, Plant Simulation outputs the speed according to the settings under **File > Model Settings/Preferences > Units > Speed**.

- **Type:** Function
- **Syntax:** `str_to_speed(Data:string) → speed`
- **Parameter:** `Data` (string) — the data to convert.
- **Return Value:** data type `speed`.

```simtalk
// reads values in dialog box
var entry : string
entry := dialog.getValue("move forward")
print str_to_speed(entry)
str_to_speed("10")
// interprets 10 according to the speed setting you selected under Preferences
str_to_speed("10m/ss")
// interprets 10 as meters per square second
```

### str_to_weight

Converts the specified data into a number of data type `weight`.

> **Remarks:** You can specify one of these units: `"g"`, `"kg"`, `"t"`, `"lb"`, or `"oz"`. If you do not specify a unit, Plant Simulation outputs the weight according to the settings under **File > Model Settings/Preferences > Units > Mass**.

- **Type:** Function
- **Syntax:** `str_to_weight(Data:string) → weight`
- **Parameter:** `Data` (string) — the data to convert.
- **Return Value:** data type `weight`.

```simtalk
// reads values in dialog box
var entry: string
entry := dialog.getValue("net")
print str_to_weight(entry)
entry := dialog.getValue("gross")
print str_to_weight(entry)
str_to_weight("10")
// interprets 10 according to the mass setting you selected under Preferences
str_to_weight("10kg")
// interprets 10 as kilograms
```

---

## Converting Physical Data Types with Units into Data Types without Units

SimTalk provides the following functions for converting physical data types with units into data types without units. This is especially handy if you want to assign incompatible physical data types, which would normally output a warning to the Console.

```simtalk
var w: weight
// assign a time to a weight without showing a warning
w := time_to_num(EventController.simTime)
```

### acceleration_to_num

Converts the specified acceleration into a value without a unit.

> **Remarks:** Handy if you want to assign a local variable to another local variable which has a different unit. Normally this is forbidden. Using `acceleration_to_num` you can discard the unit.

- **Type:** Function
- **Syntax:** `acceleration_to_num(Value:acceleration[, Unit:string="m/s²"]) → real`
- **Parameters:**
  - `Data` (acceleration) — the value to convert.
  - `Unit` (string, optional) — the physical unit to use; one of `"mm/s²"`, `"cm/s²"`, `"m/s²"`, `"km/h²"`, `"m/min²"`, `"in/s²"`, `"ft/s²"`, or `"yd/s²"`. **Default value:** `"m/s²"`.
- **Return Value:** data type `real`.

```simtalk
var t: time, a: acceleration
t := acceleration_to_num(a)
```

### length_to_num

Converts the specified length into a value without a unit.

- **Type:** Function
- **Syntax:** `length_to_num(Data:length[, Unit:string="m"]) → real`
- **Parameters:**
  - `Data` (length) — the value to convert.
  - `Unit` (string, optional) — one of `"mm"`, `"cm"`, `"m"`, `"km"`, `"in"`, `"ft"`, `"yd"`, or `"mi"`. **Default value:** `"m"`.
- **Return Value:** data type `real`.

```simtalk
var t: time, le: length
t := length_to_num(le)
Conveyor.Length = 2yd
print length_to_num(Conveyor.Length, "ft") // 6
```

### speed_to_num

Converts the specified speed into a value without a unit.

- **Type:** Function
- **Syntax:** `speed_to_num(Data:speed[, Unit:string="m/s"]) → real`
- **Parameters:**
  - `Data` (speed) — the value to convert.
  - `Unit` (string, optional) — one of `"mm/s"`, `"cm/s"`, `"m/s"`, `"km/h"`, `"m/min"`, `"in/s"`, `"ft/s"`, `"yd/s"`, or `"mph"`. **Default value:** `"m/s"`.
- **Return Value:** data type `real`.

```simtalk
var t: time, s: speed
t := speed_to_num(s)
```

### time_to_num

Converts the specified time into a value without a unit.

- **Type:** Function
- **Syntax:** `time_to_num(Data:time) → real`
- **Parameter:** `Data` (time) — the value to convert.
- **Return Value:** data type `real`.

```simtalk
var w: weight, t: time
w := time_to_num(t)
```

### weight_to_num

Converts the specified weight into a value without a unit.

- **Type:** Function
- **Syntax:** `weight_to_num(Data:weight[, Unit:string="kg"]) → real`
- **Parameters:**
  - `Data` (weight) — the value to convert.
  - `Unit` (string, optional) — one of `"g"`, `"kg"`, `"t"`, `"lb"`, or `"oz"`. **Default value:** `"kg"`.
- **Return Value:** data type `real`.

```simtalk
var t: time, w: weight
t := weight_to_num(w)
```

---

## Converting Values without Units into Physical Data Types with Units

SimTalk provides the following functions for converting a value of data type `real` or `integer` into a value with a physical unit.

### num_to_acceleration

Converts a specified number without a unit into a value of data type `acceleration`.

- **Type:** Function
- **Syntax:** `num_to_acceleration(Number:real[, Unit:string="m/s²"]) → acceleration`
- **Parameters:**
  - `Number` (real) — the number to convert.
  - `Unit` (string, optional) — one of `"mm/s²"`, `"cm/s²"`, `"m/s²"`, `"km/h²"`, `"m/min²"`, `"in/s²"`, `"ft/s²"`, or `"yd/s²"`. **Default value:** `"m/s²"`.
- **Return Value:** data type `acceleration`.

```simtalk
var s: speed
s := num_to_acceleration(3.7) * Conveyor3.Time
```

### num_to_length

Converts the specified number without a unit into a value of data type `length`.

- **Type:** Function
- **Syntax:** `num_to_length(Number:real[, Unit:string="m"]) → length`
- **Parameters:**
  - `Number` (real) — the number to convert.
  - `Unit` (string, optional) — one of `"mm"`, `"cm"`, `"m"`, `"km"`, `"in"`, `"ft"`, `"yd"`, or `"mi"`. **Default value:** `"m"`.
- **Return Value:** data type `length`.

```simtalk
// Set conveyor length to 1 ft:
Conveyor.Length = 1ft
Conveyor.Length = num_to_length(1, "ft")
```

### num_to_speed

Converts the specified number without a unit into a value of data type `speed`.

- **Type:** Function
- **Syntax:** `num_to_speed(Number:real[, Unit:string="m/s"]) → speed`
- **Parameters:**
  - `Number` (real) — the number to convert.
  - `Unit` (string, optional) — one of `"mm/s"`, `"cm/s"`, `"m/s"`, `"km/h"`, `"m/min"`, `"in/s"`, `"ft/s"`, `"yd/s"`, or `"mph"`. **Default value:** `"m/s"`.
- **Return Value:** data type `speed`.

```simtalk
var a: speed
a := num_to_speed(4.1, "m/s")
```

### num_to_time

Converts the specified number without a unit into a value of data type `time`.

- **Type:** Function
- **Syntax:** `num_to_time(Number:real) → time`
- **Parameter:** `Number` (real) — the number to convert.
- **Return Value:** data type `time`.

```simtalk
var s: speed
s := Track.length / num_to_time(30)
```

### num_to_weight

Converts the specified number without a unit into a value of data type `weight`.

- **Type:** Function
- **Syntax:** `num_to_weight(Number:real[, Unit:string="kg"]) → weight`
- **Parameters:**
  - `Number` (real) — the number to convert.
  - `Unit` (string, optional) — one of `"g"`, `"kg"`, `"t"`, `"lb"`, or `"oz"`. **Default value:** `"kg"`.
- **Return Value:** data type `weight`.

```simtalk
var w: weight
w := num_to_weight(Track4.Length)
```

---

## Converting References

SimTalk provides the following functions for converting references.

### obj_to_str

Converts the path and the name of the designated object to a value of data type `string`.

- **Type:** Function
- **Syntax:** `obj_to_str(obj:object[, MakeAbsolute:boolean:=true]) → string`
- **Parameters:**
  - `obj` (object) — the path of the object to be returned as string.
  - `MakeAbsolute` (boolean, optional) — `true` always returns the absolute path (behavior of previous versions; the default). If `false`, the function returns the actual path set in the first parameter, which can be a relative path. **Default value:** `true`.
- **Return Value:** data type `string`.

```simtalk
var o1, o2 : object
var s : string
o1 := "Station.Cont.~"
s := obj_to_str(o1)         // ".Models.Model.Station"
s := obj_to_str(o1, false)  // "Station.Cont.~"
o2 := "Station.OnEntrance"  // path to a user-defined attribute of data type method
s := obj_to_str(o2)         // "VOID"
s := obj_to_str(o2, false)  // "Station.OnEntrance"
```

### str_to_method

Checks if the path designated by the parameter `path` references an object of type `Method` or a user-defined attribute of data type `method`.

> **Remarks:** If the path is a relative path (for example `"self.OnEntrance"`), you can specify in the parameter at which object the path evaluation is to start. Use `str_to_method` to access a control that is entered into an object.

- **Type:** Function
- **Syntax:** `str_to_method(Path:any[, Context:object]) → object/method`
- **Parameters:**
  - `Path` (any) — the path to evaluate. Can be of data type `string` or `object`. This is useful to evaluate a path from an attribute of an object (e.g., the exit control `ExitCtrl`) without converting to string first.
  - `Context` (object, optional) — if a relative path is specified as `Path`, the path evaluation starts in this object instead of the surrounding Frame of the method containing the `str_to_method` statement. When the relative path starts with `self`, `self` is replaced with the second parameter. If it does not start with `self`, the path evaluation starts with the surrounding Frame of the second parameter, unless the specified object itself is a Frame.
- **Return Value:** data type `object` or `method` — the reference to the respective Method, otherwise `VOID`.

```simtalk
str_to_method(Station.ExitCtrl, Station).Program
// returns the source code of the exit control
str_to_method(Station.ExitCtrl, Station).execute
// executes the entered exit control
```

### str_to_obj

Converts the text, which designates an absolute or a relative path to an object, into an object.

> **Remarks:** The string must designate an object, not a user-defined attribute. To resolve a path to a user-defined table or method attribute, use `str_to_table` or `str_to_method` respectively.

- **Type:** Function
- **Syntax:** `str_to_obj(Text:string) → object`
- **Parameter:** `Text` (string) — the text to convert.
- **Return Value:** data type `object` — `void` if the passed string does not designate an object.

```simtalk
var o: object := str_to_obj(".Method")
```

### str_to_table

Checks if the path designated by the parameter `path` references a user-defined attribute of data type `table`, `list`, `stack`, or `queue`.

- **Syntax:** `str_to_table(Path:string/object[, Context:object]) → object/table/list/stack/queue`
- **Parameters:**
  - `Path` (string or object) — the path to evaluate.
  - `Context` (object, optional) — same relative-path behavior as `str_to_method`.
- **Return Value:**
  - data type `object` if the path points to a table or a list in the Frame.
  - data type `table`, `list`, `stack`, or `queue` if the path points to a subtable, sublist, or a user-defined attribute of data type `table` or `list`.
  - `VOID` if the path does not point to an object or user-defined attribute, or if it is not of data type `table` or `list`.

```simtalk
// returns the user-defined attribute of data type table of the Station
var anyVar:any := str_to_table(ListTypeTable, Station)
print anyVar
print getSimTalkTypename(anyVar)
```

---

## Converting Time and Date Values

SimTalk provides the following functions for converting date and time values.

### datetime_to_str

Converts a specified value according to the format string in the string to a value of data type `string`.

> **Remarks:** If you do not specify a format string, the result is the same as for the function `to_str`.

- **Type:** Function
- **Syntax:** `datetime_to_str(Value:datetime[, Format:string])`
- **Parameters:**
  - `Value` (datetime) — the value containing the date and time to convert.
  - `Format` (string) — the format string. It recognizes these special meanings:

    | Code | Meaning |
    |------|---------|
    | `%d` | Day of month as decimal number (01 – 31) |
    | `%m` | Month as decimal number (01 – 12) |
    | `%y` | Year without century, as decimal number (00 – 99) |
    | `%Y` | Year with century, as decimal number |
    | `%H` | Hour in 24-hour format (00 – 23) |
    | `%h` | Hour in 12-hour format (01 – 12) |
    | `%M` | Minute as decimal number (00 – 59) |
    | `%S` | Second as decimal number (00 – 59) |
    | `%s` | Second as real number (00.0000 – 59.9999) |
    | `%p` | a.m./p.m. indicator for 12-hour format |
    | `%P` | AM/PM indicator for 12-hour format |
    | `%x` | Date representation for current locale |
    | `%X` | Time representation for current locale |

```simtalk
print datetime_to_str(str_to_datetime("2026/03/20 0:43:22"), "%d.%m.%y %H:%M:%S")
-- 20.03.26 00:43:22
print datetime_to_str(str_to_datetime("2026/03/20 0:43:22"), "Date: %d.%m.%y Time: %H:%M:%S")
-- Date: 20.03.26 Time: 00:43:22
print datetime_to_str(str_to_datetime("2026/01/31 13:10:23"), "%Y/%m/%d %h:%M:%S %p")
-- 2026/01/31 01:10:23 p.m.
```

### isValidDateString

Returns if the passed value contains a valid date or not.

- **Type:** Function
- **Syntax:** `isValidDateString(Date:string) → boolean`
- **Parameter:** `Date` (string) — the value to check. The year can be two or four digits. The function takes leap years into account. Accepted formats: `"YYYY/MM/DD"`, `"YYYY-MM-DD"`, and `"DD.MM.YYYY"`.
- **Return Value:** data type `boolean`.

```simtalk
print isValidDateString("2024/02/10")
print isValidDateString("2024-02-10")
print isValidDateString("10.02.2024")
```

### isValidDateTimeString

Returns if the passed value contains a valid date and time or not.

- **Type:** Function
- **Syntax:** `isValidDateTimeString(DateAndTime:string) → boolean`
- **Parameter:** `DateAndTime` (string) — the value to check. The year can be two or four digits. The function takes leap years into account. Accepted formats: `"YYYY/MM/DD HH:MM:SS.s"`, `"YYYY-MM-DD HH:MM:SS.s"`, and `"DD.MM.YYYY HH:MM:SS.s"`. You can replace the space between date and time with the letter `T`.
- **Return Value:** data type `boolean`.

```simtalk
print isValidDateTimeString("2024/02/10 14:00:00.00")
print isValidDateTimeString("2024-02-10 14:00:00.00")
print isValidDateTimeString("10.02.2024 14:00:00.00")
print isValidDateTimeString("10.02.2024T14:00:00.00")
```

### isValidTimeString

Returns if the passed value contains a valid time (`true`) or not (`false`).

- **Syntax:** `isValidTimeString(Date:string) → boolean`
- **Parameter:** `Date` (string) — the value to check.
- **Return Value:** data type `boolean`.

```simtalk
print isValidDateTimeString("14:00:00.00")
```

### str_to_date

Converts the specified date-statement into a statement of data type `date`.

> **Remarks:** Conversion depends on the setting under **File > Model Settings/Preferences > Units > Time Scale**.

- **Type:** Function
- **Syntax:** `str_to_date(DateStatement:string) → date`
- **Parameter:** `DateStatement` (string) — the date to convert. The year has two or four digits. The function takes leap years into account. Accepted formats: `"YYYY/MM/DD"`, `"YYYY-MM-DD"`, and `"DD.MM.YYYY"`.
- **Return Value:** data type `date`.

```simtalk
print str_to_date("2024/02/10") // 2024/02/10
print str_to_date("2024-02-10") // 2024/02/10
print str_to_date("10.02.2024") // 2024/02/10
```

### str_to_dateTime

Converts the specified date-statement into a statement of data type `dateTime`.

> **Remarks:** Conversion depends on the setting under **File > Model Settings/Preferences > Units > Time Scale**.

- **Type:** Function
- **Syntax:** `str_to_dateTime(DateTimeStatement:string) → dateTime`
- **Parameter:** `DateTimeStatement` (string) — the date and time to convert. The year has two or four digits. The function takes leap years into account. Accepted formats: `"YYYY/MM/DD HH:MM:SS.s"`, `"YYYY-MM-DD HH:MM:SS.s"`, and `"DD.MM.YYYY HH:MM:SS.s"`. You can replace the space between date and time with the letter `T`.
- **Return Value:** data type `dateTime`.

```simtalk
print str_to_datetime("2024/02/10 14:00:00.00")
print str_to_datetime("2024-02-10 14:00:00.00")
print str_to_datetime("10.02.2024 14:00:00.00")
print str_to_datetime("10.02.2024T14:00:00.00")
```

### str_to_time

Converts the specified data into a time-statement of data type `time`.

> **Remarks:** Plant Simulation analyzes the statement from right to left. It has the format `hh:mm:ss.ss`. The value `"1:00.1"` stands for one minute plus one tenth of a second. Conversion depends on the setting under **File > Model Settings/Preferences > Units > Time Scale**.

- **Type:** Function
- **Syntax:** `str_to_time(Data:string[, FormatLikeDialogs:boolean]) → time`
- **Parameters:**
  - `Data` (string) — the data to convert.
  - `FormatLikeDialogs` (boolean, optional) — `true` uses the same time format as in text boxes of the dialogs. If omitted or `false`, uses the same time format as in tables (four decimal places).
- **Return Value:** data type `time`.

The statement `str_to_time("1:30.50")` returns different values depending on the **Time Scale** setting:

| Setting | Time scale | Transfer If | Seconds |
|---------|-----------|-------------|---------|
| 1/1.0   | 24:60:60  | 90.5        |         |
| 1/60.0  | 30:24:60  | 5430        |         |
| 1/0.6   | 24:60:100 | 78.3        |         |

```simtalk
var t: time
t := str_to_time("48:00:00.0")      // 48 hours
self.executeIn(str_to_time("5:00")) // 5 minutes
```

### timeRepresentation

Returns the preferences selected for the time scale under **File > Model Settings/Preferences > Units > Time Scale**.

- **Type:** Function
- **Syntax:** `timeRepresentation → list`
- **Return Value:** a `DataList` of data type `real`. The first entry contains the conversion factor for the time (the reciprocal value; you can only specify the denominator). The following three entries are the values taken from **File > Model Settings/Preferences > Units > Time Scale**, normally represented by `60`, `60`, and `24`.

```simtalk
var l: list[real]
var timeDivision: real
var SecondCarriedOver, HourCarriedOver, DayCarriedOver : real
l := timeRepresentation
timeDivision := l.read(1)
secondCarriedOver := l.read(2)
hourCarriedOver := l.read(3)
dayCarriedOver := l.read(4)
```

---

## Converting Arrays

SimTalk provides the following functions for converting arrays.

### bytes_to_str

Converts an array of integer numbers to text.

> **Remarks:** Plant Simulation uses the specified encoding to interpret the sequence of numbers correctly and to create text from them. Use `bytes_to_str` to convert application-specific or binary data received from the MQTT Interface or the HTTP request functions to a string using a known code page or code page detection. You can use `bytes_to_str` in combination with `readBytesFromFile` instead of `readStringFromFile` when the file has an encoding not supported by `readStringFromFile`.

- **Type:** Function
- **Syntax:** `bytes_to_str(Encoding:string/integer, Bytes:integer[]) → string`
- **Parameters:**
  - `Encoding` (integer or string) — the encoding to use. As an integer, it is a Windows code page identifier (e.g., `28591` for ISO 8859-1 / Latin 1, or `1201` for UTF-16 Big Endian). Specifying an invalid integer causes an error. Named encodings:
    - `ANSI` — uses the encoding of the user interface language of Plant Simulation.
    - `UTF-8` — uses UTF-8 encoding.
    - `UTF-16` / `Unicode` — interprets the sequence as Unicode text; two integers/bytes are mapped to a single letter.
    - `BOM` — checks for a Byte Order Mark (BOM) at the beginning and uses the encoding derived from it (supports UTF-8 and UTF-16 Little Endian).
    - `Codepoints` — treats the sequence as Unicode values; each number represents a Unicode letter. Numbers outside the UTF-16 range or that do not represent a valid letter cause an invalid argument error.
  - `Bytes` (integer array) — the values to interpret as a sequence of bytes or Unicode code points.
- **Return Value:** data type `string`.

```simtalk
var fileName:string := "c:\temp\helloWorld_UTF7.txt"
var bytes:integer[] := readStringFromFile(fileName)
print bytes
// prints [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
print bytes_to_str(65000 /* UTF-7 */, bytes)
// prints Hello World
```
