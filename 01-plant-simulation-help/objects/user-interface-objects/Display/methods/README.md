# Display 对象的方法（Methods）— 目录说明

本目录（`Display/methods`）汇总了 Plant Simulation 用户界面对象 **Display（显示器）** 的方法（Methods）与只读属性（Read-Only Attributes）相关文档，包含以下文件：

- `methods.md` — Display 方法的 Markdown 版本说明。
- `methods.txtx` — Display 方法的原始帮助文本（内容与 `methods.md` 对应）。

## 内容总结

### 1. 概述
Display 对象提供：

- 左侧目录中列出的方法；
- 所有对象共有的方法（Methods of All Objects）。

可通过 **Show Attributes and Methods** 窗口查看对象的所有方法、只读属性和属性：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，查看所选类的方法、只读属性与属性；
- 在已插入实例的 Frame 中按 **F8** 或点击 Home 选项卡上的 **Show Attributes and Methods**，查看所选实例的方法、只读属性与属性。

### 2. 语法行（Syntax line）说明
方法语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示方法所应用对象的路径；
- 括号内为方法签名，由参数标识符和数据类型组成，如 `(Parameter:string)`；
- 可选参数写在方括号内，如 `[,Parameter:boolean]`；
- 参数默认值以 `:=` 表示，如 `:= false`；
- 返回值类型以箭头 `→` 表示，如 `→ boolean`。

> **注意**：括号内的表达式必须保留括号 `(…)`，否则可能导致意外结果并打开调试器（Debugger）。

### 3. 方法列表

#### `resetMinMax [SimTalk]`
删除 Display 显示的的最小值与最大值，并将其重置为默认值。

- **类型**：Method
- **语法**：`<Path>.resetMinMax`
- **示例**：`print MyDisplay.resetMinMax`
- **另见**：Reset Values [button]

#### `update [SimTalk] - Display`
在一定时间过后更新 Display 显示的值。

- **备注**：`update` 仅在 Sample 模式下有用，可用于强制 Display 显示当前值（例如修改输入值之后）。为兼容旧版 Plant Simulation，可指定 time 类型的参数 `Time`。
- **类型**：Method
- **语法**：`<Path>.update`
- **示例**：`MyDisplay.update`
- **另见**：Interval [text box] - Display

### 4. Display 的只读属性（Read-Only Attributes）
Display 提供：

- 左侧目录中列出的只读属性；
- 所有对象共有的只读属性（Read-Only Attributes of All Objects）。

只读属性的值只能查询、不能设置，由 Plant Simulation 在查询时刻自动计算。多数情况下，只读属性对应对象某个选项卡（如 Statistics 选项卡）上不可用的对话框项。
