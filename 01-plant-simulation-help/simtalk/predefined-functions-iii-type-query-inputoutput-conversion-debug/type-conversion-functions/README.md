# 类型转换函数 (Functions for Converting Data Types)

本目录收录了 SimTalk 提供的**数据类型转换函数**。原始内容见同目录下的 `type-conversion-functions.md`。

> **提示：** 任意值都可以通过 `to_str` 转换为字符串。

转换函数按用途分为以下七类：

1. [转换数值 (Converting Numerical Values)](#converting-numerical-values)
2. [转换物理数据类型 (Converting Physical Data Types)](#converting-physical-data-types)
3. [将带单位的物理数据类型转为无单位类型 (Converting Physical Data Types with Units into Data Types without Units)](#converting-physical-data-types-with-units-into-data-types-without-units)
4. [将无单位值转为带单位的物理数据类型 (Converting Values without Units into Physical Data Types with Units)](#converting-values-without-units-into-physical-data-types-with-units)
5. [转换引用 (Converting References)](#converting-references)
6. [转换时间和日期值 (Converting Time and Date Values)](#converting-time-and-date-values)
7. [转换数组 (Converting Arrays)](#converting-arrays)

---

## Converting Numerical Values

数值类型之间的相互转换（boolean / integer / real / string / time）。

| 函数 | 语法 | 说明 |
|------|------|------|
| `bool_to_num` | `bool_to_num(Value:boolean) → integer` | 布尔值转整数，`true`→1，`false`→0 |
| `bool_to_str` | `bool_to_str(Value:boolean) → string` | 布尔值转字符串 |
| `num_to_bool` | `num_to_bool(Value:real) → boolean` | 数字转布尔值，非零为 `true`，零为 `false` |
| `num_to_hex` | `num_to_hex(Value:integer[, Is64Bit:boolean:=false]) → string` | 整数转十六进制字符串，可选 64 位 |
| `num_to_str` | `num_to_str(Number:real[, Precision:integer, Width:integer]) → string` | 数字转字符串，可指定精度与宽度（不足补零） |
| `str_to_bool` | `str_to_bool(Value:string) → boolean` | 字符串转布尔值（大小写不敏感） |
| `str_to_num` | `str_to_num(Value:string) → real` | 字符串转实数，支持正负号、小数点、指数、`0x` 十六进制前缀 |
| `time_to_str` | `time_to_str(Value:time[, FormatLikeDialogs:boolean]) → string` | 时间值转字符串 |
| `to_str` | `to_str(Parameter1:any[, …]) → string` | 将任意多个参数分别转字符串后拼接返回 |

---

## Converting Physical Data Types

将字符串转换为带单位的物理数据类型（可指定单位，缺省时按 **File > Model Settings/Preferences > Units** 中的设置解释）。

| 函数 | 语法 | 可用单位 |
|------|------|----------|
| `str_to_acceleration` | `str_to_acceleration(Data:string) → acceleration` | `mm/s²`, `cm/s²`, `m/s²`, `km/h²`, `m/min²`, `in/s²`, `ft/s²`, `yd/s²` |
| `str_to_length` | `str_to_length(Data:string) → length` | `mm`, `cm`, `m`, `km`, `in`, `ft`, `yd`, `mi` |
| `str_to_speed` | `str_to_speed(Data:string) → speed` | `mm/s`, `cm/s`, `m/s`, `km/h`, `m/min`, `in/s`, `ft/s`, `yd/s`, `mph` |
| `str_to_weight` | `str_to_weight(Data:string) → weight` | `g`, `kg`, `t`, `lb`, `oz` |

---

## Converting Physical Data Types with Units into Data Types without Units

将带单位的物理类型转换为无单位的 `real`，用于规避给不兼容物理类型赋值时产生的警告。

| 函数 | 语法 | 默认单位 |
|------|------|----------|
| `acceleration_to_num` | `acceleration_to_num(Value:acceleration[, Unit:string="m/s²"]) → real` | `m/s²` |
| `length_to_num` | `length_to_num(Data:length[, Unit:string="m"]) → real` | `m` |
| `speed_to_num` | `speed_to_num(Data:speed[, Unit:string="m/s"]) → real` | `m/s` |
| `time_to_num` | `time_to_num(Data:time) → real` | — |
| `weight_to_num` | `weight_to_num(Data:weight[, Unit:string="kg"]) → real` | `kg` |

---

## Converting Values without Units into Physical Data Types with Units

将无单位的 `real` / `integer` 数值转换为带物理单位的数据类型。

| 函数 | 语法 | 默认单位 |
|------|------|----------|
| `num_to_acceleration` | `num_to_acceleration(Number:real[, Unit:string="m/s²"]) → acceleration` | `m/s²` |
| `num_to_length` | `num_to_length(Number:real[, Unit:string="m"]) → length` | `m` |
| `num_to_speed` | `num_to_speed(Number:real[, Unit:string="m/s"]) → speed` | `m/s` |
| `num_to_time` | `num_to_time(Number:real) → time` | — |
| `num_to_weight` | `num_to_weight(Number:real[, Unit:string="kg"]) → weight` | `kg` |

---

## Converting References

对象路径 / 引用 与字符串之间的相互转换。

| 函数 | 语法 | 说明 |
|------|------|------|
| `obj_to_str` | `obj_to_str(obj:object[, MakeAbsolute:boolean:=true]) → string` | 将对象的路径与名称转为字符串，可选返回绝对/相对路径 |
| `str_to_method` | `str_to_method(Path:any[, Context:object]) → object/method` | 将路径解析为 Method 对象或 `method` 类型属性，找不到返回 `VOID` |
| `str_to_obj` | `str_to_obj(Text:string) → object` | 将绝对/相对路径文本转为对象，找不到返回 `void` |
| `str_to_table` | `str_to_table(Path:string/object[, Context:object]) → object/table/list/stack/queue` | 将路径解析为 `table` / `list` / `stack` / `queue` 类型 |

---

## Converting Time and Date Values

日期与时间字符串、`date` / `dateTime` / `time` 类型之间的转换与校验。

| 函数 | 语法 | 说明 |
|------|------|------|
| `datetime_to_str` | `datetime_to_str(Value:datetime[, Format:string])` | 按格式串（`%d` `%m` `%y` `%Y` `%H` `%h` `%M` `%S` `%s` `%p` `%P` `%x` `%X`）将日期时间转为字符串 |
| `isValidDateString` | `isValidDateString(Date:string) → boolean` | 校验日期字符串是否合法（考虑闰年） |
| `isValidDateTimeString` | `isValidDateTimeString(DateAndTime:string) → boolean` | 校验日期时间字符串是否合法 |
| `isValidTimeString` | `isValidTimeString(Date:string) → boolean` | 校验时间字符串是否合法 |
| `str_to_date` | `str_to_date(DateStatement:string) → date` | 字符串转 `date`，支持 `YYYY/MM/DD`、`YYYY-MM-DD`、`DD.MM.YYYY` |
| `str_to_dateTime` | `str_to_dateTime(DateTimeStatement:string) → dateTime` | 字符串转 `dateTime` |
| `str_to_time` | `str_to_time(Data:string[, FormatLikeDialogs:boolean]) → time` | 字符串转 `time`（格式 `hh:mm:ss.ss`），结果受 Time Scale 设置影响 |
| `timeRepresentation` | `timeRepresentation → list` | 返回 **Units > Time Scale** 中的时间刻度偏好设置（`DataList`，含转换因子与 60/60/24 三个值） |

---

## Converting Arrays

| 函数 | 语法 | 说明 |
|------|------|------|
| `bytes_to_str` | `bytes_to_str(Encoding:string/integer, Bytes:integer[]) → string` | 将整数数组按指定编码（ANSI、UTF-8、UTF-16、BOM、Codepoints 或 Windows 代码页）解释为文本，常用于 MQTT / HTTP / 文件读取的二进制数据 |

---

## 目录结构

```
type-conversion-functions/
├── README.md                    # 本文件（总结）
└── type-conversion-functions.md # 详细函数说明（含示例代码）
```
