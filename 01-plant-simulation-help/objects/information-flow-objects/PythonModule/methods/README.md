# PythonModule 方法（Methods）总结

本目录整理了 Plant Simulation 中 **PythonModule** 对象的方法文档。内容来源为同目录下的 `methods.md`（另有原始文本 `methods.txtx`，内容一致）。本目录下没有子文件夹，因此不存在子文件夹中的 README.md。

## 概述

PythonModule 提供：

- 左侧目录中列出的方法。
- 「所有对象的方法（Methods of All Objects）」。

可以通过 **Show Attributes and Methods** 窗口查看对象的所有方法、只读属性和属性：

- 在类库（Class Library）上下文菜单中选择 **Show Attributes and Methods**，查看所选类的一般描述。
- 选中实例后按 **F8**，或点击 Frame 的 Home 功能区的 **Show Attributes and Methods**，查看所选实例的一般描述。

## 语法行约定

方法语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法所作用对象的路径。
- 括号内为方法签名，由参数标识符和数据类型组成，例如 `(Parameter:string)` 表示字符串类型参数。
- 方括号 `[ ]` 内为可选参数。
- `:=` 后面为参数的默认值。
- 箭头 `->` 后面为方法返回值的数据类型。

> **注意：** 嵌套括号表达式必须正确输入括号，否则可能导致意外结果并打开调试器（Debugger）。

## 方法列表

### call [SimTalk]

从 SimTalk 执行 `<Path>` 所指定 PythonModule 的 Python 代码。

- **语法：** `<Path>.call([functionName:string, ...]) -> any`
- **参数：** `functionName`（string）—— 要执行的函数代码。
- **返回值：** `any`
- **示例：**
  ```python
  def multiply(a, b):
      return a*b
  ```
  ```simtalk
  print MyPythonModule.call("multiply", 3, 4)
  ```
- **另见：** callKw [SimTalk]

### callKw [SimTalk]

从 SimTalk 执行指定 Python 代码，支持关键字参数。

- **语法：** `<Path>.callKw([functionName:string, ..., KeyValuePairs:any[] ]) -> any`
- **参数：**
  - `functionName`（string）—— 要执行的函数代码。
  - `KeyValuePairs`（any）—— 关键字参数，以「关键字 + 值」成对组成的数组指定。
- **返回值：** `any`
- **示例：**
  ```simtalk
  print MyPythonModule.call("multiply", 3, 4)
  print MyPythonModule.callKw("multiply", ["a", 3, "b", 4])
  ```
- **另见：** call [SimTalk]

### callMethod [SimTalk]

调用 `<Path>` 所指定 PythonModule 的方法。

- **语法：** `<Path>.callMethod(VariableName:string, MethodName:string[, Argument:any, ...]) -> any`
- **参数：**
  - `VariableName`（string）—— Python 变量名。
  - `MethodName`（string）—— SimTalk 方法名。
  - `Argument`（any，可选）—— 附加参数。
- **返回值：** `any`
- **示例：** 返回字符串 `"Sum=35m"`。
  ```simtalk
  print PyClassMethod.callMethod("vp", "getSumString", "Sum=", "m")
  ```
- **另见：** callMethodKw [SimTalk]

### callMethodKw [SimTalk]

调用 `<Path>` 所指定 PythonModule 的方法，支持位置参数和关键字参数。

- **语法：** `<Path>.callMethodKw(VariableName:string, MethodName:string[, Positionargument:any, ...] [, Keywordargument:any[] ]) -> any`
- **参数：**
  - `VariableName`（string）—— Python 变量名。
  - `MethodName`（string）—— SimTalk 方法名。
  - `Positionargument`（any，可选）—— 附加位置参数。
  - `Keywordargument`（any，可选）—— 附加关键字参数。
- **返回值：** `any`
- **示例：** 返回字符串 `"Sum=35m"`。
  ```simtalk
  print PyClassMethod.callMethodKw("vp", "getSumString", ["prefix", "Sum=", "suffix", "m"])
  print PyClassMethod.callMethodKw("vp", "getSumString", "Sum=", ["suffix", "m"])
  ```
- **另见：** callMethod [SimTalk]

### get [SimTalk]

返回 `<Path>` 所指定 PythonModule 的 Python 变量的值。

- **语法：** `<Path>.get(VariablenName:string) -> any`
- **参数：** `VariableName`（string）—— Python 变量名。
- **返回值：** `any`
- **备注：** `get` 只把能转换到 SimTalk 数据类型（string、real、integer、boolean、time、date、dateTime）的 Python 类型进行转换；其他 Python 类型以 SimTalk 的 `any` 类型返回，从而可继续访问该 PythonModule。
- **示例：**
  ```simtalk
  var po = PythonModule.get("vp")
  print po.get("Val1") // -> 12
  print po.get("Val2") // -> 23
  print po.callMethod("getSumString", "Sum=", "m") // 返回 "Sum=35m"

  var calcArea = PythonModule.get("calcArea")
  print calcArea.call(3, 4)

  var valList = PythonModule.get("valList")
  print valList.call(__len__) // -> 3
  print valList[1]            // -> 2

  var valDict = PythonModule.get("valDict")
  print valDict["Col1"]       // 返回 [None, 12]
  valDict["Col1"] = [11,12]
  print valDict["Col1"]       // 返回 [11, 12]
  ```

### import [SimTalk] - Python

将 `<Path>` 所指定 PythonModule 的模块导入 Python 解释器。

- **语法：** `<Path>.import → void`
- **返回值：** `void`
- **示例：**
  ```python
  import keyword
  print("The list of keywords is : ")
  print(keyword.kwlist)
  ```
- **另见：** Import [button] - PythonModule

### importPythonModule [SimTalk]

在 `<Path>` 所指定的 PythonModule 中访问另一个 Plant Simulation PythonModule 的方法和属性。

- **语法：** `<PlantSimulation-Path>.importPythonModule(Plant Simulation PythonModule) -> Python module object`
- **参数：** `Plant Simulation PythonModule` —— Plant Simulation PythonModule 的名称。
- **返回值：** Python 模块对象（Python module object）。
- **示例：**
  ```python
  import PlantSimulation as ps
  mm = ps.importPythonModule(current.MathModule)
  print(mm.multiply(3,4))
  ```

### set [SimTalk]

设置 `<Path>` 所指定 PythonModule 的 Python 变量的值。

- **语法：** `<Path>.set(VariableName:string, Value:any)`
- **参数：**
  - `VariableName`（string）—— Python 变量名。
  - `Value`（any）—— Python 变量的值。
- **示例：**
  ```simtalk
  PythonModule.set("BatchSize", 40)
  ```
- **另见：** get [SimTalk]

## 只读属性（Read-Only Attributes）

PythonModule 提供「所有对象的只读属性（Read-Only Attributes of All Objects）」。

- 只读属性的值可以查询，但不能设置，因为其值由 Plant Simulation 在查询时刻计算得出。
- 大多数只读属性对应对象标签页上的某个不可用对话框项，例如 Statistics 标签页。
- 查询示例：
  ```simtalk
  print MyPythonModule.UUID
  ```

## 快速索引

| 方法 | 用途 | 返回值 |
| --- | --- | --- |
| `call` | 从 SimTalk 执行 Python 代码 | `any` |
| `callKw` | 从 SimTalk 执行 Python 代码（关键字参数） | `any` |
| `callMethod` | 调用 Python 对象的方法 | `any` |
| `callMethodKw` | 调用 Python 对象的方法（位置/关键字参数） | `any` |
| `get` | 获取 Python 变量的值 | `any` |
| `import` | 导入 Python 模块到解释器 | `void` |
| `importPythonModule` | 访问另一个 PythonModule 的方法和属性 | Python module object |
| `set` | 设置 Python 变量的值 | — |
