# Chart 对象 — 只读属性（Read-Only Attributes）

本目录汇总 **Chart** 对象的只读属性说明（`read-only-attributes.md` / `read-only-attributes.txtx`）。本目录无子文件夹。

## 概述

**Chart** 提供 **所有对象的只读属性（Read-Only Attributes of All Objects）**。只读属性只能查询、不能设置——其值由 Plant Simulation 在你查询的时间点即时计算。多数只读属性对应对象某个选项卡上不可编辑的对话框项（例如 **Statistics** 选项卡）。

查询只读属性的值，例如：

```simtalk
print MyChart.UUID
```

Chart 提供：

- 左侧目录中列出的属性。
- 所有对象的通用属性（Attributes of All Objects）。

## 查看方法、只读属性与属性

打开 **Show Attributes and Methods** 窗口，可查看对象的全部方法、只读属性与属性：

- 在类库上下文菜单中选择 **Show Attributes and Methods**，显示所选类的成员。
- 在插入实例的 Frame 中按 **F8** 键，或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，显示所选实例的成员。

## 方法 `update`

刷新由 `<Path>` 指定的 Chart 显示，用当前值重新绘制。

**类型**：方法

**语法**：

```simtalk
<Path>.update -> boolean
```

**返回值**（数据类型 `boolean`）：

- `true`：Chart 处于打开状态。
- `false`：Chart 处于关闭状态。

**备注**：若 Chart 为 Sample 模式下的 Plotter，`update` 方法有额外效果——会设置一个新的数据点，即 Chart 再采样一次，即使 Chart 已关闭且方法因此返回 `false` 也会采样。

**示例**：

```simtalk
MyChart.update
```

**另请参阅**：

- Mode [drop-down list] - Chart
- Read-Only Attributes of the Chart

## 相关文档

- 一般说明（General）：[`../general/README.md`](../general/README.md)
- 属性（Attributes）：[`../attributes/attributes.md`](../attributes/attributes.md)
- 方法（Methods）：[`../methods/README.md`](../methods/README.md)
