# Methods of the ShiftCalendar

The ShiftCalendar provides:

- The methods listed in the table of contents to the left.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## Syntax Line Conventions

An example of the Syntax line of the individual methods might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. The expression `(Parameter:string)`, for example, designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note**
> Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. The expression `[,Parameter:boolean]`, for example, means that you can, but do not have to enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `→ boolean` in the example above.

## calculateWorkingDuration [SimTalk]

Calculates the Working Duration between two points in time for the ShiftCalendar designated by `<Path>`.

**Remarks**

While calculating the working duration, `calculateWorkingDuration` takes pauses and shifts into account.

**Type**

Read-only attribute

**Syntax**

```
<Path>.calculateWorkingDuration(StartTime:dateTime, EndTime:dateTime) → time
```

**Parameters**

You can specify the following parameters:

- The parameter `StartTime` of data type `dateTime` designates the start time from which on the ShiftCalendar computes the working duration.
- The parameter `EndTime` of data type `dateTime` designates the end time until which the ShiftCalendar computes the working duration.

**Return Value**

The return value has the data type `time`.

**Example**

```
var startDateTime   : dateTime
var endDateTime     : dateTime
var workingDuration : time
startDateTime := str_to_dateTime("02.01.2006 0:00")
endDateTime   := str_to_dateTime("02.01.2006 10:15")
workingDuration := MyShiftCalendar.calculateWorkingDuration(startDateTime,
endDateTime)
print workingDuration
```

**See also**

Working [state, material flow objects]

## schedule [SimTalk] - ShiftCalendar

Schedules the date and time to start or to finish the production process for the ShiftCalendar designated by `<Path>`.

**Remarks**

The method `schedule` can schedule 100 years into the future.

**Type**

Method

**Syntax**

```
<Path>.schedule(StartTime:dateTime, Duration:time, Direction:string) → dateTime
```

**Parameters**

You can specify the following parameters:

- The parameter `StartTime` of data type `dateTime` designates the start or end date and time from which on the ShiftCalendar schedules the production date.
- The parameter `Duration` of data type `time` designates the duration of the production process.
- The parameter `Direction` of data type `string` designates direction, i.e., if the ShiftCalendar computes forward or backward in time.
  - For **forward scheduling**, the production order requires a defined production time for manufacturing the product. Beginning at the start date, which normally is the active date, the method `schedule` computes the date on which the product has to be finished. It takes production time, shift times, weekends and holidays into consideration.
  - For **backward scheduling**, where you know the date on which the product has to available, as well as the production time, the method `schedule` computes the start date on which production has to start. It takes production time, shift times, weekends and holidays into consideration.

**Return Value**

The return value has the data type `dateTime`.

**Example**

```
startDateAndTime := str_to_dateTime("4.1.2003
9:00")                             // Friday 9:00
Duration :=
str_to_time("10:00:00.0")                                            // 10 hours
endDateAndTime := MyShiftCalendar.schedule(startDateAndTime,Duration,
"forward") // Monday 12:00
```

**See also**

Schedule Date and Time to Start or Finish the Production Process

# Read-Only Attributes of the ShiftCalendar

The ShiftCalendar provides:

- The read-only attributes listed in the table of contents to the left.
- The Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.
