# Packaging and Sharing Models

## Preventing Message Dialogs

You can use the user-defined boolean attributes `ShowRuntimeAtEnd`, `AskForSaveModel`, and
`ShowHTMLatEnd` (for the distributed simulation) to prevent opening any message dialogs.

When you set the user-defined attribute `ShowHTMLatEnd` to `false`, Plant Simulation does not open the
Report at the end of the optimization.

To change the values of these attributes:

1. Click the GAWizard in the Frame into which you inserted it.
2. Press the F8 key.
3. Double-click the name of the attribute to change the value to `false`.

## Pack a Model and Send It to Another User

This section demonstrates how to pack and send a Plant Simulation model with Pack & Go to somebody
who does not have Plant Simulation installed on their computer.

When you create a Pack and Go model, you can select whether you want to restrict the permissions to a
Plant Simulation Viewer License. If the check box is not selected, you can pass the license to be used with
the start parameter `/L` to the Pack&Go application. This enables you to use features of the superior
license, provided this license is available. If you do not specify the start parameter, the freely available
Viewer license will be used.

```
/L
```

Pack and Go takes all files needed for starting the selected simulation model with a Plant Simulation
Viewer License, packs the files, and saves them as a self-extracting executable. You can send this packed
model to a customer, for example, who can open the model by double-clicking it.

> **Note**
> The Pack and Go executable does not include all Plant Simulation features, even if you do not restrict
> the license. As the executable should be as small as possible, the entire Plant Simulation installation is
> not included. This prevents you from using the OPCUA Interface or the Teamcenter Interface in Plant
> Simulation, for example.

### Steps to Pack and Send a Model

1. To start Pack and Go, select **File > Share > Pack and Go** in the Plant Simulation window.
2. To save your model before sending it, click **Yes** in the dialog that opens.
3. Navigate to the folder into which you want to save the model file. Enter a name and click **Save**.
4. Click **OK** after Pack-and-Go successfully created the package. Then, distribute the file, for example
   by sending it as an e-mail or by putting it in your Intranet, etc.

---

*Source: Plant Simulation Help 10-886 / 10-887. Unpublished work. © 2026 Siemens.*
