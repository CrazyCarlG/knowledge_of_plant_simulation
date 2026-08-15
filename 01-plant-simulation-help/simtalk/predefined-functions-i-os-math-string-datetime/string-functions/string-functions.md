# SimTalk String Functions

This document summarizes the SimTalk string functions for working with strings, regular expressions, and character codes.

> Note: The SimTalk parser uses the backslash (`\`) as an escape character. To search for a literal backslash and replace it with another character, type four backslashes `\\\\`.

---

## regex_replace

Searches for text matching a regular expression and replaces all matching strings with the specified replacing text.

**Syntax**

```
regex_replace(Text:string, RegularExpression:string, ReplacingText:string) → string
```

**Parameters**

- `Text` — the text to search for the regular expression.
- `RegularExpression` — the regular expression to replace.
- `ReplacingText` — the text that replaces the regular expression.

**Return Value** — `string`: the text with the original regular expression replaced.

**Examples**

```simtalk
// replaces the backslash with an empty space
regex_replace("my\\text", "\\\\", " ")
print regex_replace("my\\text", "\\\\", " ")
-- outputs my text

// replaces the time by the hour
regex_replace("1234567 9:45pm 1234567 7:45pm 1234", "((1[0-2])|(0?[1-9])):([0-5][0-9])((am)|(pm))", "$1")
// results in "1234567 9 1234567 7 1234"

// Removes all space characters
print regex_replace("This is a test", " ", "")
// Results in Thisisatest

// Replaces the characters /, : and space by the character |
print regex_replace("2018/09/12 12:33", "[/: ]", "|")
// Results in 2018|09|12|12|33
```

---

## regex_search

Searches for text that matches a regular expression and returns the first matching substring.

**Syntax**

```
regex_search(Text:string, RegularExpression:string) → string
```

**Parameters**

- `Text` — the text to search for the regular expression.
- `RegularExpression` — the regular expression to find.

**Return Value** — `string`: the string which first matches the expression; empty string `""` if no match is found.

**Examples**

```simtalk
// extracts the time portion
regex_search("12345678 11:53am test", "((1[0-2])|(0?[1-9])):([0-5][0-9])((am)|(pm))")
-- returns "11:53am"

// extracts a HTML group
regex_search("thrth <h1>123123</h1> etheth 123", "<(.+)>(.*)</(\1)>")
-- returns <h1>123123</h1>
```

### Regular Expression Metacharacters

| Metacharacter | Description | Example |
|---|---|---|
| `.` | Matches any single character. Within bracket expressions, matches a literal dot. | `a.c` matches "abc"; `[a.c]` matches only "a", ".", or "c". |
| `?` | Matches the preceding element zero or one time. | `ab?c` matches only "ac" or "abc". |
| `?` (lazy) | Modifies the preceding `*`, `+`, `?` or `{m,n}` to match as few times as possible. | — |
| `*` | Matches the preceding element zero or more times. | `ab*c` matches "ac", "abc", "abbbc"; `[xyz]*` matches "", "x", "y", "z", "zx", "zyx", "xyzzy"; `(ab)*` matches "", "ab", "abab", "ababab". |
| `+` | Matches the preceding element one or more times. | `ab+c` matches "abc", "abbc", "abbbc", but not "ac". |
| `{m,n}` | Matches the preceding element at least `m` and not more than `n` times. | `a{3,5}` matches only "aaa", "aaaa", "aaaaa". |
| `[ ]` | Bracket expression. Matches a single character contained within the brackets. | `[abc]` matches "a", "b", or "c"; `[a-z]` matches any lowercase letter; `[abcx-z]` matches "a", "b", "c", "x", "y", or "z". The `-` is literal if last or first (after `^`); `]` can be included if first after `^`. Backslash escapes are not allowed inside brackets. |
| `[^ ]` | Matches a single character not contained within the brackets. | `[^abc]` matches any character other than "a", "b", or "c"; `[^a-z]` matches any single non-lowercase character. |
| `^` | Matches the starting position within the string. | — |
| `$` | Matches the ending position of the string or the position just before a string-ending newline. | — |
| `( )` | Defines a subexpression. | — |
| `\|` | Choice (alternation / set union) operator. Matches either the expression before or after the operator. | `abc\|def` matches "abc" or "def". |
| `\b` | Matches a zero-width boundary between a word-class character and a non-word-class character or an edge. | — |
| `\w` | Matches an alphanumeric character, including `_`. | — |
| `\W` | Matches a non-alphanumeric character, excluding `_`. | — |
| `\s` | Matches a whitespace character (tab, line feed, form feed, carriage return, space). | — |
| `\S` | Matches anything but a whitespace. | — |
| `\d` | Matches a digit. | — |
| `\D` | Matches a non-digit. | — |
| `(?=subpattern)` | The characters following the assertion must match subpattern, but no characters are consumed. | — |
| `(?!subpattern)` | The characters following the assertion must not match subpattern, but no characters are consumed. | — |
| `(?:subpattern)` | Defines a subexpression. Does not create a backreference. | — |
| `$1, $2, …` | References the backreference with the given number. | — |

---

## regex_search2

Searches for text matching a regular expression. Unlike `regex_search`, returns an array of `string` containing all found partial expressions, followed by the preceding text, followed by the text at the end.

**Syntax**

```
regex_search2(Text:string, RegularExpression:string) → string[]
```

**Parameters**

- `Text` — the text to search for the regular expression.
- `RegularExpression` — the regular expression to find.

**Return Value** — `string[]`: an array of all found partial expressions, then preceding text, then trailing text.

**Examples**

```simtalk
print regex_search2("John.Doe@acme.com", "(\w*)\.(\w*)@(\w*)\.(\w*)")
[John.Doe@acme.com, John, Doe, acme, com, , ]

print regex_search2("EMail:John.Doe@acme.com [John Doe]", ":(\w*)\.(\w*)@(\w*)\.(\w*)")
[:John.Doe@acme.com, John, Doe, acme, com, EMail,  [John Doe]]
```

---

## splitString

Splits a string into its individual string components.

**Syntax**

```
splitString(Text:string, Delimiter:string[, KeepEmptyItems:boolean:=false]) → string[]
```

**Parameters**

- `Text` — the string to split.
- `Delimiter` — the delimiter used to separate components. The delimiter can be any character. If empty, the result is an array of the individual letters of the text.
- `KeepEmptyItems` (optional, `boolean`, default `false`) — if `true`, empty strings are incorporated into the array; if `false`, they are not.

**Return Value** — `string[]`.

**Examples**

```simtalk
print splitString("a,b,c,d", ",")       -- returns [a, b, c, d] in the Console
print splitString("one,two;three;four,five", ",;")
-- returns [one, two, three, four, five] in the Console
print splitString("a;b;;c", ";", true) -- returns [a, b, , c] in the Console
print splitString("a;b;;c", ";")       -- returns [a, b, c]

var text:string := "Hello World"
var letters:string[] := splitString(text, "")
print letters
-- returns [H, e, l, l, o,  , W, o, r, l, d]
```

---

## splitStringToNum

Splits a string into an array of numbers of data type `real`.

**Syntax**

```
splitStringToNum(Text:string, Delimiter:string) → real
```

**Parameters**

- `Text` — the real numbers to split.
- `Delimiter` — the delimiter used to separate components.

**Return Value** — an array of data type `real`.

**Example**

```simtalk
print splitStringToNum("1.2;2.8!3.4;4.5;6.8!3.6", ";!")
// returns [1.2, 2.8, 3.4, 4.5, 6.8, 3.6] in the Console
```

---

## strAscii

Returns the Unicode character code of the specified character of a string.

If the optional parameter `PositionOfCharacter` is not specified, returns the character code of the first character.

**Syntax**

```
strAscii(String:string[, PositionOfCharacter:integer]) → integer
```

**Parameters**

- `String` — the string.
- `PositionOfCharacter` (optional, `integer`) — position of the character whose code you want. `1` is the first character; range is `1` to string length. A negative value receives the n-th character starting from the end.

**Return Value** — `integer`: a number between 1 and 65535.

**Examples**

```simtalk
var s: string := "Hello World!"
for var i := 1 to strlen(s)
   print strChr(strAscii(s, i)), ", ", strAscii(s, i)
next
print strAscii("Test", -1) // returns 116, the Ascii-Code of the letter 't'
```

---

## strChr

Returns a string of length 1 consisting of the character with the given Unicode character code.

**Syntax**

```
strChr(UnicodeNumber:integer) → string
```

**Parameter** — `UnicodeNumber` (`integer`): the Unicode character code. Useful for creating strings with special characters that cannot be entered on the keyboard.

**Return Value** — `string`.

**Examples**

```simtalk
print "cost:"+strChr(9)+"$42" // strChr(9) returns a tab
print strChr(20616) // prints the Chinese character 傈
```

---

## strCopy

Copies the specified segment of a string and returns it.

**Syntax**

```
strCopy(String:string, Position:integer, NumberOfCharacters:integer)
```

**Parameters**

- `String` — the string from which the segment is copied.
- `Position` — the position from which the segment is copied. No error message if `Position` is less than 1 or `NumberOfCharacters` is greater than the string length.
- `NumberOfCharacters` — the number of characters to copy.

**Example**

```simtalk
print strCopy("abcdef",2,3)   // returns "bcd"
print strCopy("abcdef",4,10)  // returns "def"
print strCopy("abcdef",-1,4)  // returns "ab" (-1 and 0 letter are counted)
```

---

## strIncl

Inserts the specified text into another string and returns the combined text of both.

**Syntax**

```
strIncl(TextToBeInserted:string, Text:string, Position:integer) → string
```

**Parameters**

- `TextToBeInserted` — the text to insert into the other string.
- `Text` — the text into which the string will be inserted.
- `Position` — the position in front of which `TextToBeInserted` will be inserted. The first character has index `1`. No error message if `Position` is less than 1 or greater than the string length; the text is inserted before or after `Text` respectively.

**Return Value** — `string`.

**Example**

```simtalk
print strIncl("XYZ","abcdef",3)   // returns "abXYZcdef"
print strIncl("XYZ","abcdef",-1)  // returns "XYZabcdef"
print strIncl("XYZ","abcdef",1)   // returns "XYZabcdef"
print strIncl("XYZ","abcdef",20)  // returns "abcdefXYZ"
```

---

## strLen

Returns the length, i.e., the number of characters of the specified string.

**Syntax**

```
strLen(Text:string) → integer
```

**Parameter** — `Text`: the string.

**Return Value** — `integer`.

**Example**

```simtalk
print strLen("shop") // returns 4
```

---

## strLPos

Returns the position at which the designated text occurs for the first time within the specified string.

**Syntax**

```
strLPos(StrToSearchFor:string, StrToSearchIn:string) → integer
```

**Parameters**

- `StrToSearchFor` — the string whose position you want to know.
- `StrToSearchIn` — the string in which the first occurrence is searched.

**Return Value** — `integer`; `0` if the search string was not found.

**Example**

```simtalk
print strLPos("b","abcdefb") // returns 2
```

---

## strOmit

Copies the specified string and deletes a succession of characters from it.

**Syntax**

```
strOmit(SourceText:string, Position:integer, NumberOfCharacters:integer) → string
```

**Parameters**

- `SourceText` — the string to copy.
- `Position` — the position from which characters are deleted.
- `NumberOfCharacters` — the number of characters to delete.

**Return Value** — `string`.

**Example**

```simtalk
print strOmit("abcdef",3,2) // returns "abef"
print strOmit("abcdef",0,3) // returns "cdef" (0 letter is counted)
```

---

## strRcopy

Copies a number of characters within the string, starting from the right.

**Syntax**

```
strRcopy(SourceText:string, NumberOfCharacters:integer) → string
```

**Parameters**

- `SourceText` — the string from which to copy characters.
- `NumberOfCharacters` — the number of characters to copy, starting from the right.

**Return Value** — `string`.

**Example**

```simtalk
print strRcopy("abcde",2) // returns de
```

---

## strReplace

Searches for `TextToFind` within `SourceText` and replaces all occurrences with `ReplaceBy`. Returns the resulting string. The source text is not modified.

**Syntax**

```
strReplace(SourceText:string, TextToFind:string, ReplaceBy:string) -> string
```

**Parameters**

- `SourceText` — the source text to search within.
- `TextToFind` — the text to find.
- `ReplaceBy` — the text that replaces all found occurrences.

**Return Value** — `string`.

**Example**

```simtalk
var SourceText : string := "hello world"
var Result1 : string := strReplace(SourceText, "l", "XY") -- returns "heXYXYo worXYd"
var Result2 : string := strReplace(SourceText, "ll", "x") -- returns "hexo world"
var Result3 : string := strReplace(SourceText, "L", "x")  -- returns "hello world" because upper-case L is not contained
```

---

## strRpos

Returns the position at which the designated text occurs for the last time within the `SourceText`.

**Syntax**

```
strRpos(TextToBeFound:string, SourceText:string) → integer
```

**Parameters**

- `TextToBeFound` — the text whose position you want to query.
- `SourceText` — the string within which you want to query.

**Return Value** — `integer`; `0` if no match was found.

**Example**

```simtalk
print strRpos("bb","abbabbaaabaa") // returns 5
```

---

## strToHtml

Replaces all occurrences of characters that have syntactic meaning in HTML with the respective HTML entities to create valid HTML code.

**Syntax**

```
strToHtml(Text:string) → string
```

**Parameter** — `Text`: the text to convert to valid HTML.

**Return Value** — `string`.

**Examples**

```simtalk
-- replaces the greater-than-sign > with the HTML entity &gt;
var s: string := strToHtml("var > 4") -- results in var &gt; 4

-- replaces the double-quotation marks " with the respective HTML entity &quot;
print strToHtml("This is a \"quotation\"") -- results in This is a &quot;quotation&quot;
```

---

## strToLower

Changes upper-case letters within the specified string to lower-case letters.

**Syntax**

```
strToLower(UpperCaseLetter:string) → string
```

**Parameter** — `UpperCaseLetter`: any combination of upper-case letters, lower-case letters, and special characters. The result contains only lower-case letters and special characters.

**Return Value** — `string`.

**Examples**

```simtalk
print strToLower("SHANIA")        // returns "shania"
print strToLower("Hello World!")  // returns "hello world!"
```

---

## strToUpper

Changes lower-case letters in the specified string to upper-case letters.

**Syntax**

```
strToUpper(LowerCaseLetters:string) → string
```

**Parameter** — `LowerCaseLetters`: any combination of upper-case letters, lower-case letters, and special characters. The result contains only upper-case letters and special characters.

**Return Value** — `string`.

**Examples**

```simtalk
print strToUpper("shania")         // returns "SHANIA"
print strToUpper("Hello World!")   // returns "HELLO WORLD!"
```
