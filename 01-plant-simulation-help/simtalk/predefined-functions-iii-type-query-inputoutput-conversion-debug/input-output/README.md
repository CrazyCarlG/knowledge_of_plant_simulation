# Input/Output 函数（SimTalk 输入/输出）

本目录介绍 SimTalk 中用于**输入**和**输出**数据的预定义函数。这些函数打开的所有对话框均为**模态（modal）**对话框——只有用户对请求的交互做出反应后，仿真才会继续运行。

> 详细内容见 [input-output.md](./input-output.md)。

## 函数一览

| 分类 | 函数 | 语法 | 说明 |
| --- | --- | --- | --- |
| 输入 | `prompt` | `prompt(Text:string[, MoreText:string, ...]) → string` | 弹出对话框，请求用户输入数据，返回输入的字符串 |
| 输入 | `promptList1` | `promptList1(Entry:list[, Text:string, ...]) → integer` | 从单列列表中单选一项，返回所选条目索引（取消返回 `0`） |
| 输入 | `promptListN` | `promptListN(List:list[, Text:string, ...]) → list` | 从列表中多选（Ctrl/Shift+点击），返回所选索引列表（取消返回 `0`） |
| 输出 | `beep` | `beep` | 播放蜂鸣声，用于提醒消息或关键情况 |
| 输出 | `bell` | `bell(Frequency:integer, Duration:integer)` | 在扬声器上输出指定频率与持续时间的声学信号 |
| 输出 | `getUnit` | `getUnit(Value:any) → string` | 返回长度/重量/时间/速度/货币/加速度值的单位 |
| 输出 | `infoBox` | `infoBox(Text:string, Modal:boolean)` | 显示消息框；再次调用并传入 `""` 可关闭 |
| 输出 | `print` | `print ...` | 向控制台（Console）输出任意数量的文本 |

## 输入函数（Input Functions）

- **`prompt`**：请求用户输入数据。最多可显示 4 行、每行最多 45 个字符；在两条竖线 `|...|` 之间的文本会显示在对话框标题栏。返回用户输入的内容（`string`），可配合数据类型转换函数（如 `str_to_num`）使用。
- **`promptList1`**：让用户从单列列表中**单选**一项。返回所选条目的索引（`integer`），点击 Cancel 时返回 `0`。
- **`promptListN`**：让用户从列表中**多选**一项或多项（按住 Ctrl/Shift 点击）。返回所选条目索引组成的列表（`list[integer]`，无序保存），点击 Cancel 时返回 `0`。

## 输出函数（Output Functions）

- **`beep`**：在扬声器上播放蜂鸣声，可用于声音警报。
- **`bell`**：输出声学信号，需指定频率 `Frequency` 与持续时间 `Duration`。
- **`getUnit`**：返回传入值（length、weight、time、speed、money、acceleration 类型）的单位，即 **File > Model Settings > Units** 中所选的单位。面积等无对应设置时返回 SI 单位（如 `m²`）。
- **`infoBox`**：显示消息框；参数 `Modal` 决定是否为模态（`true` 时无法访问其他 Plant Simulation 窗口）。再次调用 `infoBox("", false)` 可关闭。若误开模态消息框未关闭，按住 Shift+Ctrl+Alt 5 秒可强制关闭。
- **`print`**：向控制台输出任意数量的文本；对 length、weight、speed、acceleration 类型的值会在其后显示单位；`print` 无参数时可插入空行。

## 目录结构

- `input-output.md` — 详细的函数参考文档（正式 Markdown 版本）。
- `input-output.txtx` — 原始资料文本（内容与 `input-output.md` 一致）。
