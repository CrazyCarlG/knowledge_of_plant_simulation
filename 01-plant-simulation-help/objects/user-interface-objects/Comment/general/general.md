# Comment

The **Comment** object shows explanatory notes that you added to your simulation model.

## Description

A comment helps you and your colleagues better understand the intentions behind your model and how it is supposed to work. You can access it like any other object, but the Comment is usually not involved in the simulation itself.

- Select **Options > Show Comments** on the View ribbon tab of the Frame, or click the icon, to display all Comment objects inserted into that Frame.
- Plant Simulation displays the text in the Frame window that you entered under **Display > Text**.
- To open a window that only shows the comment (without formatting and editing options), right-click the Comment and select **Open Comment Window**.
- Hover over the Comment to show a tooltip with information about it.
- To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press `M`.

### Add the Object to the Simulation Model

Click **Manage Class Library > Basic Objects > UserInterface > Comment** on the Home ribbon tab.

## Dialog Box of the Comment

Double-click the icon of the Comment inserted into a Frame to open its dialog box. Drag any side or corner to make the dialog box larger or smaller.

- **Open Comment Window** — right-click the Comment and select **Open Comment Window**. Plant Simulation opens the comment window with the size the **Comment** tab had when you entered the comment, and with the formatting you applied.
- Close the comment window by clicking **Close** in the title bar.

### Edit Animation Properties

To edit the 3D properties in the dialog **Edit 3D Properties**:

- Click **Edit 3D Properties** in the lower-left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic, click **Show Manipulators** on the Edit ribbon tab or press `M`.

### Name [text box] - Comment

Shows the name of the object — either the predefined name or a name you specify. Double-click and type over it to change it.

**Remarks:** You can use letters, digits, and underscore (`_`), for example `MyComment`, `MyComment1`, `My_Comment_1`. The name cannot start with a digit (e.g., `1Comment` is not allowed).

## Tab Comment

Type a detailed description appending the short note entered into the Text box on the Tab Display.

**Note:** Formatting properties only apply if you select **Save the Content in Rich-text Format**.

- Apply formatting to selected text with the **Formatting Toolbar** buttons or the **Context Menu for Formatting the Comment**.
- Character format properties:
  - Apply a typeface, a font size, and a font color.
  - Apply bold face, underline, or italicize text.
- Paragraph format properties:
  - Set alignment: Align Left, Center, or Align Right.
  - Set an indentation with bullets.
- Or copy text formatted in a word processor that works with rich text format (`.rtf`), such as WordPad or MS Word, and paste it (including formatting) into the text box.
- Or type text into the text box, copy it back to the word processor, apply formatting, and paste it back. Press `Ctrl+A` to select all, `Ctrl+C` to copy, `Ctrl+V` to paste.

### Formatting Toolbar

Apply formatting to selected text in RTF format. Settings only apply when **Save the Content in Rich-text Format** is selected.

| Action | Attribute |
| --- | --- |
| Undo the most recent action | — |
| Open the dialog **Font** (Font, Font style, Size, Effects) | `Font` |
| Open the dialog **Colors** (select a Color) | `Color` |
| Apply bold face | — |
| Italicize text | — |
| Underline text | — |
| Align text left | — |
| Center text | — |
| Align text right | — |
| Add bullets (press `Enter` for a line break) | — |
| Open **Insert Date and Time** | — |

### Inherit Contents

To inherit or not inherit the contents of the Comment, click the inheritance check box next to the text box.

### Save the Content in Rich-text Format

Select this check box to save the text box contents in rich-text format, preserving all formatting. When selected, Plant Simulation activates the Formatting Toolbar settings and the Context Menu for Formatting the Comment.

### Context Menu for Formatting the Comment

Provides the formatting menu commands. You can also select these options on the Formatting Toolbar.

- **Undo** — undoes the most recent action.
- **Font** — select font settings (Font, Font Style, Size, Effects) in the **Font** dialog. Click OK to apply.
- **Color** — select color settings in the **Color** dialog. Click **Apply** to apply and keep the dialog open, or **OK** to apply and close.
- **Bold** — applies bold face to selected text.
- **Italic** — italicizes selected text.
- **Underline** — underlines selected text.
- **Align Left** — aligns text to the left.
- **Center** — centers text.
- **Align Right** — aligns text to the right.
- **Bullets** — adds a bullet in front of selected text (press `Enter` to insert a line break before a sentence).
- **Insert Date or Time** — opens the **Insert Date and Time** dialog; select a format and click OK to insert at the cursor position.

## Tab Display

On the **Display** tab, select how to display the Comment in the model.

### Text [text box] - Comment

Type the text that Plant Simulation shows when you insert the Comment object into a Frame.

- Type a short text, or you will not be able to see or select the Comment in the Frame.
- If you only entered text here (nothing on the **Comment** tab), Plant Simulation shows the **Display** tab the next time you open the dialog.
- Use the inheritance check box to inherit or not inherit the Text.

### Font Size [drop-down list] - Comment

Select a font size for displaying the Comment in the Frame.

### Font Color [Comment]

Click the drop-down arrow to select the color of the text shown in the Frame.

- The color is only shown in the Frame, not in the open dialog box.
- Select a predefined color, or click **More Colors** and click **Select** to choose a color in the color matrix, then click OK.

### Background Color [drop-down list] - Comment

Click the drop-down arrow to select the background color of the Comment.

- Select a predefined color, or click **More Colors** and click **Select** to choose a color in the color matrix, then click OK.

### Transparent [check box] - Comment

Select this check box to make the background shine through the hollow parts of the text.

- With a transparent background, the Comment is shown in the Font Color on the Frame background.
- Clear the check box to show the text on a white background.

## Menus

- **Navigate Menu** — commands are described under the Navigate Menu.
- **View Menu** — commands are described under the View Menu.
- **Tools Menu** — provides commands to access its functions (e.g., Edit Observers).
- **Help Menu** — commands are described under the Help Menu.

## Methods of the Comment

The Comment provides:

- The methods listed in the table of contents.
- The **Methods of All Objects**.

To view all methods, read-only attributes, and attributes, open **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the Class Library context menu to show a selected Class's members.
- Press `F8` or click **Show Attributes and Methods** on the Home ribbon tab of the Frame to show a selected Instance's members.

### SimTalk references

- `appendToContent`
- `openComment`
- `Name`
- `Font`
- `Color`
- `SaveAsRichedit`
- `Text`
- `BackgroundColor`
- `Transparent`
- `updateDialog`

## See also

- Add Text and Display Boards
- Dialog Box of the Comment
- Inherit Contents [Comment]
- `appendToContent` [SimTalk]
- `openComment` [SimTalk]
- `Font` [SimTalk] - Comment
- `Color` [SimTalk] - Comment
- `SaveAsRichedit` [SimTalk]
- `Text` [SimTalk] - Comment
- `BackgroundColor` [SimTalk] - Comment
- `Transparent` [SimTalk] - Comment
- `updateDialog` [SimTalk]
