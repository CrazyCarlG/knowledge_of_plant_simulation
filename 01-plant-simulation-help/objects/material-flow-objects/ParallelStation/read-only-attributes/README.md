# Read-Only Attributes of the ParallelStation

本目录（`read-only-attributes`）汇总了 **ParallelStation** 对象的只读属性相关帮助内容，来源为 `read-only-attributes.md`（及其同内容源文件 `read-only-attributes.txtx`）。本目录不含子文件夹。

## 概述

ParallelStation 提供以下只读属性：

- **Capacity [SimTalk] - ParallelStation**
- 所有对象的只读属性（_Read-Only Attributes of All Objects）
- 物流对象的只读属性（Read-Only Attributes of the Material Flow Objects）

只读属性的值可以**查询**，但不能**设置**，因为 Plant Simulation 会在查询的时间点计算其值。大多数情况下，只读属性对应对象某个选项卡（例如 Statistics 选项卡）上不可用的对话框项。

### 查看方法与属性

查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，显示所选**类**的方法、只读属性和属性。
- 按下 **F8** 键，或点击插入实例的 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，显示所选**实例**的方法、只读属性和属性。

## Capacity [SimTalk] - ParallelStation

返回由 `<Path>` 指定的 ParallelStation 的容量（capacity）。

| 项目 | 说明 |
| --- | --- |
| **Remarks** | 容量等于 `XDim × YDim` 的乘积。 |
| **Type** | 只读属性（Read-only attribute） |
| **Syntax** | `<Path>.Capacity → integer` |
| **Watchable** | 该属性可监视（watchable）。 |
| **Return Value** | 返回值为 `integer` 数据类型。 |

### 示例

```simtalk
if ParallelStation.Capacity >= lotsize 
   @.move(ParallelStation)
end
```

### See also

- XDim [SimTalk] - ParallelStation
- YDim [SimTalk] - ParallelStation
- Y-Dimension [ParallelStation]
- X-Dimension [ParallelStation]
- Capacity [SimTalk] - ParallelStation

## 查询只读属性示例

```simtalk
print ParallelStation.Capacity
```

## 附：ParallelStation 的属性（Attributes）

ParallelStation 还提供可读写的属性：

- 左侧目录中列出的属性。
- 所有对象的属性（Attributes of All Objects）。
- 物流对象的属性（Attributes of the Material Flow Objects）。

属性的值可以**设置**（set）也可以**获取**（get），既可通过对话框中的复选框、文本框和下拉列表，也可通过为相应属性赋值。

- **设置**属性值：

```simtalk
ParallelStation.XDim := 3
ParallelStation.YDim := 4
```

- **获取**属性值：

```simtalk
print ParallelStation.XDim
posit := MyStation.Cont.XPos
```

---

> 来源：Plant Simulation Help（11-1748 ~ 11-1750），Unpublished work. © 2026 Siemens
