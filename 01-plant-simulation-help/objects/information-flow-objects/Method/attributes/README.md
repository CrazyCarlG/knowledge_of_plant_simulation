# Method 对象的属性（Attributes）汇总

本目录汇总了 `Method` 对象的属性相关内容。`Method` 对象提供下列属性，外加所有对象共有的属性（*Attributes of All Objects*）。

> 源文件：`attributes.md`（内容详见该文件）；原始导出文本：`attributes.txtx`。

> **注意**：只能通过引用运算符 `&` 访问指向 `Method` 对象自身的属性；不使用 `&` 运算符时，属性会作用于 Method 的**内容**（源代码文本）。

## 如何查看

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性和属性。
- 在已插入实例的 Frame 上按 **F8**，或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，可查看所选实例的方法、只读属性和属性。
- 访问 Method 时使用引用运算符 `&` 或匿名标识符 `self`。

## 属性列表

| 属性 | 说明 | 类型 / 数据类型 |
| --- | --- | --- |
| `NumInExecution` | 返回由引用运算符 `<&>` 指定的 Method 当前正在执行的次数 | 只读属性 / `integer` |
| `Program` | 指定传给由 `<&>` 指定的 Method 的源代码 | 属性 / `string` |
| `RandomSeed` | 设置由 `<&>` 指定的 Method 或数据类型为 `Method`/`RandTime` 的用户定义属性的随机数流 | 属性 / `integer` |
| `UsingNewSyntax` | 为 `<&>` 指定的 Method 激活（`true`）或停用（`false`）SimTalk 2.0 语法 | 属性 / `boolean` |
| `PythonModule` | 用于在 Plant Simulation 模型中调用 Python 代码，并可从 Python 代码内完整访问 Plant Simulation 对象模型 | 对象 |

---

## 1. NumInExecution [SimTalk]

返回由引用运算符 `<&>` 指定的 Method 当前正在执行的次数。

- **类型**：只读属性
- **语法**：`<&>Method.NumInExecution → integer`
- **返回值**：数据类型 `integer`

```simtalk
print &MyMethod.NumInExecution
```

---

## 2. Program [SimTalk]

指定传给由引用运算符 `<&>` 指定的 Method 的源代码。

- **备注**：所赋的源代码会在 Method 下一次被调用时执行。
- **类型**：属性
- **语法**：`<&>Method.Program:string`
- **赋值**：可赋数据类型为 `string` 的值

```simtalk
&MyMethod.Program := "->real return 0.0"
self.Program := "->real return 0.0"
// 下一次调用即使用修改后的指令

var bInherit:boolean // 检查属性 'Program' 是否被激活
getAttribute("Program", bInherit)
print bInherit
```

---

## 3. RandomSeed [SimTalk] — Method / 用户定义属性

设置由引用运算符 `<&>` 指定的 Method 或数据类型为 `Method`/`RandTime` 的用户定义属性的随机数流。

- **类型**：属性
- **语法**：`<&>Method.RandomSeed:integer`
- **赋值**：可赋数据类型为 `integer` 的值

```simtalk
&Method1.RandomSeed := 1313
DataTable.RandomSeed := 101
```

### 备注

- 与物料流对象一样，Plant Simulation 在插入对象时自动分配随机数种子值，因此每个对象都有自己的随机数种子值。
- 在 Method 中调用分布函数时，第一个参数（指定随机数流）是可选的；若省略，则使用该 Method（或数据类型为 `Method` 的用户定义属性）的随机数流。
- 受此影响的分布函数包括：`z_beta`、`z_binomial`、`z_cEmp`、`dEmp`、`z_emp`、`z_erlang`、`z_frechet`、`z_gamma`、`z_geom`、`z_gumbel`、`z_hypgeom`、`z_laplace`、`z_logistic`、`z_logLogistic`、`z_lognorm`、`z_negexp`、`z_normal`、`z_paraLogistic`、`z_pareto`、`z_poisson`、`z_triangle`、`z_uniform` 和 `z_weibull`。
- 仍可像旧版本一样显式传入随机数流参数。公式（Formula）则必须传入，因为公式从不使用周围对象的随机数流。
- Method 随机数流生成的随机数序列与全局随机数流（在 **File > Options > Random Number Seed Values** 中设置）不同，即使种子值相同。
- Plant Simulation 在对象中保存公共种子值；插入对象时自动分配随机数值，但仅当对象能生成随机数（例如 Station 的 Processing Time，或对象具有数据类型为 `Method`/`RandTime` 的用户定义属性）时才如此。否则 `RandomSeed` 被赋值为 `0`。
- 若 `RandomSeed` 为 `0`，该属性不会显示在 **Show Attributes and Methods** 窗口中，也不会写入模型文件夹。为这样的对象创建数据类型为 `Method` 或 `RandTime` 的用户定义属性后，Plant Simulation 也会自动分配随机数值。

### 参见

- Method [SimTalk] — 数据类型
- Formula [distribution]
- Distribution Functions, z_ 函数
- Random Number Seed Values

---

## 4. UsingNewSyntax [SimTalk]

为引用运算符 `<&>` 指定的 Method 激活（`true`）或停用（`false`）SimTalk 2.0 语法。

- **类型**：属性
- **语法**：`<&>Method.UsingNewSyntax:boolean`
- **赋值**：可赋数据类型为 `boolean` 的值

```simtalk
&Method1.UsingNewSyntax := true
```

### 备注

- 点击转换一个源代码用 SimTalk 1.0 记法编写的现有 Method 时，会自动把该源代码转换为正确的 SimTalk 2.0 记法。
- 若 `UsingNewSyntax` 已激活，Method 中的源代码必须使用改进的、简化的 SimTalk 2.0 记法输入。
- 若希望所有新建 Method 都使用 SimTalk 2.0 语法，请在 Class Library 的 Method 类中激活 `UsingNewSyntax`。
- Plant Simulation 会把 `UsingNewSyntax` 的设置写入模型文件。
- 若 `UsingNewSyntax` 停用，Method 中的源代码必须使用 SimTalk 1.0 记法输入。

### 参见

- New Syntax [command]
- SimTalk 2.0 与 SimTalk 1.0 对比
- SimTalk 2.0 快速浏览
- General Access to SimTalk

---

## 5. PythonModule

使用 `PythonModule` 对象可在 Plant Simulation 模型中调用 Python 代码，并可从 Python 代码内完整访问 Plant Simulation 对象模型。

### 要求

- 使用 Python 需要安装 CPython。推荐使用官方 Python 发行版（https://www.python.org/），也可使用通过 Anaconda 安装的 Python 版本。Plant Simulation 支持 Python 3.12、3.13 和 3.14。
- 若使用多个 Python 环境，可用 SimTalk 函数 `setPythonDLLPath` 指定 Python DLL 的路径：

```simtalk
setPythonDLLPath(dllpath:string)
```

例如：

```simtalk
setPythonDLLPath("C:\Program Files\Python312\python312.dll")
```

---

## Method 对象提供的属性

`Method` 对象提供：

- 上表列出的属性。
- 所有对象共有的属性（Attributes of All Objects）。

> **注意**：访问 `Method` 对象自身（而非其内容）的属性时，必须通过引用运算符 `&`。不使用 `&` 运算符时，属性会作用于 Method 的内容（代码文本）。

## 目录内容

- `attributes.md`：Method 属性的说明文档。
- `attributes.txtx`：同内容的原始帮助文本（含页码与版权信息）。
