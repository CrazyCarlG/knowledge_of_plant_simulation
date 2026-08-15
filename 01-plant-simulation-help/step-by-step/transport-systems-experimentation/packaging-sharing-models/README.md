# Packaging and Sharing Models（模型的打包与共享）

本目录内容来源于 Plant Simulation Help（10-886 / 10-887），介绍如何打包并共享 Plant Simulation 模型，以及如何避免运行时弹出消息对话框。

## 内容概述

### 1. 防止弹出消息对话框（Preventing Message Dialogs）

可通过以下用户自定义布尔属性，阻止 Plant Simulation 在运行时弹出消息对话框：

- `ShowRuntimeAtEnd`
- `AskForSaveModel`
- `ShowHTMLatEnd`（用于分布式仿真）

其中，将 `ShowHTMLatEnd` 设为 `false` 时，优化结束后 Plant Simulation 不会自动打开报告（Report）。

**修改属性值的方法：**

1. 在 Frame 中单击插入的 GAWizard。
2. 按 F8 键。
3. 双击属性名称，将值改为 `false`。

### 2. 打包模型并发送给其他用户（Pack a Model and Send It to Another User）

本节演示如何使用 **Pack & Go** 将 Plant Simulation 模型打包并发送给未安装 Plant Simulation 的接收者。

**许可证（License）相关说明：**

- 创建 Pack and Go 模型时，可选择是否将权限限制为 Plant Simulation Viewer License。
- 若未勾选限制，可通过启动参数 `/L` 将许可证传递给 Pack&Go 应用程序，从而在许可证可用时使用更高级许可证的功能。
- 若未指定启动参数，则使用免费提供的 Viewer 许可证。

**Pack and Go 的工作原理：**

- 收集启动所选仿真模型所需的全部文件，将其打包并保存为自解压可执行文件。
- 接收者（如客户）双击该文件即可打开模型。

> **注意：** 即使不限制许可证，Pack and Go 可执行文件也不包含全部 Plant Simulation 功能。为使可执行文件尽可能小，不会包含完整的 Plant Simulation 安装，因此无法使用 OPCUA 接口或 Teamcenter 接口等。

**打包并发送模型的步骤：**

1. 在 Plant Simulation 窗口中选择 **File > Share > Pack and Go**，启动 Pack and Go。
2. 在弹出的对话框中单击 **Yes**，在发送前保存模型。
3. 选择要保存模型文件的文件夹，输入名称并单击 **Save**。
4. Pack-and-Go 成功创建软件包后，单击 **OK**。随后分发该文件，例如通过电子邮件发送或上传至内部网（Intranet）等。

## 目录文件说明

- `packaging-sharing-models.md`：本主题的 Markdown 文档。
- `packaging-sharing-models.txtx`：原始文本来源（Plant Simulation Help 10-886 / 10-887）。

*来源：Plant Simulation Help 10-886 / 10-887。Unpublished work. © 2026 Siemens.*
