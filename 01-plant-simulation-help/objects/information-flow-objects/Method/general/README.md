# Method 对象 — General（总览）

本目录包含 Method 对象（信息流对象）的通用说明。文档描述的是 **Method 对象本身**；SimTalk 编程语言的详细内容见 *SimTalk Reference*。

> 源文件：`general.md`（内容详见该文件）；原始导出文本：`general.txtx`。

## 概述

Method 是用于编写自定义程序例程的容器。通过组合**内置方法**、**关键字**、**赋值**和**控制结构**，可以构建自己的例程，从而精确修改对象行为以适配建模需求。

- 可编写**用户自定义方法**修改对象行为。
- 内置属性、大量内置方法以及**继承策略**有助于快速构建有效模型。
- **Copilot** 可辅助编写 Method 中的源代码。
- Method 功能位于 **Edit 功能区选项卡**和 **Tools 功能区选项卡**。
- Method 编辑器偏好设置：**File > Preferences > Editor**。
- 模拟运行时调用 Method 的设置：**File > Model Settings/Preferences > Simulation > Methods**。
- Method 及数据类型为 `Method` 的用户自定义属性拥有独立的**随机数流**（通过属性 `RandomSeed` 设置），插入对象时自动分配。
- 可在 **HtmlReport** 中显示 Method 的返回值。
- 悬停 Method 可显示工具提示（用户自定义属性、源代码注释或 "Suspended Method"）。
- 使用 **Profiler** 记录 Method 的运行时间和调用频率，定位性能瓶颈。
- 修改图形长度/锚点：在 Edit 功能区选项卡点击 **Show Manipulators** 或按 **M** 键。

### 添加到模型

点击 Home 功能区选项卡上的 **Manage Class Library > Basic Objects > InformationFlow > Method**。

## Method 编程

双击 Frame 中的 Method 图标即可打开并输入源代码。Method 的结构分为若干部分，可删除或省略不需要的部分。

一个用作 **Exit Control** 的 Method 示例：

```simtalk
// My Tooltip. My text, my text, my text, ...
param Sender:object
if Sender /= void
   @.move(Sender)
   return
end
var MUName:string := @.Name
if MUName = "A"
   @.move(1) // parts named 'A' will be moved to the first successor
else
   @.move(2) // parts named 'B' will be moved to the second successor
end
```

### Method 的组成部分

1. **参数（Parameters）** — 以 `param` 关键字开头，不需要时可省略。
2. **返回值（Return Value）** — 若 Method 返回结果，输入返回值的数据类型。
3. **局部变量（Local Variables）** — 按名称和数据类型声明，不需要时可省略。
4. **源代码（Source Code）** — Method 执行的代码：内置方法、赋值、控制结构、方法调用、分支和循环。

注释使用 `//` 或 `--`。注意：SimTalk 通常**不区分**方法、属性和只读属性名称的大小写；点击 **Edit > Reformat** 检查分支/循环语法。

## 在 Method 窗口中工作

双击 Method 图标打开窗口，可输入、运行和调试源代码。窗口提供对 **Method Editor** 和 **Method Debugger** 的访问。

- 点击 Tools 功能区选项卡的 **Debug** 或按 **F11** 切换到 Method Debugger；点击调试工具栏的 **Step** 按钮返回 Method Editor。
- 双击选词，三击选整行；**Ctrl+A** 全选，**Ctrl+C** 复制，**Ctrl+V** 粘贴。
- 复制的源代码以 **RTF 文本**（加纯文本）放入剪贴板，可带 SimTalk 颜色高亮粘贴到合适程序（如 MS Word）。
- 类断点随源代码一起复制；插入实例时应用 Method 类的类断点。
- **Export to File** 可选择文本格式，选择 **HTML Files** 或 **RichText Files** 以保留颜色高亮。
- 拖放移动文本；**Ctrl+Z** 撤销；**Ctrl+Y** 重做。
- 用反斜杠 `\` 插入长代码行的换行（仍作为单个整体解释）。

### 注释

- 单行注释：`//`（到行尾结束）。
- 多行注释：`/* ... */`。
- 注释显示为绿色，不影响模拟速度。
- 不能在字符串值（引号内）中放置注释。

### 断点（Method 窗口内）

- **类断点**：在行标记区单击鼠标中键/滚轮。
- **实例断点**：按住 **Shift** + 中键/滚轮。
- 激活某行断点：按住 **Ctrl** + 中键，或按 **Ctrl+F9**。
- 打开 **Breakpoint Settings**：**Ctrl+B**。
- 悬停断点显示工具提示（非活动时总是显示；若配置了 Start Time 和 Condition 也一并显示）。

### 其他快捷键

- 水平滚动：按住 **Shift** + 滚动鼠标滚轮。
- 运行 Method：**F5**；调试 Method：**F11**。
- 字体大小：按住 **Ctrl** + 滚轮（应用于所有打开的 Method 窗口）；或 **Ctrl + +**（增大）、**Ctrl + 0**（重置为 10 pt）、**Ctrl + -**（减小）。
- 在 Edit/Tools 功能区选项卡选择行号、关键字高亮和缩进。
- 全局 SimTalk 显示设置：**File > Preferences > Editor**。
- 标题栏中的星号 `*` 表示有未应用的更改；在 Edit 功能区选项卡点击 **Apply changes**。

## 调用 Method

Method 可通过以下方式调用：

- **直接调用**：点击 Tools 功能区选项卡的 **Run**（先应用更改）；按 **F5** 后 **F7** 等效。若需传参，Plant Simulation 会打开 Debugger 输入参数（主要用于开发阶段）。
- **从另一对象的控件调用**（如 Track 的 Entrance Control 在 MU 进入时触发 Method）。
- **从另一个 Method 调用**（需知道 Method 名称；若位于不同命名空间还需包含路径）。
- **从 EventController 调用**：`&method.executeIn(time)` — 经过指定秒数后启动 Method。
- **通过引用调用**：若数据类型为 `object` 的变量持有 Method 引用，用 `&Variable.execute`。

示例：

```simtalk
Method1                  // same namespace
root.Frame2.Method1      // path and name
&Method1.executeIn(8.5)  // pass to EventController, execute Method1 after 8.5 seconds
Variable.execute         // call the referenced Method; Variable has data type object
```

## 语法高亮颜色

| 颜色 | 含义 |
| --- | --- |
| 黑色 | 普通源代码 |
| 中绿色 | 注释 |
| 中蓝色 | SimTalk 函数 |
| 紫色 | SimTalk 关键字 |
| 棕色 | 字符串值 |
| 中红色 | 过时函数（不再支持） |
| 灰蓝色 | 弃用函数（过时；仅为向后兼容而支持） |
| 红色 | Method 模板中需替换的模板参数 |

## 使用断点

使用 Tools 功能区选项卡按钮或上下文菜单命令：

- **类断点**：在行标记区单击中键/滚轮。全部删除：**Delete All Class Breakpoints**。
- **实例断点**：按住 **Shift** + 中键。全部删除：**Delete All Instance Breakpoints**。
- 激活某行断点：按住 **Ctrl** + 中键，或 **Ctrl+F9**。
- 打开 **Breakpoint Settings**：**Ctrl+B**。
- 悬停断点显示工具提示。

## Method 的状态

模拟运行期间，Method 图形上边框沿线的彩色矩形指示其状态：

| 状态 | 矩形颜色 |
| --- | --- |
| 源代码包含语法错误 | 红色 |
| 源代码正在执行 | 绿色 |
| 被 `stopuntil` 或 `waituntil` 挂起 | 紫色 |
| 被 `wait` 挂起 | 蓝色 |
| 源代码已加密 | 深灰色 |
| 源代码为继承所得 | 深绿色 |

## Method 编辑器

双击 Method 图标打开窗口。要修改 **Class**（一般描述）的属性，在 Class Library 或 Toolbox 的 **Information Flow** 选项卡中双击它。窗口提供对 Method Editor 和 Method Debugger 的访问。

- 编辑 3D 属性：选中对象后按**空格键**，在 **Edit 3D Properties** 对话框中修改设置。
- **Edit Ribbon Tab [Method]** 提供编辑 Method 源代码的命令。

## 参见

- Programming a Method
- Working in the Method Window
- Calling a Method
- Colors for Syntax Highlighting
- Working with Breakpoints
- States of the Method
- The Method Editor
- Method Debugger
- Edit Ribbon Tab [Method]
- Tools Ribbon Tab
- Context Menu of the Method
- Drag-and-Drop in the Method Editor
