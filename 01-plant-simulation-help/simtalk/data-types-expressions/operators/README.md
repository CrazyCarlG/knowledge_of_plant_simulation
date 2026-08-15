# Operators（运算符）

本目录介绍 SimTalk 中的运算符与表达式，内容来源于 `operators.md`（以及 `operators.txtx` 的原文）。涵盖数据类型的手动转换、各类运算符的用法，以及不同数据类型之间的运算兼容性。

## 目录概览

- [手动数据类型转换](#手动数据类型转换)
- [运算符与表达式](#运算符与表达式)
- [算术运算符](#算术运算符)
- [关系运算符](#关系运算符)
- [逻辑运算符 AND 和 OR](#逻辑运算符-and-和-or)
- [逻辑运算符 NOT](#逻辑运算符-not)
- [赋值运算符](#赋值运算符)
- [数据类型兼容性](#数据类型兼容性)

---

## 手动数据类型转换

除自动转换外，其余数据类型需通过调用以下转换函数显式转换：

| 转换函数 | 返回值数据类型 |
| --- | --- |
| `bool_to_num` (boolean) | real |
| `num_to_bool` (integer) | boolean |
| `str_to_bool` (string) | boolean |
| `str_to_date` (string) | time |
| `str_to_dateTime` (string) | dateTime |
| `str_to_length` (string) | length |
| `str_to_num` (string) | real |
| `str_to_obj` (string) | object |
| `str_to_speed` (string) | speed |
| `str_to_time` (string) | time |
| `str_to_weight` (string) | weight |
| `to_str` (any, … ) | string |

## 运算符与表达式

表达式最基本、最简单的形式是常量或变量。通过将常量、变量与运算符组合，可以构造出越来越复杂的表达式。Plant Simulation 分析复杂表达式的顺序取决于所涉及运算符的优先级。

Plant Simulation 提供：算术运算符、逻辑运算符 AND/OR、逻辑运算符 NOT，以及关系运算符。部分运算符仅适用于特定数据类型（例如逻辑运算符用于组合布尔表达式）。

## 算术运算符

SimTalk 支持基本算术运算符：

- **加法 `+`、减法 `-`、乘法 `*`、浮点除法 `/`**：由两个数值计算出一个新数值。

```simtalk
x += y      // 加法赋值（等价于 x := x + y）
x -= y      // 减法赋值（等价于 x := x - y）
x *= y      // 乘法赋值（等价于 x := x * y）
1 + 2  * 3  // 返回 7
(1 + 2) * 3 // 返回 9
```

对于 `Variable` 类型的对象，以及数据类型为 `time`、`length`、`weight`、`speed`、`acceleration` 的用户自定义属性，`+=` 与 `-=` 运算符会进行比旧版本更精确的类型检查，例如：

```simtalk
var len : length
VariableObjectOfTypeSpeed += len   // 现在不再被允许
len += VariableObjectOfTypeSpeed   // 一直都不被允许
```

- **整除 `//`**：针对 `integer` 数据类型定义，返回另一个整数并忽略余数。

```simtalk
15 div 5 // 返回 3
17 div 5 // 也返回 3
```

- **取模运算 `mod`**：返回整数除法中被舍弃的余数。

```simtalk
15 mod 5 // 返回 0
17 mod 5 // 返回 2
Variable := Variable mod 360
```

可用取模运算判断整数是奇数还是偶数：

```simtalk
14 mod 2 = 0
15 mod 2 = 1
```

取模运算 `mod` 也适用于浮点数：

```simtalk
print 6.123 mod 2.5 // 输出 1.123
```

## 关系运算符

关系运算符比较两个值，结果为布尔类型 `boolean`。

| 运算符 | 名称 | 比较结果 |
| --- | --- | --- |
| `=` | 等于 | 左右相等则为 true，否则为 false（字符串区分大小写） |
| `/=` 或 `!=` | 不等于 | 左右不相等则为 true，否则为 false |
| `<` | 小于 | 左侧小于右侧则为 true，否则为 false |
| `<=` | 小于或等于 | 左侧小于或等于右侧则为 true，否则为 false |
| `>` | 大于 | 左侧大于右侧则为 true，否则为 false |
| `>=` | 大于或等于 | 左侧大于或等于右侧则为 true，否则为 false |
| `~=` | 约等于 | 左右约相等则为 true，否则为 false * |
| `<~=` | 小于或约等于 | 左侧小于或约等于右侧则为 true，否则为 false * |
| `>~=` | 大于或约等于 | 左侧大于或约等于右侧则为 true，否则为 false * |

### 约等于运算符

`~=`、`<~=`、`>~=` 三个约等于运算符：比较字符串时忽略大小写；比较数值时忽略小于 epsilon（容差）的差值。数值比较的容差可通过 *Tolerance for About Equal Comparison* 设置。

```simtalk
print "a" = "A"              -- false
print "a" ~= "A"             -- true
print 1 = 1.00000000000001   -- false
print 1 ~= 1.00000000000001  -- true
```

可用约等于运算符 `~=` 进行模糊匹配：

```simtalk
-- 模糊匹配 1：忽略大小写
"hello" ~= "HELLO"
-- 模糊匹配 2：忽略首尾空格
strTrim("  hello  ") ~= strTrim("hello    ")
-- 模糊匹配 3：同时忽略以上两者
strTrim(s1) ~= strTrim(s2)
```

> 模糊匹配可能因字符串包含不可见字符（例如控制字符）而失败。

### 用约等于运算符比较对象与存储位

所有可接收 MU 的物流对象都拥有一个或多个存储位（storage place）。约等于运算符 `~=` 在以下条件下返回 true：

- 两个值的数据类型均为 `object`，且对象相同；
- 两个值的数据类型均为 `storage place`，且两个存储位位于同一对象上；
- 一个值为 `storage place`，另一个为 `object`，且该存储位位于该对象上。

```simtalk
var L : object := "Store"
var L11 : any := Store[1,1]
var L23 : any := Store[2,3]
var W : object := TwoLaneTrack
var WA : any := TwoLaneTrack.A
var WB : any := TwoLaneTrack.B
print L ~= L11    -- true
print L11 ~= L23  -- true
print W ~= WA     -- true
print WA ~= WB    -- true
print L ~= W      -- false
print L11 ~= WA   -- false
```

### 支持的数据类型

关系运算符 `=` 和 `/=` 支持比较以下数据类型：

| 左侧 | 右侧 |
| --- | --- |
| integer, real, length, weight, speed, time, acceleration | integer, real, length, weight, speed, time, acceleration |
| date, dateTime | date, dateTime |
| string | string |
| boolean | boolean |
| object | object |
| table, list, stack, queue | table, list, stack, queue |

> 比较 `object` 类型值时，Plant Simulation 始终比较绝对对象路径，比较前会先解析相对路径。
>
> 比较 `table`、`list`、`stack`、`queue` 类型值时，Plant Simulation 检查是否为同一列表/表。将列表/表与其副本比较时，`=` 返回 `false`。

关系运算符 `<`、`<=`、`>=`、`>`、`~=`、`<~=`、`>~=` 支持比较以下数据类型：

| 左侧 | 右侧 |
| --- | --- |
| integer, real, length, weight, speed, time, acceleration | integer, real, length, weight, speed, time, acceleration |
| date, dateTime | date, dateTime |
| string | string |

比较结果可用于嵌套表达式，例如用逻辑运算符 AND、OR、NOT 连接多个比较：

```simtalk
if index > 0 and index <= DataList.Dim
   print "index in valid range"
end
```

## 逻辑运算符 AND 和 OR

逻辑运算符连接两个布尔表达式，返回条件如下：

- **AND**：仅当两个操作数均为 true 时返回 true。

| AND | false | true |
| --- | --- | --- |
| false | false | false |
| true | false | true |

- **OR**：至少一个操作数为 true 时返回 true。

| OR | false | true |
| --- | --- | --- |
| false | false | true |
| true | true | true |

Plant Simulation 从左到右分析逻辑组合，一旦表达式的值已确定就停止求值：

```simtalk
expression1 AND expression2
```

如果 `expression1` 为 false，则无论 `expression2` 为何值，组合结果都已为 false，因此 `expression2` 不会被求值。可用于分支操作和循环终止条件：

```simtalk
if i <= DataList.dim AND DataList[i] > 0
   // 处理条目
end
```

OR 同理：左侧为 true 时，Plant Simulation 立即停止求值。

示例——在列表中查找大于 0 的值：

```simtalk
var i := 0
repeat
    i := i + 1
until i > DataList.Dim OR DataList[i] > 0
```

若列表中没有大于 0 的值，当索引比允许的最大索引大 1 时退出循环，且不会访问表达式的第二部分。

## 逻辑运算符 NOT

逻辑运算符 NOT 对布尔值取反，即 true 变 false，false 变 true。

```simtalk
failure := false
print failure         // 输出 false
print NOT failure     // 输出 true
print NOT NOT failure // 输出 false

var i,j :real
i:=4.00000001
j:=3.999999
if NOT {i~=j}
```

## 赋值运算符

SimTalk 提供多种赋值运算符：

- 赋值运算符 `:=`（或 `=`）
- 引用运算符 `&`
- `byRef`
- `void`

### `:=` — 赋值运算符

`:=` 给变量赋新值。Plant Simulation 先求值运算符右侧的表达式；若值与变量数据类型相同，则赋给变量。也可用 `=` 代替 `:=`。

若数据类型不同，需先转换。Plant Simulation 会自动将 real 与 integer 互转；real 转 integer 时会去掉小数点后的数字。date 与 dateTime 互转同理（赋给 date 时会丢弃时间部分）。

```simtalk
integerVar := 2.999 // 值为 2，去掉小数点后数字
```

其余数据类型必须用相应转换函数显式转换（见“手动数据类型转换”）：

```simtalk
var r: real; var b: boolean; var s: string; var d: date; var dt: dateTime
r := 1.0 + 4 * (3 - 0.18)                      // 12.28
b := true and (b or true)                      // true
s := "new" + " value"                          // "new value"
dt := str_to_dateTime("2018/1/31 13:45:44")    // 日期和时间
d := dt                                        // 无时间，即午夜
```

赋值前先完整求值右侧，因此可直接自增：

```simtalk
a := a + 3 // integer
```

若变量 `a` 值为 5，则右侧为 5+3=8，再赋回给 `a`，覆盖原值。

### `&` — 引用运算符

引用运算符 `&` 用于访问对象的属性或方法。

访问 `Variable` 或 `Method` 类型对象、或数据类型为 `object`/`json` 的用户自定义属性之前，需注意：

- 访问全局 `Variable` 时返回其内容，属性/方法名会作用于内容而非 Variable 对象本身；
- 访问 `Method` 时开始执行该方法，属性/方法名会作用于结果而非 Method 对象本身；
- 访问数据类型为 `object` 或 `json` 的用户自定义属性时，访问的是属性值而非属性本身。

引用运算符阻止读取 Variable 内容或调用 Method，返回对象本身的引用，可将该引用放入列表/表或作为参数传入其他方法。

对象路径中，`&` 直接放在 Method 或 Variable 名称前：

```simtalk
print &MyVariable.DataType
print .UserObjects.&MyVariable.DataType
var obj: object
obj := &MyMethod
obj := &MyVariable
MyStation.&ObjAttr.InitValue := Buffer     // 设置 object 类型用户属性的初始值
MyStation.&JsonAttr.InheritValue := false  // 关闭 JSON 类型用户属性的继承
```

若持有全局 Variable 的引用并想读取其值，对引用应用 `Value` 属性；若持有 Method 引用并想调用它，对引用调用 `execute` 方法：

```simtalk
MyVariable := .MaterialFlow.Station  // object 类型变量
var obj := &MyVariable
print obj.Name                       // 返回 MyVariable
print obj.Value.Name                 // 返回 Station

obj := &MyMethod                     // 引用
obj.execute                          // 调用
obj := &methodWithArgument
obj.execute(1.0, true,"parameter")   // 带参数调用
```

> 若使用数据类型为 `method` 的用户自定义属性，并想访问其属性和方法，则不能使用引用运算符。

```simtalk
Station.method                // 执行用户自定义方法
Station.method.executeIn(60)  // 调度该方法在 60 秒后调用
```

### `byref` — 引用运算符

`byref` 运算符按引用传递参数。被调用的 Method 直接访问调用方的局部变量，而非复制值。`byref` 可返回多个结果给调用方 Method，且只能指定局部变量。被传局部变量的数据类型必须与形式参数完全一致——Plant Simulation 不会转换引用参数的数据类型。

```simtalk
param byref a,b : real             // 声明 method1
a := a + 1
b := b + 1
                                   // 声明 method2
var x, y : real
print x, " ", y                    // 0 0
method1(x, y)
print x, " ", y                    // 1 1
method1(x, x)
print x, " ", y                    // 3 1
```

### `void` — 变量

当数据类型为 `object` 的局部变量指向一个不存在的 Plant Simulation 对象时，Plant Simulation 将其赋值为 `void`。

## 数据类型兼容性

数学运算符和关系运算符只能用于某些数据类型，运算结果可能是完全不同的数据类型。

下述表格列出了允许的组合及结果的数据类型。查找 `a op b` 时，在行中找 `a`，在列中找 `b`，表格项即结果的数据类型。

`time`、`length`、`weight`、`speed`、`acceleration` 互不兼容。例如，只能将 `length`、`real` 或 `integer` 类型的值赋给 `length` 类型的变量。

### 赋值时的兼容性

赋值给变量或属性时，Plant Simulation 保留变量或属性的数据类型。仅当类型匹配，或待赋值的值与变量/属性均为数值类型（但物理单位不同时除外）时，赋值才被允许。例如可将 `length` 值赋给 integer/real 变量，但不能赋给 speed 变量。

只有 `integer` 类型会改变值（截去小数点后数字）。例如赋 2.5 给 integer 变量得 2。

表格读取方式：列 = 待赋值的数据类型；行 = 目标变量或属性的数据类型。

| `:=` | integer | real | length | weight | speed | time | date | datetime | string | object |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| integer | integer | integer | integer | integer | integer | integer | — | — | — | — |
| real | real | real | real | real | real | real | — | — | — | — |
| length | length | length | length | — | — | — | — | — | — | — |
| weight | weight | weight | — | weight | — | — | — | — | — | — |
| speed | speed | speed | — | — | speed | — | — | — | — | — |
| time | time | time | — | — | — | time | — | — | — | — |
| date | — | — | — | — | — | — | date | date | — | — |
| datetime | — | — | — | — | — | — | datetime | datetime | — | — |
| string | — | — | — | — | — | — | — | — | string | string |
| object | — | — | — | — | — | — | — | — | object | object |

### 加法时的兼容性

加法时，`integer` 与 `real` 被视为无单位。若操作数数据类型不兼容，结果为 `real`。

表格读取方式：行 = 左操作数；列 = 右操作数。

| `+` | integer | real | length | weight | speed | time | date | datetime | string |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| integer | integer | real | length | weight | speed | time | date | datetime | — |
| real | real | real | length | weight | speed | time | datetime | datetime | — |
| length | length | length | length | — | — | — | — | — | — |
| weight | weight | weight | real | weight | — | — | — | — | — |
| speed | speed | speed | — | — | speed | — | — | — | — |
| time | time | time | — | — | — | time | datetime | datetime | — |
| date | date | datetime | — | — | — | datetime | — | — | — |
| datetime | datetime | datetime | — | — | — | datetime | — | — | — |
| string | string | — | — | — | — | — | — | — | string |

### 减法时的兼容性

减法时，`integer` 与 `real` 被视为无单位。若操作数数据类型不兼容，结果为 `real`。

表格读取方式：行 = 左操作数；列 = 右操作数。

| `-` | integer | real | length | weight | speed | time | date | datetime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| integer | integer | real | length | weight | speed | time | — | — |
| real | real | real | length | weight | speed | time | — | — |
| length | length | length | length | — | — | — | — | — |
| weight | weight | weight | — | weight | — | — | — | — |
| speed | speed | speed | — | — | speed | — | — | — |
| time | time | time | — | — | — | time | — | — |
| date | date | datetime | — | — | — | datetime | integer (days) | time |
| datetime | datetime | datetime | — | — | — | datetime | time | time |

### 乘法时的兼容性

乘法时，`integer` 与 `real` 被视为无单位。若操作数数据类型不兼容，结果为 `real`。

表格读取方式：行 = 左操作数；列 = 右操作数。

| `*` | integer | real | length | weight | speed | time |
| --- | --- | --- | --- | --- | --- | --- |
| integer | integer | real | length | weight | speed | time |
| real | real | real | length | weight | speed | time |
| length | length | length | real* | real* | real* | real* |
| weight | weight | weight | real* | real* | real* | real* |
| speed | speed | speed | real* | real* | real* | length |
| time | time | time | real* | real* | length | real* |

\* 乘法结果保留正确的物理单位。

### 除法时的兼容性

除法时，`integer` 与 `real` 被视为无单位。若操作数数据类型不兼容，结果为 `real`。

表格读取方式：行 = 左操作数；列 = 右操作数。

| `/` | integer | real | length | weight | speed | time |
| --- | --- | --- | --- | --- | --- | --- |
| integer | integer | real | real* | real* | real* | real* |
| real | real | real | real* | real* | real* | real* |
| length | length | length | real | real* | time | speed |
| weight | weight | weight | real* | real | real* | real* |
| speed | speed | speed | real* | real* | real | acceleration |
| time | time | time | real* | real* | real* | real |

\* 除法结果保留正确的物理单位。

### string 数据类型的兼容性

`string` 类型只支持加法运算符 `+`。Plant Simulation 将两个字符串拼接成一个新字符串（把第二个字符串追加到第一个之后）。

```simtalk
print "My short string " + "plus my long string with many words."
```

例外：也可以将整数值加到字符串上，Plant Simulation 会把整数转换为字符串后追加。

```simtalk
param obj : object -> string
return obj.Name + obj.Label + obj.XPos
```
