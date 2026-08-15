# Method Debugger（方法调试器）汇总

本文件汇总了 `debugger.md` 中关于 **Method Debugger（方法调试器）** 的全部内容。Method Debugger 用于在 Method 执行期间，调试你在 Method Editor 中编写的 SimTalk 源代码。

> 源文件：`debugger.md`（内容详见该文件）；原始导出文本：`debugger.txtx`。

---

## 1. 打开 Method Debugger

- 在 Method Editor 窗口按 `F11`；
- 在 Method Editor 窗口的 Tools 功能区选项卡选择 **Debug Method**。

> **注意：** 若 Plant Simulation 在前台运行且陷入死循环，按住 `Ctrl+Alt+左Shift` 数秒可打开调试器；若不在前台，则按住 `Ctrl+Alt+右Shift` 数秒。

> **注意：** 当执行源代码遇到错误或命中断点时，Plant Simulation 会自动打开调试器。

---

## 2. 调试器窗口（Debugger Window）

调试器窗口显示 Method 的源代码、参数和局部变量。你可以在关键点设置断点，并逐步检查 Method 的执行。

### 2.1 断点（Breakpoints）

- 按 `F9`（或按住 `Shift` 的同时右键单击）插入 **类断点（Class Breakpoint）**，以行左侧的实心红圆标记。
- 按 `Shift+F9`（或按住 `Shift+Ctrl` 的同时右键单击）插入 **实例断点（Instance Breakpoint）**，以红星标记，仅作用于该实例。

### 2.2 源代码操作

- 将鼠标拖过指令时，调试器以 **Tooltip** 显示属性和局部变量的值。
- 双击选中一个单词；三击选中整行；四击选中整个源代码。
- 有错误的源代码行以 **红色** 高亮，并在状态栏显示错误信息。
- 断点或错误后要重新执行源代码：按住 `Ctrl` 并双击该行。
- 若因运行时错误打开调试器后直接关闭它，Plant Simulation 会终止所有调用链并停止仿真。
- 只想终止错误的调用链并继续仿真：按 `F5`。
- 想在某一行继续执行错误的 Method：使用 **Set Next Statement**（光标置于该行后按 `Ctrl+F10`，或按住 `Ctrl` 并双击该行），然后按 `F5`。

---

## 3. Watch Window（监视窗口）

调试器窗口的下半部分是 Watch Window，包含以下选项卡：

**Variables（变量）、Anonymous Identifiers（匿名标识符）、Call Stack（调用栈）、Call Chains（调用链）、Suspended（挂起）、Expressions（表达式）。**

- 可点击拆分按钮打开第二个 Watch Window，同时显示两个选项卡；拖动分隔条可调整其高度。

### 3.1 打开 Watch Window

- 点击工具栏上的 Watch Window 图标；
- 按 `F12`；
- 选择 **Debug > Watch Window**。

### 3.2 Tab Variables（变量）

显示所有局部变量的名称和值。

- 双击变量打开 **Variable** 对话框修改其值。
- 上下文菜单以 **17 位浮点数** 精确显示数据类型为 `real`、`length`、`weight`、`speed`、`acceleration` 的局部变量值。
- 带物理单位的值以相应的 **SI 单位** 显示（Plant Simulation 内部始终以 SI 单位保存值，单位转换仅用于显示）。

### 3.3 Tab Anonymous Identifiers（匿名标识符）

显示匿名标识符 `@`、`?`、`current`、`self`、`root`、`rootfolder`。

- 数据类型为 Method 的用户自定义属性额外显示 `self.~`；公式和表显示 `xSelf` 和 `ySelf`。
- `@` 和 `?` 旁的单元格允许你在不运行仿真的情况下测试 Method：若输入路径，Plant Simulation 内部会用该路径替换对应的匿名标识符。
- 更改后的值在 Value 列下以红色显示。

#### @（at sign）

`@` 单元格显示 **当前 MU**（在控件中触发当前 Method 调用的 MU）的标识符。内容不可更改。

- 按 `F2` 打开该 MU 的对话框。

#### ?（question mark）

`?` 单元格显示 **调用该 Method 的对象的名称**（可能是另一个 Method 名，或 MU 触发控件调用的对象）。内容不可更改。

- 按 `F2` 打开调用对象的对话框。

### 3.4 Tab Call Stack（调用栈）

显示 Method 的调用顺序（调用链）。最先被调用的 Method 位于底部，顶行显示当前正在执行的 Method。

- 双击某单元格可在调试器中打开对应 Method 及其当前的局部变量和参数设置；双击最顶行返回当前执行的 Method。
- 列 **Method** 显示 Method 名称；列 **Parameters** 显示参数。
- Parameters 列始终显示参数的 **当前值**（若中途被修改，显示新值而非最初传入的值）。

SimTalk：`getCallStack`

### 3.5 Tab Call Chains（调用链）

显示已准备好立即执行的 Method（不要与当前正在执行的活动 Method 混淆）。活动 Method 是已被调用、并在其他 Method 执行时等待执行的 Method。

### 3.6 Tab Suspended（挂起）

显示被 `waituntil` 或 `stopuntil` 语句（以及 `wait`、`sleep` 指令）挂起的 Method。

- 调用者显示在括号中，前面是绝对路径；双击某条目可切换到该 Method。
- 第三列显示挂起该 Method 的语句。
- 若 `waituntil`/`stopuntil`/`wait`/`sleep` 语句后的注释以三个连字符 `---` 或三个正斜杠 `///` 开头，则只显示该注释（而非整个语句）。

SimTalk：`deleteSuspendedMethods`

`deleteSuspendedMethods` 删除所有 Method 的所有挂起。Plant Simulation 在 Frame 窗口显示工具提示，包含调用者和挂起的指令（例如 `waituntil SP.empty prio @.ID wait 5:00 ? = PP`）。

### 3.7 Tab Expressions（表达式）

输入任意表达式供调试器求值。

- 双击一行，输入表达式（例如 `self.xPos+1`），点击 OK。
- 选择 **Show Expression for all Methods** 可在所有 Method 的对话框中显示该表达式。
- 值的数据类型为 `object` 的变量或表达式：点击单元格并按 `F2` 打开。
- 若该选项卡显示局部变量或属性，可在 Value 列编辑其值。

> **注意：** 若 Method 作为公式执行，Expressions 选项卡不可用。

---

## 4. Method Debugger 工具栏（Toolbar）

| 操作 | 命令 / SimTalk |
|---|---|
| 打开 Method 所在位置（Frame） | Open Location, `Location` |
| 打开活动 Method 的派生来源 | Open Origin, `Origin` |
| 返回当前执行的 Method | — |
| 打开 Watch Window | Watch Window |
| 一次执行一行（不加载被调用的 Method） | Step Over |
| 一次执行一行（也加载被调用的 Method） | Step Into |
| 跳出当前 Method，到调用者的下一语句 | Step Out |
| 继续执行活动 Method | Continue |
| 停止仿真（停止所有活动 Method） | Terminate Simulation |
| 插入/移除类断点 | Class Breakpoint |
| 插入/移除实例断点 | Instance Breakpoint |
| 删除 Method 中的所有断点 | Remove All Breakpoints, `clearAllBreakpoints` |
| 临时激活/停用 MU 和状态动画 | MU and State Animation |

---

## 5. 菜单栏（Menu Bar）

提供 **File Menu**、**Edit Menu**、**Navigate Menu**、**Debug Menu**、**View Menu**、**Tools Menu**、**Help Menu**。

### 5.1 File Menu（文件菜单）

- Export to File、Print、Apply Changes（参见 Edit Ribbon Tab [Method]）。

### 5.2 Edit Menu（编辑菜单）

命令参见 Edit Ribbon Tab。

### 5.3 Navigate Menu（导航菜单）

- Open Location、Open Origin、Open Class、Go to Class、Open Frame。

#### Open Frame

打开插入该 Method 的 Frame（若已打开则将其置于前台）。

### 5.4 Debug Menu（调试菜单）

#### Stop On（子菜单）

- **Stop on Controls** — 当 EventController 遇到由对象启动的控件 Method（Entrance/Exit Control）时，在执行调用 Method 之前停止仿真。
- **Stop on Formulas** — 每当公式被求值时停止仿真并打开调试器。
- **Stop on Error Handler** — 每当执行错误处理方法时停止仿真并打开调试器。
- **Stop on Wakeup** — 当挂起的 Method 恢复时（用 `waituntil`、`stopuntil`、`wait` 或 `sleep(true, false)` 挂起）停止仿真并打开调试器。

#### On Step Into（子菜单）

- **Step into Controls** — 单步进入其他调用链（控件或被唤醒的挂起 Method）。
- **Step into Formulas** — 单步进入其他公式（例如 `print table[1,1]` 计算该单元格中的公式）。
- **Step into Encrypted Methods** — 设置 Step Into（`F11`）是否在加密 Method 中停止。默认停用；激活时调试器显示 "The source code is encrypted"。

#### Ignore（子菜单）

- **Ignore Breakpoints** — 忽略用户定义的断点。SimTalk：`ignoreBreakpoints`
- **Ignore Error Handlers** — 运行时错误时不执行错误处理方法，而是在错误位置打开调试器。
- **Ignore Errors** — 当前 Method 出错后停止仿真；以红色高亮错误行。错误消息显示描述、Method、行号和活动调用链。SimTalk：`setErrorStop`
- **Ignore Errors in Formulas** — 公式中发生运行时错误时不打开调试器。

#### Step Commands（单步命令）

- **Step Over** — 一次执行一行；不加载被调用的 Method。
- **Step Into** — 一次执行一行；也加载被调用的 Method。不跳入加密 Method（表现同 Step Over）。若下一行不包含方法调用，Step Into 与 Step Over 无区别。
- **Step Out** — 完成当前 Method，并在调用 Method 的下一语句停止。
- **Continue** — 继续执行活动 Method。
- **Run to Cursor** — 继续执行直到光标所在语句。

> 用 Step Over、Step Into、Step Out 或 Run to Cursor 执行指令时，若执行耗时 **10 毫秒或以上**，调试器会显示 **elapsed time（耗时）**。

- **Set Next Statement** — 设置下一条要执行的语句（与 `Ctrl` + 双击相同）。可用于跳出死循环：按住 `Shift+Ctrl+Alt`，将光标置于循环外，按 `Ctrl+F10`，再按 `F5`。
- **Return From Current Call Chain** — 终止调用当前 Method 的整个调用链；之后仿真继续。
- **Terminate Simulation** — 终止所有调用链并停止仿真。
- **Restart Simulation** — 重置并重新启动仿真（同 EventController 中的 Reset 后再 Start）。

#### Breakpoint Commands（断点命令）

- **Class Breakpoint** — 在类中插入/移除断点。
- **Instance Breakpoint** — 添加/删除实例断点。
- **Breakpoint Active** — 激活或停用所选断点。
- **Breakpoint Settings** — 打开对话框设置 Start Time 和 Condition：
  - **Active** — 勾选激活，取消停用。
  - **Start Time** — 当 EventController 达到或超过该时间时断点激活。
  - **Condition** — 每次到达断点时求值；仅当满足时才停止。
- **Next Breakpoint** — 转到下一个断点。
- **Previous Breakpoint** — 转到上一个断点。
- **Delete Class Breakpoints** — 删除所有类断点。
- **Delete Instance Breakpoints** — 删除所有实例断点。
- **Delete All Breakpoints** — 删除所有类和实例断点。SimTalk：`clearAllBreakpoints`
- **Delete Breakpoints in All Methods** — 删除所有 Method 中的所有断点。

#### Other

- **Watch Window** — 打开 Watch Window。

### 5.5 View Menu（视图菜单）

- Show Line Numbers、Syntax-controlled Indentation。

#### MUs and States

临时一起激活或停用 MU 动画和图标动画；关闭调试器窗口时恢复原始状态。

### 5.6 Tools Menu（工具菜单）

- Edit Controls、Edit Observers、User-defined Attributes、Rename。

#### User-defined Attributes

打开对话框，添加、编辑或删除 Method 的用户自定义属性。

#### Rename

打开 Rename 对话框，修改 Method 的名称和标签。

### 5.7 Help Menu（帮助菜单）

- **Help on Debugger** — 打开 Method Debugger 的帮助主题。
- **Help on Word**（或 `F1`）— 打开光标下单词的帮助。

---

## 6. 上下文菜单（Context Menu）

提供：Breakpoint Active、Breakpoint Settings、Toggle Class Breakpoint、Toggle Instance Breakpoint、User-defined Attributes、Run to Cursor、Set Next Statement、Open Object、Show Object、Cut、Copy、Paste、Delete。

- **Open Object** — 打开鼠标所在指令上方的对象。
- **Show Object** — 打开对象所在的 Frame 并选中它；若该对象引用了另一个对象，则显示被引用的对象。
- **Cut / Copy / Paste / Delete** — 对选中文本执行标准剪贴板操作。

---

## 7. Method 对象的方法（Methods of the Method）

访问 Method 会自动执行其源代码。要访问内置方法、只读属性或属性，须使用引用运算符 `&`。

> **注意：** 只能通过 `&` 运算符访问指向对象本身的 Method 对象方法；不使用 `&` 时，方法作用于 Method 的内容。

要查看对象的所有方法、只读属性和属性，打开 **Show Attributes and Methods** 窗口。

---

## 相关主题（Related Topics）

- Toolbar of the Method Debugger
- Menu Bar of the Method Debugger
- Context Menu of the Method Debugger
- Functions for Debugging the Model
- Watch Window（Variables / Anonymous Identifiers / Call Stack / Call Chains / Suspended / Expressions）
- Anonymous Identifiers（`@`、`?`、`current`、`self`、`root`、`rootfolder`）
