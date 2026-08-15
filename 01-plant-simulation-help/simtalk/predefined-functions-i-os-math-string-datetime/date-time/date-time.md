# Functions for Managing Date and Time

SimTalk provides the functions listed below for managing date and time information.

> **Note:** Plant Simulation uses the Date and Time Format of the Model Language you selected.

---

## strTrim

Returns a string from which Plant Simulation removed leading and trailing blanks, tab stops, and carriage returns.

- **Type:** Function
- **Syntax:** `strTrim(Text:string) → string`
- **Parameter:** `Text` (string) — the string containing leading/trailing whitespace characters.
- **Return value:** `string`

**Examples**

```simtalk
print strTrim(" ab c ") // returns "ab c"
strTrim("  hello  ") = strTrim("hello    ") -- ignores leading and trailing spaces
```

---

## CalendarWeek

Returns the calendar week of the specified date according to DIN 1355 / ISO 8601.

- **Remarks:** A new week always starts on Monday. The first calendar week of a year is the first week that contains at least four days of the new year.
- **Type:** Function
- **Syntax:** `CalendarWeek(Date:dateTime) → integer`
- **Parameter:** `Date` (dateTime) — the date.
- **Return value:** `integer`

**Examples**

```simtalk
print CalendarWeek(str_to_date("2023/11/21")) // returns 47, model language English
print CalendarWeek(str_to_date("21.11.2023")) // returns 47, model language German
```

**See also:** `week`

---

## CalendarYear

Returns the current year of the Gregorian Calendar.

- **Type:** Function
- **Syntax:** `CalendarYear(Value:dateTime) → integer`
- **Parameter:** `Value` (dateTime) — the date.
- **Return value:** `integer`

**Example**

```simtalk
print(CalendarYear(sysdate)) // 2024
print(year(sysdate))         // 124
```

**See also:** `year`

---

## day

Extracts the day from a dateTime value.

- **Type:** Function
- **Syntax:**
  - `day(Date:date) → integer`
  - `day(DateTime:dateTime) → integer`
- **Parameter:**
  - `Date` (date) — the date.
  - `DateTime` (dateTime) — the date and time.
- **Return value:** `integer`

**Examples**

```simtalk
print day(str_to_date("23/12/24"))            // returns 24, model language English
print day(str_to_dateTime("24/1/1 1:00:00"))  // returns 1
print day(str_to_date("24.12.23"))            // returns 24, model language German
print day(str_to_dateTime("1.1.24 1:00:00"))  // returns 1
```

---

## dayOfWeek

Returns the number of days that has elapsed since the last Sunday.

- **Type:** Function
- **Syntax:**
  - `dayOfWeek(Date:date) → integer`
  - `dayOfWeek(DateTime:dateTime) → integer`
- **Parameter:**
  - `Date` (date) — the date.
  - `DateTime` (dateTime) — the date and time.
- **Return value:** `integer`

**Day of Week Return Values**

| Day of Week | Return Value |
|-------------|:------------:|
| Monday      | 1            |
| Tuesday     | 2            |
| Wednesday   | 3            |
| Thursday    | 4            |
| Friday      | 5            |
| Saturday    | 6            |
| Sunday      | 0            |

**Examples**

```simtalk
var d: date; var dt: dateTime
dt := str_to_dateTime("24/1/3 1:20:30")
d := str_to_date("24/1/1")
print dayOfWeek(dt)  // returns 3, model language English
print dayOfWeek(d)   // returns 1

var d: date; var dt: dateTime
dt := str_to_dateTime("3.1.24 1:20:30")
d := str_to_date("1.1.24")
print dayOfWeek(dt)  // returns 3, model language German
print dayOfWeek(d)   // returns 1
```

---

## dayOfYear

Returns the number of days that has elapsed since January first.

- **Type:** Function
- **Syntax:**
  - `dayOfYear(Date:date) → integer`
  - `dayOfYear(DateTime:dateTime) → integer`
- **Parameter:**
  - `Date` (date) — the date.
  - `DateTime` (dateTime) — the date and time.
- **Return value:** `integer`

**Examples**

```simtalk
var d: date; var dt: dateTime
dt := str_to_dateTime("23/12/31 23:59:59")
d := str_to_date("24/1/1")
print dayOfYear(dt)  // returns 364, model language English
print dayOfYear(d)   // returns 0

var d: date; var dt: dateTime
dt := str_to_dateTime("31.12.23 23:59:59")
d := str_to_date("1.1.24")
print dayOfYear(dt)  // returns 364, model language German
print dayOfYear(d)   // returns 0
```

---

## getDate

Returns the date of a value containing date and time.

- **Type:** Function
- **Syntax:** `getDate(Date/Datetime:dateTime)`
- **Parameter:** `Date` or `DateTime` (date or dateTime) — the value containing date and time.

**Examples**

```simtalk
var d: date; var dt: dateTime
dt := str_to_dateTime("2023/11/12 11:30:00")
d := getDate(dt)
print d // returns 2023/11/11, model language English

var d: date; var dt: dateTime
dt := str_to_dateTime("12.11.2023 11:30:00")
d := getDate(dt)
print d // returns 12.11.2023, model language German
```

---

## month

Returns the month of a value containing date and time.

- **Type:** Function
- **Syntax:**
  - `month(Date:date) → integer`
  - `month(DateTime:dateTime) → integer`
- **Parameter:**
  - `Date` (date) — the date.
  - `DateTime` (dateTime) — the date.
- **Return value:** `integer`

**Example**

```simtalk
print month(str_to_date("24.12.23"))             // returns 12
print month(str_to_dateTime("1.1.24 1:00:00"))   // returns 1
```

---

## setDaylightSavingTime

Sets the beginning and the end of daylight saving time.

- **Type:** Function
- **Syntax:** `setDaylightSavingTime(BeginningAndEndOfDaylightSavingTime:string)`
- **Parameter:** `BeginningAndEndOfDaylightSavingTime` (string) — consists of the following components:
  - **First set of four numbers** sets the beginning of daylight saving time:
    - monthOfYear
    - weekOfMonth
    - dayInWeek
    - hour
  - **Second set of four numbers** sets the end of daylight saving time:
    - monthOfYear
    - weekOfMonth
    - dayInWeek
    - hour
  - To deactivate daylight saving time, specify an empty string `""`.

**Example**

```simtalk
setDaylightSavingTime("4,3,3,12,10,4,3,3")
setDaylightSavingTime("") // no daylight saving time
```

**See also:** Daylight Saving Time [preferences]

---

## sysDate

Returns the current system time of the computer on which Plant Simulation runs.

- **Title:** Function
- **Syntax:** `sysDate → dateTime`
- **Return value:** `dateTime` — has a resolution of 1 millisecond.

**Example**

```simtalk
print sysDate                          // current time
EventController.StartDate := sysDate   // apply to simulation
```

**See also:** `getHighResolutionClock`, `processTime`

---

## timeOfDay

Returns the time portion of a value containing date and time.

- **Type:** Function
- **Syntax:** `timeOfDay(DateTime:dateTime) → time`
- **Parameter:** `DateTime` (dateTime) — the value containing date and time.
- **Return value:** `time`

**Examples**

```simtalk
var EclipseOfTheSun: datetime; var t: time; var d: date
EclipseOfTheSun := str_to_datetime("11.08.1999 11:30:00")
t := timeOfDay(EclipseOfTheSun)
print t // 11:30:00.0000
d := getDate(EclipseOfTheSun)
print d // returns 11.08.1999, model language English

var Sonnenfinsternis: datetime; var t: time; var d: date
Sonnenfinsternis := str_to_datetime("11.8.99 11:30:00")
t := timeOfDay(Sonnenfinsternis)
print t // 11:30:00.0000
d := getDate(Sonnenfinsternis)
print d // returns 11.08.1999, model language German
```

---

## week

Returns the number of weeks that started since January first of a year.

- **Remarks:** The week always begins on a Monday. This week does not correspond to the calendar week.
- **Type:** Function
- **Syntax:**
  - `week(Date:date) → integer`
  - `week(DateTime:dateTime) → integer`
- **Parameter:**
  - `Date` (date) — the date.
  - `DateTime` (dateTime) — the date and the time.
- **Return value:** `integer`

**Example**

```simtalk
print week(str_to_date("1.1.24"))             // returns 1
print week(str_to_date("1.2.24"))             // returns 5
print week(str_to_dateTime("1.1.24 1:00:00")) // returns 1
```

**See also:** `CalendarWeek`

---

## year

Computes the number of years elapsed since the year 1900.

- **Type:** Function
- **Syntax:**
  - `year(Date:date) → integer`
  - `year(DateTime:dateTime) → integer`
- **Parameter:**
  - `Date` (date) — the date.
  - `DateTime` (dateTime) — the date and the time.
- **Return value:** `integer`

---

## See also

- Date and Time Format [model settings]
- Model Language [model settings]

---

*Source: Plant Simulation Help. Unpublished work. © 2026 Siemens*
