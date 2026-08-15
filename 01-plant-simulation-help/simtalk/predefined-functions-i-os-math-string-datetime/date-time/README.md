# Date and Time Functions

本目录汇总 SimTalk 中用于管理日期与时间信息的预定义函数。

> **Note:** Plant Simulation 使用所选模型语言（Model Language）的日期与时间格式。

## 函数概览

| 函数 | 说明 | 返回类型 |
|------|------|:--------:|
| `strTrim` | 去除字符串首尾的空白、制表符与回车符 | string |
| `CalendarWeek` | 按 DIN 1355 / ISO 8601 返回指定日期的日历周 | integer |
| `CalendarYear` | 返回公历的当前年份 | integer |
| `day` | 从 dateTime/date 值中提取"日" | integer |
| `dayOfWeek` | 返回自上一个星期日以来经过的天数 | integer |
| `dayOfYear` | 返回自 1 月 1 日以来经过的天数 | integer |
| `getDate` | 返回包含日期与时间的值中的日期部分 | date |
| `month` | 返回包含日期与时间的值中的月份 | integer |
| `setDaylightSavingTime` | 设置夏令时的开始与结束时间 | — |
| `sysDate` | 返回运行 Plant Simulation 的计算机当前系统时间 | dateTime |
| `timeOfDay` | 返回包含日期与时间的值中的时间部分 | time |
| `week` | 返回自年初以来开始的周数 | integer |
| `year` | 计算自 1900 年以来经过的年数 | integer |

## 函数详解

### strTrim
去除字符串首尾的空白字符（空格、制表符、回车符）。

- **语法：** `strTrim(Text:string) → string`
- **参数：** `Text`（string）— 含有首尾空白字符的字符串。

### CalendarWeek
按 DIN 1355 / ISO 8601 返回指定日期的日历周。一周始终从星期一开始；一年的第一个日历周是至少包含新年四天的那一周。

- **语法：** `CalendarWeek(Date:dateTime) → integer`
- **See also:** `week`

### CalendarYear
返回公历的当前年份（例如 `CalendarYear(sysdate)` 返回 2024）。

- **语法：** `CalendarYear(Value:dateTime) → integer`
- **See also:** `year`

### day
从 date 或 dateTime 值中提取"日"。

- **语法：** `day(Date:date) → integer` / `day(DateTime:dateTime) → integer`

### dayOfWeek
返回自上一个星期日以来经过的天数。返回值对照：

| 星期 | 返回值 |
|------|:------:|
| 星期日 | 0 |
| 星期一 | 1 |
| 星期二 | 2 |
| 星期三 | 3 |
| 星期四 | 4 |
| 星期五 | 5 |
| 星期六 | 6 |

- **语法：** `dayOfWeek(Date:date) → integer` / `dayOfWeek(DateTime:dateTime) → integer`

### dayOfYear
返回自 1 月 1 日以来经过的天数。

- **语法：** `dayOfYear(Date:date) → integer` / `dayOfYear(DateTime:dateTime) → integer`

### getDate
返回包含日期与时间的值中的日期部分。

- **语法：** `getDate(Date/Datetime:dateTime)`

### month
返回包含日期与时间的值中的月份。

- **语法：** `month(Date:date) → integer` / `month(DateTime:dateTime) → integer`

### setDaylightSavingTime
设置夏令时的开始与结束时间。参数字符串由两组各四个数字组成：

- **第一组四个数字**（开始时间）：`monthOfYear`, `weekOfMonth`, `dayInWeek`, `hour`
- **第二组四个数字**（结束时间）：`monthOfYear`, `weekOfMonth`, `dayInWeek`, `hour`
- 传入空字符串 `""` 可停用夏令时。

- **语法：** `setDaylightSavingTime(BeginningAndEndOfDaylightSavingTime:string)`

### sysDate
返回运行 Plant Simulation 的计算机的当前系统时间，分辨率为 1 毫秒。

- **语法：** `sysDate → dateTime`
- **See also:** `getHighResolutionClock`, `processTime`

### timeOfDay
返回包含日期与时间的值中的时间部分。

- **语法：** `timeOfDay(DateTime:dateTime) → time`

### week
返回自年初以来开始的周数。一周始终从星期一开始（注意：该"周"与日历周不同）。

- **语法：** `week(Date:date) → integer` / `week(DateTime:dateTime) → integer`
- **See also:** `CalendarWeek`

### year
计算自 1900 年以来经过的年数（例如 `year(sysdate)` 返回 124）。

- **语法：** `year(Date:date) → integer` / `year(DateTime:dateTime) → integer`

## 相关主题

- Date and Time Format [model settings]
- Model Language [model settings]
