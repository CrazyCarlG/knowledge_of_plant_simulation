# Reference 目录说明

本目录包含 SimTalk Reference（SimTalk 参考）主题的文档，目前包含以下文件：

- `reference.md` — SimTalk Reference 的 Markdown 版本
- `reference.txtx` — 同一主题的原始文本版本（内容与 `reference.md` 基本一致）

## 内容总结

本主题介绍 Plant Simulation 内置的编程语言 **SimTalk**，它用于实现内置仿真对象功能无法覆盖的自定义行为与逻辑。

### 核心要点

- **解释器（Interpreter）**：SimTalk 包含一个解释器，在仿真运行时直接执行写在 Method 对象中的指令。
- **与仿真对象的紧密集成**：可通过 SimTalk 访问所有内置对象的属性（attributes）、只读属性（read-only attributes）和方法（methods）。
- **Copilot 辅助编程**：Copilot 可访问 Plant Simulation 帮助，辅助在 Method 中编写源代码；Copilot (local) 提供更好的知识库，并支持接入自己的 LLM。
- **可复用对象**：可在 Dialog 类型对象中用 SimTalk 创建自定义可复用对象，配合集成的 Method Debugger 构成易用的编程环境。
- **Python 替代**：除 SimTalk 外，也可使用 Python 编程。

### Python 与 SimTalk 的关系

- Python 代码**并非用于取代** SimTalk 代码。
- SimTalk 代码访问编译后的内置函数，执行速度通常快于 Python 代码。
- 由于许多大学毕业生熟悉 Python，PythonModule 使 Plant Simulation 编程更加简单快捷。

### SimTalk 2.0

- SimTalk 2.0 在 Plant Simulation 12.1 中引入，简化了语法并新增了功能。
- Plant Simulation 帮助仅描述 SimTalk 2.0；主要差异见主题 "SimTalk 2.0 and SimTalk 1.0 Compared"。
- SimTalk 1.0 在当前及旧版本中仍可使用，新旧模型均可继续使用。
- Debugger 功能区选项卡上的 "Find Outdated Functions" 命令可查找仿真模型中所有 Method 源代码里的过时方法、属性、只读属性和函数。

### 描述结构

SimTalk 的描述分为两部分：

- General Access to SimTalk（SimTalk 的通用访问）
- SimTalk Access to 3D Functions（SimTalk 对 3D 功能的访问）

### 语言支持

- SimTalk 支持使用**英语和德语**编写 Method 源代码。
- 德语帮助会在德语名称旁以正斜杠分隔显示英语名称，例如 `EnergieAktiv [SimTalk] / EnergyActive`。
- 这便于在使用德语版 Plant Simulation 时创建可供其他国家同事使用的英语模型。

### 参见（See Also）

- What's New
- SimTalk Reference
- Introducing Plant Simulation
- Update Arbitrary Old Models
- The User Interface Components
- The Step-by-Step Help
- Outdated SimTalk Names
- The Quick Reference Card
- The Add-Ins Reference Help
- The Libraries Reference
