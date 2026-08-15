# Comment 对象属性总结

本目录包含 Comment（注释）对象的属性文档。Comment 对象提供以下属性，以及所有对象共有的属性（Attributes of All Objects）。

## 查看属性和方法

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 **Class Library** 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的属性。
- 按下 **F8** 键，或在插入实例的 Frame 的 **Home** 功能区选项卡上点击 **Show Attributes and Methods**，可查看所选实例的属性。

查询只读属性示例：

```simtalk
print MyComment.UUID
```

设置和获取属性值，可以通过对话框中的复选框、文本框和下拉列表，也可以通过给属性赋值：

```simtalk
MyComment.Color := makeRGBColor(255,0,0)   // 设置属性
print MyComment.font                        // 获取属性
posit := Station.Cont.XPos
```

## 属性列表

| 属性 | 语法 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| BackgroundColor | `<Path>.BackgroundColor:integer` | integer | 设置插入到 Frame 中的 Comment 的背景色 |
| Color | `<Path>.Color:integer` | integer | 设置 Plant Simulation 在 Frame 中显示 Comment 文本的颜色 |
| Cont | `<Path>.Cont:string` | string | 设置 Comment 选项卡上文本框的内容 |
| Font | `<Path>.Font:integer` | integer | 设置 Comment 在 Frame 中显示的字体大小 |
| SaveAsRichedit | `<Path>.SaveAsRichedit:boolean` | boolean | 使 Comment 以富文本格式保存文本框内容 |
| Text | `<Path>.Text:string` | string | 设置 Comment 在 Frame 中显示的注释文本 |
| Transparent | `<Path>.Transparent:boolean` | boolean | 使 Comment 的背景在 Frame 中透明 |

## 属性详解

### BackgroundColor

设置插入到 Frame 中的 Comment 的背景色。

- **备注：** 使用 `makeRGBValue` 方法设置颜色的 RGB 值。
- **示例：**

```simtalk
MyComment.BackgroundColor := makeRGBValue(100,100,100)
MyComment.BackgroundColor := 6579300 // 与上面的颜色相同
```

### Color

设置 Plant Simulation 在 Frame 中显示 Comment 文本的颜色。

- **备注：** 使用 `makeRGBValue` 方法设置颜色的 RGB 值。
- **示例：**

```simtalk
MyComment.Color := makeRGBValue(255,0,0)
```

### Cont

设置 Comment 选项卡上文本框的内容。

- **备注：** 输入反斜杠 `\` 可插入换行符。
- **示例：**

```simtalk
MyComment.Cont := "Species: Aardvark\
                 amount: 45 \
                 weight: 780kg" // 分配多行注释
```

### Font

设置 Plant Simulation 在 Frame 中显示 Comment 的字体大小。

- **取值：** `1` 表示小（Small），`2` 表示中（Medium），`3` 表示大（Large），`4` 表示特大（Extra Large）。
- **示例：**

```simtalk
if MyComment.Font < 4 
   MyComment.Font := MyComment.Font + 1
```

### SaveAsRichedit

使 Comment 以富文本格式保存文本框内容（`true`）或不保存（`false`）。

- **备注：** 富文本会保留所应用的所有格式属性。
- **示例：**

```simtalk
MyComment.SaveAsRichedit := false
```

### Text

设置 Comment 在 Frame 中显示的注释文本。

- **备注：** 文本可以包含空格和/或特殊字符。
- **示例：**

```simtalk
MyComment.Text := "Buffer utilization in %"
```

### Transparent

使 Comment 的背景在 Frame 中透明（`true`）或不透明（`false`）。

- `true`：以所选字体颜色（Font Color）在 Frame 背景上显示 Comment。
- `false`：文本周围的空间以白色显示。
- **示例：**

```simtalk
MyComment.Transparent := false
```
