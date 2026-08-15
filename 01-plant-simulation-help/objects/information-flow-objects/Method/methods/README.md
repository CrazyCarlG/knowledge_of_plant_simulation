# Method 对象的方法（Methods of the Method）汇总

本文件汇总了 `methods.md` 中关于 **Method 对象内置方法** 的全部内容。Method 对象提供下列方法，外加所有对象通用的方法（*Methods of All Objects*）。

> 源文件：`methods.md`（内容详见该文件）；原始导出文本：`methods.txtx`。

> **注意：** 只能通过引用运算符 `&` 访问指向 Method 对象本身的方法；不使用 `&` 时，方法作用于 Method 的**内容**（源代码）。

---

## 1. 概述

- 访问 Method 会自动执行其源代码。
- 要访问内置方法、只读属性或属性，须使用引用运算符 `&`。
- Method 对象提供下列方法，外加 *Methods of All Objects*。
- 查看所有方法、只读属性和属性：打开 **Show Attributes and Methods**（按 `F8` 或使用 Class Library 的上下文菜单）。

### 语法约定

示例签名：

```
&Method.execute([Argument1:any, ...[, @:object:=@, ?:object:=self]])
```

- 签名由匿名标识符 `&`、方法名和括号中的参数数据类型组成。
- `(Parameter:string)` 表示数据类型为 `string` 的参数；可用所需类型的变量或返回该类型的方法代替常量。
- 可选参数列在方括号中，如 `[,Parameter:boolean]`。
- 默认值出现在签名中参数之后。
- 若方法有返回值，其数据类型出现在箭头 `->` 之后。

---

## 2. 调试器编辑命令

- **Copy** — 复制选中文本到剪贴板。
- **Paste** — 在光标处粘贴剪贴板内容。
- **Delete** — 删除选中文本。

---

## 3. 内置方法一览

| 方法 | 说明 | 返回值 |
|---|---|---|
| `checkArguments` | 检查传入参数的数据类型是否兼容 | — |
| `decrypt` | 解密已加密的 Method | `boolean` |
| `deleteMethCall` | 删除 EventController 中所有已调度的 Method 调用 | — |
| `encrypt` | 加密 Method 源代码 | `boolean` |
| `execute` | 将 Method 作为子程序运行 | — |
| `executeIn` | 经过指定秒数后调用 Method | — |
| `executeNewCallChain` | 处理完所有活动调用链后运行 Method | — |
| `hasSyntaxError` | 判断源代码是否有语法错误 | `boolean` |
| `load` | 从 ASCII 文本文件加载源代码 | `boolean` |

---

## 4. 方法详解

### 4.1 checkArguments [SimTalk]

检查传入 Method（由 `&` 指定）的参数是否具有兼容的数据类型。

- **用途：** 用于确保对话框中输入的值可以传给 Method。
- **语法：** `<&>Method.checkArguments([Argument1:any, ...])`
- **参数：** 可选 `Argument`（数据类型 `any`）—— 要检查的参数。

```simtalk
&MyMethod.checkArguments(42, void)
```

---

### 4.2 decrypt [SimTalk]

解密之前被加密的 Method（由 `&` 指定）。

- **语法：** `<&>Method.decrypt(Key:string) → boolean`
- **参数：** `Key`（string）—— 密码。
- **返回值：** `boolean`

```simtalk
&MyMethod.decrypt("zTrqYa8%e")
```

**参见：** Encrypt Method

---

### 4.3 deleteMethCall [SimTalk]

删除 EventController 中所有已调度的 Method（由 `&` 指定）调用。

- **用途：** 删除不再需要的调用。
- **语法：** `<&>Method.deleteMethCall`

```simtalk
&MyMethod.deleteMethCall // 删除所有已调度的 Method 调用
```

**参见：** executeIn

---

### 4.4 encrypt [SimTalk]

加密 Method（由 `&` 指定）的源代码。

- **语法：** `<&>Method.encrypt(Key:string) → boolean`
- **参数：** `Key`（string）—— 密码。
- **返回值：** `boolean`

```simtalk
&MyMethod.encrypt("zTrqYa8%e")
```

**参见：** Decrypt Method

---

### 4.5 execute [SimTalk] — Method

将 Method（由 `&` 指定）作为子程序运行。

- **备注：**
  - 调用方 Method 的执行会中断，直到被调用的 Method 完成。
  - 当 Method 的路径存储在数据类型为 `object` 的变量中时尤其方便。
- **语法：** `<&>Method.execute([Argument1:any, ... ][, @:object=@, ?:object=self])`
- **参数：** 可选 `Argument`（any）—— 要执行的参数。若额外给出两个 `object` 类型的可选参数，则 `@` 被赋给匿名标识符 `@`，`?` 被赋给 `self`。

```simtalk
Variable := &MyMethod1      // 变量数据类型为 object
Variable.execute            // 执行 MyMethod1
&MyMethod2.execute("abc")   // 执行 MyMethod2，它需要一个 string 类型参数
self.execute(n+1)           // 递归调用一个 Method
```

> **注意：** 从 Python 调用时，`execute` 像公式一样运行，因此不能在 Method 中移动或删除 MU，也不能使用 `wait`、`waituntil`、`stopuntil` 指令；Plant Simulation 也不会显示 Method Debugger 的 Expressions 选项卡。

```python
# 从 Python 调用 myMethod
res = current.myMethod.execute()
print(res)
```

**参见：** Run [button] — Method、Tab Expressions [Watch window]

---

### 4.6 executeIn [SimTalk]

在经过指定的仿真秒数后，调用由 `&` 指定的 Method（或数据类型为 `method` 的用户自定义属性）。

- **备注：**
  - Plant Simulation 在当前仿真时间加 `CallAt` 的时刻，向 EventController 的已调度事件列表写入一个 `MethCall` 事件。
  - `CallAt` 必须 `>= 0`。若该时刻已有事件，则 `MethCall` 追加到现有同时事件末尾。
  - 在被调用的 Method 中，`?` 引用调用方；`@` 引用 EventController。
- **语法：**
  - `<&>Method.executeIn(CallAt:time[, Argument1:any, ...])`
  - `<&>Method.executeIn(CallAt:dateTime[, Argument1:any, ...])`
- **参数：** `CallAt`（以秒为单位的时间，或 `dateTime` 值）指定何时调用 Method。可选 `Argument1, ...` 在调用时传给 Method。

```simtalk
&MyMethod1.executeIn(23.5)
// 5 秒后将引擎节流到 85%
&ThrottleEngine.executeIn(5, 0.85)
// 2025 年元旦午夜，年-月-日记法
&MyMethod2.executeIn(str_to_date("2025/12/31"))
// 2025 年元旦午夜，日-月-年记法
&MyMethod2.executeIn(str_to_date("31.12.2025"))
// 用局部变量引用调用 Method，并传入两个参数
var obj: object := &MyMethod3
obj.executeIn(4, "my string", true)
```

**参见：** deleteMethCall、executeNewCallChain、List of Events

---

### 4.7 executeNewCallChain [SimTalk]

在 Plant Simulation 处理完所有活动调用链之后，运行由 `&` 指定的 Method。

- **备注：**
  - 与 `&Method.executeIn(0)` 类似，但不同：`executeIn` 需要 EventController，且用 `executeIn(0)` 调度的 Method 只在已调度的同时事件之后运行。
  - 若用 `executeNewCallChain` 调度的 Method 触发了控件，被中断的 Method 只在这些控件完成后才继续；新 Method 在控件之后、被中断的 Method 恢复之前运行。
  - 在被调用的 Method 中，`?` 引用调用方（或数据类型为 `method` 的用户自定义属性所在位置）。
- **语法：** `<&>Method.executeNewCallChain([Argument1:any, ...][,@:object:=@, ?:object:=self])`
- **参数：** 可选 `Argument1`（any）及其后参数 —— 要执行的参数。若额外输入两个 `object` 类型的可选参数，则 `@` 被赋给 `@`，`?` 被赋给 `self`。

```simtalk
var o : object := .Models.Model.&MyMethodWithoutParameters
o.executeNewCallChain
```

**参见：** `&`（引用运算符）、executeIn

---

### 4.8 hasSyntaxError [SimTalk]

返回由 `&` 指定的 Method 源代码是否存在语法错误。

- **备注：** 也适用于数据类型为 `method` 的用户自定义属性。
- **语法：** `<&>Method.HasSyntaxError([byref ErrorMessage:string, byref Line:integer]) → boolean`
- **参数：**
  - 可选 `ErrorMessage`（string）—— 接收错误消息的局部变量（无错误时为空字符串）。
  - 可选 `Line`（integer）—— 接收错误所在行号的局部变量。
- **返回值：** `boolean`

```simtalk
var NewSourceCode: string := prompt  -- 用户输入
&MyMethod.Program := NewSourceCode   -- 赋新源代码
if &MyMethod.HasSyntaxError
   print "syntax error"
else
   MyMethod   -- 调用 Method 并执行新源代码
end
```

---

### 4.9 load [SimTalk] — source code

将 ASCII 文本文件的内容作为源代码加载到由 `&` 指定的 Method 中。

- **语法：** `<&>Method.load(FileName:string) → boolean`
- **参数：** `FileName`（string）—— 文本文件名。
- **返回值：** `boolean`

```simtalk
&MyMethod.load("C:\Users\Ralf\sourcecode.txt")
```

**参见：** Import from File

---

## 5. Method 对象的只读属性（Read-Only Attributes）

Method 提供目录中列出的只读属性，外加 *Read-Only Attributes of All Objects*。

> **注意：** 只能通过引用运算符 `&` 访问指向 Method 对象本身的只读属性。可以查询它们的值，但不能设置 —— Plant Simulation 在查询时刻才计算该值。

查看所有属性：打开 **Show Attributes and Methods**（`F8`）。

示例查询：

```simtalk
print &Method.Encrypted
```

---

## 相关主题（Related Topics）

- Methods of the Method（本文件）
- Read-Only Attributes of the Method
- Attributes of the Method
- Method（信息流对象）
- Encrypt Method / Decrypt Method
- executeIn / executeNewCallChain / deleteMethCall
