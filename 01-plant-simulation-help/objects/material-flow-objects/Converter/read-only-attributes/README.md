# Converter 只读属性汇总

本目录汇总了 Plant Simulation 中 **Converter（升降机/转换器）** 对象的只读属性（Read-Only Attributes）文档。资料来源为本目录下的 `read-only-attributes.md` 与 `read-only-attributes.txtx`（两者内容一致），无子目录。

## 概述

Converter 提供以下几类只读属性：

- 本页列出的只读属性
- 所有对象的只读属性（Read-Only Attributes of All Objects）
- 物流对象（Material Flow Objects）的只读属性

只读属性可以查询取值，但**不能赋值**——Plant Simulation 会在查询的时间点计算其值。多数只读属性对应对象某个选项卡（如 **Statistics** 统计选项卡）上不可编辑的对话框项。

查看对象全部方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口（类库上下文菜单，或选中实例后按 **F8** / 点击 Home 选项卡上的 Show Attributes and Methods）。

查询只读属性示例：

```simtalk
print Converter.GetCurrentExit
```

## 只读属性列表

| 属性 | 返回类型 | 说明 |
| --- | --- | --- |
| `GetCurrentExit` | `integer` | 返回 MU 从 `<Path>` 指定的 Converter 退出的侧面编号 |
| `GetNextEntranceNumber` | `integer` | 返回下一个 MU 可以进入 `<Path>` 指定的 Converter 的侧面编号 |
| `IsUp` | `boolean` | 返回 Converter 处于上升位置（`true`）还是下降位置（`false`） |
| `StatMovingEmptyPortion` | `real` | 统计周期内 Converter 处于升降状态且**未**输送 MU 的时间占比 |
| `StatMovingEmptyTime` | `time` | Converter 处于升降状态且**未**输送 MU 的总时间 |
| `StatMovingLoadedPortion` | `real` | 统计周期内 Converter 处于升降状态且**正在**输送 MU 的时间占比 |
| `StatMovingLoadedTime` | `time` | Converter 处于升降状态且**正在**输送 MU 的总时间 |

## 各属性详情

### GetCurrentExit

返回 MU 从 `<Path>` 指定的 Converter 退出的侧面编号。侧面编号取决于 Converter 插入仿真模型时的方向。

- **类型**：只读属性
- **语法**：`<Path>.GetCurrentExit → integer`

```simtalk
No := ?.GetCurrentExit
```

### GetNextEntranceNumber

返回下一个 MU 可以进入 `<Path>` 指定的 Converter 的侧面编号。侧面编号取决于 Converter 插入模型时的方向。

- **类型**：只读属性
- **语法**：`<Path>.GetNextEntranceNumber → integer`

```simtalk
No := ?.GetNextEntranceNumber
```

### IsUp

返回 `<Path>` 指定的 Converter 是否处于上升位置（`true`）或下降位置（`false`）。

- **类型**：只读属性
- **语法**：`<Path>.IsUp → boolean`

```simtalk
PosUpDown := MyConverter.IsUp
```

该属性也可用于**启动升降过程**：

```simtalk
MyConverter.IsUp := true
```

### StatMovingEmptyPortion

返回统计采集周期内，Converter 处于升降状态且**未**输送 MU 的时间占比。

- **类型**：只读属性
- **语法**：`<Path>.StatMovingEmptyPortion → real`

```simtalk
print Converter.StatMovingEmptyPortion
```

**参见**：Tab Statistics [Converter]、Moving Time [statistics report]

### StatMovingEmptyTime

返回 Converter 处于升降状态且**未**输送 MU 的总时间。

- **类型**：只读属性
- **语法**：`<Path>.StatMovingEmptyTime → time`

```simtalk
print Converter.StatMovingEmptyTime
```

**参见**：Moving Time [statistics report]

### StatMovingLoadedPortion

返回统计采集周期内，Converter 处于升降状态且**正在**输送 MU 的时间占比。

- **类型**：只读属性
- **语法**：`<Path>.StatMovingLoadedPortion → real`

```simtalk
print Converter.StatMovingLoadedPortion
```

**参见**：Tab Statistics [Converter]、Moving Time [statistics report]

### StatMovingLoadedTime

返回 Converter 处于升降状态且**正在**输送 MU 的总时间。

- **类型**：只读属性
- **语法**：`<Path>.StatMovingLoadedTime → time`

```simtalk
print Converter.StatMovingLoadedTime
```

**参见**：Moving Time [statistics report]

## 相关主题

目录中还引用了以下相关主题：

- `setAttributeList(AttributeList:table)` — 将传入列表的内容复制到 Converter 的目标列表中

  ```simtalk
  Converter.setAttributeList(MyAttributes)
  ```

- `getAttributeList` — 参见 "getAttributeList [SimTalk] - Converter"
- Open List [button] - Converter
- Data Held in Tabular Form in Attributes [material flow objects]
- Strategy [drop-down list] - Converter
- Attributes of the Converter
