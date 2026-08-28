# knowledge_of_plant_simulation

An **English knowledge base** for the Siemens Tecnomatix Plant Simulation help
documentation, plus an **automated toolchain** that converts the official PDF
help into structured Markdown.

> The help content originates from Siemens *Plant Simulation Help* (Unpublished
> work, © 2026 Siemens). This project is for learning and knowledge management
> only; all rights belong to Siemens.

## What's Inside

The repository contains two parts:

1. **`01-plant-simulation-help/`** — The converted knowledge base (Markdown),
   organized by topic.
2. **`scripts/`** — Python scripts for the PDF → knowledge-base conversion
   pipeline.

## Directory Structure

```
knowledge_of_plant_simulation/
├── 01-plant-simulation-help/          # Knowledge base (Markdown + extracted text)
│   ├── getting-to-know-plant-simulation/   # Getting to know Plant Simulation
│   ├── objects/                            # Object reference
│   │   ├── fluid-objects/                  #   Fluid objects
│   │   ├── information-flow-objects/       #   Information flow objects
│   │   ├── material-flow-objects/          #   Material flow objects
│   │   ├── resource-objects/               #   Resource objects
│   │   └── user-interface-objects/         #   User interface objects
│   ├── simtalk/                            # SimTalk programming language
│   │   ├── language-fundamentals/          #   Language fundamentals
│   │   ├── data-types-expressions/         #   Data types & expressions
│   │   ├── control-flow-error-handling/    #   Control flow & error handling
│   │   ├── predefined-functions-i/ii/iii/  #   Predefined functions (three parts)
│   │   ├── 3d-*/                           #   3D-related APIs
│   │   ├── overview-migration/             #   Overview & migration
│   │   ├── deprecated-unsupported-names/   #   Deprecated & unsupported names
│   │   └── access-to-toolbox-and-folder-library/  # Toolbox & Class Library folder access
│   └── step-by-step/                       # Step-by-step guides
├── scripts/                          # Conversion & processing scripts
│   ├── pdf-to-knowledge/
│   │   ├── batch_split_pdf_pages.py        # Batch split PDF by Excel config
│   │   ├── batch_txt_to_md.py              # Batch txtx → md
│   │   ├── objects-pdf/                    # Excel configs for object sections
│   │   └── process/
│   │       ├── split_pdf_pages.py          # Split a single PDF by page range
│   │       ├── extract_pdf_bookmarks.py    # Extract PDF bookmarks → CSV/Excel
│   │       ├── extract_unique_pdf_text.py  # Extract text of the only PDF → txtx
│   │       ├── openclaude_unique_txt_session.py  # Invoke openclaude to summarize txtx → md
│   │       └── openclaude_readme_session.py      # Invoke openclaude to generate README
│   ├── bookmarks.csv                  # Extracted bookmarks (CSV)
│   ├── bookmarks_usercomfirmed.xlsx   # Manually confirmed bookmarks (Excel)
│   ├── step_by_step_restructured_chapters.csv   # Step-by-step chapter restructure config
│   └── simtalk_restructured_chapters.csv        # SimTalk chapter restructure config
├── LICENSE                            # GPL-3.0
└── README.md
```

## Knowledge Base Sections

| Section | Directory | Description |
|---|---|---|
| Getting to know Plant Simulation | `getting-to-know-plant-simulation/` | Introduction & concepts |
| Object reference | `objects/` | Material flow, resource, information flow, UI, fluid objects |
| SimTalk language | `simtalk/` | Syntax, data types, control flow, predefined functions, 3D APIs, etc. |
| Step-by-step guides | `step-by-step/` | Hands-on guides from modeling basics to transport systems, robots, animation, etc. |

Each topic subdirectory typically contains `.md` source files, a `README.md`
summary, and some `.txtx` files (raw text extracted from the PDF).

## PDF → Knowledge Base Conversion Pipeline

Overall pipeline (in `scripts/pdf-to-knowledge/`):

```
Official PDF help
      │  (1) extract_pdf_bookmarks.py
      ▼
Bookmarks/outline (CSV / Excel)
      │  (2) Manually organize chapter split configs
      ▼
Split PDF by topic
      │  (batch_split_pdf_pages.py + split_pdf_pages.py)
      ▼
Extract full text → .txtx
      │  (3) extract_unique_pdf_text.py
      ▼
Summarize into Markdown (.md)
      │  (4) openclaude_unique_txt_session.py
      ▼
Directory-level README summary
      │  (5) openclaude_readme_session.py
      ▼
Knowledge base
```

### Dependencies

The scripts are Python-based.

```bash
pip install pypdf openpyxl
```

The `openclaude_*` scripts also invoke the locally installed `openclaude` CLI.

### Common Usage

```bash
# Extract bookmarks
python scripts/pdf-to-knowledge/process/extract_pdf_bookmarks.py \
  "manual.pdf" --csv bookmarks.csv --excel bookmarks.xlsx

# Split a single PDF by page range
python scripts/pdf-to-knowledge/process/split_pdf_pages.py \
  "manual.pdf" 10 25 "output/" "objects/material-flow"

# Batch split by Excel config
python scripts/pdf-to-knowledge/batch_split_pdf_pages.py \
  "sections.xlsx" "manual.pdf" "/abs/output"

# Extract the only PDF's text → txtx
python scripts/pdf-to-knowledge/process/extract_unique_pdf_text.py "some-directory"

# Invoke openclaude to summarize txtx → md (--dry-run previews the command)
python scripts/pdf-to-knowledge/process/openclaude_unique_txt_session.py "some-directory" --dry-run
```

## License & Copyright

- Code & scripts: **GPL-3.0**, see [LICENSE](LICENSE).
- Documentation content: sourced from Siemens *Plant Simulation Help* (© 2026
  Siemens, Unpublished work), for learning and knowledge management only; all
  rights belong to Siemens.