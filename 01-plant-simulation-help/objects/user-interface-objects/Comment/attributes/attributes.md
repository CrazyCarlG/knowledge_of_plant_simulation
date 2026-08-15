# Attributes of the Comment

The **Comment** object provides:

- The attributes listed in the table of contents.
- The **Attributes of All Objects**.

## Viewing Attributes and Methods

To view all methods, read-only attributes, and attributes of an object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the **Class Library** to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the **Home** ribbon tab of the Frame into which you inserted an instance, to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, for example:

```simtalk
print MyComment.UUID
```

You can set and get the value of an attribute, either with the check boxes, text boxes and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

- To set the value of an attribute:

```simtalk
MyComment.Color := makeRGBColor(255,0,0)
```

- To get the value of an attribute:

```simtalk
print MyComment.font
posit := Station.Cont.XPos
```

---

## BackgroundColor [SimTalk] - Comment

Sets the **Background Color** of the Comment designated by `<Path>` which you inserted into a Frame.

- **Remarks:** Set the RGB values of the color with the method `makeRGBValue`.
- **Type:** Attribute
- **Syntax:** `<Path>.BackgroundColor:integer`
- **Assignment Value:** You can assign a value of data type integer.

**Example**

```simtalk
MyComment.BackgroundColor := makeRGBValue(100,100,100)
MyComment.BackgroundColor := 6579300 // is the same as the color above
```

- **SimTalk:** `makeRGBValue [SimTalk]`
- **See also:** Background Color [drop-down list] - Comment

---

## Color [SimTalk] - Comment

Sets the **Color** with which Plant Simulation displays the text of the Comment designated by `<Path>` in the Frame.

- **Remarks:** Set the RGB values of the color with the method `makeRGBValue`.
- **Type:** Attribute
- **Syntax:** `<Path>.Color:integer`
- **Assignment Value:** You can assign a value of data type integer.

**Example**

```simtalk
MyComment.Color := makeRGBValue(255,0,0)
```

- **SimTalk:** `makeRGBValue [SimTalk]`
- **See also:** Font Color [Comment]

---

## Cont [SimTalk] - Comment

Sets the **Contents** of the text box on the tab **Comment** of the Comment designated by `<Path>`.

- **Remarks:** Enter a backslash `\` to insert a line break.
- **Type:** Attribute
- **Syntax:** `<Path>.Cont:string`
- **Assignment Value:** You can assign a value of data type string.

**Example**

```simtalk
MyComment.Cont := "Species: Aardvark\
                 amount: 45 \
                 weight: 780kg" // assign a multi-line comment
```

- **SimTalk:** `mu [SimTalk] - material flow objects`
- **See also:** Tab Comment [Comment]

---

## Font [SimTalk] - Comment

Sets the **Font Size** with which Plant Simulation displays the Comment designated by `<Path>` in the Frame.

- **Type:** Attribute
- **Syntax:** `<Path>.Font:integer`
- **Assignment Value:** You can assign a value of data type integer. You can specify `1` for Small, `2` for Medium, `3` for Large, `4` for Extra Large.

**Example**

```simtalk
if MyComment.Font < 4 
   MyComment.Font := MyComment.Font + 1
```

- **See also:** Font Size [drop-down list] - Comment

---

## SaveAsRichedit [SimTalk]

Makes the Comment designated by `<Path>` save the contents of the text box in rich-text format (`true`) or not (`false`).

- **Remarks:** Rich-text preserves all the formatting properties you applied.
- **Type:** Attribute
- **Syntax:** `<Path>.SaveAsRichedit:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

**Example**

```simtalk
MyComment.SaveAsRichedit := false
```

- **See also:** Save the Content in Rich-text Format

---

## Text [SimTalk] - Comment

Sets the comment text that the Comment designated by `<Path>` shows in the Frame.

- **Remarks:** The text may also contain blanks and/or special characters.
- **Type:** Attribute
- **Syntax:** `<Path>.Text:string`
- **Assignment Value:** You can assign a value of data type string.

**Example**

```simtalk
MyComment.Text := "Buffer utilization in %"
```

- **See also:** Text [text box] - Comment

---

## Transparent [SimTalk] - Comment

Makes the background of the object designated by `<Path>` transparent in the Frame (`true`) or not transparent (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.Transparent:boolean`
- **Assignment Value:** You can assign a value of data type boolean.
  - Specify `true` to show the Comment in the color that you selected as the **Font Color** on the background of the Frame.
  - Specify `false` to show the space around the text in white.

**Example**

```simtalk
MyComment.Transparent := false
```

- **See also:** Transparent [check box] - Comment, Font Color [Comment]
