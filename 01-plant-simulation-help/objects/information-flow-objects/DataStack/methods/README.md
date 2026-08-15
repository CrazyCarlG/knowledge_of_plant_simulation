# DataStack — Methods (README)

本目录包含 Plant Simulation 中 **DataStack** 对象（信息流对象）的方法文档。

## 目录内容

- `methods.md` — DataStack 方法的 Markdown 说明文档
- `methods.txtx` — DataStack 方法的原始文档源文件（供参考）

## DataStack 提供的方法

DataStack 提供以下方法：

- `createNestedList [SimTalk]` — DataQueue
- `pop [SimTalk]` — DataStack
- `push [SimTalk]` — Stack
- `pushList [SimTalk]`
- `top [SimTalk]`

此外，DataStack 还继承：

- **Lists 与 Tables 的方法**
- **所有对象（All Objects）的方法**

> 要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口。
>
> - 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选 *Class* 的属性和方法。
> - 在插入实例的 Frame 的 Home 功能区选项卡上按 **F8** 键或点击 **Show Attributes and Methods**，可显示所选 *Instance* 的属性和方法。

## 语法约定

方法语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示该方法所应用对象的路径。
- 方法签名（由参数标识符和数据类型组成）列在括号内。例如 `(Parameter:string)` 表示数据类型为 `string` 的参数。除常量值外，也可使用所需类型的变量或返回所需数据类型的方法。
- 可选参数列在方括号内。例如 `[,Parameter:boolean]` 表示可以输入、也可以不输入该布尔参数。
- 若参数有默认值，签名会在参数后显示该默认值。
- 若方法有返回值，签名会在箭头 `->` 后显示其数据类型。

> **注意：** 请务必为括号内的表达式输入括号 `(…)`。不输入括号可能导致意外结果并打开调试器（Debugger）。

### 签名中使用的缩写

| 参数 | 数据类型 | 取值范围 |
|---|---|---|
| `integer` | integer | 大于零的整数 |
| `any` | 所有数据类型 | 取决于数据类型 |
| `listrange` | — | 一个范围 |
| `direction` | string | `"up"`、`"down"`、`" "` |
| `attributes` | string | 属性的名称 |

## DataQueue 与 DataStack 的只读属性

DataStack 和 DataQueue 提供：

- Lists 与 Tables 的只读属性
- 所有对象（All Objects）的只读属性

可以查询只读属性的值，但不能设置它们，因为 Plant Simulation 会在查询的时刻计算该值。大多数情况下，只读属性对应对象某个选项卡（例如 **Statistics** 选项卡）上不可用的对话框项。

查询只读属性示例：

```
print MyDataStack.Full
```

## DataQueue 与 DataStack 的属性

DataStack 和 DataQueue 提供：

- Lists 与 Tables 的属性
- 所有对象（All Objects）的属性
