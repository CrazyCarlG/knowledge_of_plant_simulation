# README — Primitive & Structured Data Types

本目录对应 SimTalk 参考文档的 **Primitive & Structured Data Types** 章节，源文件为 `primitive-structured.md`。

## 概述

该章节介绍 SimTalk 中的原始（primitive）与结构化（structured）数据类型，涵盖其取值范围、单位，以及可用的方法与属性。每个局部变量都有一个数据类型，用于定义其取值范围和允许的操作。

## 支持的 SimTalk 数据类型

SimTalk 提供以下数据类型，且这些类型名都是关键字，不能用于命名对象、局部变量或函数：

`Acceleration`、`Any`、`Array`、`Boolean`、`Date`、`DateTime`、`Integer`、`JSON`、`Length`、`List`、`Method`、`Object`、`Queue`、`Real`、`Speed`、`Stack`、`String`、`Table`、`Time`、`Weight`

> 说明：`Money`、`RandTime`、`Path` 不是 SimTalk 数据类型（`money` 仅用于全局变量/用户定义属性，用 `real` 代替；`randtime` 返回 `time` 值；`path` 是签名而非可赋值类型，可赋 `object` 或 `string`）。

## 各数据类型要点

| 数据类型 | 说明 | 关键点 |
| --- | --- | --- |
| **Acceleration** | 加速度，范围 `-8.9e307 … 8.9e307` | 单位 m/s²；SimTalk 2.0 支持 `mps²`、`cm²`、`fps²`、`LU/s²` 字面量 |
| **Any** | 可容纳任意值 | 类型随首次赋值确定；用 `forget` 重置；可用 `getSimTalkTypename`、`isLength` 等查询 |
| **Array** | 一维/二维数组 | 索引从 1 开始；支持 `integer[n]`、`boolean[n,m]`、`string[]` 等声明；支持加减乘除与矩阵运算 |
| **Boolean** | 布尔值 | `true` / `false` |
| **Date** | 日期 `01.01.1900 … 31.12.9999` | 用 `str_to_date` 转换 |
| **DateTime** | 日期时间 `01.01.1900 00:00:00 … 31.12.9999 23:59:59` | 用 `str_to_dateTime` 转换 |
| **Integer** | 整数 | 范围 `-9.223.372.036.854.775.808 … 9.223.372.036.854.775.807` |
| **JSON** | JSON 数据（名称-值对，可嵌套） | 支持字面量、`object` 类型元素扩展；提供 `parse`/`asString`/`readFile`/`writeFile` 等 |
| **Length** | 长度，范围 `-8.9e307 … 8.9e307` | 单位 m；SimTalk 2.0 支持 `m`、`mm`、`km`、`cm`、`yd`、`ft`、`in` |
| **List** | 列表，与 `DataList` 共享属性 | 首次访问前需 `create` 或赋值 |
| **Method** | 属性方法（用户定义属性） | 拥有独立随机数流；用 `&` 引用执行方法本身 |
| **Object** | 指向模型对象，或为 `void` | 可赋对象或字符串（路径）；对象引用赋给字符串时带 `*` 前缀 |
| **Queue** | 队列，与 `DataQueue` 共享属性 | 首次访问前需 `create` 或赋值 |
| **Real** | 浮点数，范围约 `±1.7976931348623158e+308` | 精度约 16 位；比较浮点用 `~=` 而非 `=` |
| **Speed** | 速度，范围 `-8.9e307 … 8.9e307` | 单位 m/s；SimTalk 2.0 支持 `mps`、`fps`、`kmh`、`mph` |
| **Stack** | 栈，与 `DataStack` 共享属性 | 首次访问前需 `create` 或赋值 |
| **String** | 字符串 | 用引号 `""` 括起 |
| **Table** | 表格，与 `DataTable` 共享属性 | 首次访问前需 `create` 或赋值 |
| **Time** | 时间，范围 `-8.9e307 … 8.9e307` | 单位为秒；输出为 `hh:mm:ss.ss` 格式 |

## 重点说明

### Array（最详细的部分）
- **索引一基**：数组索引从 1 开始（不是 0）。
- **声明形式**：固定大小 `integer[10]`、二维 `boolean[10,20]`、可变大小 `string[]`。
- **运算**：数值型数组支持加、减；浮点型数组支持乘/除与矩阵乘法。
- **比较**：`real`/`length`/`time`/`speed`/`weight` 与 `any` 数组按内容比较；`integer` 数组不能与其他数值类型数组比较。
- **方法与属性**（共 40 个）：
  `append`、`appendArray`、`appendValueOfType`、`asAny`、`contains`、`copyFromList`、`copyFromTable`、`copyFromTableColumn`、`copyToList`、`copyToTable`、`copyToTableColumn`、`delete`、`deleteValue`、`Dim`、`Empty`、`find`、`getValueOfType`、`insert`、`join`、`Magnitude`、`makeRGBValue`、`max`、`min`、`normalize`、`pop`、`sort`、`sum`、`X`、`xDim`、`Y`、`yDim`（另含 `Y`/`Z` 等索引便捷访问）。
  - 二进制读写：`appendValueOfType` / `getValueOfType` 支持 `int8…uint64`、`real32/real64`，大小写控制端序（小写 = little-endian，大写 = big-endian）。

### JSON
- **结构**：可嵌套的名称-值对，名称区分大小写，值可为 `Integer`/`Real`/`Boolean`/`String`/`Array`/`JSON`/`null`。
- **字面量**：用 `{ "name": value, ... }` 形式。
- **扩展**：可存放 `object` 类型元素（Plant Simulation 特有扩展）。
- **方法与属性**：`asString`、`contains`、`copy`、`copyToTableColumn`、`copyToTableRow`、`delete`、`Dim`、`getOrCreateJSON`、`parse`、`readFile`、`unshareAndDelete`、`writeFile`。

### 单位兼容性
`time`、`length`、`weight`、`speed`、`acceleration` 之间互不兼容。例如，只能向 `length` 类型变量赋 `length`、`real` 或 `integer` 值。

## 文档结构索引

源文件 `primitive-structured.md` 的章节顺序：
1. Overview
2. Data Types [SimTalk]
3. Money / RandTime / Path
4. Acceleration
5. Any
6. Array（含全部方法）
7. Boolean / Date / DateTime / Integer
8. JSON（含全部方法）
9. Length
10. List / Method / Object / Queue / Real / Speed / Stack / String / Table / Time
