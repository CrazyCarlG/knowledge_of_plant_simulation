# Outdated SimTalk Names

Previous versions of Plant Simulation provided a number of SimTalk attributes, SimTalk read-only attributes, and SimTalk methods that the current version no longer supports.

The tables below list the outdated names (English and German) together with the attributes, read-only attributes, and methods that replace them, in alphabetical order.

## Working with outdated functions

- The command **Find Outdated Functions** on the **Debugger** tab finds all outdated functions in a model and shows them in a window.
- Plant Simulation shows outdated functions in the source code in a distinct color (see *Colors for Syntax Highlighting*).

---

## Reference: Outdated → Replacement (A–Z)

| Outdated English | Replaced by | Outdated German |
|---|---|---|
| `__checkForLicense` | `checkForLicense` [SimTalk] | `__checkForLicense` |
| `__setRandomSeedCounter` | `setRandomSeedCounter` [SimTalk] | `__setRandomSeedCounter` |
| `Active` | `ServerSocket` [SimTalk] | `Aktiv` |
| `Active` (Chart, GanttChart, SankeyDiagram) | `IsShown` [SimTalk] | `Chart Aktiv` |
| `ActReceiver` | no longer supported, EventController | `AktEmpfaenger` / `AktEmpfänger` |
| `animIcon` | `animation` [SimTalk] | `animIcon` |
| `animMU` | `animation` [SimTalk] | `animBE` |
| `AttributType` | `AttributeType` [SimTalk] – material flow objects | `AttributType` |
| `AutoFormat` | no longer supported, Sorter | `AutoFormat` |
| `Available` | `Failed` [SimTalk] – material flow objects, `Pause` [SimTalk] – material flow objects, `Unplanned` [SimTalk] – material flow objects | `Verfuegbar` / `Verfügbar` |
| `BarMode` | `DisplayType` [SimTalk] | `BalkenModus` |
| `BatChargeCnt` | `StatBatChargeCount` [SimTalk] | `BatAnzLaden` |
| `BatChargeStat` | `StatBatChargePortion` [SimTalk] | `BatLadeStat` |
| `blockingPercentage` | `StatBlockingPortion` [SimTalk] | `blockiertAnteil` |
| `BlockTimeStat` | no longer supported, MUs | `Blockzeitstat` |
| `BookPnt` | `BookPntLRelative` [SimTalk] | `BuchPkt` |
| `BookPntH` | `BookPntHRelative` [SimTalk] | `BuchPktH` |
| `BookPntL` | `BookPntLRelative` [SimTalk] | `BuchPktL` |
| `BookPntW` | `BookPntWRelative` [SimTalk] | `BuchPktW` |
| `BreakCtrl` | `PauseCtrl` [SimTalk] | `BreakCtrl` |
| `BumpCtrl` | `CollisionCtrl` [SimTalk] – Transporter | `BumpCtrl` |
| `Bumped` | `Collided` [SimTalk] | `Bumped` |
| `ChannelID` | no longer supported | `KanalID` |
| `closeFile` | no longer supported | `schliesseDatei` |
| `columnwise` | no longer supported | `Spaltenorientiert` |
| `commonFormat` | `setCommonFormat` [SimTalk], `setCommonFormatData` [SimTalk] – DataTable | `gemeinsamesFormat` |
| `connect3DViewer` | no longer supported | `verbinde3DViewer` |
| `ConnectTo3D` | no longer supported | `Mit3DVerbinden` |
| `continue` | `Stopped` [SimTalk] – MUs `:= false` | `fahren` |
| `copyToClipboard` | no longer supported | `kopiereInZwischenablage` |
| `create` | `createNestedList` [SimTalk] – local variable | `create` |
| `createAttribute` | `createAttr` [SimTalk] | `createAttribute` |
| `createBuildingBlock` | `derive` [SimTalk], `duplicate` [SimTalk] | `erzeugeBaustein` |
| `createObject` | `derive` [SimTalk], `duplicate` [SimTalk] | `erzeugeObjekt` |
| `creationTable` | `getWorkersToCreateTableRow` [SimTalk] – WorkerPool | `erzeugungsTabelle` |
| `Ctrl` | `Control` [SimTalk] – sensors | `Ctrl` |
| `CurAmount` | `CurrentAmount` [SimTalk] – Mixer | `CurAmount` |
| `CurrImg` | no longer supported | `CurrImg` |
| `cutRow` | `remove` [SimTalk] – DataList | `cutRow` |
| `deleteAttribute` | `deleteAttr` [SimTalk] | `deleteAttribute` |
| `deleteBuildingBlock` | `deleteObject` [SimTalk] | `vernichteBaustein` |
| `deleteBreakpoint` | no longer supported, EventController | `vernichteHaltepunkt` |
| `DeleteMUsOnReset` | no longer supported, EventController | `BEsBeimResetLöschen` |
| `DestList` | `FwDestList` [SimTalk] | `Zielliste` |
| `DisplayMode` | `DisplayType` [SimTalk] | `Typ` |
| `DisplayText` | `Text` [SimTalk] – Comment | `Anzeige` |
| `DismantleList` | `DismantleTable` [SimTalk] | `DemontageListe` |
| `DistanceIsBelowLimit` | `DistanceObjectBelowLimit` [SimTalk] | `AbstandUnterschritten` |
| `drawLineSegment` | no longer supported | `zeichneLinienAbschnitt` |
| `emptyPercentage` | `StatEmptyPortion` [SimTalk] | `leerAnteil` |
| `EntryAutoFormat` | no longer supported, FlowControl | `AutoFormatEingang` |
| `entryOpen` | `EntranceOpen` [SimTalk] – material flow objects | `entryOpen` |
| `EvaluationInterface` | no longer supported, GAOptimization | `BewertungsSchnittstelle` |
| `executeSilentOld` | `executeSilent` [SimTalk] | `executeSilentOld` |
| `ExitAutoFormat` | no longer supported, FlowControl | `AutoFormatAusgang` |
| `ExitForNextEnteringMU` | `ExitForMU` [SimTalk] | `AusgangFürEintretendesBE` |
| `exitSimple` | `exitApplication` [SimTalk] | `beendeSimple` |
| `ExitStrategyPercentageList` | `ExitStrategyPercentageValues` [SimTalk] – material flow objects | `AusgangsStrategieProzentListe` |
| `ExitStrategyRandomPercentageList` | `ExitStrategyPercentageValues` [SimTalk] – material flow objects | `AusgangsStrategieZufallProzentListe` |
| `ExitStrategySequenceList` | `ExitStrategySequence` [SimTalk] | `AusgangsStrategieReihenfolgeListe` |
| `exportData` | no longer supported, Plotter | `exportiereWerte` |
| `exp` | no longer supported, Exporter, Worker | `exp` |
| `Expression` | `Path` [SimTalk] – Source | `Ausdruck` |
| `externCall` | no longer supported | `externCall` |
| `F3DBlock3DUpdate` | no longer supported | `F3DBlock3DUpdate` |
| `FailImporterActive` | `FailImp.Active` [SimTalk] – importer | `StoerImporterAktiv` / `StörImporterAktiv` |
| `failPercentage` | `StatFailPortion` [SimTalk] | `stoerungsAnteil` |
| `failRelToWorkTime` | `Failures.<NameOfFailureProfile>.Mode` [SimTalk] – failure profile | `FehlerArbeitszeitbezogen` |
| `FaultTimeStat` | `StatFailTimePortion` [SimTalk] | `Gestoertzeitstat` |
| `FileCursor` | no longer supported | `DateiZeiger` |
| `freeEntry` | `EntranceFree` [SimTalk] | `freeEntry` |
| `generationTable` | `creationTable` [SimTalk] – Source | `generationTable` |
| `GenerationTableActive` | `creationTable` [SimTalk] – Source | `GenerationTableActive` |
| `getAdministeredExporters` | `AdministeredExporters` [SimTalk] | `getAdministeredExporters` |
| `getAttributList` | `getAttributeList` [SimTalk] – Converter, `setAttributeList` [SimTalk] – Converter | `getAttributList` |
| `getBreakpointCondition` | no longer supported, EventController | `holeHaltepunktBedingung` |
| `getBreakpointReceiver` | no longer supported, EventController | `holeHaltepunktEmpfaenger` / `holeHaltepunktEmpfänger` |
| `getBreakpointSender` | no longer supported, EventController | `holeHaltepunktSender` |
| `getBreakpointStartTime` | no longer supported, EventController | `holeHaltepunktStartZeit` |
| `getBreakpointStopTime` | no longer supported, EventController | `holeHaltepunktStopZeit` |
| `getBreakpointTraceFile` | no longer supported, EventController | `holeHaltepunktTraceFile` |
| `getBreakpointType` | no longer supported, EventController | `holeHaltepunktTyp` |
| `getBValue`<br>`getRValue`<br>`getGValue` | `getColor` [SimTalk] | `holeBWert`<br>`holeRWert`<br>`holeGWert` |
| `getColumnNumber` | `getColumnNo` [SimTalk] | `holeSpaltenNr` |
| `getCreationTable` | `getWorkersToCreateTable` [SimTalk] | `holeErzeugungsTabelle` |
| `getCurrIcon` | no longer supported | `getCurrIcon` |
| `getCurrIconNo` | no longer supported | `getCurrIconNo` |
| `getCursor` | `CursorX` [SimTalk], `CursorY` [SimTalk] | `holeZeiger` |
| `getCursorX` | `CursorX` [SimTalk] | `getCursorX` |
| `getCursorY` | `CursorY` [SimTalk] | `getCursorY` |
| `getData` | no longer supported, Dialog | `holeDaten` |
| `getFileCursor` | no longer supported | `holeDateiZeiger` |
| `getFileName` | `FileName` [SimTalk] – FileInterface | `holeDateiName` |
| `getFormatData` | `copyFormatTo` [SimTalk] | `holeFormatDaten` |
| `getItems` | `Items` [SimTalk] – DropDownList | `holeEinträge` |
| `getListIndex` | `getIndex` [SimTalk] | `holeListIndex` |
| `getLoadedExternal` | `getLoadedLibrary` [SimTalk] | `getLoadedExternal` |
| `getLocalTime` | `sysDate` [SimTalk] | `getLocalTime` |
| `getLockoutZoneList` | `AssignedLockoutzones` [SimTalk] | `holeSchutzkreisListe` |
| `getMaxDepthOfCalls` | no longer supported | `holeMaxAufruftiefe` |
| `getMaxNumberOfCallChains` | no longer supported | `holeMaxAnzAufrufketten` |
| `getMaxSuspendedMethods` | no longer supported | `holeMaxSuspendierteMethoden` |
| `getObjects` | `Objects` [SimTalk] – LockoutZone | `holeObjekte` |
| `getPopIndex` | no longer supported | `holePopIndex` |
| `getRouteToDestination` | `getRoute` [SimTalk] – Transporter | `holeRouteZuZiel` |
| `getRowNumber` | `getRowNo` [SimTalk] | `holeZeilenNr` |
| `getServices` | `Services` [SimTalk] – Worker | `holeDienste` |
| `getSupportedServices` | `SupportedServices` [SimTalk] | `holeUnterstützteDienste` |
| `getTabIndex` | `getIndex` [SimTalk] | `holeRegisterkartenIndex` |
| `getTriggerList` | `Trigger` [SimTalk] | `holeTriggerListe` |
| `getValue` | `value` [SimTalk] – TimeSequence | `holeWert` |
| `getValue` [Python] | `get` [SimTalk] | `getValue` [Python] |
| `getWorkerCreationTable` | `getWorkersToCreateTableRow` [SimTalk] – WorkerPool | `holeWerkerErzeugungsTabelle` |
| `graphicsMode` | `ChartType` [SimTalk] | `Grafikmodus` |
| `gridlines` | `getAnnotations` [SimTalk], `setAnnotations` [SimTalk] | `Gitterlinien` |
| `Height` | `ObjectHeight` [SimTalk] – Button | `Höhe` |
| `hideLockBBL` | no longer supported | `hideLockBBL` |
| `homeDrivingTime` | `StatHomeDrivingTime` [SimTalk] | `Heimfahrzeit` |
| `HTMLHelp` | no longer supported | `HTMLHelp` |
| `IconAngle` | no longer supported | `BildWinkel` |
| `IconRotation` | no longer supported | `BildDrehung` |
| `ImporterActive` | `Imp.Active` [SimTalk] – importer | `ImporterAktiv` |
| `ImportTable` | no longer supported, XMLInterface | `ImportTabelle` |
| `inactive` | `Pause` [SimTalk] – material flow objects | `inactive` |
| `increment` | `+=` operator in SimTalk | `inkrementiere` |
| `indexXDim` | `XDimIndex` [SimTalk] | `indexXDim` |
| `indexYDim` | `YDimIndex` [SimTalk] | `indexYDim` |
| `InheritHasInitValue` | `inheritAttribute` [SimTalk] – user-defined attribute, `getAttribute` [SimTalk] – user-defined attribute, `setAttribute` [SimTalk] – user-defined attribute | `ErbeHatAnfangsWert` |
| `InheritInitValue` | `inheritAttribute` [SimTalk] – user-defined attribute, `getAttribute` [SimTalk] – user-defined attribute, `setAttribute` [SimTalk] – user-defined attribute | `ErbeAnfangsWert` |
| `inheritPos` | `inheritAttribute` [SimTalk] – `object("Coordinate3D")` | `inheritPos` |
| `inheritPosition` | `inheritAttribute` [SimTalk] – `object("Coordinate3D")`, `_3D.inheritAttribute` [SimTalk] | `erbePosition` |
| `inheritSizeAndOrientation` | `inheritAttribute` [SimTalk] – object, `_3D.inheritAttribute` [SimTalk] | `erbeGrößeUndAusrichtung` |
| `InheritsProgram` | `getAttribute` [SimTalk] – object | `ErbtProgramm` |
| `InheritValue` (user-defined attribute) | `inheritAttribute` [SimTalk] – user-defined attribute, `getAttribute` [SimTalk], `setAttribute` [SimTalk] | `erbeWert` |
| `InheritValue` (Variable) | `Variable.inheritAttribute` [SimTalk] – `object("Value")` | `erbeWert` |
| `InitVal` | `InitValue` [SimTalk] – Variable | `InitVal` |
| `InternalClassName` | `InternalClassType` [SimTalk] | `InternalClassName` |
| `Interval` | `Distance` [SimTalk] | `Intervall` |
| `IntTimeStat` | no longer supported | `UbzeitStat` |
| `is64BitApplication` | no longer supported | `is64BitApplication` |
| `ItemID` | `TargetFolder` [SimTalk] | `ElementID` |
| `lineSeparator` | no longer supported | `zeilenTrennzeichen` |
| `list` table for the Empirical Distributions | — | `liste` |
| `loadExternal` | no longer supported | `loadExternal` |
| `markers` | no longer supported | `Markierungen` |
| `MatrixLoadBay` | `LoadBayType` [SimTalk] | `Matrixladeflaeche` |
| `maxNumMU` | `StatMaxNumMU` [SimTalk] – MUs | `maxAnzahlBes` |
| `methcall` | `executeIn` [SimTalk] | `methaufr` |
| `mirrorHorizontally` | no longer supported | `spiegelnHorizontal` |
| `mirrorVertically` | no longer supported | `spiegelnVertikal` |
| `ModifyStructure` | `LockStructure` [SimTalk] | `StrukturAendern` / `StrukturÄndern` |
| `move` | no longer supported, PickAndPlace-Robot | `umlagern` |
| `MovingAcceleration` | `CurrentAcceleration` [SimTalk] – Conveyor | `Bewegungsbeschl` |
| `MovingSpeed` | `CurrentSpeed` [SimTalk] – Conveyor | `Bewegungsgeschw` |
| `MU` | `Alpha` [SimTalk], Gamma distribution, Weibull distribution | `MU` |
| `newCallChain` | `executeNewCallChain` [SimTalk] | `neueAufrufkette` |
| `numAttributes` | `NumAttr` [SimTalk] | `numAttributes` |
| `numIn` | `StatNumIn` [SimTalk] – material flow objects | `anzahlEin` |
| `numOut` | `StatNumOut` [SimTalk] – material flow objects | `anzahlAus` |
| `open3DWindow` | `_3D.openWindow` [SimTalk] | `öffne3DFenster` |
| `openURLInMainWindow` | no longer supported | `openURLInMainWindow` |
| `orderEmptyTime` | `StatOrderEmptyTime` [SimTalk] | `AuftragLeerZeit` |
| `orderOccTime` | `StatOrderOccTime` [SimTalk] | `AuftragBelegtZeit` |
| `paste` | `insertList` [SimTalk] | `einfuegeListe` |
| `pasteColumn` | `insertColumn` [SimTalk] | `einfuegenSpalte` / `einfuegeSpalte` |
| `pasteRow` | `insertRow` [SimTalk] | `einfuegenZeile` |
| `PauseTimeStat` | `StatPauseTimePortion` [SimTalk] | `PausenzeitStat` |
| `pausingPercentage` | `StatPausingPortion` [SimTalk] | `pausenAnteil` |
| `ProductionTimeStat` | `StatProductionTimePortion` [SimTalk] | `Produktionszeitstat` |
| `promptMessage` | `messageBox` [SimTalk] | `promptMessage` |
| `putRouteToDestinationIntoTable` | `setRoute` [SimTalk] – Transporter | `setzeRouteZuZielInTabelle` |
| `read` | `[row]` [SimTalk] | `lesen` |
| `readFileRow` | `readFile` [SimTalk] – lists | `leseDateiZeile` |
| `relativeOccupation` | `StatRelativeOccupation` [SimTalk] – material flow objects | `relativeBelegung` |
| `relativeOccupationIR` | `StatRelativeOccupationIR` [SimTalk] – material flow objects | `relativeBelegungUB` |
| `resetClipboard` | no longer supported | `zwischenablageRücksetzen` |
| `resetInitBox` | no longer supported | `resetInitBox` |
| `Retardation` | `Deceleration` [SimTalk] – Conveyor | `Verzoegerung` |
| `Sampler` | `Mode` [SimTalk] – Chart | `Sampler` |
| `scaling` | `_3D.Scale` [SimTalk] | `Skalierung` |
| `Selected` | `_3D.Selected` [SimTalk] | `Selektiert` |
| `SeedReset` | no longer supported | `SeedReset` |
| `SegmentsTable` | no longer supported | `SegmenteTabelle` |
| `sendMessage` | `_3D.Selected` [SimTalk] | `sendeNachricht` |
| `set3DRotation` | `_3D.Rotation` [SimTalk] | `setze3DRotation` |
| `setActive` | `endPause` [SimTalk] – material flow objects | `arbeiten` |
| `setAnimationRefreshRate` | no longer supported | `setAnimationRefreshRate` |
| `setBreakpointCondition` | no longer supported, EventController | `setzeHaltepunktBedingung` |
| `setBreakpointReceiver` | no longer supported, EventController | `setzeHaltepunktEmpfänger` |
| `setBreakpointSender` | no longer supported, EventController | `setzeHaltepunktSender` |
| `setBreakpointStartTime` | no longer supported, EventController | `setzeHaltepunktStartZeit` |
| `setBreakpointStopTime` | no longer supported, EventController | `setzeHaltepunktStopZeit` |
| `setBreakpointTraceFile` | no longer supported, EventController | `setzeHaltepunktTraceFile` |
| `setBreakpointType` | no longer supported, EventController | `setzeHaltepunktTyp` |
| `setCreationTable` | `setWorkersToCreateTable` [SimTalk] | `setzeErzeugungsTabelle` |
| `setCurrIcon` | no longer supported | `setzeBild` |
| `setDim` | no longer supported | `setzeDim` |
| `setFileCursor` | no longer supported | `setzeDateiZeiger` |
| `setFileName` | `FileName` [SimTalk] – FileInterface | `setzeDateiName` |
| `setFormatData` | `copyFormatTo` [SimTalk] | `setzeFormatDaten` |
| `setInactive` | `startPause` [SimTalk] – material flow objects | `setInactive` |
| `setItems` | `Items` [SimTalk] – DropDownList | `setzeEinträge` |
| `setLabelFont` | `LabelFont` [SimTalk] | `setzeSchriftAchsen` |
| `setListIndex` | `setIndex` [SimTalk] | `setzeListIndex` |
| `setListText` | `setList` [SimTalk] | `setzeListText` |
| `setName` [user-defined attribute] | `Name` [SimTalk] – general description, `Name` [SimTalk] – failure profile | `setzeName` |
| `setObjects` | `Objects` [SimTalk] – LockoutZone | `setzeObjekte` |
| `setParam` | `setTypeAndAttr` [SimTalk] | `setzeParam` |
| `setPopIndex` | no longer supported | `setzePopIndex` |
| `setPopText` | no longer supported | `setzePopText` |
| `setRGB` | `setColor` [SimTalk] | `setzeRGB` |
| `setServices` | `Services` [SimTalk] – Worker | `setzeDienste` |
| `setSubtitleFont` | `SubtitleFont` [SimTalk] | `setzeSchriftUntertitel` |
| `setSupportedServices` | `SupportedServices` [SimTalk] | `setzeUnterstützteDienste` |
| `setTabIndex` | `setIndex` [SimTalk] | `setzeRegisterkartenIndex` |
| `setTableFont` | `TableFont` [SimTalk] | `setzeSchriftTabelle` |
| `setTabText` | `setList` [SimTalk] | `setzeRegisterkartenText` |
| `setText` | `setCaption` [SimTalk] | `setzeText` |
| `setTitleFont` | `TitleFont` [SimTalk] | `setzeSchriftÜberschrift` |
| `setTriggerList` | `Trigger` [SimTalk] | `setzeTriggerListe` |
| `Setup` | `ResSetup` [SimTalk] – material flow objects | `Ruestet` |
| `SetUpAlways` | no longer supported | `ImmerRüsten` |
| `SetupImp` | `_Attributes` of the Importer | `RuestImp` |
| `setupPercentage` | `StatSetUpPortion` [SimTalk] | `ruestAnteil` |
| `SetUpTimeStat` | `StatSetUpTimePortion` [SimTalk] | `Ruestzeitstat` |
| `setValue` | `Value` [SimTalk] – Checkbox | `setzeWert` |
| `setValue` [Python] | `set` [SimTalk] | `setValue` [Python] |
| `setWorkerCreationTable` | `creationTable` [SimTalk] – Source | `setzeWerkerErzeugungsTabelle` |
| `SHGetFolderPath` | `SHGetKnownFolderPath` [SimTalk] | `SHGetFolderPath` |
| `ShowStandardMenus` | no longer supported | `ZeigeStandardmenues` / `ZeigeStandardmenüs` |
| `ShowToolbar` | no longer supported | `ZeigeSymbolleiste` |
| `simpleHome` | no longer supported | `simpleHome` |
| `SmartAnimation` | no longer supported | `SmartAnimation` |
| `Start` | `LowerBound` | `Start` |
| `Speed` | no longer supported, EventController | `Geschwindigkeit` |
| `startWithoutAnimation` | `start` [SimTalk] – EventController | `startOhneAnimation` |
| `StatBlockingExpCount` | no longer supported | `StatBlockiertExpAnzahl` |
| `StatBlockingExpDelta` | no longer supported | `StatBlockiertExpDelta` |
| `StatBlockingExpMu` | no longer supported | `StatBlockiertExpMu` |
| `StatBlockingExpPortion` | no longer supported | `StatBlockiertExpAnteil` |
| `StatBlockingExpTime` | no longer supported | `StatBlockiertExpZeit` |
| `StateFailed` | `Failed` [SimTalk] – Frame | `StatusGestört` |
| `StatePause` | `Pause` [SimTalk] – Frame | `StatusPause` |
| `StatExporterWorkingPortion` | `StatExporterOperationalPortion` [SimTalk] | `StatExporterArbeitendAnteil` |
| `StatExporterWorkingTime` | `StatExporterOperationalTime` [SimTalk] | `StatExporterArbeitendZeit` |
| `StatisticsOn` | `ProdStatOn` [SimTalk] | `StatistikAn` |
| `StatStoppedDurationDelta` | `StatStoppedDelta` [SimTalk] – material flow objects | `StatStoppedDurationDelta` |
| `StatStoppedDurationMu` | `StatStoppedMu` [SimTalk] – material flow objects | `StatStoppedDurationMu` |
| `StatStoppedDurationSum` | `StatStoppedTime` [SimTalk] | `StatStoppedDurationSum` |
| `StatWaitingExpCount` | `StatExporterUnplannedCount` [SimTalk] | `StatWarteExpAnzahl` |
| `StatWaitingExpDelta` | `StatExporterUnplannedDelta` [SimTalk] | `StatWarteExpDelta` |
| `StatWaitingExpMu` | `StatExporterUnplannedMu` [SimTalk] | `StatWarteExpMu` |
| `StatWaitingExpPortion` | `StatExporterUnplannedPortion` [SimTalk] | `StatWarteExpAnteil` |
| `StatWaitingExpTime` | `StatExporterUnplannedTime` [SimTalk] | `StatWarteExpZeit` |
| `stDev` | `standardDeviation` [SimTalk] | `stAbw` |
| `stDevAttr` | `standardDeviationAttr` [SimTalk] | `stAbwAttr` |
| `stop` | `Stopped` [SimTalk] – material flow objects | `anhalten` |
| `Stop` | `UpperBound` [SimTalk] – distribution parameter | `Stop` |
| `StorageTimeStat` | `StatStorageTimePortion` [SimTalk] | `LagerzeitStat` |
| `TransportTimeStat` | `StatTransportTimePortion` [SimTalk] | `Transportzeitstat` |
| `unloadExternal` | no longer supported | `unloadExternal` |
| `update3D` | `_3D.updateAll`, `_3D.updateNew`, `_3D.updateMovables`, `_3D.updateConnections`, `_3D.updatePositions` | `update3D` |
| `UseActiveWorkspace` | `ImportMode` [SimTalk] | `ActiveWorkspaceVerwenden` |
| `v` | `Speed` [SimTalk] – Turnplate | `v` |
| `Val` | `Value` [SimTalk] – Checkbox | `Val` |
| `version` | `applicationVersion` [SimTalk] | `version` |
| `waitingPercentage` | `StatWaitingPortion` [SimTalk] | `warteAnteil` |
| `WaitTimeStat` | `StatWaitTimePortion` [SimTalk] | `WartezeitStat` |
| `Width` | `ObjectWidth` [SimTalk] – Button | `Breite` |
| `WorkersCanBeam` | `WorkersTravelMode` [SimTalk] | `WerkerKönnenBeamen` |
| `workingPercentage` | `StatWorkingPortion` [SimTalk] | `arbeitsAnteil` |
| `WorkTimeStat` | `StatWorkTimePortion` [SimTalk] | `Bearbzeitstat` |
| `writeString` | `write` [SimTalk] – FileInterface | `writeString` |
| `YPosOrigin3D` | no longer supported | `YPosUrsprung3D` |
| `z_exp` | Distribution Functions, z_ functions (`Negexp` [distribution], `z_negexp` [SimTalk]) | `z_exp` |
| `ZPos` | `Coordinate3D` [SimTalk] – general description | `Zpos` |

---

## Reference: `_3D.*` outdated names

| Outdated English | Replaced by | Outdated German |
|---|---|---|
| `_3D.acceptRotation` | no longer supported | `_3D.übernehmeDrehung` |
| `_3D.acceptScale` | no longer supported | `_3D.übernehmeSkalierung` |
| `_3D.activateMaterialWithColor` | no longer supported | `_3D.aktiviereMaterialMitFarbe` |
| `_3D.addGraphicTransformation` | `_3D.getGraphic` [SimTalk], `addGraphicTransformation` [SimTalk] | `_3D.fügeGrafiktransformationHinzu` / `3D.fuegeGrafiktransformationHinzu` |
| `_3D.AutoGraphicsAmbientColor` | `_3D.MaterialAmbientColor` [SimTalk] | `_3D.Autografikumgebungslicht` |
| `_3D.AutoGraphicsDiffuseColor` | `_3D.MaterialDiffuseColor` [SimTalk] | `3D.AutografikDiffuseFarbe` |
| `_3D.AutoGraphicsEmissiveColor` | `_3D.MaterialEmissiveColor` [SimTalk] | `_3D.AutografikSelbstleuchtendeFarbe` |
| `_3D.AutoGraphicsOverride2D` | `MaterialActive` [SimTalk] | `_3D.AutografikMaterialStatt2D` |
| `_3D.AutoGraphicsShininess` | `_3D.MaterialShininess` [SimTalk] | `3D.Autografikglanz` |
| `_3D.AutoGraphicsSpecularColor` | `_3D.MaterialSpecularColor` [SimTalk] | `_3D.AutografikGlänzendeFarbe` |
| `_3D.AutoGraphicsTransparency` | `_3D.MaterialTransparency` [SimTalk] | `_3D.Autografiktransparenz` |
| `_3D.BoardDepth` | `BayDepth` [SimTalk] | `_3D.Brettiefe` |
| `_3D.cancelRedirection` | `_3D.AnimationObject` [SimTalk] | `_3D.hebeUmleitungAuf` |
| `_3D.ChildrenSelection` | no longer supported | `_3D.Kinderselektion` |
| `_3D.closeAllWindows` | `closeAllWindows` [SimTalk] | `_3D.schließeAlleFenster` |
| `_3D.connectLengths` | no longer supported | `_3D.verbindeLängen` |
| `_3D.connectPositions` | no longer supported | `_3D.verbindePositionen` |
| `_3D.connectPositionsAndRotations` | no longer supported | `_3D.verbindePositionenUndDrehungen` |
| `_3D.countGraphics` | `_3D.getGraphic` [SimTalk].`NumGraphics` [SimTalk] | `_3D.zähleGrafiken` |
| `_3D.createBox` | `createBox` [SimTalk] | `_3D.erzeugeKasten` |
| `_3D.createCone` | `createConeFrustum` [SimTalk] | `_3D.erzeugeKegel` |
| `_3D.createConeFrustum` | `createConeFrustum` [SimTalk] | `_3D.erzeugeKegelstumpf` |
| `_3D.createCuboid` | `createCuboid` [SimTalk] | `_3D.erzeugeQuader` |
| `_3D.createCylinder` | `createConeFrustum` [SimTalk] | `_3D.erzeugeZylinder` |
| `_3D.createIndexedFaceSet` | `createIndexedFaceSet` [SimTalk] | `_3D.erzeugeFlächengrafik` |
| `_3D.createIndexedLineSet` | `createIndexedLineSet` [SimTalk] | `3D.erzeugeDrahtgitter` |
| `_3D.createMissingViewerObjects` | no longer supported | `_3D.erstelleFehlendeViewerobjekte` |
| `_3D.createPicture` | `createPicture` [SimTalk] | `_3D.erzeugeBild` |
| `_3D.createSphere` | `createSphere` [SimTalk] | `_3D.erzeugeKugel` |
| `_3D.createText` | `createText` [SimTalk] | `_3D.erzeugeText` |
| `_3D.createTiledPlate` | `createTiledPlate` [SimTalk] | `_3D.erzeugeGekacheltePlatte` |
| `_3D.CurvePrecision` | no longer supported | `_3D.Kurvengenauigkeit` |
| `_3D.deleteGraphic` | `_3D.getGraphic` [SimTalk].`deleteGraphic` [SimTalk] | `_3D.vernichteGrafik` |
| `_3D.deletePlainGraphics` | `_3D.deleteGraphicGroupContent` [SimTalk] | `_3D.vernichteReineGrafiken` |
| `_3D.disconnectLengths` | no longer supported | `_3D.trenneLängenverbindung` |
| `_3D.disconnectPositions` | no longer supported | `_3D.trennePositionsverbindung` |
| `_3D.disconnectPositionsAndRotations` | no longer supported | `_3D.trennePositionsUndDrehungsverbindung` |
| `3D.disconnectRotations` | no longer supported | `_3D.trenneDrehungsverbindung` |
| `_3D.EstimatedBlockAnimationTime` | `_3D.CameraAnimations.AnimationTimeBlock` [SimTalk], `_3D.SelfAnimations.AnimationTimeBlock` [SimTalk] | `_3D.VoraussichtlicheBlockanimationszeit` |
| `_3D.EstimatedTotalAnimationTime` | `_3D.SelfAnimations.AnimationTimeTotal` [SimTalk], `_3D.CameraAnimations.AnimationTimeTotal` [SimTalk] | `_3D.VoraussichtlicheGesamtanimationszeit` |
| `_3D.ExtPolycurve` | `_3D.getExtSegments` [SimTalk], `_3D.setExtSegments` [SimTalk] | `_3D.ExtPolykurve` |
| `_3D.exportAsBitmap` | `_3D.exportModelingViewBitmap` [SimTalk], `_3D.exportPlanningViewBitmap` [SimTalk] | `_3D.exportiereAlsBitmap` |
| `_3D.ExtSpline` | no longer supported | `_3D.ExtSpline` |
| `_3D.flattenGraph` | `_3D.getGraphic` [SimTalk].`optimizeByStructureFlattening` [SimTalk] | `_3D.vereinfacheGrafik` |
| `_3D.generateEllipse` | `F3DgenerateEllipse` [SimTalk] | `_3D.erzeugeEllipse` |
| `_3D.generateHollowEllipse` | `F3DgenerateHollowEllipse` [SimTalk] | `_3D.erzeugeHohleEllipse` |
| `_3D.generateHollowRectangle` | `F3DgenerateHollowRectangle` [SimTalk] | `_3D.erzeugeHohlesRechteck` |
| `_3D.generateRectangle` | `F3DgenerateRectangle` [SimTalk] | `_3D.erzeugeRechteck` |
| `_3D.getAnimationPoint` | `_3D.getMUAnimationPosition` [SimTalk] | `_3D.holeAnimationspunkt` |
| `_3D.getGraphicIndex` | `_3D.getGraphic` [SimTalk].`Index` [SimTalk] – graphic in 3D | `_3D.holeGrafikindex` |
| `_3D.getGraphicName` | `_3D.getGraphic` [SimTalk].`Name` [SimTalk] – graphic | `_3D.holeGrafiknamen` |
| `_3D.getGraphicPosition` | `_3D.getGraphic` [SimTalk].`Position` [SimTalk] – graphic | `_3D.holeGrafikPosition` |
| `_3D.getGraphicRotation` | `_3D.getGraphic` [SimTalk].`Rotation` [SimTalk] – graphic | `_3D.holeGrafikdrehung` |
| `_3D.getGraphicScale` | `_3D.getGraphic` [SimTalk].`Scale` [SimTalk] – graphic | `_3D.holeGrafikskalierung` |
| `_3D.GridVisibleInNewWindows` | no longer supported | `_3D.RasterSichtbarInNeuenFenstern` |
| `3D.groupGraphics` | `groupGraphics` [SimTalk] | `_3D.gruppiereGrafiken` |
| `_3D.hideGraphicGroup` | `Visible` [SimTalk] – graphic group | `_3D.blendeGrafikgruppeAus` |
| `_3D.HideInRepresentationOfLocation` | `_3D.ExcludeFromShowContentOfLocation` [SimTalk] | `_3D.BlendeInDarstellungDesStandortsAus` |
| `_3D.importGeometry` | `_3D.getGraphic` [SimTalk].`importGraphics` [SimTalk] | `_3D.importiereGeometrie` |
| `_3D.importGraphics` | `_3D.getGraphic` [SimTalk].`importGraphics` [SimTalk] | `_3D.InterneGraphiken` |
| `_3D.InheritGraphicVisibilities` | `_3D.inheritAttribute` [SimTalk] | `_3D.ErbeGrafiksichtbarkeiten` |
| `_3D.InsertMode` | no longer supported | `_3D.Einfügemodus` |
| `_3D.InternalGraphics` | `_3D.InternalGraphicGroups` [SimTalk] | `_3D.InterneGraphiken` |
| `_3D.isGraphicGroupGenerated` | `Generated` [SimTalk] – graphic group | `_3D.istGrafikgruppeGeneriert` |
| `_3D.isGraphicGroupInternal` | `Internal` [SimTalk] – graphic group | `_3D.setzeGrafikgruppeIntern` |
| `_3D.isGraphicGroupLocked` | `Locked` [SimTalk] – graphic group | `_3D.istGrafikgruppeGesperrt` |
| `_3D.isGraphicGroupVisible` | `Visible` [SimTalk] – graphic group | `_3D.istGrafikgruppeSichtbar` |
| `_3D.LastViewpoint` | no longer supported | `_3D.LetzteAnsicht` |
| `_3D.Length` | no longer supported | `_3D.Länge` |
| `_3D.Location` | `Location` [SimTalk] – material flow objects | `_3D.Standort` |
| `_3D.LockedGraphics` | `_3D.LockedGraphicGroups` [SimTalk] | `_3D.GesperrteGraphiken` |
| `_3D.lockGraphicGroup` | `Locked` [SimTalk] – graphic group | `_3D.sperreGrafikgruppe` |
| `_3D.makeAnimatableObject` | `_3D.getGraphic` [SimTalk].`makeAnimatableObject` [SimTalk] | `_3D.erstelleAnimierbaresObjekt` |
| `_3D.MaterialAmbientColor` | `_3D.getGraphic` [SimTalk].`MaterialAmbientColor` [SimTalk] | `_3D.MaterialumUmgebungsfarbe` |
| `_3D.MaterialSpecularCoor` | `_3D.getGraphic` [SimTalk].`MaterialSpecularColor` [SimTalk] | `_3D.MaterialGlänzendeFarbe` |
| `_.3D.MUAnimationAreaCenter` | `_3D.MUAnimationAreaRelativeCenter` [SimTalk] | `_3D.BEAnimationsflächenzentrum` |
| `_.3D.MUAnimationAreaSize` | `_3D.MUAnimationAreaRelativeSize` [SimTalk] | `_3D.BEAnimationsflächengröße` |
| `_3D.MUAnimations.<AnimationPathName>.getPositionAt` | `_3D.MUAnimations.<AnimationPathName>.getMUAnimationPosition` [SimTalk] | `_3D.BEAnimationen.<Animationspfadnamee>.holePositionBei` |
| `_3D.optimizeByPruningTinyGraphics` | `_3D.getGraphic` [SimTalk].`optimizeByPruningTinyGraphics` [SimTalk] | `_3D.optimiereDurchKleinstgrafikenLöschen` |
| `_3D.optimizeByStructureFlattening` | `_3D.getGraphic` [SimTalk].`optimizeByStructureFlattening` [SimTalk] | `_3D.optimiereDurchStrukturverflachung` |
| `_3D.optimizeByVisibilityFilter` | `_3D.getGraphic` [SimTalk].`optimizeByVisibilityFilter` [SimTalk] | `_3D.optimiereDurchSichtbarkeitsfilter` |
| `_3D.optimizeGraphic` | `_3D.getGraphic` [SimTalk].`optimizeByPruningTinyGraphics` [SimTalk], `_3D.getGraphic` [SimTalk].`optimizeByVisibilityFilter` [SimTalk] | `_3D.optimiereGrafik` |
| `_3D.pauseAnimation` | `_3D.CameraAnimations.pause` [SimTalk], `_3D.SelfAnimations.pause` [SimTalk] | `3D.pausiereAnimation` |
| `_3D.playAnimation` | `_3D.SelfAnimations.play` [SimTalk], `_3D.CameraAnimations.play` [SimTalk] | `_3D.spieleAnimationAb` |
| `_3D.PointCloudRotationAngle` | `_3D.PointCloudRotation` [SimTalk] | `_3D.Punktwolkendrehwinkel` |
| `_3D.pruneTinyGraphics` | `_3D.getGraphic` [SimTalk].`optimizeByPruningTinyGraphics` [SimTalk] | `_3D.bereinigeKleinstgrafiken` |
| `_3D.redirectTo` | `_3D.AnimationObject` [SimTalk] | `_3D.leiteUmZu` |
| `_3D.RelRotation` | `Rotation` | `_3D.RelDrehung` |
| `_3D.removeGraphicMaterial` | `_3D.getGraphic` [SimTalk].`MaterialDiffuseColor` [SimTalk], etc. | `_3D.entferneGrafikmaterial` |
| `_3D.renameGraphicGroup` | `Name` [SimTalk] – graphic | `_3D.benenneGrafikgruppeUm` |
| `_3D.Representation` | `_3D.ShowContent` [SimTalk] | `_3D.Darstellung` |
| `_3D.resetAnimation` | `_3D.CameraAnimations.resetAnimation` [SimTalk], `_3D.SelfAnimations.resetAnimation` [SimTalk] | `_3D.setzeAnimationZurück` |
| `_3D.Selection` | no longer supported | `_3D.Auswahl` |
| `_3D.SelectionMode` | no longer supported | `_3D.Auswahlmodus` |
| `_3D.setGraphicMaterial` | `_3D.getGraphic` [SimTalk].`MaterialDiffuseColor` [SimTalk], etc. | `_3D.setzeGrafikmaterial` |
| `_3D.setGraphicGroupExternal` | `External` [SimTalk] – graphic group | `_3D.setzeGrafikgruppeExtern` |
| `_3D.setGraphicGroupInternal` | `Internal` [SimTalk] – graphic group | `_3D.setzeGrafikgruppeIntern` |
| `_3D.setGraphicName` | `_3D.getGraphic` [SimTalk].`Name` [SimTalk] – graphic | `_3D.setzeGrafiknamen` |
| `_3D.setGraphicPosition` | `_3D.getGraphic` [SimTalk].`Position` [SimTalk] – graphic | `_3D.setzeGrafikposition` |
| `_3D.setGraphicRotation` | `_3D.getGraphic` [SimTalk].`Rotation` [SimTalk] – graphic | `_3D.setzeGrafikdrehung` |
| `_3D.setGraphicScale` | `_3D.getGraphic` [SimTalk].`Scale` [SimTalk] – graphic | `_3D.setzeGrafikskalierung` |
| `_3D.setGraphicTransformation` | no longer supported | `_3D.setzeGrafiktransformation` |
| `_3D.setGraphicTransformationMatrix` | `_3D.getGraphic` [SimTalk].`TransformationMatrix` [SimTalk] | `_3D.setzeGrafiktransformationsmatrix` |
| `_3D.showGraphicGroup` | `Visible` [SimTalk] – graphic group | `_3D.zeigeGrafikgruppe` |
| `_3D.ShowPlainGraphics` | no longer supported | `_3D.ReineGrafikenAnzeigen` |
| `_3D.startAnimation` | `_3D.CameraAnimations.play` [SimTalk], `_3D.SelfAnimations.play` [SimTalk] | `_3D.starteAnimation` |
| `_3D.unlockGraphicGroup` | `Locked` [SimTalk] – graphic group | `_3D.entsperreGrafikgruppe` |
| `3D.StatesVertical` | `_3D.StatesOrientation` [SimTalk] | `_3D.ZuständeVertikal` |
| `_3D.ungroupGraphic` | `ungroupGraphic` [SimTalk] | `_3D.hebeGruppierungAuf` |
| `_3D.updateAll` | no longer supported | `_3D.aktualisiereAlles` |
| `_3D.updateConnectors` | no longer supported | `_3D.aktualisiereKanten` |
| `_3D.updateMUs` | no longer supported | `_3D.aktualisiereBEs` |
| `_3D.updatePositions` | no longer supported | `_3D.aktualisierePositionen` |
| `_3D.VisibleGraphics` | `_3D.VisibleGraphicGroups` [SimTalk] | `_3D.SichtbareGraphiken` |

---

## See also

- Colors for Syntax Highlighting
- No Longer Supported SimTalk Names of the 2D Visualization

> Source: *Outdated SimTalk Names*, Plant Simulation Help 12-1290 – 12-1308. Unpublished work. © 2026 Siemens.
