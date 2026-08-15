# Read-Only Attributes of the Workplace

本目录包含 Workplace（工作场所）对象的只读属性相关文档。目录内现有文件：

- `read-only-attributes.md` — 结构化的 Markdown 文档
- `read-only-attributes.txtx` — 纯文本版本，内容与前者一致

> 注：该目录下没有子文件夹，因此无子目录 README.md 可汇总。

## 概述

Workplace 提供了 **所有对象的只读属性（Read-Only Attributes of All Objects）**。

- 只读属性的值**只能查询，不能设置**。Plant Simulation 会在查询的时间点即时计算该值。
- 大多数只读属性对应对象某个选项卡（如 **Statistics（统计）** 选项卡）上不可用的对话框条目。
- 可通过 **Show Attributes and Methods（显示属性和方法）** 窗口查看对象的所有方法、只读属性和属性：
  - 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，显示所选 **Class（类）** 的成员。
  - 在插入实例的 Frame 的 Home 功能区选项卡上按 **F8** 键或点击 **Show Attributes and Methods**，显示所选 **Instance（实例）** 的成员。

查询只读属性值的示例：

```simtalk
print MyWorkplace.UUID
```

## Workplace 的属性

Workplace 提供：

- 左侧目录中列出的属性
- 所有对象的属性（Attributes of All Objects）
- 物料流对象的属性（Attributes of the Material Flow Objects）

## getRouteLength [SimTalk] - Workplace

返回一个 Worker 从 `<Path>` 指定的 Workplace 走到另一个 Workplace 或 WorkerPool 所需经过的**路径长度**。

### 类型

Method（方法）

### 语法

```
<Path>.getRouteLength(ToWorkplace:path[, FreelyWithinArea:boolean:=false]) → length
```

### 参数

- `ToWorkplace`（数据类型 `path`）：指定目标 Workplace。
- `FreelyWithinArea`（数据类型 `boolean`，可选）：设置 Worker 是否在区域内自由行走到达 Workplace。
  - 接受默认值 `false` 或不指定该参数：通过由 **Connectors（连接器）** 连接的 **Footpaths（步行路径）** 计算两个 Workplace 之间的路径长度。
  - 指定 `true`：计算区域内自由行走的路径长度。

### 参数默认值

默认值为 `false`。

### 返回值

返回值的数据类型为 `length`。

如果 Plant Simulation 未找到路径，则返回 `-1`。

```simtalk
var len:length := Workplace1.getRouteLength(Workplace2)
```

## 参考资料

- Plant Simulation Help 11-3019
- Plant Simulation Help 11-3020
