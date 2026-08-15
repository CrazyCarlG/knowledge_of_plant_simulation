# Cycle 对象的方法（Methods）— 总结

本目录汇总了 **Cycle** 对象（物料流对象，Material Flow Object）所提供的方法与只读属性。来源为 Plant Simulation 帮助文档（`methods.md` / `methods.txtx`，内容一致）。

## 一、Cycle 对象提供的方法

Cycle 对象提供以下方法：

- `setFirstAndLastStation` [SimTalk] —— Cycle 独有的方法。
- **Material Flow Objects（物料流对象）的方法**。
- **All Objects（所有对象）的方法**。

## 二、查看方法、只读属性与属性

可通过 **Show Attributes and Methods** 窗口查看对象的全部方法、只读属性和属性：

- 在 Class Library 的类上，通过上下文菜单选择 **Show Attributes and Methods**，可查看所选 **类（Class）** 的方法、只读属性与属性。
- 在 Frame 中选中已插入的实例后，按 **F8** 键，或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，可查看所选 **实例（Instance）** 的方法、只读属性与属性。

## 三、语法行（Syntax Line）说明

方法语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法所作用对象的路径。
- 括号内为方法签名（标识符 + 参数数据类型），例如 `(Parameter:string)` 表示 `string` 类型的参数；除常量外也可使用相应类型的变量或返回相应类型的方法。
- 可选参数写在方括号 `[]` 内，例如 `[,Parameter:boolean]` 表示该布尔参数可省略。
- 若参数有默认值，则写在参数之后，如 `:= false`。
- 若方法有返回值，其数据类型写在箭头 `→` 之后，如 `→ boolean`。

> **注意**：表达式内部的括号 `(…)` 必须输入，否则可能导致意外结果并打开调试器（Debugger）。

## 四、setFirstAndLastStation [SimTalk]

**作用**：设置由 `<Path>` 指定的 Cycle 工位所同步的平衡生产线（balanced line）的 **第一个工位（First Station）** 与 **最后一个工位（Last Station）**。

- **备注（Remarks）**：这两个工位之间所有通过连接器（Connectors）连接的工位共同构成平衡生产线。
- **类型**：Method
- **语法**：

```
<Path>.setFirstAndLastStation(FirstStation:path, LastStation:path) → boolean
```

- **参数**：
  - `FirstStation`（数据类型 `object/path`）：指定第一个工位。
  - `LastStation`（数据类型 `object/path`）：指定最后一个工位。
- **返回值**：数据类型为 `boolean`。
- **示例**：

```simtalk
MyCycleObject.setFirstAndLastStation(MyStation1, MyStation4)
```

- **相关方法**：
  - `GetFirstStation` [SimTalk]
  - `GetLastStation` [SimTalk]
  - `setFirstAndLastStation` [SimTalk]

## 五、Cycle 的只读属性（Read-Only Attributes）

Cycle 对象提供：

- 目录中列出的只读属性（如 `GetFirstStation`、`GetLastStation`）。
- **All Objects 的只读属性**。
- **Material Flow Objects 的只读属性**。

只读属性的值可以查询，但不能设置——Plant Simulation 会在查询的时间点计算该值。多数情况下，只读属性对应对象某个选项卡（例如 **Statistics** 选项卡）上不可编辑的对话框项。

查询只读属性值的示例：

```simtalk
print Cycle.GetFirstStation
```

---
*来源：Plant Simulation Help — Unpublished work. © 2026 Siemens*
