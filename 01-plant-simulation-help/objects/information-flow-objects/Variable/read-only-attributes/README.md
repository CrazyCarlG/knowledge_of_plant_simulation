# Read-Only Attributes of the Variable

本目录包含 Variable 对象的只读属性（Read-Only Attributes）说明文档。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `read-only-attributes.md` | Variable 只读属性的主要文档 |
| `read-only-attributes.txtx` | 同一内容的原始帮助文本（Plant Simulation Help） |

## 内容概要

只读属性对应对象某个选项卡（例如 **Statistics** 选项卡）上的对话框条目。这些属性只能查询，不能直接修改。

### 查看方式

- 在 **Class Library** 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **Class** 的方法、只读属性和属性。
- 按 **F8**（或点击 Frame 的 **Home** 功能区选项卡中的 **Show Attributes and Methods**），可查看所选 **Instance** 的方法、只读属性和属性。

查询只读属性值的示例：

```simtalk
print &MyVariable.AsString
```

### 只读属性

#### `asString`

以字符串形式返回 Variable 的值。

- **备注**：以字符串形式获取值对于数据类型为 `object` 的 Variable 尤其有用。若 Variable 包含相对路径，`asString` 返回该相对路径。
- **类型**：只读属性
- **语法**：

  ```simtalk
  <&>Variable.asString → string
  ```

- **返回值**：数据类型为 `string`。
- **示例**：

  ```simtalk
  ObjVariable := "~.ProdMgr.prodplan"
  var a1 := ObjVariable             // 赋值 .Models.Model.ProdMgr.prodplan
  var a2 := &ObjVariable.asString   // 赋值 "~.ProdMgr.prodplan"
  ```

### 访问 Variable 的属性

对象 **Variable** 提供：

- 目录中列出的属性。
- **所有对象的属性**（Attributes of All Objects）。

> **注意**
>
> 只能通过引用运算符 `&` 访问 Variable 对象本身所引用的属性；不使用该运算符时，属性将作用于 Variable 的内容。

```simtalk
&Variable.Name := "MyVariable"
```
