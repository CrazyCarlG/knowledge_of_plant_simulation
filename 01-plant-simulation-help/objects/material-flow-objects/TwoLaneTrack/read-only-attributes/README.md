# TwoLaneTrack 只读属性（Read-Only Attributes）

本目录收录了 TwoLaneTrack（双车道轨道）对象的只读属性文档。

## 目录内容

- `read-only-attributes.md` — TwoLaneTrack 只读属性的详细说明
- `read-only-attributes.txtx` — 同名文本源文件
- `Plant-Simulation-Help2606_5452-5459.pdf` — 对应的 Plant Simulation 帮助手册 PDF

## 概述

TwoLaneTrack 对象提供以下只读属性，同时继承了所有对象（All Objects）和物料流对象（Material Flow Objects）的只读属性。

只读属性的值只能查询（query），不能设置（set）——Plant Simulation 会在查询的那一刻计算其值。大多数只读属性对应对象某个选项卡（例如 Statistics 选项卡）上不可编辑的对话框项。

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口。对于 TwoLaneTrack，该对话框会分别显示 A 车道和 B 车道（lane A / lane B）的内容。

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，可显示所选类的方法、只读属性和属性。
- 在插入实例的 Frame 中按 F8 键，或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，可显示所选实例的方法、只读属性和属性。

查询只读属性的示例：

```simtalk
print TwoLaneTrack.A.NumPred
```

## 只读属性清单

| 属性 | 类型 | 适用车道 | 说明 | 返回值 |
| --- | --- | --- | --- | --- |
| `succLaneNo` | Method（方法） | A / B | 返回指定车道的后继车道编号 | `integer` |
| `IsLaneA` | 只读属性 | A | 判断 Transporters（运输设备）是否在 A 车道上行驶 | `boolean` |
| `IsLaneB` | 只读属性 | B | 判断 Transporters 是否在 B 车道上行驶 | `boolean` |
| `NumPred` | 只读属性 | A / B | 返回指定车道的前驱（predecessors）数量 | `integer` |
| `NumSucc` | 只读属性 | A / B | 返回指定车道的后继（successors）数量 | `integer` |
| `OccupiedLength` | 只读属性 | A / B | 返回车道上所有 Transporters 占用的长度 | `length` |

## 各属性语法

### succLaneNo

```simtalk
<Path>.A.succLaneNo([LaneNumber:integer]) → integer
<Path>.B.succLaneNo([LaneNumber:integer]) → integer
```

- 可选参数 `LaneNumber`（`integer`）指定第 n 个后继车道的编号，对象需要先建立连接。
- 返回值类型为 `integer`。

### IsLaneA / IsLaneB

```simtalk
<Path>.A.IsLaneA → boolean
<Path>.B.IsLaneB → boolean
```

- 返回值类型为 `boolean`。
- 参见：Lane A / Lane B。

### NumPred / NumSucc

```simtalk
<Path>.A.NumPred → integer
<Path>.B.NumPred → integer
<Path>.A.NumSucc → integer
<Path>.B.NumSucc → integer
```

- 返回值类型为 `integer`。

### OccupiedLength

```simtalk
<Path>.A.OccupiedLength → length
<Path>.B.OccupiedLength → length
```

- 返回值类型为 `length`。
- 说明：位于 TwoLaneTrack 上的每个 Transporter 都会占用轨道总长度的一部分。
- 参见：Length 文本框（车道 A）、Length 文本框（车道 B）、TwoLaneTrack 的属性。

## 相关文档

- TwoLaneTrack 的属性（Attributes of the TwoLaneTrack）
- 所有对象的只读属性（Read-Only Attributes of All Objects）
- 物料流对象的只读属性（Read-Only Attributes of the Material Flow Objects）
