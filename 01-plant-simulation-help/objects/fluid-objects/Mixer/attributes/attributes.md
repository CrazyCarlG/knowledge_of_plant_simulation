# Attributes of the Mixer

The Mixer provides:

- The attributes listed in the table of contents to the left.
- The Attributes of the Fluid Objects.
- The Attributes of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the F8 key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```simtalk
MyMixer.OutflowRate := 1
```

- To get the value of an attribute, you might, for example, type:

```simtalk
print MyMixer.OutflowRate
posit := MyStation.Cont.XPos
```

---

## TimeUntilEntranceOpen [SimTalk] - Mixer

Returns the time until the entrance of the Mixer designated by `<Path>` opens again after the recovery time has elapsed.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.TimeUntilEntranceOpen → real`
- **Return Value:** The return value has the data type `real`.

```simtalk
print MyMixer.TimeUntilEntranceOpen
```

**See also:** EntranceOpen [SimTalk] - Mixer, Attributes of the Mixer

---

## IngredientCompleteCtrl [SimTalk]

Designates a Method object of the object designated by `<Path>`.

**Remarks**

Plant Simulation executes the Ingredient Complete Control when an ingredient of the recipe has completely arrived in the Mixer designated by `<Path>`. This way you can define/start any actions that need to take place in your simulation model via SimTalk.

The Ingredient Complete Control will also be called if the last ingredient or the last ingredients arrived at the same time at which the Mixer reached the Volume you specified.

- **Type:** Attribute
- **Syntax:** `<Path>.IngredientCompleteCtrl:method`
- **Assignment Value:** You can assign a value of data type object/method.

```simtalk
MyMixer.IngredientCompleteCtrl := &myIngredientCompleteCtrl
```

**See also:** Ingredient Complete Control, Volume [Mixer]

---

## MaterialsTable [SimTalk] - Mixer

Sets the MaterialsTable which contains the data of the different materials which the Mixer designated by `<Path>` can mix.

**Remarks**

If you specify -1 for a recipe in the column Product Amount of the MaterialsTable of the Mixer, Plant Simulation assumes the sum of all ingredients as the Product Amount. You only have to explicitly specify the Product Amount if mixing the ingredients increases or decreases the volume, i.e., if the Product Amount is not the sum of the ingredients.

- **Syntax:** `<Path>.MaterialsTable:path`
- **Assignment Value:** You can assign a value of data type path.

```simtalk
MyMixer.MaterialsTable := MyMaterialsTable
```

**See also:** Materials Table [Mixer]

---

## OutflowRate [SimTalk] - Mixer

Sets the Outflow Rate of the material which the Mixer designated by `<Path>` creates.

**Remarks**

The material then flows off through objects of type Pipe to the next object in the flow of materials.

The Outflow Rate is the amount of liters of the material that flows off in a second.

**Note**

The current Outflow Rate depends on the number of attached Pipes. Let's say you attached two Pipes, then the specified Outflow Rate flows through each one of these Pipes in case the Outflow Rate of the connected Pipes permits this.

If you just want to let the specified amount flow out of the object, attach a single Pipe and split that up into several Pipes later on.

- **Type:** Attribute
- **Syntax:** `<Path>.OutflowRate:real`
- **Assignment Value:** You can assign a value of data type real.

```simtalk
MyMixer.OutflowRate := 1
```

**See also:** Outflow Rate [Mixer]

---

## ProcTime [SimTalk] - Mixer

Sets the duration of the Processing Time of the Mixer designated by `<Path>`.

**Remarks**

The Processing Time is the time during which the Mixer transmutes materials.

- **Type:** Attribute
- **Syntax:** `<Path>.ProcTime:time`
- **Assignment Value:** You can assign a value of data type time.

```simtalk
MyMixer.ProcTime := 1:00:00 // one hour
```

**See also:** Processing Time [general description]

---

## Product [SimTalk]

Sets the name of the intermediate or of the finished Product, which the Mixer designated by `<Path>` is to produce by mixing the ingredients.

**Remarks**

The name of this Product has to be defined in the MaterialsTable.

- **Type:** Attribute
- **Syntax:** `<Path>.Product:string`
- **Assignment Value:** You can assign a value of data type string.

```simtalk
MyMixer.Product := "MyProduct"
```

**See also:** Product [text box] - Mixer, Materials Table [Mixer]

---

## ProductAmount [SimTalk]

Sets the amount of the intermediate or of the finished product which the Mixer designated by `<Path>` is to produce by mixing the ingredients.

**Remarks**

The default value -1 means that the finished product fully utilizes the volume of the Mixer. The product amount is measured in liters.

**Note**

If the product amount differs from the product amount which you typed into the MaterialsTable, Plant Simulation adjusts the amounts of the individual ingredients accordingly to ensure that the ratio of the ingredients is retained.

**Note**

If you specify -1 for a recipe into the column Product Amount of the MaterialsTable of the Mixer, Plant Simulation assumes the sum of all ingredients as the Product Amount. You only have to explicitly specify the Product Amount if mixing the ingredients increases or decreases the volume, i.e., if the Product Amount is not the sum of the ingredients.

- **Type:** Attribute
- **Syntax:** `<Path>.ProductAmount:real`
- **Assignment Value:** You can assign a value of data type real.

```simtalk
MyMixer.ProductAmount := 70
```

**See also:** Product Amount [text box], Materials Table [Mixer]

---

## RecoveryTime [SimTalk] - Mixer

Sets the duration of the Recovery Time of the Mixer designated by `<Path>`.

**Remarks**

The Recovery Time is the time which is required to flush and clean the Mixer and to prepare it for the next process.

- **Type:** Attribute
- **Syntax:** `<Path>.RecoveryTime:time`
- **Assignment Value:** You can assign a value of data type time.

Specify 0 to allow materials to enter continually.

```simtalk
MyMixer.RecoveryTime := 1:00:00
```

**See also:** Recovery Time [general description]

---

## Volume [SimTalk] - Mixer

Sets the Volume that is available for the ingredients or the product respectively in the mixing container of the Mixer designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.Volume:real`
- **Assignment Value:** You can assign a value of data type real.

```simtalk
MyMixer.Volume := 10
```

**See also:** Volume [Mixer], ContinuousMixer

---

## ContinuousMixer

Use the object ContinuousMixer to transmute the ingredients of the process into an intermediate or a finished product by mixing them.

**Description**

The ingredients can flow into the ContinuousMixer simultaneously from several preceding fluid objects.

- The ContinuousMixer only processes fluids if the product and the ingredients information is defined in the MaterialsTable.
