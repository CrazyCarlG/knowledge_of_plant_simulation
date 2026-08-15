# Method Editor 汇总

本文件汇总了 `editor.md` 中关于 **Method Editor（方法编辑器）** 的全部内容。Method Editor 是 Plant Simulation 中用于编写和编辑 Method 对象 SimTalk 源代码的编辑器。

> 编辑对象 3D 属性的方式：在 3D 模型中选中对象后按空格键，然后在 **Edit 3D Properties** 对话框中修改设置。

---

## 1. Edit 功能区选项卡（Edit Ribbon Tab）

**Edit** 功能区选项卡提供编辑 Method 源代码的命令，主要包括：

| 命令 | 说明 | SimTalk 对应 |
|---|---|---|
| Import from File | 从文本文件导入源代码 | `load [SimTalk] - source code` |
| Export to File | 将源代码导出到文件 | `writeStringToFile [SimTalk]` |
| Print | 打印源代码 | — |
| Find Text | 查找（可替换）源代码中的表达式 | — |
| Find Previous / Find Next | 查找上一个/下一个匹配项 | — |
| Incremental Search | 边输入边增量查找 | — |
| Undo / Redo | 撤销 / 重做 | — |
| Auto Complete | 自动补全属性/方法名 | — |
| Toggle Comment | 注释/取消注释 | — |
| Increase / Decrease Indent | 增加 / 减少缩进 | — |
| Reformat Selection | 重新格式化缩进 | — |
| Move Up / Move Down | 上移 / 下移代码行 | — |
| Line Operations | 行操作（复制/删除/剪切/复制行） | — |
| Select Template | 选择模板插入代码 | `setErrorHandler [SimTalk]` |
| Insert Control Structure | 插入控制结构 | `if-else`, `while-end`, `for-next` 等 |
| Inherit Source Code | 开关源代码继承 | `getAttribute [SimTalk] - object` |
| Apply Changes | 应用更改（不关闭对话框） | — |
| Help on Word | 打开光标/双击单词的帮助 | — |

### 关键命令详解

- **Find Text**：支持正则表达式（`.`、`^`、`$`、`\<`、`\>`、`\(\)`、`?`、`*`、`+`、`[ ]`、`[^]`、`\|`），以及 `Match Whole Word Only`、`Match Case`、查找方向（Up/Down）、`Replace`、`Mark All`、`Replace All` 等选项。可用 `Ctrl+F2` 临时标记选中文本。
- **Incremental Search**：边输入边高亮匹配，`F3` 查找下一个，`Esc` 结束。还可查找 Workers（含类名和实例计数器，如 `Worker:1`）。
- **Auto Complete**：输入首字母后按 `Ctrl+Spacebar`（或 `Shift+Ctrl+Spacebar`）补全，可按 Standard/Expert Users、General/UI/Control/Simulation/Energy/3D/Statistics、Attributes/Read-Only Attributes/Methods/Global Functions/Objects/Keywords 等分类筛选。
- **Select Template**：选择分类与模板插入常用代码；可自定义模板（文本文件保存在 `Templates\English\...` 子文件夹，用 `--` 注释、`«attribute»` 占位符、`§§*/` 定义 Tooltip）。
- **Insert Control Structure**：插入 `if-else`、`if-else-end`、`if-elseif-end`、`switch-case-end`、`switch-case-else-end`、`while-end`、`repeat-until`、`for-next`、`for-downto-next` 等现成 SimTalk 结构（SimTalk 1.0 不可用）。
- **Inherit Source Code**：继承开启时不可修改源代码（使用其派生来源 Method 的代码），点击后可关闭继承并编辑。
- **Help on Word**：为双击/光标前的单词打开帮助主题。

---

## 2. Tools 功能区选项卡（Tools Ribbon Tab）

**Tools** 功能区选项卡提供与 Method 源代码运行、调试、书签、断点等相关的命令：

| 命令 | 说明 | SimTalk 对应 |
|---|---|---|
| Run | 运行整个 Method | `execute [SimTalk] - Method` |
| Debug Method | 单步调试 Method | `debug [SimTalk]` |
| Toggle / Clear All Bookmarks | 添加/清除书签 | — |
| Previous / Next Bookmark | 上一个/下一个书签 | — |
| Toggle Class / Instance Breakpoint | 类断点 / 实例断点 | — |
| Delete All (Class/Instance) Breakpoints | 删除断点 | — |
| Previous / Next Breakpoint | 上一个/下一个断点 | — |
| Toggle / Previous / Next Outline | 折叠/展开大纲 | — |
| Collapse / Expand All Outlines | 折叠/展开全部大纲 | — |
| Hide/Unhide Text | 隐藏/显示文本 | — |
| Encrypt / Decrypt Method | 加密/解密源代码 | `encrypt` / `decrypt [SimTalk]` |
| New Syntax | 激活 SimTalk 2.0 语法 | `UsingNewSyntax [SimTalk]` |
| Syntax-controlled Indentation | 语法控制缩进 | — |
| Show Line Numbers | 显示行号 | — |
| View | 显示大纲/高亮当前行/补全提示 | — |

### 关键命令详解

- **Run / Debug Method**：`Run` 运行整个 Method；`Debug Method` 打开 Method Debugger 逐步执行（同 `Ctrl+Alt+Shift` 运行）。陷入死循环时，前台按 `Ctrl+Alt+左Shift` 5 秒、非前台按 `Ctrl+Alt+右Shift` 打开调试器。
- **Bookmarks（书签）**：为当前行/选区添加书签；临时书签（如超出原代码末尾的更改）比已保存书签更亮，未应用源代码时会丢失。
- **Breakpoints（断点）**：
  - 类断点 `F9`（实心红圆，作用于共享该类源代码的所有实例）；实例断点 `Shift+F9`（红星，仅该实例）。
  - 同一行同时有类断点与实例断点时显示红星套红圆。
  - 到达断点时 Method Debugger 打开并高亮该行（黄色），可查看/修改局部变量与参数。
  - `Ctrl+双击` 激活该行所有断点；`Shift+Ctrl+双击` 打开 **Breakpoint Settings** 对话框。
  - 加密 Method 也可设置断点。
- **Outlining（大纲）**：折叠/展开控制/循环结构；`Hide/Unhide Text` 从选中代码创建大纲或删除现有大纲。
- **Encrypt / Decrypt Method**：加密源代码防止未授权访问（需密码）；加密后命令变为 Decrypt。可通过 **File > Options > Encrypt/Decrypt Methods** 批量加密/解密整个模型。
- **New Syntax**：激活 SimTalk 2.0 简化语法；对现有 1.0 Method 点击会自动转换。批量转换：按住 `Shift` 右键 Class Library 中的 **Basis**，选择 **Convert all Methods to New Syntax**。
- **Syntax-controlled Indentation**：按 SimTalk 语法自动缩进（对本次会话所有新打开的 Method 生效；1.0 不可用）。
- **Show Line Numbers**：显示/隐藏行号。

> 部分设置也可在 **File > Preferences > Editor** 中设置（作用于所有新 Method），Tools 选项卡上的设置只作用于当前打开的 Method。

---

## 3. View 子菜单

**View** 子菜单控制 Frame 窗口中显示的内容，覆盖 **File > Preferences > Editor** 中的设置，对本次会话所有新打开的 Method 生效：

- **Show Outlining** — 以可折叠结构显示控制/循环结构（1.0 不可用）。
- **Highlight Current Line** — 高亮当前行。
- **Show Completion Tooltip** — 当 Auto Complete 达到名称唯一时显示提示，便于按 `Ctrl+Spacebar` 补全。

---

## 4. Method 的上下文菜单（Context Menu）

右键点击 Method 弹出的上下文菜单提供最常用命令（部分在迷你工具栏上）：

Open Location、Open Origin、Open Class、Copy/Cut/Paste/Delete Objects、Inherit Source Code、Apply Changes、Toggle Class/Instance Breakpoint、Open/Show Object、Run、Debug、Insert Control Structure。

---

## 5. Method Editor 中的拖放（Drag-and-Drop）

在 Method Editor 中拖放可完成多种操作（按住对应按键）：

| 操作 | 从 | 到 | 类型 | 快捷键 |
|---|---|---|---|---|
| 移动选中文本 | 文本窗口 | 文本窗口 | text | 无 |
| 复制选中文本 | 文本窗口 | 文本窗口 | text | Ctrl |
| 插入选中文本 | 任意 | 文本窗口 | text | 任意 |
| 复制选中文本 | 文本窗口 | 任意 | text | Ctrl |
| 剪切选中文本 | 文本窗口 | 任意 | text | 无 |
| 将拖入对象作为数组参数传给 Method | Frame 窗口 | Method | object | 无 |

### 多对象拖放示例（SimTalk）

```simtalk
param a: object[]
for var i := 1 to a.Dim
   print "i=", i, " : ", a[i]
next
```

将 `Station`、`Station1`、`ParallelStation` 拖到 Method 图标上后，Console 输出各自路径（如 `.Models.Model.Station`）。

---

## 6. Method Debugger（方法调试器）

在 Method 执行期间调试 Method Editor 中编写的源代码。

**打开方式：**
- 在 Method Editor 窗口按 `F11`；
- 在 Tools 功能区选项卡选择 **Debug Method**。

> 陷入死循环时：前台按 `Ctrl+Alt+左Shift` 数秒；非前台按 `Ctrl+Alt+右Shift`。

当执行源代码遇到错误或命中断点时，Plant Simulation 会自动打开 Debugger。

---

## 相关主题（Related Topics）

- Edit Ribbon Tab [Method]
- Tools Ribbon Tab
- Context Menu of the Method
- Drag-and-Drop in the Method Editor
- Method Debugger
- Programming a Method
- Working in the Method Window
- Colors for Syntax Highlighting
