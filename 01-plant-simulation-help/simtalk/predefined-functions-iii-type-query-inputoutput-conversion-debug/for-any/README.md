# for-any 目录总结

本目录对应 Plant Simulation SimTalk 帮助文档中的「查询 `any` 数据类型变量的数据类型」章节，内容来源为 `for-any.md`（以及其原始文本导出 `for-any.txtx`）。

## 章节概述

SimTalk 提供了一组函数，用于查询数据类型为 `Any` 的变量的具体数据类型。这些函数接收一个参数，Plant Simulation 会将该参数的实际数据类型与目标数据类型进行比较，并返回布尔值（或字符串）。

> 相关数据类型说明参见：`Any [SimTalk] - data type`

## 函数清单

### getSimTalkTypename

返回任意值的数据类型名称。

- **类型：** Function
- **语法：** `getSimTalkTypename(Value:any) → string`
- **返回值：**
  - 对 `table` / `stack` / `queue` 分别返回字符串 `"table"`、`"stack"`、`"queue"`。
  - 对赋值了特殊对象（如传感器）的 `any` 类型局部变量，根据特殊对象类型返回 `sensor`、`lane`、`storage place`、`3D object` 或 `3D animation`。
  - 若传入值为 `Array` 数据类型，返回 `array`。

### is* 类型判断函数

以下函数均用于判断指定参数是否为某种数据类型，返回布尔值 `true` / `false`。

| 函数 | 语法 | 判断的数据类型 |
| --- | --- | --- |
| `isAcceleration` | `isAcceleration(Argument:any) → boolean` | Acceleration（加速度） |
| `isArray` | `isArray(Argument:Value) → boolean` | Array（数组） |
| `isBoolean` | `isBoolean(Argument:any) → boolean` | Boolean（布尔） |
| `isDate` | `isDate(Argument:any) → boolean` | Date（日期） |
| `isDatetime` | `isDatetime(Argument:any) → boolean` | DateTime（日期时间） |
| `isInteger` | `isInteger(Argument:any) → boolean` | Integer（整数） |
| `isJson` | `isJson(Argument:any) → boolean` | JSON |
| `isLength` | `isLength(Argument:any) → boolean` | Length（长度） |
| `isList` | `isList(Argument:any) → boolean` | List（列表） |
| `isListRange` | `isListRange(Argument:any) → boolean` | 列表范围（如 `{1,1}..{2,*}`） |
| `isObject` | `isObject(Argument:any) → boolean` | Object（对象） |
| `isQueue` | `isQueue(Argument:any) → boolean` | Queue（队列） |
| `isReal` | `isReal(Argument:any) → boolean` | Real（实数） |
| `isSpeed` | `isSpeed(Argument:any) → boolean` | Speed（速度） |
| `isStack` | `isStack(Argument:any) → boolean` | Stack（堆栈） |
| `isString` | `isString(Argument:any) → boolean` | String（字符串） |
| `isTable` | `isTable(Argument:any) → boolean` | Table（表格） |
| `isTime` | `isTime(Argument:any) → boolean` | Time（时间） |
| `isWeight` | `isWeight(Argument:any) → boolean` | Weight（重量） |

- **通用参数：** `Argument` 为数据类型 `any`，指定要检查的参数。
- **通用返回值：** 返回值的数据类型为 `boolean`。

## 重要说明：VOID 值

对于 `isObject`、`isTable` 和 `isList`：

值 `VOID` 没有数据类型，因为数据类型为 `object`、`table` 和 `list` 的局部变量都可以取 `void` 值。因此，当向 `any` 类型的局部变量赋值 `void` 时，该变量不会获得数据类型。此时调用 `isObject` 会返回 `false`。

示例：

```simtalk
var a: any := void
print isObject(a)  // 输出 false
print a = void     // 输出 true

var b : any := 123
print b = void     // 输出 false
```

## 文件说明

- `for-any.md`：本目录的主要 Markdown 文档，包含上述全部函数的详细说明与示例。
- `for-any.txtx`：`for-any.md` 对应的原始文本导出文件，内容与之等价（含额外的分页页眉/页脚等导出信息）。
