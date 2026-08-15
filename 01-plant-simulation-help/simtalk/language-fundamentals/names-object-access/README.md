# Names & Object Access（名称与对象访问）

本目录对应 Plant Simulation SimTalk 帮助文档中关于 **命名规范、预定义名称、关键字、匿名标识符与对象路径** 的内容。以下是对 `names-object-access.md` 的总结。

## 目录结构

- `names-object-access.md` — 本节内容的整理版（Markdown）
- `names-object-access.txtx` — 原始帮助文本（源文件）

> 本目录下没有子文件夹，也没有其他 `.md` 或 `README.md` 文件。

## 内容概览

本文档涵盖五个主题：

1. **Names（名称）**
2. **User-defined Names in Methods（方法中的用户自定义名称）**
3. **Predefined Names（预定义名称）**
4. **Keywords（关键字）**
5. **Anonymous Identifiers（匿名标识符）**
6. **Object Paths in SimTalk（对象路径）**

---

## 1. Names（名称）

- Plant Simulation 中所有对象和局部变量都通过 **名称（name）** 或 **路径（path）** 来标识。
- 命名限制：
  - 不能使用 **关键字（keywords）** 作为对象或局部变量的名称。
  - 建议使用自解释名称（如 `.building1`、`forklift`），便于模型维护。
- SimTalk 对方法、属性、只读属性的名称 **通常不区分大小写**（`upper`、`UpPER`、`UPPER` 等价）。
  - 但 **输入的数据本身区分大小写**，字符串比较时会考虑大小写。

## 2. User-defined Names in Methods（方法中的用户自定义名称）

- Plant Simulation 会自动为新对象分配合法名称；在控制方法中需自行命名变量。
- 命名规则：
  - 名称不能以数字开头，可以以字母或下划线 `_` 开头，后续可包含字母、数字、下划线。
    - 合法：`MyStation`、`_MyStation`、`MyStation1`、`My_Station_1`
    - 非法：`1Station`
  - 不能包含 SimTalk 中有特殊含义的字符（`+`、`-`、`*`、`/`、`=`、`<`、`>` 等）。
  - 不能使用关键字、内置函数/方法的名称。
  - 名称不区分大小写。
- 建议使用能标识对象/变量角色的名称，例如：
  ```simtalk
  forklift.destination := .building1.station_1  -- 比 MU1.attrib := .Frame1.Station21 更易读
  ```

## 3. Predefined Names（预定义名称）

预定义方法名在仿真的相应阶段自动执行，对应 EventController **Controls** 选项卡上的 **Reset Simulation** 与 **Start/Stop Simulation** 按钮：

| 名称 | 作用 |
| --- | --- |
| `reset` | 将仿真模型重置到初始状态 |
| `init` | 初始化仿真模型 |
| `autoexec` | 自动启动仿真运行 |
| `endSim` | 结束仿真运行 |

### autoexec
- 打开模型后立即调用，前提是 `autoexec` 方法位于类库（Class Library）中。
- 可创建任意多个 `autoexec` 方法。批量运行时在 `autoexec` 中调用 `startExperiment`。

### autoexecLoadObj
- 加载对象文件（`*.psobj`）或库文件（`*.pslib`）时执行所有名为 `autoexecLoadObj` 的方法类 / 用户自定义 method 属性。
- 触发场景：`loadObjectAs`、**Load Object / Load Object into Folder / Update**、**Manage Class Library** 中新增库。
- **打开模型文件时不执行** `autoexecLoadObj`。
- 可选布尔参数：第 1 个参数为 `true` 表示更新类库、`false` 表示加载对象；第 2 个参数可表示库更新（旧版本号字符串）或新增（空字符串 `""`）。

### endSim
- 仿真运行结束时调用所有 `endSim` 方法，常用于评估并保存运行数据。
- 仿真在 EventController 处理完所有已调度事件、或到达 **End Time** 时结束。
- 调用顺序：按对象插入顺序的 **逆序** 执行；Frame 自身的 `init`/`reset` 在其内部所有对象的 `endSim` 之后执行。
- 剪切/粘贴、Bring to Front / Send to Back 会改变插入顺序，从而改变调用顺序。

### init
- Init 事件是启动仿真时的第一个事件，执行当前模型中所有名为 `init` 的方法。
- **Init 控件（init controls）** 在事件计算之前执行；普通 **init 方法** 在初始事件计算之后执行。
- `init` 方法可带 `integer` 参数 `phase`：`1` 表示对象尚未初始化（可设置故障参数），`2` 表示对象已初始化。

### Init Methods 与 Init Controls 的区别
- **Init control**：物流对象的 `InitCtrl` 属性指向的方法，在对象初始化 **之前** 执行（可修改 WorkerPool 的 Workers to Create 表）。
- **Init method**：名为 `init` 的 Method 对象（可带参数），在所有对象初始化 **之后** 执行。
- 调用顺序：EventController 的 Init 控件 → 其他对象的 Init 控件 → 带参数 `1` 的 init 方法 → 对象初始化 → 带参数 `2` 的 init 方法 → 插入对象的 init 方法 → 模型 Frame 的 init 方法。
- Init 控件与 init 方法均遵循“插入到 Frame 的对象先于 Frame 自身执行，模型 Frame 最后执行”的递归顺序。

### reset
- 点击 **Reset Simulation** 时调用所有 `reset` 方法，同时清空已调度事件列表、将仿真时间归零、删除统计数据并清除故障。
- 注意：Importer 的 Request/Receive/Release Control 在重置时不会被调用；`executeIn` 在 reset 方法中无效（因为事件被删除），应改用 init 方法调度事件。

---

## 4. Keywords（关键字）

- 关键字是 SimTalk 中的保留字，不能用作对象、局部变量或函数的标识符。
- 关键字不区分大小写；在关键字前后添加字母或数字后就不再是关键字（如 `list` 非法，`alist`、`list0` 合法）。
- 函数 `checkID` 可检查某表达式能否作为对象名（考虑所有关键字与函数调用）。
- **所有数据类型也是关键字**：`Acceleration`、`Any`、`Array`、`Boolean`、`Date`、`DateTime`、`Integer`、`JSON`、`Length`、`List`、`Method`、`Object`、`Queue`、`Real`、`Speed`、`Stack`、`String`、`Table`、`Time`、`Weight`。

### 关键字列表
`and`, `basis`, `byref`, `case`, `continue`, `create`, `current`, `div`, `downto`, `else`, `elseif`, `end`, `exitloop`, `false`, `for`, `forget`, `if`, `loop`, `mod`, `next`, `not`, `or`, `param`, `pi`, `prio`, `print`, `repeat`, `result`, `return`, `root`, `rootfolder`, `self`, `stopuntil`, `switch`, `then`, `to`, `true`, `until`, `var`, `void`, `wait`, `waitExpired`, `waituntil`, `when`, `while`

### 部分关键字说明
- **and / or / not**：逻辑运算符。
- **case / switch / when**：`switch` 控制结构。
- **continue**：跳过本次循环剩余部分进入下一次迭代（可用整数 `continue 2` 继续外层循环）。
- **div / mod**：整数除法 / 整数取模。
- **downto / for / next / to**：`for` 循环。
- **else / elseif / if / then / end**：if-else-end-elseif 语句。
- **exitloop**：退出循环（可 `exitloop 2` 指定退出层数）。
- **false / true**：布尔值。
- **forget**：用于 `table`、`list`、`queue`、`stack`、`any` 类型的局部变量。
- **loop**：允许把循环写在单行。
- **param**：声明方法的参数（用 `-> 类型` 声明返回值类型）。
- **prio**：设置 `waituntil`/`stopuntil` 的执行优先级。
- **repeat / until**：repeat 循环。
- **result**：指定方法的返回值。
- **return**：退出方法。
- **stopuntil / waituntil**：挂起方法执行直到条件为真。
- **var**：声明局部变量。
- **wait**：按仿真时间中断执行。
- **waitExpired**：配合 `waituntil`/`stopuntil` 设置时间上限。
- **while**：while 循环。

---

## 5. Anonymous Identifiers（匿名标识符）

匿名标识符使方法更灵活、与上下文无关，可在不同模型中复用而不修改源码。包括：`@`、`?`、`basis`、`current`、`root`、`rootfolder`、`self`。

| 标识符 | 含义 |
| --- | --- |
| `@` | 触发当前控件的 MU（进入或准备离开物流对象的移动单元） |
| `?` | 调用该方法的物流对象或控件（Method），使控件可被多个对象复用 |
| `basis` | 类库（Class Library），仅用于 `=` / `/=` 比较 |
| `current` | 当前 Method 所在的 Frame；也可用于区分同名局部变量与全局变量（`current.name` 为全局） |
| `root` | Frame 层级中最顶层的 Frame，无需知道根 Frame 名称 |
| `rootfolder` | 类库中用于存放被多个对象共享方法的文件夹（`RootFolder` 属性），节省内存、缩短路径 |
| `self` | 当前正在执行的方法；`self.Name` 仅返回方法名；在 method 属性中用 `self.~` 访问其所属对象 |

示例：
```simtalk
@.move(ParallelStation.succ(3))
?.Cont.move(E2)
if location = basis ... end
self.executeIn(60)
self.~.pause := true
```

---

## 6. Object Paths in SimTalk（对象路径）

当对象不在同一 Frame（命名空间）内时，需要加路径来唯一标识。路径由点号分隔的名称序列组成：

```
[.]name[.name.name[...]]
```

方法语法示例：`<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean`
- `<Path>`：方法所作用对象的路径；括号内为参数签名；`[]` 为可选参数；`→` 后为返回值类型。

### 两种路径
- **绝对路径（Absolute path）**：以句点开头（代表类库），后接文件夹、顶层 Frame，再以句点交替连接名称。例：`.Models.MyPlant.Engine_Assembly_Anytown.MyStation`
- **相对路径（Relative path）**：从当前命名空间开始，由内置方法、名称等组合标识。例：`MyPlant.Engine_Assembly_Anytown.MyStation`
- 此外，可通过 **对象引用（object reference）** 访问 `object` 类型变量。

### 绝对路径
- 用于永不改变的方法（如类库中的控制方法）；建模复杂工站时 MU 必须使用绝对路径。
- 拖放时按住 **Shift + Ctrl** 可插入绝对路径。

### 相对路径
- 从当前命名空间（Method 所在 Frame）开始，以匿名标识符、名称或内置方法开头。
- 不同对象中相对路径的起始位置（所在 Frame）详见原文表格，例如物流对象中的 object 属性从“包含该物流对象的 Frame”开始，MU 中的 object 属性从“包含 MU 的物流对象的父 Frame”开始。
- 示例：
  ```simtalk
  Frame1.Station1      -- 访问子 Frame Frame1 中的 Station1
  Location.Station2    -- 从 Frame2 的子 Frame 访问 Frame2 中的 Station2
  ~.Station2           -- 波浪号 ~ 是内置属性 Location 的缩写
  ```
- 可用 `root`、`self`、`RootFolder` 改变相对路径起点；拖放对象到文本框时默认插入相对路径。

### 对象引用（Object Reference）
- `object` 类型变量可接受相对/绝对路径或对象引用，适用于全局/局部变量、形参和 object 类型表格值。
- 对象引用始终指向单个对象；对象重命名后引用仍然有效；删除对象后引用无法解析（即使再插入同名新对象）。
- 以星号 `*` 前缀表示：`*.Models.Model.Station`
- 优点：访问速度更快、对重命名更健壮；需要相对寻址时使用相对路径。

---

## 关键要点速记

- 命名不能以数字开头、不能用关键字/内置函数名、不能含特殊符号，且不区分大小写。
- `reset` / `init` / `autoexec` / `endSim` 是仿真四个阶段对应的预定义方法名。
- Init 控件在对象初始化前执行，init 方法在初始化后执行。
- 关键字是保留字；所有数据类型也是关键字；`checkID` 可校验名称合法性。
- 匿名标识符（`@`、`?`、`current`、`root`、`self` 等）提高方法可移植性。
- 路径分绝对路径（`.` 开头）与相对路径；`*` 前缀表示对象引用。
