# Sorter / read-only-attributes — 内容总结

> **说明：** 本目录虽然位于 `Sorter/read-only-attributes` 路径下，但其中的文档（`read-only-attributes.md` 与 `read-only-attributes.txtx`）实际记录的是 **Store（仓库/存储）** 对象的只读属性（Read-Only Attributes）。本 README 忠实按照源文件内容进行总结。

本目录包含以下文件：

- `read-only-attributes.md` — Store 对象只读属性的完整帮助文档（Markdown 格式）
- `read-only-attributes.txtx` — 与 `read-only-attributes.md` 内容对应的纯文本源文件
- `Plant-Simulation-Help2606_4961-4964.pdf` — 对应的 PDF 参考文件（Plant Simulation Help 11-2031 至 11-2034）

目录下没有子文件夹，因此不存在子文件夹中的 README.md 需要合并。`Sorter` 下相邻的 `general/` 与 `methods/` 目录各有 README.md，均同样记录 Store 对象，可交叉参考（见文末第 4 节）。

---

## 1. 只读属性概述

只读属性（Read-Only Attributes）的**值只能查询，不能设置**——Plant Simulation 会在你查询的时间点实时计算该值。多数情况下，只读属性对应对象某个选项卡（例如 **Statistics** 选项卡）上不可编辑的对话框项。

查看对象的所有方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口：

- 在 **Class Library（类库）** 的上下文菜单中选择 **Show Attributes and Methods**，查看所选 Class 的方法、只读属性与属性。
- 在插入实例的 Frame 的 Home 功能区选项卡上按 **F8**，或点击 **Show Attributes and Methods**，查看所选 Instance 的方法、只读属性与属性。

查询只读属性值的示例：

```simtalk
print Store.Capacity
```

---

## 2. Store 的只读属性

Store 提供以下只读属性：

| 只读属性 | 类型 | 返回值 | 作用 |
| --- | --- | --- | --- |
| `Capacity` | 只读属性 | `integer` | 返回 Store 的容量 |
| `XDim` / `YDim` / `ZDim` | 只读属性 | — | 对应 X-/Y-/Z-Dimension 对话框项 |
| `Stock.MyPartName` | 只读属性 | `integer` | 返回指定零件的当前库存 |

### Capacity

返回 `<Path>` 所指定的 Store 的容量。

**备注：** 容量（Capacity）等于 `XDim × YDim × ZDim` 的乘积。

**类型：** 只读属性

**语法：**

```simtalk
<Path>.Capacity → integer
```

**可监视（Watchable）：** 该只读属性可监视。

**返回值：** 数据类型为 `integer`。

**示例：**

```simtalk
if MyStore.Capacity <= lotsize
   @.move(MyStore)
end
```

**参见：** XDim、YDim、ZDim、X-Dimension、Y-Dimension、Z-Dimension

### XDim / YDim / ZDim

Store 的只读属性，分别对应 **X-Dimension**、**Y-Dimension**、**Z-Dimension** 对话框项。

**参见：** Capacity

### Stock.MyPartName

返回 `<Path>` 所指定的 Store 中，由 `MyPartName` 指定的零件的当前库存。

**备注：** `MyPartName` 是相应零件的名称，在 Store 的 **Configuration Table（配置表）** 中设置。

**类型：** 只读属性

**语法：**

```simtalk
<Path>.Stock.MyPartName → integer
```

**返回值：** 数据类型为 `integer`。

**示例：**

```simtalk
print MyStore.Stock.PartRed
// 例如可能返回 1
```

**参见：** Configuration（按钮）、Attributes of the Store

---

## 3. Store 的属性

Store 提供：

- 目录中列出的属性。
- 所有对象的属性（Attributes of All Objects）。
- 物料流对象的属性（Attributes of the Material Flow Objects）。

若要查看对象的所有方法、只读属性与属性，请打开 **Show Attributes and Methods** 窗口。

---

## 4. 相关目录交叉参考

`Sorter` 目录下的相邻子目录同样记录 Store 对象：

- `../general/README.md` — Store 对象的总体说明（概述、对话框、各选项卡、菜单、方法等）。
- `../methods/README.md` — Store 中 PE（库位/生产元素）的方法与只读属性：`Cont`、`exitBlockList`、`getStackHeight`、`mu`、`NumMU`。
- `../attributes/attributes.md` — Store 的可设置属性：`Stock.MyPartName`、`FillWholeLayer`、`Supermarket`、`XDim`/`YDim`/`ZDim`、`PlaceBuffer` 等。

---

*Source: Plant Simulation Help (11-2031 / 11-2034). Unpublished work. © 2026 Siemens.*
