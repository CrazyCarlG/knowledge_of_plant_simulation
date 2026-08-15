# Checkbox — Attributes（属性）总结

本目录记录 Plant Simulation 帮助文档中 **Checkbox（复选框）** 对象「属性（Attributes）」部分的内容，来源为 `attributes.md`（其同内容的原始文本提取见 `attributes.txtx`）。同时汇总了 Checkbox 对象其他子目录（`general`、`methods`、`read-only-attributes`）中 README.md 的要点。

## 概述

Checkbox（复选框）对象用于在 **开（on）/ 关（off）** 两种状态之间切换，例如切换运行模式、运行时模式与调试模式等。

- 添加方式：在 Home 功能区标签页点击 **Manage Class Library > Basic Objects > UserInterface > Checkbox**。
- Checkbox 提供：
  - 目录（table of contents）中列出的属性。
  - **Attributes of All Objects**（所有对象的通用属性）。

## 查看属性与方法

可通过 **Show Attributes and Methods（显示属性与方法）** 窗口查看对象的全部方法、只读属性与属性：

- 在 **Class Library（类库）** 中，右键所选 **Class（类）**，选择 **Show Attributes and Methods**。
- 对于已插入 Frame 的 **Instance（实例）**，按 **F8** 键，或在 Frame 的 **Home（开始）** 功能区选项卡上点击 **Show Attributes and Methods**。

属性值既可以**设置**也可以**获取**：既可通过对话框窗口中的复选框、文本框和下拉列表，也可通过直接给相应属性赋值。

示例：

```simtalk
MyCheckbox.Value := false      -- 设置属性值
print MyCheckbox.Value         -- 获取属性值
```

## 本目录的属性（Attributes of the Checkbox）

### Control [SimTalk] — Checkbox

设置由 `<Path>` 指定的 Checkbox 所执行的 **Control（控制方法）**。

- **说明**：
  - 当你点击对象使 **Value** 值发生变化时，Plant Simulation 会调用该 Control。
  - Plant Simulation 只调用对象**自身**的 Control，而**不调用其实例**的 Control。
- **类型（Type）**：Attribute（属性）
- **语法（Syntax）**：

```simtalk
<Path>.Control:method
```

- **赋值（Assignment Value）**：可赋 `method` 数据类型。
- **示例（Example）**：

```simtalk
MyCheckbox.Control := "myControl"
```

- **参见（See also）**：Control [Checkbox]

### Value [SimTalk] — Checkbox

激活（`true`）或停用（`false`）由 `<Path>` 指定的 Checkbox。当其值变化时，Checkbox 会执行一个 Control。

- **语法（Syntax）**：

```simtalk
<Path>.Value:boolean
```

- **可监视（Watchable）**：该属性可监视（watchable）。
- **赋值（Assignment Value）**：可赋 `boolean` 数据类型。
- **示例（Example）**：

```simtalk
MyCheckbox.Value := false
```

- **参见（See also）**：
  - Value [drop-down list] - Checkbox
  - Control [Checkbox]

### 相关说明：Button [object]

`attributes.md` 末尾附带说明了 **Button（按钮）** 对象：用于在 Frame 中显示一个按钮；当点击按钮时，它执行你在 Control 中编写的动作。

## 其他子目录要点汇总

Checkbox 对象的内容分布在以下子目录，各自均有 README.md 总结：

### `general`（通用）

- Checkbox 默认外观为一个可点击的复选框图形；在模型窗口中每方向至少占据 **10 像素** 时才会被可靠识别点击，缩小过多可能无法识别。
- 单击图形切换开/关；双击图标右侧名称 **Checkbox** 打开对话框。
- 可为 Checkbox 创建任意数量的图标，Plant Simulation 会根据图标的**名称/状态**自动切换；图标需**成对命名**，例如 `TrueIcon1` 与 `FalseIcon1`。
- 对话框包括 **Edit Simulation Properties**（仿真属性）与 **Edit Animation Properties**（3D 属性，按空格键或 **Edit 3D Properties** 按钮进入）。
- **Tab Data（数据选项卡）**：
  - **Value [drop-down list]**：设置 Checkbox 是否激活（`true`/`false`）。
  - **Value [SimTalk]**：对应的 SimTalk 引用。
  - **Control [Checkbox]**：修改对象内置行为；可**选择已有 Method** 或**创建对象自身的 Control**（插入 `self.名称` 或 `self.On内置名称`）；标准 **OnClicked** 控件示例为 `(self)`。
- **Tab User-defined（用户自定义选项卡）**：定义自己的属性。
- 菜单：**Navigate Menu**、**View Menu**（含 `updateDialog [SimTalk]`）、**Tools Menu**（Edit Controls、Edit Observers）、**Help Menu**。
- 另附属性 **ShowStandardButtons**：设置 Dialog 是否显示 **OK / Cancel / Apply** 标准按钮，语法 `<Path>.ShowStandardButtons:boolean`。

### `methods`（方法）

- Checkbox 提供 **Methods of All Objects**（所有对象的通用方法），方法集合继承自通用对象方法。
- 方法语法示例：

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- **语法约定**：
  - `<Path>` 表示方法所作用对象的路径。
  - 方法签名由参数标识符及其数据类型组成，写在括号内，如 `(Parameter:string)`。
  - 可选参数写在方括号内，如 `[,Parameter:boolean]`。
  - 默认值在参数后以 `:=` 标注，如 `:= false`。
  - 返回值在箭头 `→`（或 `->`）后标注数据类型，如 `→ boolean`。
  - **注意**：括号内表达式 `(…)` 必须输入括号，否则可能产生意外结果并打开 **Debugger（调试器）**。

### `read-only-attributes`（只读属性）

- Checkbox 提供 **Read-Only Attributes of All Objects**（所有对象的通用只读属性）。
- 只读属性值**可以查询，但不能设置**：Plant Simulation 在你查询的那一刻计算其值；多数情况下只读属性对应对象某个选项卡（如 **Statistics** 选项卡）上不可用的对话框项。
- 示例：

```simtalk
print MyCheckbox.UUID
```

## 目录结构

```
Checkbox/
├── attributes/
│   ├── README.md          # 本总结文件
│   ├── attributes.md      # Checkbox 属性说明（Markdown 版本）
│   └── attributes.txtx    # 同内容的文本源
├── general/               # 通用说明（含 README.md）
├── methods/               # 方法说明（含 README.md）
└── read-only-attributes/  # 只读属性说明（含 README.md）
```

## 来源

Siemens Plant Simulation Help — Checkbox（User Interface Objects）相关章节，© 2026 Siemens。
