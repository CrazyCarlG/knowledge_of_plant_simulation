# Classes, Libraries & Toolboxes

This document summarizes the Plant Simulation Help section covering simulation model creation, classes/subclasses/instances, inheritance, the Class Library, user-defined classes, saving/loading objects and libraries, and the Toolbox.

---

## 1. Creating a Simulation Model

You build a simulation model by inserting instances of built-in objects and user-defined (application) objects from the **Class Library** into the **Frame named `Model`** in the folder **Models**.

The most important built-in objects:

- **Frame** — the object in which you create your model. You insert station objects into the Frame named `Model`.
- **EventController** — starts, stops, and resets the simulation run.
- **Active material flow objects** — transport and/or actively process mobile objects (MUs).
- **Passive material flow objects** — store parts and represent tracks on which parts are moved.
- **Mobile objects (MUs)** — represent the parts created, stored, transported, processed, and removed.
- **Fluid objects** — simulate free-flowing materials (liquid, gaseous, or pourable); suited for food/beverage and pharmaceutical industries.
- **Resource objects** — model how and when Workers move from the WorkerPool to Workplaces.
- **Method objects** — program actions using the **SimTalk** programming language; provide the **Method Debugger**.
- **Lists and tables** — enable random exchange of information between all objects.
- **Chart and Report** — graphically display statistical values collected during simulation runs.
- **Dialog** — create custom dialog boxes for a simple user interface.
- **BottleneckAnalyzer / SankeyDiagram** — analyze and evaluate simulation results; **ExperimentManager** defines how experiments execute.

Key modeling concepts:

- **Nested hierarchy** — inserting Frames into Frames creates a randomly nested hierarchy of models.
- **Inheritance** — derive or duplicate objects; a derived (child) object keeps a controllable link to its parent (template). Deactivate inheritance per feature via the inheritance check box.
- **Interfaces** — exchange data with other programs during (not only before/after) simulation runs.

Two modeling strategies:

- **Top-down** — roughly structured model broken down step-by-step; requires abstraction but the big picture becomes obvious quickly.
- **Bottom-up** — detailed model from prefabricated components; quick detail analysis but harder to see the big picture.

> **Recommendation:** Do not change the default settings of built-in objects. If you customize them and later merge models or update the Class Library, Plant Simulation discards your changes. Instead, derive objects in the Class Library; they are added by default to the folder `UserObjects`.

---

## 2. Creating a German Model with English Identifiers

The SimTalk interpreter can process both German and English command names. To create a model with English identifiers:

1. Start Plant Simulation.
2. Select **Datei/File > Voreinstellungen/Preferences** before opening a model.
3. Click the tab **Allgemein/General** and select **English** as the language of the model.
4. Click **Create New Model** on the Start page.

Result: folders and object names are shown in English, while menus and dialog items remain German.

- Activate **Activate Listenfelder in der SimTalk-Sprache des Modells anzeigen / Display Drop-down List Boxes in the SimTalk Language of the Model** to see which values attributes and methods return.

```simtalk
Einzelstation.Bearbeitungszeit.Typ  -- German model language returns "Konst"
Station.ProcTime.Type               -- English model language returns "Const"
```

- The German Help and the **Show Attributes and Methods (F8)** window show English names next to German names.

---

## 3. Introducing Classes

Example: finding the optimum type of store for a production plant. You build several model variants of a single basic model (same production plant, modified store).

- **Conventional systems:** copy the basic model; every change must be repeated on each copy.
- **Plant Simulation:** **inherit** the basic model (the *parent* model) to get *child* models. A child model recognizes its parent, whereas a copied model knows nothing about its origin. A change made once in the parent propagates to all children (unless the setting was changed in the child).

---

## 4. Classes, Subclasses, and Instances

- **Class** — the template for an instance inserted into a Frame. All objects in the Class Library (built-in and user-defined) are class objects.
  - A class passes **all** of its properties to an **instance** derived from it.
  - A class passes to a **subclass** only those properties for which inheritance is still active.
- **Subclass** — an object in the Class Library that inherits *some but not all* properties from another class. Deactivate inheritance for specific dialog items to define subclass-only properties.
  - Create a subclass: right-click the class → **Derive** (places the object in `UserObjects`). Inheritance is active for all items; then change the identifying property.
  - Example: derive `Conveyor`, rename to `Conveyor_5m`, change length to 5 meters.
- **Instance** — an object inserted into a model by dragging a class object from the Class Library/Toolbox into a Frame.

**Creation shortcuts:**

- **Derive (subclass):** right-click → `Derive`, or hold **Ctrl + Shift** and drag the object to another location.
- **Duplicate (copy):** right-click → `Duplicate`, or hold **Ctrl** and drag the object.

**Class vs. origin relations:**

- The object inherits basic properties from its **class object** (the object in the Class Library it was instantiated from).
- The object inherits settings from its **origin object** (the object it was derived from), provided they were not changed locally.

> Inheritance only works from class to subclass/instance, **not** the other way around.

---

## 5. Replacing and Merging Objects with Drag-and-Drop

- **Replace an instance with a class:** hold **Alt** while dragging the class object onto the instance. E.g., replace a `Station` with an `AssemblyStation`. Plant Simulation preserves all connected Connectors but deletes all MUs on the object.
  - You can copy attribute values of the previous instance into the new instance; otherwise the new instance starts as if inserted from the Class Library (user-defined attributes and sensors are discarded).
  - Plant Simulation retains the existing name.
- **Merge classes:** hold **Alt** + left mouse button, drag the replacing object over the class to be replaced, and drop it.

---

## 6. Using Inheritance

Inheritance enables one class/object to incorporate data or behavior of another. Applications:

- **Specialization** — new data/behavior not part of the inherited class.
- **Extension** — additional data/behavior that could have been in the inherited class.
- **Code re-use** — reuse settings that already exist in another class.

The check box to the right of each dialog item toggles inheritance:

- Inheritance **on** — the object uses the value from its origin object. Changing the origin changes the derived object.
- Inheritance **off** — values only apply to the current object. The minus sign in the orange button assists vision-impaired users.

Example: derive `Station` in the Class Library and insert it into Frame `Model1`; derive `Model2` from `Model1`. The origin of the Station in `Model2` is the Station in `Model1`. Changing an inherited attribute value in `Model1` also applies to `Model2`.

> The object may display the current value only after clicking **Apply**.

---

## 7. Show Inheritance Relations in the Class Library

Right-click an object in the Class Library → **Show Inheritance** to open the dialog **Inheritance**, showing the paths of all objects derived from the selected object.

---

## 8. Show the Origin of an Object in the Class Library

Right-click an object in the Class Library → **Show Origin** to select the object it was instantiated/derived from. Repeat to move up the hierarchy until you reach the original origin.

---

## 9. Working with Classes in the Class Library

The Class Library shows built-in objects in a hierarchical folder structure. By default it contains folders for **MaterialFlow**, **Fluid**, **Resource**, **InformationFlow**, **MUs**, **UserInterface**, **UserObjects**, **Models**, and **Tools**.

- Derive child objects from built-in class objects or from classes you/co-workers build from scratch.
- Plant Simulation initially opens the Frame named `Model` in the **Models** folder.
- Add-in programs appear on the topmost level below **Basis** (which designates the Class Library itself; compare the anonymous identifier `basis`).

> **Recommendation:** Do not change built-in object standard settings; derive instead. Duplicated/derived objects are placed in `UserObjects`.

---

## 10. Configure the Class Library

You can configure the Class Library for new and existing models (lean library, uncluttered Toolbox). You can:

- Add/remove basic objects.
- Optimize the model — **Clean up class library** deletes unused classes.
- Add/remove libraries and tools.
- Add your own libraries.
- Update libraries.

Selecting **File > New Model** for the first time opens the **Manage Class Library** dialog by default.

### Add Basic Objects to the Class Library or Remove Them from It

1. In **Manage Class Library**, select the objects you need; clear check boxes for objects you do not need.
2. Click **Apply** to add/remove them.
3. (Optional) Select **Always Show This Dialog When You Open a New Model**.
4. Click **Apply to New Models** to apply settings to all new models.
5. Click **OK**.

### Add a Library or a Tool to or Remove it from the Class Library

1. Select one or several tools/libraries; clear check boxes for unneeded ones.
2. Click **Apply**. Plant Simulation adds the selected folder to the Class Library and the tool's toolbar to the Toolbox.

### Add a Library Which You Yourself Developed

1. Set the library location under **File > Preferences > Libraries Directories** (type several directories separated by a semicolon). The library manager checks these folders for the most up-to-date version.
2. The **Manage Class Library** dialog shows the library under **Additional Libraries** on the **Libraries** tab.
3. Click **OK** to add the library to the Class Library and Toolbox.

### Update a Library

1. If the library manager finds a newer version in **Libraries Directories**, the Message Bar shows a message → click **Manage Libraries** (outdated libraries shown in red).
2. In **Manage Class Library**, click the cell below **version**, select the newest version, click **OK**. A **Merge Report** shows added/deleted objects and affected instances.
3. Use **Update All Libraries** (only shown when a model is opened) to update all libraries; updates take effect when you click **OK** or **Apply**.

---

## 11. Create a Folder Structure for Your Simulation Model

Plan the Class Library structure before modeling. Installed libraries are located by default at:

```
C:\Program Files\Siemens\Tecnomatix Plant Simulation XX\Libraries
```

- Create new folders for your objects rather than storing them in built-in folders (avoids accidental changes to built-in objects).
- Use the folder `UserObjects` for this purpose; add objects to the **User Objects** tab in the Toolbox.

To create your own folder:

1. Right-click **Basis** (same level as built-in folders) or any folder (to nest inside it).
2. Select **New > Folder**.
3. Rename the folder (e.g., `ApplicationObjects`).
4. Recommended: create a subfolder for basic built-in objects (e.g., `BasicObjects`), making the library independent of model language and naming conventions.

---

## 12. Set the Root Folder for Your Simulation Model

Use the anonymous identifier `RootFolder` to avoid long paths when calling a shared Method directly from the Class Library.

- `RootFolder` is a folder in the Class Library whose attribute `RootFolder` is set to `true`. Plant Simulation searches for that folder starting with the class of the Method, upward in the hierarchy.

```simtalk
.ApplicationObjects.Transport.RootFolder := true
```

Alternatively, right-click the folder → **Show Attributes and Methods**, find `RootFolder`, double-click, type `true`, click **OK**. An uppercase **R** is added to the folder icon.

Example usage: designate `ApplicationObjects` as the RootFolder; access a central method on a Frame ribbon tab:

```simtalk
RootFolder.MyComponent.openComponent
```

`RootFolder` can also be used inside Methods containing controls.

---

## 13. Creating User-defined Classes

> **Recommendation:** Do not change built-in object standard settings. Instead, **duplicate** or **derive** the object in the Class Library. Duplicated/derived objects are placed in `UserObjects`.

### Create Your Own Classes

- **Class sharing all features with the parent:** right-click → **Derive** (or **Ctrl + Shift** drag), then rename. Also: select multiple objects in a Frame and drag them onto a folder in the Class Library.
- **Subclass sharing some features:** deactivate inheritance for the features to modify, then right-click → **Derive** (or **Ctrl + Shift** drag), then rename.
- **Class without an inheritance relation:** right-click → **Duplicate** (or **Ctrl** drag). This severs all inheritance relations; changes to the original are not passed on.

### Work with Your Own Classes

- Duplicated/derived objects are placed in `UserObjects`; double-click to edit properties, insert like built-in classes.
- Add your classes to the toolbar: drag the object class from `UserObjects` to the toolbar **UserObjects**.

---

## 14. Work with Folders, Frames, Objects in the Class Library

- **Move a folder:** click it, drag above the target position, drop.
- **Move into another folder:** **Shift** + drag to destination folder.
- **Copy into another folder:** **Ctrl** + drag to destination folder.
- **Merge folders:** **Alt** + drag the replacing folder onto the folder to be replaced (forms the superset and merges common classes).
- **Merge objects:** **Alt** + drag the replacing object onto the object to be replaced.
- **Arrange order:** click, hold, drag to the desired location within a folder.
- **Add icons to the toolbar:** drag the object to the toolbar name at the bottom of the folder.
- **Rename:** double-click → type into **Name**; press **F2**; select **Rename** on the context menu; or (for an open object) press **F4**.

---

## 15. Show the Contents of a Frame in the Class Library

The Class Library only shows *classes* of objects, not *instances* (objects inserted into a Frame in the Models folder). To view the hierarchical structure within a Frame, right-click the Frame in the Class Library → **Show Structure**.

---

## 16. Saving a Folder or an Object and Loading it into Another Model

You can load a user-defined object (single object or an entire Frame model) into other models. A **library** (`.pslib`) is a collection of objects with a version number you maintain and share, enabling you to update models or stay with an older version.

### Save a Folder as a Library

Right-click the folder → **Make Library** → opens the **Library Information** dialog:

1. Type the **Name**.
2. Type the **Version** (numbers and letters separated by periods).
3. Type a **Description**.
4. Click **OK**.

To use the library in other models, save it as a file: right-click the library → **Save/Load > Save Library As**. Store it under **File > Preferences > General > Libraries Directories** to make it available in **Manage Class Library**.

- Edit library info: right-click → **Edit Library Information**.
- **Alternative paths:** Plant Simulation identifies a library by its absolute path. Use alternative paths when renaming/moving the library folder, or to assign names in different languages.

```simtalk
$German$.Tools.EngpassAnalyse
```

Prefixing a path with a language between `$` signs (e.g., `$German$`) makes Plant Simulation use that path when loading the library into a model with that language. Separate multiple alternative paths with line breaks.

> When renaming a library, clicking **No** retains the library properties; clicking **Yes** makes it a normal folder.

> **Library constraints:** When inserting objects into a library Frame, use only objects from inside your library or other libraries; dependent libraries are saved into the `.pslib` file. Do **not** modify classes inside a library — **derive** them instead; the derived class is placed in a subfolder named `Public`.

### Save an Object or a Folder as an Object

- **Save an object:** right-click → **Save Object As** (saves `.psobj`, including all objects it uses with their folders and paths).
- **Save a folder:** right-click → **Save Folder As** (saves `.psobj` of the folder and all contents).

### Load an Object or a Folder into Your Simulation Model

Right-click any folder → **Load Object**. Plant Simulation loads the object with its paths, folders, subfolders, and classes at the **Basis** level.

- To preserve existing objects and discard duplicates: use **Load Object**, then select **Replace the Loaded Class with the One in the Class Library**.
- To port a lower version to a higher version: use **Update Class Library**.

If a name conflict occurs, the **Replace or Rename Class** dialog opens:

- **Replace the Loaded Class with the One in the Class Library** — merges inheritance hierarchies.
- **Replace All** — replaces all duplicate objects.
- **Rename and Keep the Duplicate Class** — enter a new name.

> When replacing a **Frame**, click **Replacement Mode** on the Frame ribbon tab, then select **Merge** or **Exchange**.

To compare uncertainly-identical classes, enter a new name and replace later: hold **Alt**, drag the replacing object over the object to be replaced.

You can also drag an `.psobj` file from Windows Explorer into the Class Library.

### Load an Object or a Folder into Another Folder

Right-click a folder → **Load Object into Folder** to load a `.psobj` (with its complete structure) into the selected folder without replacing existing objects. The tools in the **Tools** folder (e.g., BottleneckAnalyzer) use this technique with their own parametrized BasicObjects.

### Update the Class Library

1. Save the object as `.psobj` (**Save Object As**).
2. Right-click any folder → **Save/Load > Update Class Library** (loads into the Class Library at the Basis level).

The loaded file's classes are treated as the most recent; existing classes with the same name are replaced while instances are attached to the new class (preserving instance settings). Classes outside the direct hierarchy trigger a dialog to replace or rename duplicates.

---

## 17. Working with Objects in the Toolbox

The **Toolbox** holds toolbars with the objects of the Class Library. By default it shows toolbars **Material Flow, Fluids, Resources, Information Flow, User Interface, Mobile Units, Tools** (toolbars are at the bottom of their folders, next to the toolbar icon).

- Add-ins add their own tab/toolbar via **Manage Class Library**.
- **Add a toolbar:** right-click a folder → **New > Toolbar**.
- **Add an object to a toolbar:** drag it from the Class Library tree view to the toolbar.
- **Change a toolbar label:** select the toolbar icon at the bottom of the folder, press **F2**, enter a **Label**.
- **Open an object's class:** right-click → **Show Class**.

> After inserting an object from the Toolbox into a Frame, Plant Simulation automatically switches back to the tool **Select**.

### Add Objects to the Toolbox or Delete Them from It

- **Add single/multiple objects:** drag them from their folder to the toolbar.
- **Remove:** right-click → **Remove from Toolbar**.
- **Reorder icons:** drag a button to a different location.

### Copy Objects from Toolbar to Toolbar

1. Select the toolbar containing the object.
2. Right-click the target folder in the tree → **Show Structure** (opens the Structure window).
3. **Ctrl** + click the object on its toolbar in the Toolbox to select it in the tree.
4. Drag the object from the tree window to the toolbar icon in the Structure dialog.
