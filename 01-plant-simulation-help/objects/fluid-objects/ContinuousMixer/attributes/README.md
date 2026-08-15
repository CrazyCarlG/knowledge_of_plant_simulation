# ContinuousMixer — Attributes（属性）

本目录收录 ContinuousMixer（连续搅拌器 / 连续混合器）对象的属性（Attributes）文档。ContinuousMixer 提供的属性来源包括：

- 左侧目录中列出的属性
- 流体对象（Fluid Objects）的公共属性
- 所有对象（All Objects）的公共属性

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `attributes.md` | ContinuousMixer 对象属性的 Markdown 文档（主内容） |
| `attributes.txtx` | 同一内容的原始导出文本（含页码脚注，内容与 attributes.md 基本一致） |

> 本目录下没有子文件夹，也没有其他 README.md 文件，因此本总结基于 `attributes.md` 的内容整理。

## 查看属性与方法

- 在 Class Library（类库）的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **类（Class）** 的方法、只读属性和属性。
- 按 **F8** 键，或点击已插入实例所在 Frame 的 Home 功能区中的 **Show Attributes and Methods**，可查看所选 **实例（Instance）** 的方法、只读属性和属性。

### 查询只读属性

```simtalk
print ContinuousMixer.Full
```

## 设置与获取属性值

可通过对话框中的复选框、文本框和下拉列表，或直接为属性赋值来设置/获取属性值。

设置属性示例：

```simtalk
MyContinuousMixer.OutflowRate := 1
```

获取属性示例：

```simtalk
print MyContinuousMixer.OutflowRate
```

```simtalk
posit := MyStation.Cont.XPos
```

## 属性参考

### MaterialsTable [SimTalk] - ContinuousMixer

设置 MaterialsTable（物料表），其中包含最终产品以及各 FluidSource 原料的配比、密度、颜色等详细信息，供 `<Path>` 指定的 ContinuousMixer 进行混合。

- **语法**：`<Path>.MaterialsTable:path`
- **赋值类型**：path
- **示例**：

```simtalk
MyContinuousMixer.MaterialsTable := MyMaterialsTable
```

- **参见**：Materials Table [Mixer] 对象

### Product [SimTalk] - ContinuousMixer

设置 ContinuousMixer 通过混合原料所要生产的中间产品或最终产品的名称。

- **备注**：该 Product 名称必须在 MaterialsTable 中定义。
- **类型**：Attribute
- **语法**：`<Path>.Product:string`
- **赋值类型**：string
- **示例**：

```simtalk
MyContinuousMixer.Product := "MyProduct"
```

- **参见**：Product [文本框] - Mixer、Materials Table [Mixer]、Portioner

## 相关对象：Portioner

使用 **Portioner** 对象可将自由流动的产品生成移动对象（MU），随后可将 Portioner 与某个物流对象连接，以进一步加工所生成的 MU。
