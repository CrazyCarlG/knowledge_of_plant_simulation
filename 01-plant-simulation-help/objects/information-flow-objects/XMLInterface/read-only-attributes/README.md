# XMLInterface 只读属性（Read-Only Attributes）

本目录整理了 `XMLInterface`（信息流对象）的**只读属性**相关文档。内容来源为 Plant Simulation 帮助文档中「Read-Only Attributes of the XMLInterface」一节。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `read-only-attributes.md` | XMLInterface 只读属性的 Markdown 文档（主文档） |
| `read-only-attributes.txtx` | 同一内容的纯文本导出 |

## 内容总结

`XMLInterface` 提供：

- 只读属性 **GetNumberAttributes [SimTalk]**。
- **_Read-Only Attributes of All Objects**（所有对象的只读属性）。

### 只读属性说明

- **可以查询**只读属性的值，但**不能设置**它们。因为 Plant Simulation 会在你查询的那一刻动态计算出该值。
- 大多数只读属性对应于对象某个选项卡（例如 **Statistics** 选项卡）上不可用的对话框项。
- 若要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods**（显示属性和方法）窗口：
  - 在类库（Class Library）上下文菜单中选择 **Show Attributes and Methods**，可显示所选类的相关项。
  - 在已插入实例的 Frame 的 Home 功能区选项卡中按 **F8** 或点击 **Show Attributes and Methods**，可显示所选实例的相关项。

### GetNumberAttributes [SimTalk]

- **功能**：返回由 `<Path>` 指定的 XMLInterface 活动节点的属性数量。
- **备注**：`GetNumberAttributes` 适用于随机遍历数据（randomly traverse data）的场景。
- **类型**：只读属性
- **语法**：

```simtalk
<Path>.GetNumberAttributes → integer
```

- **返回值**：数据类型为 `integer`。
- **示例**：

```simtalk
numberAttributes := MyXMLInterface.GetNumberAttributes
```

查询只读属性值的示例：

```simtalk
print MyXMLInterface.GetNumberAttributes
```

## 相关：XMLInterface 的属性（可读写）

文档同时涵盖了 **Attributes of the XML Interface**，与只读属性相区分：

- 可设置和获取属性的值：既可通过对话框窗口中的复选框、文本框和下拉列表，也可通过给相应属性赋值。
- 设置属性值示例：

```simtalk
MyFileInterface.FileName := "C:\users\johnE\myData.txt"
```

- 获取属性值示例：

```simtalk
print MyXMLInterface.Context
posit := Station.Cont.XPos
```

## 相关代码上下文

```simtalk
MyXMLInterface.writeElement("description", "An in-depth ...")
// terminate the item 'book'
MyXMLInterface.endElement
// terminate the item named 'catalog'
MyXMLInterface.endElement
MyXMLInterface.close
```
