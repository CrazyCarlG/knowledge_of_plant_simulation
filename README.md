# knowledge_of_plant_simulation

Plant Simulation（Siemens Tecnomatix）帮助文档的**中文知识库**，以及把官方 PDF 帮助文档转换成结构化 Markdown 的**自动化工具链**。

**English:** A **Chinese knowledge base** for the Siemens Tecnomatix Plant Simulation help documentation, plus an **automated toolchain** that converts the official PDF help into structured Markdown.

> 帮助文档内容来源于 Siemens《Plant Simulation Help》（Unpublished work，© 2026 Siemens）。本项目仅做学习与知识管理用途，版权归 Siemens 所有。
>
> **English:** The help content originates from Siemens *Plant Simulation Help* (Unpublished work, © 2026 Siemens). This project is for learning and knowledge management only; all rights belong to Siemens.

## 项目内容 / What's Inside

仓库包含两部分。**English:** The repository contains two parts.

1. **`01-plant-simulation-help/`** —— 转换后的知识库成品（Markdown），按主题分目录组织。
   **English:** The converted knowledge base (Markdown), organized by topic.
2. **`scripts/`** —— PDF → 知识库的转换与处理脚本（Python）。
   **English:** Python scripts for the PDF → knowledge-base conversion pipeline.

## 目录结构 / Directory Structure

```
knowledge_of_plant_simulation/
├── 01-plant-simulation-help/          # 知识库成品（Markdown + 提取文本）/ Knowledge base (Markdown + extracted text)
│   ├── getting-to-know-plant-simulation/   # 认识 Plant Simulation / Getting to know Plant Simulation
│   ├── objects/                            # 对象参考 / Object reference
│   │   ├── fluid-objects/                  #   流体对象 / Fluid objects
│   │   ├── information-flow-objects/       #   信息流对象 / Information flow objects
│   │   ├── material-flow-objects/          #   物流对象 / Material flow objects
│   │   ├── resource-objects/               #   资源对象 / Resource objects
│   │   └── user-interface-objects/         #   用户界面对象 / User interface objects
│   ├── simtalk/                            # SimTalk 编程语言 / SimTalk programming language
│   │   ├── language-fundamentals/          #   语言基础 / Language fundamentals
│   │   ├── data-types-expressions/         #   数据类型与表达式 / Data types & expressions
│   │   ├── control-flow-error-handling/    #   控制流与错误处理 / Control flow & error handling
│   │   ├── predefined-functions-i/ii/iii/  #   预定义函数（三部分）/ Predefined functions (three parts)
│   │   ├── 3d-*/                           #   3D 相关 API / 3D-related APIs
│   │   ├── overview-migration/             #   概述与迁移 / Overview & migration
│   │   └── deprecated-unsupported-names/   #   已弃用/不支持名称 / Deprecated & unsupported names
│   └── step-by-step/                       # 分步指南 / Step-by-step guides
├── scripts/                          # 转换与处理脚本 / Conversion & processing scripts
│   ├── pdf-to-knowledge/
│   │   ├── batch_split_pdf_pages.py        # 按 Excel 配置批量切分 PDF / Batch split PDF by Excel config
│   │   ├── batch_txt_to_md.py              # 批量 txtx → md / Batch txtx → md
│   │   ├── objects-pdf/                    # 对象章节的 Excel 配置 / Excel configs for object sections
│   │   └── process/
│   │       ├── split_pdf_pages.py          # 按页码范围切分单个 PDF / Split a single PDF by page range
│   │       ├── extract_pdf_bookmarks.py    # 提取 PDF 书签 → CSV/Excel / Extract PDF bookmarks → CSV/Excel
│   │       ├── extract_unique_pdf_text.py  # 提取目录内唯一 PDF 全文 → txtx / Extract text of the only PDF → txtx
│   │       ├── openclaude_unique_txt_session.py  # 调 openclaude 把 txtx 总结成 md / Invoke openclaude to summarize txtx → md
│   │       └── openclaude_readme_session.py      # 调 openclaude 生成目录级 README / Invoke openclaude to generate README
│   ├── bookmarks.csv                  # 提取出的书签（CSV）/ Extracted bookmarks (CSV)
│   ├── bookmarks_usercomfirmed.xlsx   # 人工确认后的书签（Excel）/ Manually confirmed bookmarks (Excel)
│   ├── step_by_step_restructured_chapters.csv   # 分步指南章节重构配置 / Step-by-step chapter restructure config
│   └── simtalk_restructured_chapters.csv        # SimTalk 章节重构配置 / SimTalk chapter restructure config
├── LICENSE                            # GPL-3.0
└── README.md
```

## 知识库内容板块 / Knowledge Base Sections

| 板块 Section | 目录 Directory | 说明 Description |
|---|---|---|
| 认识 Plant Simulation | `getting-to-know-plant-simulation/` | 入门与概念介绍 / Introduction & concepts |
| 对象参考 | `objects/` | 物流 / 资源 / 信息流 / 用户界面 / 流体对象 / Material flow, resource, information flow, UI, fluid objects |
| SimTalk 语言 | `simtalk/` | 语法、数据类型、控制流、预定义函数、3D API 等 / Syntax, data types, control flow, predefined functions, 3D APIs, etc. |
| 分步指南 | `step-by-step/` | 从建模入门到传输系统、机器人、动画等的实操指南 / Hands-on guides from modeling basics to transport systems, robots, animation, etc. |

每个主题子目录内通常包含 `.md` 源文件、`README.md` 目录总结，以及部分 `.txtx`（从 PDF 提取的原文文本）。

**English:** Each topic subdirectory typically contains `.md` source files, a `README.md` summary, and some `.txtx` files (raw text extracted from the PDF).

## PDF → 知识库 转换流程 / Conversion Pipeline

整体流水线（`scripts/pdf-to-knowledge/`）。**English:** Overall pipeline (in `scripts/pdf-to-knowledge/`):

```
官方 PDF 帮助文档 / Official PDF help
      │  (1) extract_pdf_bookmarks.py
      ▼
书签/大纲 (CSV / Excel) / Bookmarks/outline (CSV / Excel)
      │  (2) 人工整理章节切分配置 / Manually organize chapter split configs
      ▼
按主题切分 PDF / Split PDF by topic
      │  (batch_split_pdf_pages.py + split_pdf_pages.py)
      ▼
提取全文 .txtx / Extract full text → .txtx
      │  (3) extract_unique_pdf_text.py
      ▼
总结成 Markdown (.md) / Summarize into Markdown (.md)
      │  (4) openclaude_unique_txt_session.py
      ▼
目录级 README 总结 / Directory-level README summary
      │  (5) openclaude_readme_session.py
      ▼
知识库 / Knowledge base
```

### 依赖 / Dependencies

脚本基于 Python。**English:** The scripts are Python-based.

```bash
pip install pypdf openpyxl
```

`openclaude_*` 脚本还会调用本机已安装的 `openclaude` CLI。
**English:** The `openclaude_*` scripts also invoke the locally installed `openclaude` CLI.

### 常用命令示例 / Common Usage

```bash
# 提取书签 / Extract bookmarks
python scripts/pdf-to-knowledge/process/extract_pdf_bookmarks.py \
  "manual.pdf" --csv bookmarks.csv --excel bookmarks.xlsx

# 按页码切分单个 PDF / Split a single PDF by page range
python scripts/pdf-to-knowledge/process/split_pdf_pages.py \
  "manual.pdf" 10 25 "output/" "objects/material-flow"

# 按 Excel 配置批量切分 / Batch split by Excel config
python scripts/pdf-to-knowledge/batch_split_pdf_pages.py \
  "sections.xlsx" "manual.pdf" "/abs/output"

# 提取目录内唯一 PDF 全文 → txtx / Extract the only PDF's text → txtx
python scripts/pdf-to-knowledge/process/extract_unique_pdf_text.py "某目录"

# 调 openclaude 把 txtx 总结成 md（--dry-run 可先预览命令）
# Invoke openclaude to summarize txtx → md (--dry-run previews the command)
python scripts/pdf-to-knowledge/process/openclaude_unique_txt_session.py "某目录" --dry-run
```

## 许可证与版权 / License & Copyright

- 代码与脚本：**GPL-3.0**，见 [LICENSE](LICENSE)。**English:** Code & scripts: **GPL-3.0**, see [LICENSE](LICENSE).
- 知识库文档内容：来源于 Siemens《Plant Simulation Help》（© 2026 Siemens，Unpublished work），仅用于学习与知识管理，版权归 Siemens 所有。
  **English:** Documentation content: sourced from Siemens *Plant Simulation Help* (© 2026 Siemens, Unpublished work), for learning and knowledge management only; all rights belong to Siemens.
