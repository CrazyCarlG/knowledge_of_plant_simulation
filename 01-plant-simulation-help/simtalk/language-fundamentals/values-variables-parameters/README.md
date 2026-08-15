# Values, Variables & Parameters（值、变量与参数）

本目录对应 Plant Simulation SimTalk 帮助文档中关于 **命名空间、常量值、变量（局部变量与全局变量）以及参数（声明、默认参数、返回值）** 的内容。以下是对 `values-variables-parameters.md` 的总结。

## 目录结构

- `values-variables-parameters.md` — 本节内容的整理版（Markdown）
- `values-variables-parameters.txtx` — 原始帮助文本（源文件）

> 本目录下没有子文件夹，也没有其他 `.md` 或 `README.md` 文件。

## 内容概览

本文档涵盖四个主题：

1. **Namespace（命名空间）**
2. **Constant Values（常量值）**
3. **Variables（变量）**
4. **Parameters（参数）**

---

## 1. Namespace（命名空间）

- 插入到某个 Frame 中的所有对象，加上该 Frame 的内置属性/方法名和用户自定义属性名，共同构成一个 **命名空间（namespace）**。文件夹以及提供内置属性/方法并带有用户自定义属性的对象同理。
- 在同一个命名空间内，每个名称必须**唯一**，不能重复。
- 不同命名空间中可以使用相同名称，Plant Simulation 通过**路径（path）** 加以区分。

**参见：** Name、`isNameUnique`。

---

## 2. Constant Values（常量值）

常量包含不会改变的值，可赋给以下数据类型的常量值：**Boolean、Integer、Real、String、pi**。

### Boolean
- 给布尔常量赋 `true` 或 `false`。
- 示例：`order_done := true`

### Integer
- 给整数常量赋 0–9 的数字，可带正负号（`+` / `-`）。
- 取值范围：**−9223372036854775807** 到 **9223372036854775807**。
- 示例：`order_number := -112304`

### pi
- 常量 `pi` 是圆周率（圆周长与直径之比），数据类型为 `real`。
- 示例：`print pi // 3.141592653589793`

### Real
- 给实型常量赋小数点后的一位或多位数字（也可用指数形式，如 `1.0e2` 表示 `100`）。
- 指数范围限制在 `[307, -307]`。
- 实型常量靠**小数点**识别；没有小数点则被当作范围有限的 `integer`。
- 数据类型 `time`、`date`、`dateTime` **不支持**常量值，需使用 real/integer 常量或转换函数 `str_to_time`、`str_to_date`、`str_to_dateTime`。
- 示例：
  ```simtalk
  Conveyor.Speed := 2.5
  Avogadro := 6.5e23
  epsilon := 1.0e-6 // 0.000001
  ```

### String
- 给字符串常量赋引号 `""` 内的字母、数字与特殊字符。
- 示例：`priority := "Urgent"`

字符串常量规则：

- 字符串内要使用引号时，需在其前面加反斜杠 `\` 进行保护：
  ```simtalk
  print "It is \"very\" urgent."  -- 输出 It is "very" urgent.
  ```
- 要在字符串内换行，在该行末尾以反斜杠 `\` 结尾并在下一行继续：
  ```simtalk
  var address : string
  address := "Frank Jones\
  Halford Lane 9\
  Cedar Rapids, IA 52409"
  ```
- 要保护反斜杠本身，再输入一个反斜杠 `\\`（当字符串字面量以反斜杠结尾时必需）：
  ```simtalk
  a := "It is \"very\" urgent." -- 反斜杠保护引号
  Path := "C:\Temp"             -- 此处无需保护反斜杠
  Path := "C:\\" + FolderName   -- 字符串末尾的反斜杠需保护
  ```
- 字符串常量最多 **1024 个字符**；可用 `+` 把多个字符串连接成任意长度。

---

## 3. Variables（变量）

局部变量、全局变量和参数都能在一段时间内保存值并在之后访问，其值可随时改变。

### Local Variables（局部变量）

当计算结果只需在**同一次 Method 调用内**复用（调用结束后不再需要）时使用局部变量。

- 局部变量名仅在声明它的 Method 内可见，其他 Method 无法访问。
- 每次 Method 调用都会创建**一套新的局部变量**；Method 递归调用自身时也会创建新的一套，且只能访问新的一套，直到调用结束。
- 使用前必须先声明。

**赋值前的初始值：**

| 数据类型 | 初始值 |
| --- | --- |
| 数值类型 | `0` |
| boolean | `false` |
| string | `""` |
| object、list/table | `void` |
| date | `1900/01/01` |
| dateTime | `1900/01/01 00:00:00.0000` |

（对于最初在 Plant Simulation 13 或更早版本中创建的模型，初始值因版本而异。）

若之后还需访问保存的值，请改用对象 `Variable`（参见全局变量）。

### Data Types in Local Variables（局部变量中的数据类型）

可用数据类型：`Integer`、`Real`、`Length`、`Speed`、`Acceleration`、`Weight`、`Time`、`Date`、`DateTime`、`Json`、`Boolean`、`String`、`Object`、`Table`、`List`、`Stack`、`Queue` 和 `Any`。

- 对 `stack`、`queue`、`list`、`table` 需在方括号 `[data type]` 中填写列的数据类型。这些局部变量与插入 Frame 的对象不同，它们只提供 **Instantiation、State、Access、Order** 的内置方法。

| 数据类型 | 共享内置属性的对象 |
| --- | --- |
| List | DataList |
| Queue | DataQueue |
| Stack | DataStack |
| Table | DataTable |

- 首次访问这些数据类型前，需用 `create` 创建局部变量或为其赋值。

```simtalk
var l: list[string]
l.create
l.insert(1,"Hello")
```

**初始值：**

| 数据类型 | 初始值 |
| --- | --- |
| integer、real、length 等 | `0` |
| boolean | `false` |
| string | `""` |
| object | `void` |
| time | `0:00:00` |

### Declare Local Variables in the Source Code（在源码中声明局部变量）

- 以关键字 `var` 开头，后跟一个或多个标识符，之后可加冒号和数据类型。
  ```simtalk
  var x, y: integer
  ```
- 声明时可同时赋值，此时数据类型声明可省略（由所赋的值决定）。
  ```simtalk
  var a: length := Track1.Length
  var b: Length := Track2.Length
  var c: Length := sqrt(a*a + b*b)
  print c
  ```
  ```simtalk
  var a := Track1.length
  var b := Track2.length
  var c := sqrt(a*a + b*b)
  print c
  ```
- 这样声明的变量从其声明行起，到源码末尾均可见。

**循环行为：** 若在循环内声明局部变量，初始值**不会**每次循环都被重置，变量会保留上一次的值；但声明中的赋值会在每次循环时重新执行。

```simtalk
// 循环输出：0 0 --> 1 0 --> 2 0
for var i := 1 to 3
    var x: integer
    var y: integer := 0
    print x, " ", y
    x += 1
    y += 1
next
```

**可见性：** 在 `if` 语句内声明的局部变量，在该语句之后仍可见，即使其中的指令没有执行——此时变量持有初始值（即使声明中带有赋值）。

```simtalk
if 1 = 2
   var x: integer := 1
end
print x  // 输出 0
```

循环同理：若循环因条件一开始就不满足而从未执行，循环内声明的变量在循环后仍可访问并持有初始值。

```simtalk
for var y := 1 to DataTable.yDim
    var i : integer
    i := DataTable[1,y]
next
print i    // 若 DataTable 为空则输出 0
```

### Global Variables（全局变量）

全局变量保存的是**非固定值**，可被任何 Method 访问；Method 执行结束后数据仍然存在。

- 用全局变量（或列表条目）在仿真运行期间长期保存数据。
- Plant Simulation 提供对象 `Variable` 作为全局变量，任何 Method 都可通过名称和绝对/相对路径访问它。
- 如果之后不需要该值，改用局部变量。

```simtalk
MyVariable := Transporter:1.CurrentSpeed  -- 给全局变量 'MyVariable' 赋新值
print MyVariable                          -- 读取该值并打印到控制台
print &MyVariable.DataType       -- 打印 'MyVariable' 的数据类型
var obj : object := &MyVariable  -- 把 'MyVariable' 的引用存入 object 类型的局部变量
```

---

## 4. Parameters（参数）

调用 Method 时可向其传递值（称为**实参 arguments**）。Method 中需声明与实参**数量相同、数据类型相同**的形参。例外：integer 与 real 值会自动转换。

下例中 `x` 是参数名，`123` 是实参值：

```simtalk
param x: integer := 123
```

> **注意：** real → integer 转换时，Plant Simulation 会删除小数点后的数字，可能导致意外行为。通常应避免自动类型转换。

### Declare Parameters（声明参数）

- 参数声明在源码开头，以关键字 `param` 开头，后跟标识符、冒号和数据类型。
- 同一数据类型的多个参数可在单个冒号和数据类型前用逗号分隔列出。
- 不同数据类型的参数用逗号分隔（各自带冒号和数据类型）。

```simtalk
param repeats: integer                           // 单个 integer 参数
param minimum, maximum: real                     // 两个 real 参数
param rpm: real, tool: string                    // 两个不同数据类型的参数
param workpiece: string, Islength, shorten: real // 三个不同数据类型的参数
```

- 参数用法与局部变量相同，初始值由调用者设置。
- 在参数前加关键字 `byref` 可传递**引用**而非值——对参数的修改会影响到调用者。
- 对 `stack`、`queue`、`list`、`table` 只需填写数据类型（无需额外的类型参数）。

```simtalk
param order: list                                 // 任意类型的 DataList
param orders, deliveries: queue                   // 两个任意类型的 DataQueue
param cost: table, VAT: real, complaints: stack   // DataTable 与 DataStack 混合声明
```

**可选参数（Optional parameters）：**

```simtalk
param maxValue:real := 1.0 -> real                // 可选参数
return z_uniform(0,maxValue)
```

**函数返回值（Function result）** —— 无参数时仅声明返回类型；也可带参数：

```simtalk
-> boolean // 无参数
// 或带参数
param v1,v2: integer, name: string -> boolean
```

### Declare Default Arguments（声明默认参数）

SimTalk 2.0 支持默认参数（可选参数/可选实参）。若调用 Method 时未传该实参，参数取默认值。

```simtalk
param x: integer := 123
```

该方法可带实参调用，也可不带；不带时 `x` 的值为 `123`。

若某个参数有默认参数，则**其后的所有参数都必须有默认参数**。

```simtalk
param a: string,
      b, c: string := "",
      d: boolean := true
```

该方法可用一至四个实参调用（但不能零个，因为 `a` 没有默认值）：

```simtalk
Method("A")
Method("A", "B")
Method("A", "B", "C")
Method("A", "B", "C", false)
```

**默认参数允许的值：**

- 只接受常量值：数字、字符串常量、`true`、`false`、`void` 和 `pi`。
- 数据类型为 `object`、`table`、`list`、`stack`、`queue`、`any` 的参数只能以 `void` 为默认值。
- 数据类型为 `date` 和 `dateTime` 的参数**不能**有默认参数。
- 数据类型为 `array` 的参数可用空数组 `[]` 或空 JSON 对象 `{}` 作为默认值。
- 引用参数（`byref`）**不能**有默认参数。

### Declare the Function Result of a Method（声明方法的返回值）

Method 可以像函数一样返回结果：指定 `->`（减号 + 大于号）后跟数据类型。若函数需要参数，把参数写在 `->` 返回值声明之前。

- 函数只返回**一个**结果。
- 在函数内部把结果赋给返回值 `result`；Plant Simulation 会把其内容返回给调用者。

示例：

```simtalk
-> real                                     // 无参数函数，计算 real 值

param CustomerNo:integer
-> string                                   // 带参数函数，返回 string

param orders,deliveries: list, delivery_date: time
-> table                                    // 带多个参数的函数，返回 table
```

> **注意：** 除了 `result`，也可用 `return` 结束 Method。

对于 `stack`、`queue`、`list`、`table`，局部变量 `result` 初始为空——访问前需先赋值或调用 `create`。

---

## 关键要点速记

- **命名空间**内名称必须唯一；跨命名空间可重名，靠路径区分。
- **常量**：Integer 范围约 ±9.22×10¹⁸；Real 靠小数点识别、指数范围 `[307, -307]`；String 最多 1024 字符、用 `\` 转义引号/换行/反斜杠；time/date/dateTime 无常量值。
- **局部变量**每次 Method 调用新建一套，仅在声明它的 Method 内可见，需先声明后使用；循环内声明不重置初始值，`if`/循环内声明的变量在块外仍可见（未执行时持初始值）。
- **全局变量**用对象 `Variable` 保存，可长期跨 Method 访问。
- **参数**以 `param` 声明，数量与类型需与实参匹配（integer/real 会自动转换，建议避免）；`byref` 传引用。
- **默认参数**（SimTalk 2.0）：只接受常量值，某参数有默认值时其后所有参数也须有默认值；object/table/list/stack/queue/any 默认只能为 `void`，date/dateTime 不能有默认值，`byref` 不能有默认值。
- **函数返回值**用 `-> 类型` 声明，只返回一个结果，通过 `result`（或 `return`）返回。
