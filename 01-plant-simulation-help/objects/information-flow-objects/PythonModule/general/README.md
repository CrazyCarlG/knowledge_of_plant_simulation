# PythonModule 对象 — General（总览）

本目录包含 **PythonModule 对象**（信息流对象）的通用说明。文档描述的是 PythonModule 对象本身，即在 Plant Simulation 模型中使用 Python 代码并可从 Python 代码内部完全访问 Plant Simulation 对象模型。

> 源文件：`general.md`（内容详见该文件）；原始导出文本：`general.txtx`。

## 概述

**PythonModule** 是一个用于在 Plant Simulation 模型中编写和执行 Python 代码的容器，通过它可以在 Python 代码中完全访问 Plant Simulation 对象模型。

- 需要计算机上安装 **CPython**（推荐 <https://www.python.org/> 官方发行版；Anaconda 安装的版本也可用）。
- 支持 Python 版本：**3.12、3.13、3.14**。
- 使用多个 Python 环境时，可用 SimTalk 函数 `setPythonDLLPath` 指定 Python DLL 路径。
- 提供内置属性 **`PythonCode`**（数据类型 string），用于从 SimTalk Method 获取/设置 Python 源代码。
- 通过 SimTalk 方法 **`call`** 和 **`callKw`** 从 SimTalk 运行 Python 代码。
- Python 代码**不替代 SimTalk**：SimTalk 访问编译后的内置函数，通常比 Python 更快；但 Python 凭借大量库和普及度，让编程更简单。

## 使用 Python 库的限制

- 使用 **Pandas / NumPy** 等库时，应**直接退出 Plant Simulation**，而不是只关闭模型再打开新模型——关闭模型会反初始化 Python 解释器，重新打开并复用这些库可能崩溃（它们不支持重新初始化）。
- **MatPlotLib** 等库可能打开一个会启动新 Windows 消息泵的窗口；再次与 Plant Simulation 交互前先关闭该窗口，否则可能崩溃。
- 将鼠标悬停在 PythonModule 上可显示工具提示。

## 添加到模型

1. 在 Home 功能区选项卡点击 **Manage Class Library > Basic Objects > Information Flow > PythonModule**，将其加入 Class Library。
2. 将 PythonModule 对象插入模型 Frame，打开其对话框，输入 Python 代码并执行。
3. 添加后，PythonModule 会在 **Tab Content** 上显示全局 Python 变量。

## 上下文菜单

在 Tab Content 中右键显示上下文菜单（点击 **Import** 后再选择菜单命令）：

- **Show White Space** — 显示单词之间的空格。
- **Show Global Variables** — 打开对话框显示该 PythonModule 中使用的全局变量。

## 使用 PythonModule 能做什么

Python 是高级语言且拥有大量库，例如可用于提取仿真结果、用 Python 库做大规模数据处理、以各种图表显示数值。

- 点击 PythonModule 对话框右上角的 **Import**，或将光标置于 Tab Content 上按 **F5**，即可把代码导入 Python 解释器。
- 点击 Import 或按 F5 时，Plant Simulation 自动应用源代码。
- 从 SimTalk 调用 Python 代码使用 `call` 和 `callKw`：

```simtalk
<Path>.call([functionName:string, ...]) -> any
<Path>.callKw([functionName:string, ..., KeyValuePairs:any[] ]) -> any
```

调用 PythonModule 中定义的函数时，第一个参数为函数名，其后为传给 Python 的参数。例如 Python 代码为：

```python
def multiply(a, b):
    return a*b
```

在 SimTalk Method 中执行：

```simtalk
print MyPythonModule.call("multiply", 3, 4)
```

以关键字参数调用时使用 `callKw`，关键字参数以 键/值 对数组传入：

```simtalk
print MyPythonModule.callKw("multiply", ["a", 3, "b", 4])
```

> **注意：** 确保模型设置中 **Prohibit Access to the Computer** 已清除；Python 错误消息以英文显示（不本地化）。

用 PythonModule 中的 Python 代码还可以：

- 从 Python 代码访问模型 Frame
- 从 Python 代码访问属性和方法
- 从 Python 代码访问 DataTable
- 从 Python 代码访问变量
- 从 Python 代码调用全局 SimTalk 函数
- 执行外部 Python 代码

此外还可以在 **HtmlReport** 中显示 PythonModule。

## 对话框（Dialog Box）

双击 PythonModule 图标打开对话框：

- **Edit Simulation Properties** — 修改仿真属性（共享属性见 "Dialog Items of the Objects"）。
- **Edit Animation Properties** — 通过 **Edit 3D Properties** 按钮（仿真属性对话框左下角）或选中对象后按空格键编辑 3D 属性；在 Edit 功能区选项卡点击 **Show Manipulators** 或按 **M** 键操作图形。

### Import [button]

点击此按钮将代码导入 Python 解释器并执行：

- 按住 **Shift** 点击 Import：重新加载模块并删除所有全局变量。
- 按住 **Shift + Ctrl** 点击：将该模块的 import 语句复制到剪贴板。

SimTalk 等价命令：`import [SimTalk] - Python`。

## Tab Content

添加 PythonModule 到模型后，Tab Content 会显示全局 Python 变量，在此输入要执行的 Python 代码。点击 **Import** 将其导入解释器。

> **注意：** 文件夹模型中 Python 代码保存在单独的 `.py` 文件里，Python 变量 `__file__` 包含该 `.py` 文件路径；若非文件夹模型，`__file__` 未定义。

### 从 Python 代码访问模型 Frame

使用全局 Python 变量 `basis`、`root`、`current`、`self`：

- **basis** — 引用 Class Library 的根。与 SimTalk 不同，Python 路径不能以句点 `.` 开头，因此绝对路径从 `basis` 开始：`print(basis.Models.Model.Station)`。
- **root** — 表示 Frame 层次结构的根（包含 EventController 的 Frame）：`print(root.EventController)`。
- **current** — 表示插入该 PythonModule 的 Frame：`print(current.Station)`。
- **self** — 表示 PythonModule 本身。

> **注意：** 与 SimTalk 不同，Python 中必须指定对象路径。

### 从 Python 代码访问属性和方法

使用与 SimTalk 相同的语法。

访问属性：

```python
print(current.Station.ProcTime)
current.Station.ProcTime = 50
```

访问方法：

```python
current.MyStation.deleteObject
print(current.Station.succ())
print(current.Station.succ(1))
```

- 若方法接受参数（即使全部可选），也必须使用括号调用。
- 从 Python 执行 SimTalk Method，使用 Method 对象的 `execute` 方法：

```python
current.MyMethod.execute()
current.MyMethod.execute("Test", 123)
print(current.MyMethod.execute("Test", 123))
```

### 从 Python 代码访问 DataTable

使用 Python 索引访问单元格。访问第 2 列第 3 行：

```python
print(root.DataTable[2,3])
```

- 上述代码返回包含行值的列表；若某个索引是切片，Plant Simulation 始终返回包含行值的列表：`print(current.DataTable[1:, 2])`。
- `print(current.DataTable[1:2, 1:2])` 返回单元格 `[1,1]` 的值——当为列和行都指定范围时，返回列表的列表。
- 获取整个 DataTable 内容：`print(root.DataTable[None])`。若 DataTable 有唯一列索引，返回以列索引为键的字典；否则返回包含行值的列表的列表。
- 也可使用 Python 切片获取部分数据。

> **注意：** Python 代码中 `#` 表示到行尾的注释。

### 从 Python 代码访问变量

使用 Variable 的属性 `Value`：

```python
print(root.Variable.Value)
root.Variable.Value = 42
```

### 从 Python 代码调用全局 SimTalk 函数

先导入 `PlantSimulation` 模块，再调用 Plant Simulation 提供的预定义函数：

```python
import PlantSimulation as ps
x = ps.existsObject(".Models.Model.EventController")
print(x)
```

### 调用另一个 PythonModule 中编写的函数

从一个 PythonModule 调用另一个 PythonModule 中编写的函数：

1. 在 PythonModule1 中调用 `print(__name__)`，将模块名打印到 Console。
2. 从 Console 复制该字符串，粘贴到要执行它的 PythonModule 的 `import` 关键字之后。
3. 点击 **Import**，乘法结果将打印到 Plant Simulation Console。

### 执行外部 Python 代码

使用 SimTalk 函数 `executePythonFile` 执行外部文件中的 Python 代码：

```simtalk
print executePythonFile("D:\test.py", "TestArg")
```

访问 Plant Simulation 模型中对象的方式与使用 PythonModule 执行 Python 代码相同。

## Tab User-defined

按 "Tab User-defined" 所述定义自己的属性。对话框提供 **Callback** 方法作为用户自定义属性。

## Navigate 菜单 / View 菜单 / Tools 菜单 / Help 菜单

- 命令在相应菜单小节中描述。
- View 菜单提供 **Refresh** 和 **Show Attributes and Methods**（SimTalk：`updateDialog`）。
- Tools 菜单和 Help 菜单的命令在各自小节中描述。

## PythonModule 的方法

PythonModule 提供：

- 目录表中列出的方法。
- 所有对象的通用方法（*Methods of All Objects*）。

查看所有方法、只读属性和属性，打开 **Show Attributes and Methods**：

- 在 Class Library（Class）的上下文菜单中选择 **Show Attributes and Methods**。
- 在 Frame（Instance）中按 **F8** 或点击 Home 功能区选项卡上的 **Show Attributes and Methods**。

## 参见

- New Syntax [command]
- SimTalk 2.0 and SimTalk 1.0 Compared
- A Quick Tour Through SimTalk 2.0
- General Access to SimTalk
- What You Can Do With the PythonModule
- View the Sample Models
- setPythonDLLPath [SimTalk]
- executePythonFile [SimTalk]
- DataTable [object]
- Variable [object]
- Value [SimTalk] - Variable
- Predefined Functions
- import [SimTalk] - Python
- execute [SimTalk] - Method
- Video on YouTube: <https://youtu.be/2QJeW5r1AF4?si=S8Ee2D-4zyOevXZG>
