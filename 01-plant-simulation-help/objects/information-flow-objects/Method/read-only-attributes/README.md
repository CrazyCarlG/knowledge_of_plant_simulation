# Method 对象的只读属性（Read-Only Attributes）

本目录汇总了 `Method` 对象的只读属性相关内容。只读属性的值只能查询、不能设置：Plant Simulation 会在查询时刻计算该值。多数情况下，只读属性对应对象某个选项卡上不可用的对话框项（例如 **Statistics** 选项卡）。

## 如何查看

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性和属性。
- 在已插入实例的 Frame 上按 **F8**，或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，可查看所选实例的方法、只读属性和属性。

## 只读属性列表

| 属性 | 说明 | 返回类型 |
| --- | --- | --- |
| `Encrypted` | 返回由引用运算符 `<&>` 指定的 Method（或数据类型为 `method` 的用户定义属性）是否已加密（`true` / `false`） | `boolean` |
| `NumInExecution` | 返回由引用运算符 `<&>` 指定的 Method 当前正在执行的次数 | `integer` |

### Encrypted [SimTalk]

- **类型**：只读属性
- **语法**：`<&>Method.Encrypted → boolean`
- **返回值**：`boolean`

示例：

```simtalk
print &MyMethod.Encrypted
```

### NumInExecution [SimTalk]

- **类型**：只读属性
- **语法**：`<&>Method.NumInExecution → integer`
- **返回值**：`integer`

示例：

```simtalk
print &MyMethod.NumInExecution
```

## Method 对象提供的属性

`Method` 对象提供：

- 上表列出的只读属性。
- 所有对象共有的属性（Attributes of All Objects）。

> **注意**：访问 `Method` 对象自身（而非其内容）的属性时，必须通过引用运算符 `&`。不使用 `&` 运算符时，属性会作用于 Method 的内容（代码文本）。

## 目录内容

- `read-only-attributes.md`：Method 只读属性的说明文档。
- `read-only-attributes.txtx`：同内容的原始帮助文本（含页码与版权信息）。
