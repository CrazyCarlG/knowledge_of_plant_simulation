# Trigger 的方法与只读属性

本目录汇总了 Plant Simulation 中 **Trigger（触发器）** 对象提供的方法（Methods）与只读属性（Read-Only Attributes）。

## 内容来源

- `methods.md`：Trigger 的方法与只读属性文档（本目录主要文档）。
- `methods.txtx`：`methods.md` 的纯文本导出，内容相同。

## 概述

Trigger 对象提供以下方法与属性：

- 左侧目录中列出的方法（见下表）。
- 所有对象共有的方法（Methods of All Objects）。
- 只读属性 `CurrentValue`。
- 所有对象共有的只读属性（Read-Only Attributes of All Objects）。

可通过 **Show Attributes and Methods** 窗口查看对象的全部方法、只读属性与属性（在 Class Library 上下文菜单中选择，或选中实例后按 **F8** / 点击 Home 选项卡的对应按钮）。

## 语法行约定

方法语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法作用对象的路径。
- 括号内为方法签名（参数标识符 + 数据类型），如 `(Parameter:string)`。
- 可选参数用方括号列出，如 `[,Parameter:boolean]`。
- 默认值在参数后用 `:=` 表示，如 `:= false`。
- 返回值类型在箭头 `→` 后表示，如 `→ boolean`。

> **注意**：表达式中的括号必须成对输入，否则可能产生意外结果并打开调试器（Debugger）。

## 方法列表

| 方法 | 语法 | 说明 | 返回 |
| --- | --- | --- | --- |
| `compute` | `<Path>.compute` | 为触发器类型 Combination 生成新的值列表。组合公式变更后建议始终调用。 | — |
| `deleteTriggeredAttr` | `<Path>.deleteTriggeredAttr(Object:object, Attribute:string) -> boolean` | 从 Triggered Attributes 表中删除指定对象与属性。 | boolean |
| `deleteTriggeredMeth` | `<Path>.deleteTriggeredMeth(Method:object) -> boolean` | 从 Triggered Methods 列表中删除指定 Method。 | boolean |
| `insertTriggeredAttr` | `<Path>.insertTriggeredAttr(Object:object, Attribute:string)` | 将指定对象的指定属性插入 Triggered Attributes 表。 | — |
| `insertTriggeredMeth` | `<Path>.insertTriggeredMeth(Method:object)` | 将指定 Method 插入 Triggered Methods 列表。 | — |

## 只读属性

| 属性 | 说明 |
| --- | --- |
| `CurrentValue` | 触发器的当前值。可查询但不可设置，由 Plant Simulation 在查询时刻计算得出。 |

查询示例：

```
print MyTrigger.CurrentValue
```
