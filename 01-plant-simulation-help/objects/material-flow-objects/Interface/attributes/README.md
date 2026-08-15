# Interface 对象属性汇总

本目录包含 **Interface（接口）** 这一物料流对象的属性说明文档。属性是对象的可读写或只读数据成员，可通过对话框中的复选框、文本框、下拉列表直接设置，也可通过 SimTalk 赋值语句设置和读取，例如：

```simtalk
Interface1.Position := 53
print Interface1.Position
posit := MyStation.Cont.XPos
```

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口（在类库中选择类的右键菜单，或选中实例后按 `F8` / 点击 Frame 的 Home 功能区中的按钮）。

Interface 对象提供以下属性（另含所有对象共有的 [Attributes of All Objects]）：

## IsExit [SimTalk]

- **类型**：只读属性（Read-only attribute）
- **功能**：返回指定 `<Path>` 所指向的 Interface 是否为 Exit 类型，是则返回 `true`，否则返回 `false`。
- **备注**：该 Interface 必须已通过 Connector 连接。
- **语法**：`<Path>.IsExit → boolean`
- **返回值**：数据类型为 `boolean`。
- **示例**：`print .Models.Model.Frame.interface.IsExit`

## MaxConnections [SimTalk] - Interface

- **类型**：属性（Attribute）
- **功能**：设置指定 `<Path>` 所指向 Interface 的最大外部连接数（Maximum Number of External Connections）。
- **语法**：`<Path>.MaxConnections:integer`
- **赋值**：可赋 `integer` 类型的值；设为 `-1` 表示无限连接数。
- **示例**：`Interface1.MaxConnections := 2`

## Position [SimTalk] - Interface

- **类型**：属性（Attribute）
- **功能**：设置 Interface 在 Frame 图标上显示传入/传出 Connector 的位置（以百分比表示）。
- **备注**：当启用 **File > Preferences > General > Connect Objects Automatically** 时使用该值。仅当 FrameA 的出口与 FrameB 的入口相距不超过 3 像素时，自动连接才生效。
- **语法**：`<Path>.Position:integer`
- **赋值**：可赋 0 到 100 之间的 `integer` 值；0 表示 Frame 图标顶部或左侧，100 表示底部或右侧。
- **示例**：`interface.Position := 53`

## Side [SimTalk]

- **类型**：属性（Attribute）
- **功能**：设置指定 `<Path>` 所指向 Interface 位于 Frame 的哪一侧。
- **语法**：`<Path>.Side:string`
- **赋值**：可赋 `string` 类型的值，可选值为 `"Top"`、`"Right"`、`"Bottom"`、`"Left"` 或 `"Angle-dependent"`。其中 `"Angle-dependent"` 会在确定 Connector 起点或终点时考虑对象之间的角度。
- **示例**：`interface.Side := "right"`
