# Mixer 的方法（Methods of the Mixer）

本目录汇总了 Plant Simulation 中 **Mixer（混合器）** 对象的方法说明，内容源自 `methods.md`（原始帮助文本见 `methods.txtx`）。

> 本目录无子文件夹，因此不包含子目录中的 README.md。

## 概述

Mixer 提供以下几组方法：

- 左侧目录中列出的方法（本目录中的 `addContent`、`setCurrentContent`）。
- **流体对象的方法（Methods of the Fluid Objects）**。
- **所有对象的方法（Methods of All Objects）**。

> 查看对象的所有方法、只读属性和属性：在类库的上下文菜单中选择 **Show Attributes and Methods**，或选中实例后按 **F8** / 点击 Frame 的 Home 选项卡上的 **Show Attributes and Methods**。

### 语法行示例

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示方法所作用对象的路径。
- 括号内为方法签名（标识符 + 各参数的数据类型），如 `(Parameter:string)` 表示数据类型为 string 的参数；也可使用所需类型的变量或返回所需类型的方法。
- 方括号内为可选参数，如 `[,Parameter:boolean]`。
- 默认值写在参数后，如 `:= false`。
- 返回值的类型写在箭头 `→` 后，如 `→ boolean`。

> **注意**：表达式内的括号 `(…)` 必须输入，否则可能产生意外结果并打开调试器（Debugger）。

---

## 方法（Methods）

### addContent [SimTalk]

将指定材料添加到 `<Path>` 所指定 Mixer 的现有内容中。

- **类型**：Method
- **语法**：

```
<Path>.addContent(Amount:real[, Material:string, MaterialsTable:path])
```

**参数**：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `Amount` | real | 材料数量 |
| `Material` | string（可选） | 材料本身 |
| `MaterialsTable` | path（可选） | MaterialsTable 的路径 |

关于可选参数 `Material` 的两种用法：

- **不指定 `Material`**：分别按指定数量增加所包含的（单一）反应物（educt）或混合操作后所包含产品的现有数量。
- **指定 `Material`**：在填充过程中将指定数量的新反应物添加到 Mixer 的内容中；混合过程结束后，指定数量被加入，且指定材料替换当前已存在的产品。

**示例**：

```simtalk
Tank1.addContent(3, "MyProduct", .Fluids.MaterialsTable)
```

---

### setCurrentContent [SimTalk] — Mixer

设置 `<Path>` 所指定 Mixer 中材料的当前内容。

- **类型**：Method
- **语法**：

```
<Path>.setCurrentContent(Amount:real[, Material:string, MaterialsTable:path])
```

**参数**：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `Amount` | real | 材料数量 |
| `Material` | string（可选） | 材料本身 |
| `MaterialsTable` | path（可选） | MaterialsTable 的路径 |

**备注**：新内容会替换之前的内容；内容既可以是反应物（educt），也可以是产品本身。

> **注意**：通常用该方法设置对象的初始状态。

**注意**：若 Mixer 已含有某种材料，只需输入新的 `Amount` 单个参数；否则还需指定 `Material` 和 `MaterialsTable`。

**示例**：

```simtalk
MyMixer.setCurrentContent(3, "MyProduct", .Fluids.MaterialsTable)
Mixer1.setCurrentContent(8) -- Mixer1 already contains a material
```

---

## 只读属性（Read-Only Attributes）

Mixer 提供：

- 左侧目录中列出的只读属性。
- **流体对象的只读属性（Read-Only Attributes of the Fluid Objects）**。
- **所有对象的只读属性（Read-Only Attributes of All Objects）**。

可以查询只读属性的值，但无法设置——Plant Simulation 会在你查询的时间点计算该值。大多数情况下，只读属性对应对象某个选项卡（如 **Statistics** 选项卡）上不可用的对话框项。

查询只读属性值的示例：

```simtalk
print Mixer.Full
```

---

## 方法速查表

| 方法 | 语法 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `addContent` | `<Path>.addContent(Amount:real[, Material:string, MaterialsTable:path])` | — | 将指定材料添加到现有内容 |
| `setCurrentContent` | `<Path>.setCurrentContent(Amount:real[, Material:string, MaterialsTable:path])` | — | 设置材料当前内容（替换之前的内容） |
