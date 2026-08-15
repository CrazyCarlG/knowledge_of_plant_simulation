# Frame 的只读属性（Read-Only Attributes）——总结

本目录包含 Frame（框架）对象的只读属性文档，文件如下：

- `read-only-attributes.md`：Markdown 格式的只读属性说明。
- `read-only-attributes.txtx`：同一内容的纯文本导出版本。

两者内容一致，均描述 Frame 提供的只读属性。

## 概述

只读属性（read-only attribute）可以查询但不能赋值，因为 Plant Simulation 会在你查询它的那一刻才计算其值。在大多数情况下，只读属性对应对象某个选项卡上不可编辑的对话框条目（例如 **Statistics** 选项卡）。

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods**（显示属性和方法）窗口：

- 在 **Class Library**（类库）的上下文菜单中选择 **Show Attributes and Methods**，可显示所选类的成员。
- 在插入实例的 Frame 的 **Home**（开始）功能区选项卡上按 **F8** 或点击 **Show Attributes and Methods**，可显示所选实例的成员。

查询只读属性值的示例：

```simtalk
print .Models.Model.Capacity
```

## Frame 提供的只读属性

| 属性 | 说明 | 返回类型 | 语法 |
| --- | --- | --- | --- |
| [Capacity](#capacity) | 返回 Frame 中所有静态物流对象的容量 | `integer` | `<Path>.Capacity` |
| [EventController](#eventcontroller) | 返回位于根 Frame 中的 EventController | `object` | `EventController` |
| [NumberOfLimitedObjects](#numberoflimitedobjects) | 统计每个包含 EventController 的 Frame 中已插入对象的数量 | `integer` | `NumberOfLimitedObjects` |
| [NumNodes](#numnodes) | 返回 Frame 中的对象数量 | `integer` | `<Path>.NumNodes` |

---

## Capacity

返回由 `<Path>` 指定的 Frame 中所有**静态物流对象**（static material flow objects）的容量。

- **注意**：Plant Simulation **不**包含 MU（移动单元）的容量。
- 当你在所选模型中放入其他模型时，Plant Simulation 会把这些模型的容量也加入。
- 如果 Frame 中至少插入了一个无限容量对象（例如容量为 `-1` 的 Conveyor），则返回 `-1`。

该属性**可被监视（watchable）**。

```simtalk
<Path>.Capacity → integer
```

示例：

```simtalk
print .Models.MyPlant.Capacity
```

---

## EventController

返回位于**根 Frame** 中的 EventController。

```simtalk
EventController → object
```

示例：

```simtalk
print EventController // 例如返回 .Models.Model.EventController
```

另请参见：EventController [object]。

---

## NumberOfLimitedObjects

统计每个包含 EventController 的 Frame 中已插入对象的数量。

- **注意**：Plant Simulation **不**统计以下对象：Lists 和 Tables、Methods、Variables、Comments、MU、Connectors、Interfaces、EventControllers、Toolbar、Folders 以及 Class 对象。
- `NumberOfLimitedObjects` 适用于 Standard、Educational、Foundation 和 Student 四种许可证。

| 许可证名称 | 允许的对象数量 |
| --- | --- |
| Standard license | 4000 |
| Educational license | 1000 |
| Foundation license | 500 |
| Student license | 80 |

- 对于 Student 许可证，Plant Simulation 会在 Class Library 中 Frame 名称旁边显示插入到该 Frame 的对象数量，以及 Student 许可证允许的最大对象数量。
- **注意**：Plant Simulation 仅对插入了 EventController 的 Frame 显示该值。

```simtalk
NumberOfLimitedObjects → integer
```

示例：

```simtalk
print NumberOfLimitedObjects // 对于名为 'Model' 的 Frame 返回 10
```

另请参见：`numOfLimitedObjects` [SimTalk]、Start Plant Simulation with Different Kinds of Licenses。

---

## NumNodes

返回由 `<Path>` 指定的 Frame 中的对象数量。

- 插入到所选 Frame 中的每个额外 Frame 都计为单个对象。
- Plant Simulation **不**统计这些 Frame 内部所包含的对象。
- Connectors（连接器）也计为对象。

```simtalk
<Path>.NumNodes → integer
```

示例：

```simtalk
print .Models.MyPlant.NumNodes
```

另请参见：`node` [SimTalk] - Frame、Attributes of the Frame。
