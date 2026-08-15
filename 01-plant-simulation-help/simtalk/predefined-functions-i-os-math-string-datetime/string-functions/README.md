# String Functions

SimTalk 字符串函数概览。本目录汇总了用于字符串处理、正则表达式匹配/替换以及字符编码转换的内置函数。

> 注意：SimTalk 解析器将反斜杠（`\`）作为转义字符。若要搜索字面反斜杠并替换为其他字符，需输入四个反斜杠 `\\\\`。

详细内容见 [string-functions.md](string-functions.md)。

---

## 函数一览

| 函数 | 用途 | 签名 | 返回类型 |
|---|---|---|---|
| `regex_replace` | 按正则表达式搜索并替换所有匹配文本 | `regex_replace(Text, RegularExpression, ReplacingText)` | `string` |
| `regex_search` | 搜索正则表达式并返回第一个匹配子串 | `regex_search(Text, RegularExpression)` | `string` |
| `regex_search2` | 类似 `regex_search`，返回所有匹配分组及前后文本的数组 | `regex_search2(Text, RegularExpression)` | `string[]` |
| `splitString` | 按分隔符拆分字符串 | `splitString(Text, Delimiter[, KeepEmptyItems:=false])` | `string[]` |
| `splitStringToNum` | 将字符串拆分为 `real` 数值数组 | `splitStringToNum(Text, Delimiter)` | `real[]` |
| `strAscii` | 返回指定字符的 Unicode 字符码 | `strAscii(String[, PositionOfCharacter])` | `integer` |
| `strChr` | 返回给定 Unicode 字符码对应的单字符字符串 | `strChr(UnicodeNumber)` | `string` |
| `strCopy` | 复制字符串中的指定片段 | `strCopy(String, Position, NumberOfCharacters)` | `string` |
| `strIncl` | 在指定位置前插入文本 | `strIncl(TextToBeInserted, Text, Position)` | `string` |
| `strLen` | 返回字符串长度（字符数） | `strLen(Text)` | `integer` |
| `strLPos` | 返回文本首次出现的位置 | `strLPos(StrToSearchFor, StrToSearchIn)` | `integer` |
| `strOmit` | 复制字符串并删除一段连续字符 | `strOmit(SourceText, Position, NumberOfCharacters)` | `string` |
| `strRcopy` | 从右侧开始复制指定数量字符 | `strRcopy(SourceText, NumberOfCharacters)` | `string` |
| `strReplace` | 查找并替换所有出现的文本 | `strReplace(SourceText, TextToFind, ReplaceBy)` | `string` |
| `strRpos` | 返回文本最后一次出现的位置 | `strRpos(TextToBeFound, SourceText)` | `integer` |
| `strToHtml` | 将 HTML 语法字符替换为 HTML 实体 | `strToHtml(Text)` | `string` |
| `strToLower` | 将大写字母转为小写 | `strToLower(UpperCaseLetter)` | `string` |
| `strToUpper` | 将小写字母转为大写 | `strToUpper(LowerCaseLetters)` | `string` |

---

## 分类说明

### 正则表达式

- **`regex_replace`** — 将匹配正则表达式的所有子串替换为指定文本。
- **`regex_search`** — 返回第一个匹配的子串；无匹配时返回空字符串 `""`。
- **`regex_search2`** — 与 `regex_search` 对应，但返回 `string[]`，依次包含：所有匹配的完整子串、各分组捕获、匹配前的文本、匹配后的文本。

`regex_search` 一节还列出了正则表达式元字符（`. ? * + {m,n} [ ] [^ ] ^ $ ( ) | \b \w \W \s \S \d \D (?=) (?!) (?:) $1 $2 …`）及其说明。

### 拆分

- **`splitString`** — 按分隔符拆分；分隔符为空时按单个字符拆分；可选参数 `KeepEmptyItems` 控制是否保留空字符串（默认 `false`）。
- **`splitStringToNum`** — 将字符串拆分为 `real` 类型数值数组。

### 字符码转换

- **`strAscii`** — 返回字符的 Unicode 码（1–65535）；负数位置表示从末尾倒数。
- **`strChr`** — 将 Unicode 码转换为单字符字符串（可生成键盘无法输入的特殊字符）。

### 子串操作

- **`strCopy`** — 复制从指定位置开始的指定数量字符（越界不报错，自动截断）。
- **`strIncl`** — 在指定位置前插入文本（位置越界时插入到开头或末尾）。
- **`strLen`** — 字符串长度。
- **`strOmit`** — 删除从指定位置开始的指定数量字符。
- **`strRcopy`** — 从字符串右侧复制指定数量字符。

### 查找

- **`strLPos`** — 首次出现的位置（未找到返回 `0`）。
- **`strRpos`** — 最后一次出现的位置（未找到返回 `0`）。

### 替换与转换

- **`strReplace`** — 替换所有出现的目标文本（源文本不被修改）。
- **`strToHtml`** — 将 `>`、`"` 等 HTML 语法字符转换为对应的 HTML 实体。
- **`strToLower`** / **`strToUpper`** — 大小写转换。
