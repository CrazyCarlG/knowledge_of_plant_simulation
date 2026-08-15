# Marker 属性（Attributes）总结

本目录用于汇总 `Marker` 对象的属性（Attributes）说明，内容来源于同目录下的 `attributes.md`（`attributes.txtx` 为其导出的纯文本版本，内容一致）。

## 概览

**Marker** 提供：

- 目录（table of contents）中列出的属性；
- 所有对象共有的属性（Attributes of All Objects）。

要查看对象的方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）的右键菜单中选择 **Show Attributes and Methods**，可查看所选类的属性；
- 在插入实例的 Frame 的 Home 选项卡中按 **F8** 或点击 **Show Attributes and Methods**，可查看所选实例的属性。

可以通过对话框中的复选框、文本框和下拉列表，或直接为属性赋值来设置属性值；同样可以查询（get）属性值。

- 查询只读属性示例：

```simtalk
print MyMarker.UUID
```

- 设置属性示例：

```simtalk
MyMarker.UseRotationOfMarker := true
```

- 获取属性示例：

```simtalk
print MyMarker.UseRotationOfMarker
```

## 属性列表

### ArrivalCtrl [SimTalk]

指定由 `<Path>` 所指对象的 Method 对象（到达控制）。

- **说明**：当在区域内自由行驶的 Transporter 到达由 `<Path>` 指定的 Marker 时，Plant Simulation 会运行该到达控制（Arrival Control）；对于全向（omnidirectional）Marker，当自由行驶的 Transporter 到达 Marker 处曲率/圆角的中点时会运行该控制。若未指定 Method，则该属性值为 `VOID`。
- **类型**：Attribute（属性）
- **语法**：

```simtalk
<Path>.ArrivalCtrl:method
```

- **可赋值类型**：`method`
- **示例**：

```simtalk
MyMarker.ArrivalCtrl := &myMethod
```

- **参见**：Arrival Control [Marker]

### UseRotationOfMarker [SimTalk]

设置 AGV 驶向目的地时是否使用由 `<Path>` 指定 Marker 的旋转（rotation）。

- **说明**：`true` 表示使用该 Marker 的旋转，`false` 表示不使用。
- **类型**：Attribute（属性）
- **语法**：

```simtalk
<Path>.UseRotationOfMarker:boolean
```

- **可赋值类型**：`boolean`
- **示例**：

```simtalk
MyMarker.UseRotationOfMarker := true
```

- **参见**：Amount [text box] - AGVPool
