# Cycle — Attributes（属性）总结

本目录存放 **Cycle（循环/同步）** 对象的属性（Attributes）相关文档，内容来源于 Siemens Plant Simulation Help（11-2643 / 11-2647）。本 README 是对 `attributes.md`（`attributes.txtx` 为其原始提取文本，两者内容一致）的总结。

## 内容来源

目录内包含以下文件：

- `attributes.md` — 属性页面的 Markdown 版总结（本 README 的依据）。
- `attributes.txtx` — 从 Plant Simulation 帮助 PDF 提取的原始文本（含页码 11-2643 至 11-2647）。

## 1. 查看属性与方法

打开 **Show Attributes and Methods（显示属性与方法）** 窗口即可查看对象的所有方法、只读属性和属性：

- 在 **类库（Class Library）** 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选 **类（Class）** 的方法、只读属性与属性。
- 在插入了实例的 Frame 中，按 **F8** 键或点击 **Home** 功能区选项卡上的 **Show Attributes and Methods**，可显示所选 **实例（Instance）** 的方法、只读属性与属性。

## 2. Cycle 提供的属性

Cycle 对象提供：

- 本目录所列的属性（`GetLastStation`、`Active`、`EmptyCycleAllowed`、`EntranceOnlyOnCycle`）。
- **所有对象的属性（The Attributes of All Objects）**
- **物料流对象的属性（The Attributes of the Material Flow Objects）**

## 3. 设置与获取属性值

既可以通过对话框窗口中的复选框、文本框和下拉列表，也可以通过对相应属性赋值来设置或获取属性值。

- **设置属性值**，例如：

```simtalk
MyCycleObject.Active := true
```

- **获取属性值**，例如：

```simtalk
print MyCycleObject.EmptyCycleAllowed
posit := MyStation.Cont.XPos
```

## 4. 属性列表

### GetLastStation [SimTalk]（只读属性）

返回由 `<Path>` 指定的 Cycle 所同步的平衡生产线（balanced line）的**最后一个工位（Last Station）**。

- **类型：** 只读属性（Read-only attribute）
- **语法：** `<Path>.GetLastStation -> object`
- **返回值：** 数据类型为 `object`。
- **示例：**

```simtalk
print MyCycleObject.GetLastStation
```

- **参见：** Last Station

### Active [SimTalk] — Cycle

激活（`true`）或停用（`false`）由 `<Path>` 指定的 Cycle 的产线平衡（line balancing）。

- **类型：** 属性（Attribute）
- **语法：** `<Path>.Active:boolean`
- **赋值：** 可赋值为 `boolean` 类型。
- **示例：**

```simtalk
MyCycleObject.Active := true
```

- **参见：** Active [check box] - Cycle

### EmptyCycleAllowed [SimTalk]

设置即使没有零件（part）准备好从同步工位的前驱（predecessor）移出，是否仍允许将 `<Path>` 指定的 Cycle 内的零件继续移出（`true`）或不移出（`false`）。

- **类型：** 属性（Attribute）
- **语法：** `<Path>.EmptyCycleAllowed:boolean`
- **赋值：** 可赋值为 `boolean` 类型。
- **示例：**

```simtalk
MyCycleObject.EmptyCycleAllowed := true
```

- **参见：** Empty Cycle Allowed [check box]

### EntranceOnlyOnCycle [SimTalk]

设置零件是否**仅在 cycle 将所有 MU 向前移动一个工位时**才允许进入由 `<Path>` 指定的 Cycle（`true`）。

- **备注（Remarks）：** 设为 `false` 可允许零件随时进入 Cycle。
- **类型：** 属性（Attribute）
- **语法：** `<Path>.EmptyCycleAllowed:boolean`（注：原文档此处语法与示例均与 `EmptyCycleAllowed` 相同，疑似源文档复制错误，实际应为 `<Path>.EntranceOnlyOnCycle:boolean`）
- **赋值：** 可赋值为 `boolean` 类型。
- **示例：**

```simtalk
MyCycleObject.EntranceOnlyOnCycle := true
```

- **参见：** Part Can Only Enter on Cycle [check box]

## 5. 相关（Related）

- **流体对象（Fluid Objects）：** Plant Simulation 提供流体对象以模拟自由流动的物料（液体、气体或可倾倒形态），尤其适用于食品饮料加工行业和制药行业。

## 目录说明

- `attributes.md`：Cycle 对象属性说明的 Markdown 版本（本总结的源文件）。
- `attributes.txtx`：相同内容的文本提取版本（含页码 11-2643 至 11-2647）。
- 本目录无子文件夹，故无子文件夹 README.md。

---

*来源：Plant Simulation Help。未发表作品。© 2026 Siemens*
