# Read-Only Attributes of the Display — 目录摘要

本目录介绍 **Display（显示）对象**的只读属性（Read-Only Attributes）。

## 文件说明

| 文件 | 说明 |
| --- | --- |
| `read-only-attributes.md` | Display 对象只读属性的正式文档 |
| `read-only-attributes.txtx` | 与 md 内容对应的原始帮助文本（含页码与版权信息） |

## 概述

Display 对象提供以下只读属性（以及所有对象的通用只读属性）。只读属性**只能查询、不能设置**——Plant Simulation 会在你查询的时间点即时计算其值。多数只读属性对应对象某个选项卡（如 Statistics 选项卡）上不可编辑的对话框项。

查看对象所有方法、只读属性和属性：打开 **Show Attributes and Methods** 窗口（类库上下文菜单，或选中实例后按 **F8** / Home 选项卡中的按钮）。

查询示例：

```simtalk
print MyDisplay.GetMaximum
```

## 只读属性列表

| 属性 | 返回类型 | 说明 |
| --- | --- | --- |
| `GetAverage` | `real` | 返回 Display 记录数值的平均值 |
| `GetMaximum` | `real` | 返回 Display 所显示数值范围的最大值 |
| `GetMinimum` | `real` | 返回 Display 所显示数值范围的最小值 |
| `GetStandardDeviation` | `real` | 返回 Display 记录数值的标准差 |

### 备注

- `GetMaximum` 与 `GetMinimum` 仅适用于 **Watch 模式**；在 **Sample 模式**下，仅当激活 **MUs and States** 且插入 Display 的 Frame 处于打开状态时才会更新值。
- 所有属性语法形式统一为 `<Path>.<属性名> → real`。

## 相关方法

文档还附带介绍了方法 **`update`**（SimTalk）：

- 用途：在经过一定时间后更新 Display 所显示的数值。
- 仅与 **Sample 模式**配合使用；例如在修改输入值后强制 Display 显示当前值。
- 为兼容旧版本，可指定 `time` 类型的参数 `Time`。
- 语法：`<Path>.update`

## 交叉引用

- `GetMaximum` / `GetMinimum` 参见：`resetMinMax`、`Maximum`/`Minimum [Display]`、`Mode [drop-down list] - Display`、`MUs and States [Home ribbon]`
- `update` 参见：`Interval [text box] - Display`
