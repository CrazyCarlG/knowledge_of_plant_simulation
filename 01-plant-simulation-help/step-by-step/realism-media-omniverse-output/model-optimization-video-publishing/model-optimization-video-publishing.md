# Model Optimization, Video Recording, and Omniverse Output

Summary of the Plant Simulation help section covering how to optimize a finished model, record videos of the simulation, and visualize the model in NVIDIA Omniverse.

## Optimizing the Model

Optimize the model only after you are done creating and modifying it, since discarded data cannot be restored. Optimizing improves performance.

- Save the model under a different name before optimizing so you can return to the previous state if the optimized model reports errors or does not meet expectations.
- Click **Optimize Model** on the **Home** ribbon tab.
- Select which optimization to run. You can choose a single setting or any combination.

The available settings and their effects (demonstrated with `MyTurnplateShrinkwrapper3D.spp`):

- **Clean Up Class Library** — removes object classes from the Class Library that are not used in the model. This reduces the file size the most. You can later re-add missing objects with **Start > Manage Class Library**.
- **Optimize 3D Attribute Inheritance** — reduces file size only marginally in the example.
- **Optimize 3D Graphic Structure** — reduces file size only marginally in the example. Do not activate this if you want to edit your graphics later.
- Combining all settings produces the smallest file size, which is only marginally smaller than **Clean Up Class Library** alone.

### Optimizing the Hierarchy of an Animatable Object

In the **Show Graphic Structure** dialog, you can flatten the hierarchy of the animatable object for better runtime performance. The appearance does not change; only the graphic structure is flattened.

> **Note:** Because discarded data cannot be restored, only flatten the structure after you are done modeling the object. Only accept the result when the optimized graphic meets your intentions in both looks and structure.

## Recording a Video

The recorder creates an AVI file that any multimedia player can play. The **Video** ribbon tab provides all tools for recording and playing video.

### Select Video Settings

- **Start Simple Recording** — records Plant Simulation or the active 3D window in real time (one minute of physical time equals one minute of playback). Useful for demonstrating how to operate a model.
- **Start Simulation Recording** — records a simulation in scaled simulation time. The number of simulation-time minutes entered as *Real-time x [video]* corresponds to one minute of playback. Useful for showing realistic production behavior.

> **Note:** To prevent overwriting the last recorded AVI file, rename the output file before recording another video.

### Set Up the Scene for Recording

- Size the window to show only what the viewer needs.
- For 720p or 1080p video, set the recorded window size in the **Start Simple Recording** and **Start Simulation Recording** dialogs.
- A larger scene requires more processor time, animates more slowly, and produces a larger video file.
- Choose the position and angle first, then rotate and zoom the scene before starting.
- For simulation videos, you can automatically link recording with a camera animation by selecting **Play Camera Path**.

### Record the Video

- To start mid-simulation, run the animation to the desired time, then click to start recording.
- Reset the model if needed, then start the simulation.
- The recorder captures the contents of the currently active window. Avoid clicking into other windows or rolling over buttons (tooltips will appear in the video).
- You can cancel, pause, and stop recording with the ribbon-tab buttons.
- When recording ends, a dialog shows where the AVI file was saved. Click **OK** to continue.
- To view the video afterward, stop the simulation first, since it uses considerable resources.

### Play the Video

Click the play button on the **Video** ribbon tab; the default Windows media player plays the video. You can also edit it with a digital video application such as Adobe Premiere or Camtasia.

## Visualizing the Simulation Model in Omniverse

The Omniverse Connector is only active with a subscription for this optional product. To visualize a Plant Simulation 2606 model in Omniverse:

1. Start the Omniverse Connector.
2. Set up a new filesystem connection.
3. Establish a live connection to Omniverse.
4. Open the project in the **Live data** area of the NVIDIA Omniverse Composer and enhance the model's looks.
5. Optionally use the `MVA_WriteUSD` function.

### Start the Omniverse Connector

- Start Plant Simulation 2606 and open the Frame containing the model to export or connect live.
- On the **Edit** ribbon tab, click **Omniverse Connector**, which opens the **LiveConnect** window.

### Set Up a New Filesystem Connection

- Click the **Omniverse** node in the LiveConnect window and select **New Filesystem connection**.
- Create a new folder (or select an existing folder) in the File Browser.
- Enter a **Description** in the **Add new Filesystem connection** dialog.
- Click the data folder and select **Connect**, then select the data folder link.
- Type a file name into the **File name** box at the bottom of the LiveConnect window. The **Frames per second** setting is currently not used and can be left empty.

#### Export the Simulation in USD Format

After setting up the filesystem connection, export the running simulation to USD (Universal Scene Description) files:

1. Click **Export** so Omniverse creates the required usd files in the configured data folder.
2. Start the simulation you want to record.
3. Stop the simulation after recording everything you want to show.
4. Click **Export** again to stop the usd recording.
5. Plant Simulation creates a library folder and a usd file in the data folder.
6. Open the exported project in the NVIDIA Omniverse Composer to visualize it.

### Establish a Live Connection to Omniverse

- Make sure the Omniverse Nucleus Server is running.
- Right-click the **Omniverse** node in the LiveConnect window and select **New Nucleus connection**.
- Enter a **Description**, the IP address or server name of the Omniverse Nucleus computer, and the configured **Port** number.
- Right-click the new server node and select **Connect** to see the Omniverse data folder.
- Create a folder structure in the NVIDIA Omniverse Composer under the **Projects** folder.
- Right-click the **Library** folder in the project and select **Set System root folder**.
- Select the project folder and type a project name into the **File name** box.
- Click **Connect** and start the simulation in the Frame.
- Open the project in the **Live data** area of the Omniverse Composer.
- Stop the simulation in Plant Simulation, then terminate the Live connection by clicking **Connect** in the LiveConnect window.

Reference video: `https://support.sw.siemens.com/en-US/knowledge-base/KB000179496_EN_US`

### Use Omniverse with the Function MVA_WriteUSD

`MVA_WriteUSD` creates and activates a Nucleus connection, creates and activates a filesystem connection, or terminates a live/filesystem connection via SimTalk.

**Remarks** — before using `MVA_WriteUSD`, either:

- Load the Omniverse DLL via SimTalk:

```simtalk
loadLibrary(applicationHome + "PlantSimOmniverse.dll")
```

- Or manually start the Omniverse connection by clicking **Omniverse Connector** on the **Edit** ribbon tab.

**Type:** Function

**Syntax:**

```simtalk
MVA_WriteUSD("parameter string")
```

**Create and Activate a Nucleus Connection:**

```simtalk
var system_root_path:string = "/Projects/My_Project01/Library"
var output_path:string = "omniverse://127.0.0.1:80/Projects/My_Project01/myExport.live"
MVA_writeUSD(output_path+"?sysroot="+system_root_path)
```

**Parameter** — the parameter string specifies the project file path in the first section and the Omniverse system root folder in the second section, used for the USD export or a live connection:

```simtalk
MVA_writeUSD(<project file path>?systemroot=<system root path>)
```
