# Marker 的方法（Methods）

本目录汇总了 Plant Simulation 中 **Marker（标记）** 资源对象的方法文档。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `methods.md` | Marker 的方法与只读属性说明（整理后的 Markdown 版本） |
| `methods.txtx` | 从 Plant Simulation Help 提取的原始文本 |

> 本目录下无子文件夹，因此无子文件夹 README.md 可供汇总。

## 概要

Marker 提供 **“所有对象的方法”（Methods of All Objects）** 以及 **“所有对象的只读属性”（Read-Only Attributes of All Objects）**，此外还包含一个 Marker 专属的 SimTalk 方法 `getRouteLength`。

### 查看方法与属性

可通过 **Show Attributes and Methods** 窗口查看对象的全部方法、只读属性和属性：

- 在 **Class Library** 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **类（Class）** 的方法、只读属性和属性。
- 在插入实例的 Frame 中按 **F8** 键，或点击 **Home** 功能区标签页上的 **Show Attributes and Methods**，可查看所选 **实例（Instance）** 的方法、只读属性和属性。

### 语法约定（Syntax conventions）

方法语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示方法所应用对象的路径。
- 括号内为方法签名（参数标识符及其数据类型），如 `(Parameter:string)` 表示 `string` 类型参数；除常量外，也可使用相应类型的变量或返回该类型的方法。
- 可选参数放在方括号内，如 `[,Parameter:boolean]`。
- 参数含默认值时，签名会在参数后标注默认值（如 `:= false`）。
- 方法有返回值时，签名会在箭头后标注返回数据类型（如 `→ boolean`）。
- **注意**：表达式中的括号 `(…)` 必须输入，否则可能产生意外结果并打开调试器（Debugger）。

## Marker 专属方法

### getRouteLength [SimTalk]

返回由 `<Path>` 指定的 Marker 到指定目的地的**路线长度**。

```
<Path>.getRouteLength(ToMarker:path[, byref ObjectsAlongRoute:object[],
RouteWeightingAttribute:string]) → length
```

**参数：**

- `ToMarker`（`path`）— 指定目的地对象。
- `ObjectsAlongRoute`（可选，`object[]`）— `object` 类型数组，Marker 会将通往目的地的沿途对象填入其中。
- `RouteWeightingAttribute`（可选，`string`）— 用于自动路由的 **Route Weighting Attribute（路线权重属性）** 名称；若未传入，Plant Simulation 不对路线长度进行加权。

**返回值：**

- 数据类型为 `length`。
- 若目的地不可达，返回 `-1`。

**示例：**

```simtalk
print Marker1.getRouteLength(Marker2)
```

## 只读属性（Read-Only Attributes）

Marker 提供 **“所有对象的只读属性”**。只读属性的值可以查询，但不能设置——Plant Simulation 会在查询的时间点计算该值。多数情况下，只读属性对应对象某个选项卡（如 **Statistics** 选项卡）上不可用的对话框项。

## 参考

- 详见 `methods.md` 获取完整方法与属性说明。
