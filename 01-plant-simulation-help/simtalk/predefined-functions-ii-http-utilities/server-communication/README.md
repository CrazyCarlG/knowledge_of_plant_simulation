# HTTP 服务器通信函数（Server Communication）

本目录汇总 Plant Simulation SimTalk 中用于与 HTTP 服务器通信的预定义函数，内容来源于 `server-communication.md`。这些函数用于发送 HTTP 请求、发送/接收数据，以及在 HTTP 服务器上创建和删除资源。

## 目录结构

- `server-communication.md` — 各 HTTP 通信函数的完整说明文档（本 README 为其摘要）。
- `server-communication.txtx` — 原始帮助文本源文件。

> 说明：本目录下没有子文件夹，因此无子文件夹 README.md 需要汇总。

## 函数总览

### HTTP 请求函数

| 函数 | 作用 |
|---|---|
| `httpGetRequest` | 发送 GET 请求，请求某资源的数据 |
| `httpPutRequest` / `httpPutFileRequest` | 发送 PUT 请求（携带数据 / 文件内容作为请求体） |
| `httpPostRequest` / `httpPostFileRequest` | 发送 POST 请求（携带数据 / 文件内容作为请求体） |
| `httpDeleteRequest` | 发送 DELETE 请求，删除资源 |
| `httpHeadRequest` | 发送 HEAD 请求（类似 GET，但不返回响应体数据） |
| `httpOptionsRequest` | 发送 OPTIONS 请求（查询资源支持的访问方式等选项） |

### URL 处理函数

| 函数 | 作用 |
|---|---|
| `httpCreateURL` | 从 URL 各组成元素的 JSON 结构构建正确的 URL |
| `httpSplitURL` | 将 URL 拆分为各组成元素的 JSON 结构，并将查询/表单数据拆分为扁平的 JSON 子结构 |
| `httpCreateFormURLEncodedString` | 从扁平 JSON 名称-值对创建 URL 的 "extra"（路径后）部分，可用于载荷或请求体 |
| `httpSplitFormUrlEncodedString` | 从 URL extra 部分的查询/表单字符串创建扁平 JSON 结构 |

### 编码 / 载荷 / 请求体函数

| 函数 | 作用 |
|---|---|
| `encodeStringQuotedPrintable` | 以 Quoted-Printable 编码字符串（掩码 URL 中不允许的字符） |
| `decodeQuotedPrintableString` | 还原 Quoted-Printable 编码的字符 |
| `encodeDataBase64` / `encodeBase64FromFile` | 对文本或文件内容进行 Base64 编码（使二进制数据可经 HTTP/MQTT 传输） |
| `decodeBase64Data` / `decodeBase64DataToFile` | 将 Base64 数据解码回原始状态（返回变量或保存到文件） |
| `readBytesFromFile` | 读取文件并以整数字节值数组返回内容 |
| `writeBytesToFile` | 将整数字节值数组写入文件 |

### 超时设置函数

| 函数 | 作用 |
|---|---|
| `httpGetTimeouts` | 获取 Windows HTTP 接口（WinHTTP）中定义的超时值 |
| `httpSetTimeouts` | 设置 Windows HTTP 接口（WinHTTP）的超时值 |

## 通用要点

### HTTP 请求体（RequestBody）类型约定

`httpPostRequest`、`httpPutRequest`、`httpDeleteRequest` 等函数的请求体支持多种数据类型：

- `string` — 按原样发送（文本，不转换）。
- `json` — 转换为字符串后发送。
- `integer[]` — 每个数字视为一个字节的二进制数据，按字节序列发送。
- `any` 数组 — 值转换为文本，与 JSON 数组兼容，自动以 `application/json` 内容类型传输。

### Content-Type 默认规则

- 若请求头未指定内容类型，`string`/`json` 请求体自动附加 `text/plain`/`application/json`。
- `integer[]` 作为字节发送且未指定内容类型时，设为 `application/octet-stream`。
- 若请求头包含 `application/x-www-form-urlencoded` 且请求体为 `json`，则自动转换为表单文本（见 `httpCreateFormURLEncodedString`）后作为载荷发送。

### 物理量（physical value）与字节的说明

- 物理量（长度、重量等）在转为文本时转换为基本单位并丢失单位（类似 `print`）。例如 `3.3km` 会发送为 `3300`。
- `integer[]` 数组映射为字节序列（二进制数据），不做文本转换。
- `any` 类型数据：若为第一列为 `integer` 的列表对象，则数字按整数数组作为二进制字节发送；若为整数、浮点数、物理量等，则转为文本后发送（物理量带单位）。

### 请求头（RequestHeader）格式

请求头支持两种形式：

- JSON 对象（或 JSON 对象的文本表示）—— 名称值对描述 HTTP 头。
- RFC 7230 合规的字符串（如 `"Accept: application/json; charset=utf-8"`）。

命名规则：名称仅允许 US-ASCII（7 位 ASCII）字母；值仅允许 ISO 8859-1（Latin1）字母。违规会抛出错误，不自动掩码（需要时可用 `encodeStringQuotedPrintable`）。

### 响应头（ResponseHeader）

响应头写入一个 `json` 变量，包含 `Status-Line`（HTTP 版本、状态码、状态短语）和 `Headers`（各头部，多个值以分号分隔时返回 JSON 数组）。

### 响应体（ResponseBody）类型约定

- `json` — 尝试将文本数据用作 JSON；若非有效 JSON 则报错。对 `application/json`、`*/*+json` 尽量返回 JSON。
- `string` — 按内容类型返回文本（`text/*`、`application/json`、`*/*+json`、`*/*+html`、`*/*+txt`、`*/*+xml`）。
- `integer[]` — 逐字节传入数组（与内容类型无关）。
- `any` — 按内容类型保存：JSON 类型返回 JSON 结构（若为 JSON 数组则返回相应类型数组），文本类型返回文本，其他类型逐字节存入 `integer[]`。

### URL 结构

标准 URL 格式：

```
http[s]://[<username>:<password>@]<hostname>[:<port>][/<path>][<extra>]
```

- `http[s]://` — 协议，仅支持 `http://` 和 `https://`（加密）。
- `hostname` — 服务器名，如 `www.siemens.com`。
- `port` — 端口号（默认标准端口如 80）。
- `path` — 资源路径，以 `/` 分隔。
- `extra` — 可引用分段（`<host>/<path>#section`）或命名参数（`<host>/<path>?name1=value1&name2=value2&…`）。

### URL 字符掩码

参数值中不允许出现用于 HTTP 协议或 URL 的字符，需以 `%` + 十六进制 Unicode 码点转义：

| 字符 | URL 合规形式 | 含义 |
|---|---|---|
| 空格 | `%20` | 禁止 |
| 斜杠 (/) | `%2F` | 仅用于路径 |
| & | `%26` | URL 参数分隔符 |
| ? | `%3F` | 路径与参数分隔符 |
| = | `%3D` | 参数与值分隔符 |
| # | `%23` | 仅用于引用分段 |
| : | `%3A` | 仅用于用户名与密码之间 |
| @ | `%40` | 认证数据与服务器名分隔符 |

非 7 位 ASCII 字符（如 `ö`→`%C3%B6`、`€`→`%E2%82%AC`）同样方式掩码。

### 默认超时时间

HTTP 请求函数的默认超时：

- 连接已解析主机：10 秒
- 发送请求：5 秒
- 接收请求响应：5 秒

### WinHTTP 超时设置（`httpSetTimeouts` / `httpGetTimeouts`）

- 所有超时值单位为毫秒。
- 值 `0` 或 `-1` 表示无限等待（不超时）。
- 非 `0`、`-1` 的负值会触发无效参数错误。
- 四个超时参数：`ResolveTimeout`（解析主机名）、`ConnectTimeout`（连接）、`SendTimeout`（发送）、`ReceiveTimeout`（接收）。

### 各请求函数典型返回

所有 HTTP 请求函数返回 `integer` 类型的 HTTP 状态码（如 `200` OK、`401` Unauthorized、`404` Not found、`501` Not implemented）。

## 函数语义要点（按函数）

- **httpGetRequest** — 请求资源数据；URL 可包含认证信息。
- **httpHeadRequest** — 类似 GET 但不返回响应体，可用于探测某 GET 请求会返回的数据类型和数据量。
- **httpOptionsRequest** — 查询资源支持的访问方法（HTTP 动词）及其他选项。
- **httpPostRequest** — 创建或修改资源；同一数据重复 POST 通常结果不同；出错时响应体会返回错误信息。
- **httpPutRequest** — 创建资源；同一数据重复 PUT 应始终返回相同结果。
- **httpDeleteRequest** — 删除 URL 指定的资源；可携带请求体并接收响应体。
- **httpPostFileRequest / httpPutFileRequest** — 以指定文件内容作为请求体发送。
- **httpCreateURL / httpSplitURL** — 相互配合：拆分 URL 修改后可用 `httpCreateURL` 重组。
- **httpCreateFormURLEncodedString / httpSplitFormUrlEncodedString** — 相互配合：在扁平 JSON 与表单编码字符串之间转换。
- **encodeStringQuotedPrintable / decodeQuotedPrintableString** — 相互配合：URL 字符掩码与还原。
- **encodeDataBase64 / decodeBase64Data**、**encodeBase64FromFile / decodeBase64DataToFile** — 相互配合：二进制数据的 Base64 编解码。
- **readBytesFromFile / writeBytesToFile** — 相互配合：文件与字节数组之间的转换。
