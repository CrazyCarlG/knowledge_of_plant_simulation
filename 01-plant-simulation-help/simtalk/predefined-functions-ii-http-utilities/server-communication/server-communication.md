# Functions for Communicating with an HTTP Server

These functions let you send HTTP requests, send data, receive data from HTTP responses, and create/delete resources on an HTTP server.

## Overview

### HTTP request functions
- `httpGetRequest` — sends a GET request (requests data of a resource)
- `httpPutRequest` / `httpPutFileRequest` — sends a PUT request with data or file contents
- `httpPostRequest` / `httpPostFileRequest` — sends a POST request
- `httpDeleteRequest` — sends a DELETE request
- `httpHeadRequest` — sends a HEAD request
- `httpOptionsRequest` — sends an OPTIONS request

### URL handling functions
- `httpCreateURL` — builds a correct URL from a JSON structure of URL components
- `httpSplitURL` — splits a URL into components as a JSON structure; also splits query/form data into a flat JSON substructure
- `httpCreateFormURLEncodedString` — creates the URL "extra" component (after the path) from a flat JSON structure of name-value pairs; usable for payload or request body
- `httpSplitFormUrlEncodedString` — creates a flat JSON structure from a query/form string in the extra part of a URL

### Encoding / payload / body functions
- `encodeStringQuotedPrintable` — encodes a string in Quoted-Printable encoding (masks characters not allowed in a URL)
- `decodeQuotedPrintableString` — unmasks Quoted-Printable-encoded characters
- `encodeDataBase64` / `encodeBase64FromFile` — Base64-encodes text or file contents (makes binary data HTTP/MQTT transportable)
- `decodeBase64Data` / `decodeBase64DataToFile` — decodes Base64 data back to the original state (returns to a variable or saves to a file)
- `readBytesFromFile` — reads a file and returns its contents as an array of integer byte values
- `writeBytesToFile` — writes an array of integer byte values to a file

---

## decodeBase64Data / decodeBase64DataToFile

Decodes Base64 data back to the original state, transforming Base64-encoded text into binary data.

**Remarks**
- Decoded data is returned as text or as an array of integers, depending on the type of the passed variable.
- If the data contains several bytes with value 0 and the passed variable is `string`, an error occurs.
- `decodeBase64DataToFile` saves the decoded data to the specified file.

**Syntax**
```
decodeBase64Data(Base64Data:string, byref Data:string/integer[])
decodeBase64DataToFile(Base64Data:string, FileName:string)
```

**Parameters**
- `Base64Data` (string) — the data to be decoded.
- `FileName` (string) — the name of the file to which the decoded data is saved.

**Example**
```simtalk
var base64:string := "SGVsbG8gV29ybGQ="
var data:string
decodeBase64Data(base64, data)
print data
// Hello World
```

---

## decodeQuotedPrintableString

Unmasks all characters masked with Quoted-Printable encoding back to their original form.

**Syntax**
```
decodeQuotedPrintableString(QuotedPrintableText:string) -> string
```

**Parameter**
- `QuotedPrintableText` (string) — the data to be decoded.

**Return value** — `string`.

**Example**
```simtalk
print decodeQuotedPrintableString("Hello%20Word")
// returns Hello World
```

---

## encodeDataBase64 / encodeBase64FromFile

Encodes the entire specified data in Base64 encoding.

**Remarks**
- The resulting text is no longer readable and cannot be compared with the original data. This makes binary data transportable via HTTP or MQTT.
- `encodeBase64FromFile` encodes the contents of the specified file.

**Syntax**
```
encodeDataBase64(Data:string/json/integer[]) -> string
encodeBase64FromFile(FileName:string) -> string
```

**Parameters**
- `Data` (string/json/integer[]/any) — the data to be encoded.
- `FileName` (string) — the name of the file whose contents are to be encoded.

**Return value** — a string of characters within the US-ASCII (7-bit ASCII) character set.

**Example**
```simtalk
var text := "Hello World"
var base64:string := encodeDataBase64(text)
print base64
// returns SGVsbG8gV29ybGQ=
```

---

## encodeStringQuotedPrintable

Encodes the passed string in Quoted-Printable encoding.

**Remarks**
All characters not allowed in a URL without changing its structure are masked. Normally these are characters outside US-ASCII (7-bit ASCII) and characters that have a function within a URL, such as `/`, `:`, `@`, `&`, `=`, spaces, etc.

**Syntax**
```
encodeStringQuotedPrintable(Text:string) -> string
```

**Parameter**
- `Text` (string) — the text to be encoded.

**Return value** — `string`.

**Example**
```simtalk
print encodeStringQuotedPrintable("Hello World")
// returns Hello%20World
```

---

## httpCreateFormURLEncodedString

Combines names and values of an HTTP request into valid text that can be attached as extraInfo after the path.

**Remarks**
If names or values contain characters illegal for a URL, they are masked using Quoted-Printable encoding.

**Syntax**
```
httpCreateFormUrlEncodedString(FormKeyValuePairs:json) -> string
```

**Parameter**
- `FormKeyValuePairs` (json) — JSON elements containing the names and values in a flat JSON structure to be used as URL query parameters.

A JSON structure might look like this:
```json
{
   "name1": "value1",
   "name 2": "value2",
   "name3": "value 3",
   ...
}
```

The result for the JSON structure above is a URL query with this format:
```
name1=value1&name%202=value2&name3=value%203&...
```

**Return value** — `string`.

**Example**
```simtalk
var requestHeaders:json
requestHeaders["Content-Type"] := "application/x-www-form-urlencoded"

var data:json
data["name1"] := "value1"
data["name 2"] := "value2"
data["name3"] := "value 3"

var requestBody:string := httpCreateFormUrlEncodedString(data)
var responseHeaders:json
var responseBody:any
// httpPostRequest(url, requestBody, requestHeaders, responseHeaders, responseBody)
print requestBody
// returns name1=value1&name%202=value2&name3=value%203
```

---

## httpCreateURL

Creates a syntactically correct URL from a JSON structure with URL elements.

**Syntax**
```
httpCreateURL(URLElements:json) -> string
```

**Parameter**
- `URLElements` (json) — the URL elements.

> Note: Elements that you do not specify are empty and thus are not part of the created URL.

Elements:
- `SSL` — `true` if the URL uses transport encryption (`https`), `false` without encryption (`http`).
- `Server` — server name (also called host name).
- `Port` — integer port number on the designated server.
- `Extra` — text to be added after the path, or a flat JSON structure. The text can be a reference to a resource section (starting with `#`) or a URL query text (starting with `?`). The function also accepts a flat JSON structure of URL query parameters which start with `?` in the URL.
- `UserName` — user name used for authentication in the URL.
- `Password` — password for the user name used for authentication.

The result is a URL with this format:
```
http[s]://[<username>:<password>@]<hostname>[:<port>][/<path>][<extra>]
```

**Return value** — `string`.

**Examples**
```simtalk
var urlData:json
urlData["Server"] := "ServerName"
urlData["Port"] := 80 -- default port
urlData["Path"] := "/A/B/C"
urlData["Scheme"] := "http"

var urlData:json
urlData["Server"] := "ServerName"
urlData["Port"] := 8080 -- HTTP port 8080
urlData["Path"] := "/A/B/C"
urlData["Scheme"] := "http"
```

---

## httpDeleteRequest

Sends a DELETE request. It deletes a resource on an HTTP server identified by the specified URL.

**Remarks**
A DELETE request can send data in the `RequestBody` and receive data from the HTTP server in the `ResponseBody`.

**Syntax**
```
httpDeleteRequest(URL:string[, RequestHeader:string/json, RequestBody:string/json/integer[]/any, byref ResponseHeader:json, byref ResponseBody:string/json/integer[]/any]) -> integer
```

**Parameters**
- `URL` (string) — the URL used to address a resource. It can also contain authentication information (see `httpGetRequest`).
- `RequestHeader` (json/string) — a JSON object, a textual representation of a JSON object, or an RFC 7230 compliant header string describing the request headers.
- `RequestBody` (string/json/integer[]/any) — the payload to be sent:
  - `string` — sent as-is (text, no conversion).
  - `json` — converted into a string and sent.
  - `integer[]` — each number is treated as one byte of binary data and sent as a sequence of bytes.
  - array of `any` — values are converted into text; compatible with JSON arrays and automatically transmitted with content type `application/json`.

**Request body examples**
```simtalk
var requestBody1:real[] := [ 1.1, 2.2, 3.3, 4.4, 5.5 ]
var status:integer      := httpPostRequest(url, requestBody1)
// post an array of reals, the Content-Type is application/json

var requestBody2:real[] := [ "A", "B", "C", "D", "E" ]
status                  := httpPostRequest(url, requestBody2)
// post an array of strings, the Content-Type is application/json

var requestBody3:real[] := [ { "A": 1 }, { "B": 2 }, { "C": 3 }, { "D": 4 }, { "E": 5 } ]
status                  := httpPostRequest(url, requestBody3)
// post an array of JSON objects, the Content-Type is application/json

var requestBody4:any[] := [ 1, 2.2, 3.3km, "4th element", { "Name": "5th element" }, false ]
status                 := httpPostRequest(url, requestBody4)
// post the mixed array of the Content-Type application/json:
// [ 1, 2.2, 3300, "4th element", { "Name": "5th element" }, false ]
```

To avoid `application/json` for an array, specify the content type in the request header:
```simtalk
var requestBody:real[]   := [ 1.1, 2.2, 3.3, 4.4, 5.5 ]
var requestHeader:string := "Content-Type: text/plain"
var status:integer        := httpPostRequest(url, requestBody, requestHeader)
// post an array of reals, the Content-Type is text/plain

var jsRequestHeader:json := { "Content-Type": "text/plain" }
status                  := httpPostRequest(url, requestBody, jsRequestHeader)
// post an array of reals, the Content-Type is text/plain
```

**Notes on physical values and bytes**
- Physical values (length, weight, etc.) are converted to their base unit during conversion to text and lose their unit, similar to `print`.
```simtalk
var len:length := 3.3km
print len // -> 3300

var status:integer := httpPostRequest(url, len)
// posts the length given in km as m: 3.3km -> 3300
```
- `integer[]` arrays map a sequence of bytes (binary data) and are not converted to text.
```simtalk
var bytes:integer[] := [ 72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33 ] // "Hello World!" in bytes
var bytesAsStr:string := bytes_to_str("UTF-8", bytes)
print bytesAsStr // -> Hello World!
var status:integer := httpPostRequest(url, bytes)
// posts the byte array as binary data with the Content-Type application/octet-stream
```

- If the data of type `any`:
  - designates a list object whose first column is `integer`, those numbers are used like an array of integer values and sent as binary bytes.
  - designates integers, floating-point numbers, physical values, or other data, these are sent after conversion to text (like `to_str`); physical values are sent with their units.

**Content-type defaults**
- If no content type is passed in `RequestHeader` and `RequestBody` is `string` or `json`, Plant Simulation automatically adds `text/plain` or `application/json`.
- If an `integer[]` is passed as bytes without a content type, it is set to `application/octet-stream`.
- If the request header contains `application/x-www-form-urlencoded` and the body is `json`, it is automatically converted to form text (see `httpCreateFormURLEncodedString`) and sent as payload.

- `ResponseHeader` — a `json` variable to which the response header is written; its scheme matches the request header format.
- `ResponseBody` (string/json/integer[]/any) — the payload/response body returned by the HTTP server (see `httpGetRequest`).

**Default timeouts**
- 10 seconds for connecting to the resolved host
- 5 seconds for sending a request
- 5 seconds for receiving a request response

**Return value** — `integer`, the HTTP status code (e.g. `200` OK, `401` Unauthorized, `404` Not found, `501` Not implemented).

---

## httpGetRequest

Sends a GET request and requests data of a resource on an HTTP server.

**Syntax**
```
httpGetRequest(URL:string, byref ResponseBody:string/json/integer[]/any[, RequestHeader:string/json, byref ResponseHeader:json]) -> integer
```

**Parameters**
- `URL` (string) — the Unified Resource Locator used to address a resource. It can also contain authentication information:
```
http[s]://[<userName>:<password>@]<hostName>[:<port>][/<path>][<extraInfo>]
```
  - `http[s]://` — scheme; only `http://` and `https://` (encrypted) are supported.
  - `hostname` — server name, e.g. `www.siemens.com`.
  - `port` — port number (default standard port such as 80); separate with a colon if different.
  - `path` — path to the resource; components separated by a forward slash `/`.
  - `extraInfo` — can reference sections (`<hostName>/<path>#section`) or contain named parameters (`<hostName>/<path>?name1=value1&name2=value2&…`).

**URL character masking**

Parameter values may not contain characters used for HTTP protocol or URLs; these must be escaped with a preceding `%` followed by the hexadecimal representation of their Unicode code points.

| Character | URL compliant | Meaning |
|---|---|---|
| Empty space ( ) | `%20` | forbidden |
| Forward slash (/) | `%2F` | in paths only |
| Ampersand (&) | `%26` | separator of URL parameters |
| Question mark (?) | `%3F` | separator of URL parameters of the path |
| Equal sign (=) | `%3D` | separator of URL parameters and values |
| Numeral (#) | `%23` | only for reference to sections |
| Colon (:) | `%3A` | only in URL schemata between user name and password |
| At sign (@) | `%40` | separator of authentication data and server name |

Non-7-bit-ASCII characters are masked the same way:

| Character | URL compliant (UTF-8) |
|---|---|
| ö | `%C3%B6` |
| Ö | `%C3%96` |
| ä | `%C3%A4` |
| Ä | `%C3%84` |
| ü | `%C3%BC` |
| Ü | `%C3%9C` |
| ß | `%C3%9F` |
| € | `%E2%82%AC` |

Example form URL parameter:
```
?w%C3%A4hrungssymbol=%E2%82%AC&w%C3%A4hrungsname=Euro
```

- `ResponseBody` (string/json/integer[]/any) — the payload/response body returned by the server, written to the specified variable:
  - `json` — attempts to use textual data as JSON; errors if not valid JSON. For content types `application/json` and `*/*+json`, Plant Simulation tries to return JSON in any case. If no content type was specified, it first tests whether the data can be used as text before trying JSON.
  - `string` — treats response data depending on content type. The following return text: `text/*`, `application/json`, `*/*+json`, `*/*+html`, `*/*+txt`, `*/*+xml`. If no content type, it tests if data can be used as text; otherwise an error is thrown.
  - `integer[]` — transfers data byte by byte into the array (regardless of content type). Use `bytes_to_str`, `readBytesFromFile`, or `writeBytesToFile` to handle byte arrays.
  - `any` — saves data according to content type:
    - `application/json` and `*/*+json` → JSON structure (unless the body is a JSON array, in which case an array of boolean/integer/real/string values, or array-of-arrays of `any`, is returned).
    - `text/*`, `*/*+html`, `*/*+txt`, `*/*+xml` → text.
    - other content types → byte-by-byte in an `integer[]`.

- `RequestHeader` (json/string) — request headers.

**Request header as JSON**
```json
{
   "name1": [ "value", … ],
   "name2": [
       "value1": value,
       "value2": value
   ],
   "name3": [
       "value1",
       "value2", {
           "value3": value
       }, …
   ]
}
```
This results in:
```
name1: value
name2: value1=value; value2=value;…
name3: value1; value2; value3=value;…
```

**Request header as string** — either:
- the textual representation of a JSON object of HTTP headers, e.g. `"{ \"Accept\": [\"application/json\", { \"charset\": \"utf-8\" }] }"`, or
- an RFC 7230 conform text, e.g. `"Accept: application/json; charset=utf-8"`.

Rules:
- Names may only contain US-ASCII (7-bit-ASCII) letters.
- Values may only contain ISO 8859-1 (Latin1) letters.
- Plant Simulation checks these rules and throws an error if violated. Invalid names/values are not automatically masked. Use `encodeStringQuotedPrintable` when needed.

The `RequestHeader` can be:
- text containing a JSON structure starting with an opening curly brace,
- ready header text per RFC 7230 (not checked for validity; text not starting with a letter is rejected), or
- a JSON object mapping the structure and contents of the HTTP headers.

- `ResponseHeader` — a `json` variable to which the response header is written. Multiple values of a header (separated by semicolon) are returned in a JSON array.

Example response header:
```json
{
   "Status-Line": {
       "HTTP-Version": {
           "Protocol": "HTTP",
           "HTTP-Version": "1.1"
       },
       "Status-Code": 200,
       "Status-Phrase": "OK"
   },
   "Headers": {
       "Connection": ["keep-alive"],
       "Date": ["Wed, 06 Oct 2021 21:27:43 GMT"],
       "Content-Length": ["42"],
       "Content-Type": ["application/json", { "charset": "utf-8" }],
       "ETag": ["W/\"2a-a6vQ6tlXYuizn89nQjHv3WKYG7M\""],
       "Server": ["nginx/1.16.1"],
       "Access-Control-Allow-Origin": ["*"],
       "Access-Control-Allow-Methods": ["GET"],
       "Access-Control-Allow-Headers": ["content type"]
   }
}
```

**Default timeouts**
- 10 seconds for connecting to the resolved host
- 5 seconds for sending a request
- 5 seconds for receiving a request response

**Return value** — `integer`, the HTTP status code.

---

## httpGetTimeouts

Retrieves the defined timeouts used in the Windows HTTP interface (WinHTTP).

**Remarks**
All timeout values are in milliseconds. A value of `0` or `-1` means the interface waits forever (no timeout).

**Syntax**
```
httpGetTimeouts(byref ResolveTimeout:integer, byref ConnectionTimeout:integer, byref SendTimeout:integer, byref ReceiveTimeout:integer) -> void
```

**Parameters**
- `ResolveTimeout` (integer, by reference) — timeout for resolving the host name in a URL.
- `ConnectTimeout` (integer, by reference) — timeout for connecting to the resolved host.
- `SendTimeout` (integer, by reference) — timeout for sending a request to a connected host.
- `ReceiveTimeout` (integer, by reference) — timeout for receiving a request response after sending a request.

**Return value** — void.

**Example**
```simtalk
var resolve:integer
var connect:integer
var send:integer
var receive:integer

httpGetTimeouts(resolve, connect, send, receive)
print to_str("resolve: ", resolve)
print to_str("connect: ", connect)
print to_str("send:    ", send)
print to_str("receive: ", receive)
/* prints, if not changed before by httpSetTimeouts, the defaults (in ms):
resolve: -1
connect: 60000
send:    30000
receive: 30000
*/
```

---

## httpHeadRequest

Sends a HEAD request. A HEAD request resembles a GET request except it does not return data via the response body.

**Remarks**
This lets you check what kind of data and how much data would be returned for a GET request. The response body is still part of the syntax though, as the server might return error information using it.

**Syntax**
```
httpHeadRequest(URL:string[, RequestHeader:string/json, byref ResponseHeader:json, byref ResponseBody:string/json/integer[]/any]) -> integer
```

**Parameters** — see `httpGetRequest`:
- `URL` (string)
- `RequestHeader` (json/string)
- `ResponseHeader` (json, by reference)
- `ResponseBody` (string/json/integer[]/any)

**Default timeouts** — 10s connect, 5s send, 5s receive.

**Return value** — `integer`, the HTTP status code.

---

## httpOptionsRequest

Sends an OPTIONS request.

**Remarks**
An OPTIONS request queries the access methods (HTTP verbs) and other options for the specified resource. The response body is still part of the syntax, as the server might return error information using it.

**Syntax**
```
httpOptionsRequest(URL:string[, RequestHeader:string/json, byref ResponseHeader:json, byref ResponseBody:string/json/integer[]/any]) -> integer
```

**Parameters** — see `httpGetRequest`:
- `URL` (string)
- `RequestHeader` (json/string)
- `ResponseHeader` (json, by reference)
- `ResponseBody` (string/json/integer[]/any)

**Default timeouts** — 10s connect, 5s send, 5s receive.

**Return value** — `integer`, the HTTP status code.

---

## httpPostFileRequest

Sends a POST request, using the contents of the specified file as payload/request body.

**Remarks**
Compared to `httpPostRequest`, this function uses the contents of the specified file as the payload/request body.

**Syntax**
```
httpPostFileRequest(URL:string, RequestBodyFile:string[, RequestHeader:string/json, byref ResponseHeader:json, byref ResponseBody:string/json/integer[]/any]) -> integer
```

**Parameters**
- `URL` (string)
- `RequestBodyFile` (string) — the file name or path whose contents are sent as payload.
- `RequestHeader` (json/string)
- `ResponseHeader` (json, by reference)
- `ResponseBody` (string/json/integer[]/any)

**Default timeouts** — 10s connect, 5s send, 5s receive.

**Return value** — `integer`, the HTTP status code.

---

## httpPostRequest

Sends a POST request.

**Remarks**
- `httpPostRequest` creates or changes a resource on an HTTP server by sending information as payload/request body.
- Normally a client does not receive data via a response body for a POST request; if an error occurs, a response body with helpful information is sent back.
- Repeated POST requests with the same data normally do not have the same result.

**Syntax**
```
httpPostRequest(URL:string, RequestBody:string/json/integer[]/any[, RequestHeader:string/json, byref ResponseHeader:json, byref ResponseBody:string/json/integer[]/any]) -> integer
```

**Parameters**
- `URL` (string)
- `RequestBody` (string/json/integer[]/any) — the payload to be sent:
  - `string` — sent as-is, without conversion.
  - `json` — converted into a string and sent.
  - `integer[]` — each number treated as one byte of binary data, sent as a sequence of bytes.
  - array of `any` — values converted into text; compatible with JSON arrays and automatically transmitted with content type `application/json`.

**Request body examples**
```simtalk
var requestBody1:real[] := [ 1.1, 2.2, 3.3, 4.4, 5.5 ]
var status:integer      := httpPostRequest(url, requestBody1)
// post an array of reals, the Content-Type is application/json

var requestBody2:real[] := [ "A", "B", "C", "D", "E" ]
status                  := httpPostRequest(url, requestBody2)
// post an array of strings, the Content-Type is application/json

var requestBody3:real[] := [ { "A": 1 }, { "B": 2 }, { "C": 3 }, { "D": 4 }, { "E": 5 } ]
status                  := httpPostRequest(url, requestBody3)
// post an array of JSON objects, the Content-Type is application/json

var requestBody4:any[] := [ 1, 2.2, 3.3km, "4th element", { "Name": "5th element" }, false ]
status                 := httpPostRequest(url, requestBody4)
// post the mixed array of the Content-Type application/json:
// [ 1, 2.2, 3300, "4th element", { "Name": "5th element" }, false ]
```

To avoid `application/json` for an array, specify the content type in the request header:
```simtalk
var requestBody:real[]   := [ 1.1, 2.2, 3.3, 4.4, 5.5 ]
var requestHeader:string := "Content-Type: text/plain"
var status:integer        := httpPostRequest(url, requestBody, requestHeader)
// post an array of reals, the Content-Type is text/plain

var jsRequestHeader:json := { "Content-Type": "text/plain" }
status                  := httpPostRequest(url, requestBody, jsRequestHeader)
// post an array of reals, the Content-Type is text/plain
```

**Notes on physical values and bytes**
```simtalk
var len:length := 3.3km
print len // -> 3300

var status:integer := httpPostRequest(url, len)
// posts the length given in km as m: 3.3km -> 3300
```
```simtalk
var bytes:integer[] := [ 72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33 ] // "Hello World!" in bytes
var bytesAsStr:string := bytes_to_str("UTF-8", bytes)
print bytesAsStr // -> Hello World!
var status:integer := httpPostRequest(url, bytes)
// posts the byte array as binary data with the Content-Type application/octet-stream
```

- If the data of type `any`:
  - designates a list object whose first column is `integer`, those numbers are used like an `integer[]` and sent as binary bytes.
  - designates integers, floating-point numbers, physical values, or other data, these are sent after conversion to text (like `to_str`); physical values are sent with their units.

**Content-type defaults** — same as `httpDeleteRequest`:
- `string`/`json` without content type → `text/plain`/`application/json`.
- `integer[]` as bytes without content type → `application/octet-stream`.
- header `application/x-www-form-urlencoded` + json body → converted to form text (see `httpCreateFormURLEncodedString`).

- `RequestHeader` (json/string)
- `ResponseHeader` (json, by reference)
- `ResponseBody` (string/json/integer[]/any)

**Default timeouts** — 10s connect, 5s send, 5s receive.

**Return value** — `integer`, the HTTP status code.

---

## httpPutFileRequest

Sends a PUT request, using the contents of the specified file as payload (RequestBody).

**Syntax**
```
httpPutFileRequest(URL:string, RequestBodyFile:string[, RequestHeader:string/json, byref ResponseHeader:json, byref ResponseBody:string/json/integer[]/any]) -> integer
```

**Parameters**
- `URL` (string)
- `RequestBodyFile` (string) — file name/path whose contents are sent as payload (noted in the parameter list; the original doc repeats `RequestHeader` here).
- `RequestHeader` (json/string)
- `ResponseHeader` (json, by reference)
- `ResponseBody` (string/json/integer[]/any)

**Default timeouts** — 10s connect, 5s send, 5s receive.

**Return value** — `integer`, the HTTP status code.

---

## httpPutRequest

Sends a PUT request.

**Remarks**
- `httpPutRequest` creates a resource on an HTTP server by sending information as payload/request body.
- Normally a client does not receive data via a response body for a POST request; if an error occurs, a response body is sent back.
- Repeated requests with the same data as a PUT should always return the same result.

**Syntax**
```
httpPutRequest(URL:string, RequestBody:string/json/integer[]/any[, RequestHeader:string/json, byref ResponseHeader:json, byref ResponseBody:string/json/integer[]/any]) -> integer
```

**Parameters**
- `URL` (string)
- `RequestBody` (string/json/integer[]/any):
  - `string` — sent as-is.
  - `json` — converted into a string and sent.
  - `integer[]` — each number treated as one byte, sent as a sequence of bytes.
  - `any`:
    - list object with first column `integer` → sent as binary bytes.
    - integers, floating-point numbers, physical values, etc. → converted to text (like `to_str`); physical values sent with units.

**Content-type defaults** — same as `httpPostRequest`:
- `string`/`json` without content type → `text/plain`/`application/json`.
- `integer[]` as bytes without content type → `application/octet-stream`.
- header `application/x-www-form-urlencoded` + json body → converted to form text.

- `RequestHeader` (json/string)
- `ResponseHeader` (json, by reference)
- `ResponseBody` (string/json/integer[]/any)

**Default timeouts** — 10s connect, 5s send, 5s receive.

**Return value** — `integer`, the HTTP status code.

---

## httpSetTimeouts

Sets the timeouts used in the Windows HTTP interface (WinHTTP).

**Remarks**
- All timeout values are in milliseconds.
- A value of `0` or `-1` sets infinite waiting.
- A negative value that is neither `0` nor `-1` causes an error about an invalid parameter.

> Note: Some HTTP server communication functions have built-in default timeout values.

**Syntax**
```
httpSetTimeouts(ResolveTimeout:integer, ConnectionTimeout:integer, SendTimeout:integer, ReceiveTimeout:integer) -> void
```

**Parameters**
- `ResolveTimeout` (integer) — timeout (ms) for resolving the host name in a URL.
- `ConnectTimeout` (integer) — timeout (ms) for connecting to the resolved host.
- `SendTimeout` (integer) — timeout (ms) for sending a request to a connected host.
- `ReceiveTimeout` (integer) — timeout (ms) for receiving a request response after sending a request.

**Return value** — void.

**Example**
```simtalk
/* sets the timeouts to:
120000ms meaning 120s to resolve an URL
60000ms meaning 60s to connect to the host
15000ms meaning 15s to send a request to the host
15000ms meaning 15s to receive the request response from a host
*/
httpSetTimeouts(120000, 60000, 15000, 15000)
```

---

## httpSplitFormUrlEncodedString

Splits the extraInfo part of a URL, or the text of a response body with Content-Type `application/x-www-form-urlencoded`.

**Remarks**
- Returns a flat JSON structure containing the recognized name-value pairs.
- Names and values containing Quoted-Printable-masked characters are unmasked.
- To extract the extraInfo part from a URL and parse it into name-value pairs, use `httpSplitURL` (it parses the URL and its extraInfo part).

**Syntax**
```
httpSplitFormUrlEncodedString(FormKeyValueString:string) -> json
```

**Parameter**
- `FormKeyValueString` (string) — the "extra info" of a URL found after the path, or the text from a response body whose Content-Type is `application/x-www-form-urlencoded`.

If part of a URL, the text starts with a question mark `?`. Name-value pairs are separated by an ampersand `&`; names and values are separated by an equal sign `=`.

Format of the query parameter in the URL:
```
name1=value1&name%202=value2&name3=value%203&...
```
(The question mark is missing in the text received in the response body of a request.)

The result is a flat JSON structure:
```json
{
   "name1": "value1",
   "name 2": "value2",
   "name3": "value 3",
   ...
}
```

**Return value** — `json`.

**Example**
```simtalk
var url:string := "…"
var respBody:string
var respHeaders:json
if httpGetRequest(url, respBody, "", respHeaders) = 200
   var values:json
   var contentType:string := respHeaders["Content-Type"]
   if contentType = "application/x-www-form-urlencoded"
      values := httpSplitFormUrlEncodedString(respBody)
   elseif contentType = "application/json"
      values.parse(respBody)
   else
      throwRuntimeError("invalid response body content-type")
   end
end
```

---

## httpSplitURL

Splits a URL into its components.

**Remarks**
You can change individual components and put them back together with `httpCreateURL`.

**Syntax**
```
httpSplitURL(URL:string) -> json
```

**Parameter**
- `URL` (string) — the URL to split. It must have this format:
```
http[s]://[<username>:<password>@]<server>[:<port>][/<path>][<extra>]
```

**Return value** — `json`, a flat JSON structure with these elements (only those found in the URL are included):
- `SSL` — `true` for encrypted transport (`https`), `false` for `http`.
- `server` — name of the server (host name).
- `port` — integer port number on the designated server.
- `path` — path to a resource, directory, or file on the server.
- `extra` — a reference to a resource section (starts with `#`) or a flat JSON structure of a URL query parameter (starts with `?`).
- `username` — user name used for authentication.
- `password` — password for the user name used for authentication.
- `scheme` — the URL scheme (`http` or `https`), matching the JSON element `SSL`.

> Note: Plant Simulation does not add elements to the JSON structure that it does not find in the URL (i.e., empty elements).

---

## readBytesFromFile

Reads the specified file and returns the contents as a sequence of byte values in an array of integers.

**Syntax**
```
readBytesFromFile(FileName:string) -> integer[]
```

**Parameter**
- `FileName` (string) — name of the file whose contents are to be converted.

**Return value** — `integer[]`.

**Example**
```simtalk
var fileName:string := "…"
var bytes:integer[] := readBytesFromFile(fileName)
print bytes
// prints [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
var text:string := bytes_to_str("ANSI", bytes)
print text
// prints Hello World
```

---

## writeBytesToFile

Writes the specified array of integers as a sequence of byte values to the specified file.

**Syntax**
```
writeBytesToFile(Bytes:integer[], FileName:string)
```

**Parameters**
- `Bytes` (integer[]) — the sequence of byte values to write to a file.
- `FileName` (string) — the name of the file to contain the sequence of bytes.

**Example**
```simtalk
param fileName:string
var bytes:integer[]
var reqHeaders:json
var respHeaders:json
var statusCode:integer := httpGetRequest("http://a.server.com/charts/resources/current", bytes, reqHeaders, respHeaders)
if statusCode = 200
   if respHeaders.contains("Content-Type") = false
      throwRuntimeError("couldn't write current chart to file: no response header Content-Type found")
   elseif regex_search(respHeaders["Content-Type"], "^image/\w+$") == ""
      throwRuntimeError("couldn't write current chart to file: expected Content-Type image/*, but got \"" + respHeaders["Content-Type"] + "\"")
   end
   writeBytesToFile(bytes, fileName)
end
```
