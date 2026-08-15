# README — 2D Visualization 已弃用/不再支持的 SimTalk 名称

本目录汇总了 Plant Simulation 中与 **2D 可视化** 相关的、**不再支持** 的 SimTalk 属性（Attributes）、只读属性（read-only attributes）和方法（Methods）。这些名称在旧版本中可用，但在当前版本中已被弃用。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `2d-visualization.md` | 主要文档，以 Markdown 表格列出不再支持的英文与德文名称 |
| `2d-visualization.txtx` | 上述文档的纯文本版本，内容一致 |

> 本目录下没有子文件夹，因此没有子文件夹内的 README 需要汇总。

## 内容概述

旧版本的 Plant Simulation 提供了一系列面向 2D 可视化的 SimTalk 属性、只读属性和方法，当前版本已不再支持。可以通过 **调试器（Debugger）** 标签页上的 **查找过时函数（Find Outdated Functions）** 命令，找出模型中所有过时的函数，并在窗口中显示；Plant Simulation 会在源代码中以高亮颜色标记这些过时的函数。

文档按对象类型将不再支持的名称分为以下几类：

### 1. Frame（框架）的不再支持的属性与方法

共 22 项，包括坐标原点、背景色、位图复制、绘图方法（椭圆、直线、矩形、文本）、图层管理（擦除图层）、显示区域、缩放、重绘等。

| 英文 | 德文 |
| --- | --- |
| AxesOrigin | AchsenUrsprung |
| BackgroundColor | Hintergrundfarbe |
| copyBitmapToClipboard | kopiereBitmapInZwischenAblage |
| copyBitmapToFile | kopiereBitmapInDatei |
| drawEllipse | zeichneEllipse |
| drawLine | zeichneLinie |
| drawRectangle | zeichneRechteck |
| drawText | zeichneText |
| eraseAllLayers | löscheAlleEbenen |
| eraseLayer | löscheEbene |
| getRepresentationArea | holeDarstellungsBereich |
| rearrange | aufräumen |
| redraw | zeichneNeu |
| RepresentationMode | DarstellungsModus |
| ScalingFactor | SkalierungsFaktor |
| selectContents | selektiereInhalt |
| setBackgroundImage | setzeHintergrundBild |
| setRepresentationArea | setzeDarstellungsBereich |
| setXYOrigin | setzeXYUrsprung |
| ShowDisplayPanels | AnzeigetafelnAnzeigen |
| ShowObjectLabels | ObjektetikettenAnzeigen |
| ZoomFactor | ZoomFaktor |

### 2. Connector（连接器）的不再支持的属性与方法

共 3 项，涉及折线角点数组以及获取起点/终点。

| 英文 | 德文 |
| --- | --- |
| CornerPointsArray | StützpunkteArray |
| getEndPoint | holeEndPunkt |
| getStartPoint | holeStartPunkt |

### 3. 面向长度的对象（Length-oriented Objects）的不再支持的属性与方法

共 16 项，涉及动画像素步长、基线高度、颜色、曲线（激活、宽度）、中线、镜像、对象角度、画笔颜色/宽度、旋转、曲线分段和透明度等。

| 英文 | 德文 |
| --- | --- |
| AnimateOnEveryXthPixel | AnimiereAufJedemXtenPixel |
| BaseHeight | Basishöhe |
| Color | Farbe |
| CurveActive | KurveAktiv |
| CurveWidth | KurvenBreite |
| MidLine | MittelLinie |
| mirrorX | spiegelnX |
| mirrorY | spiegelnY |
| ObjectAngle | ObjektWinkel |
| ObjectMirrored | ObjektGespiegelt |
| PenColor | Stiftfarbe |
| PenWidth | Stiftbreite |
| rotate | drehen |
| RotateMovables | BEsDrehen |
| setCurveSegments | setzeKurvenSegmente |
| Transparent | Transparent |

### 4. MU（可移动单元）的不再支持的属性与方法

共 9 项，涉及矢量图形相关的显示设置以及 X/Y 坐标位置。

| 英文 | 德文 |
| --- | --- |
| VectorgraphicsActive | VektorgrafikAktiv |
| VectorgraphicsAnilineDirection | VektorgrafikAnilinienRichtung |
| VectorgraphicsBorderColor | VektorgrafikRahmenFarbe |
| VectorgraphicsBorderWidth | VektorgrafikRahmenbreite |
| VectorgraphicsColor | VektorgrafikFarbe |
| VectorgraphicsShowDirectionArrow | VektorgrafikZeigeRichtungspfeil |
| VectorgraphicsShowState | VektorgrafikZeigeZustand |
| XPos | XPos |
| YPos | YPos |

### 5. 图标（Icons）的不再支持的属性与方法

共 36 项，涉及位图/图片的打开与关闭、当前图标、动画点（删除、获取、链接、移动、设置、断开）、图层、桑基图、镜像、对象角度、重绘、图标重置、旋转、选中状态、显示填充高度、缓冲区占位符、缩放、位置等。

| 英文 | 德文 |
| --- | --- |
| closeImg | schliesseBild |
| CurrIcon | BildName |
| CurrIconNo | BildNr |
| CurrIconTransparent | BildTransparent |
| delAniPoint | löscheAniPunkt |
| delAniPoints | löscheAniPunkte |
| DisplayPanel | DisplayPanel |
| drawMUs | zeichneBEs |
| getAniPoints | holeAniPunkte |
| getBoundingBox | Anzeigetafel |
| getRefPoint | spiegelnY |
| linkAniPoint | verbindeAniPunkt |
| Layer | Ebene |
| SankeyDiagram | SankeyDiagram |
| mirrorX | spiegelnX |
| mirrorY | spiegelnY |
| moveAniPoint | verschiebeAniPunkt |
| NumAnimationEvents | AnzahlAnimationsereignisse |
| ObjectAngle | ObjektWinkel |
| ObjectMirrored | ObjektGespiegelt |
| openImg | öffneBild |
| redraw | zeichneNeu |
| resetIcon | rücksetzen |
| RotateMUs | DreheBEs |
| RotateAroundRefPoint | DreheUmRefPunkt |
| Selected | Selektiert |
| setAniPoint | setzeAniPunkt |
| setAniLine | setzeAniLinie |
| setRefPoint | setzeRefPunkt |
| setPosition | setzePosition |
| ShowFillLevel | ZeigeFüllstand |
| Buffer/PlaceBuffer | Buffer/PlaceBuffer |
| turnIcon | dreheBild |
| unlinkAniPoint | löseAniPunkt |
| XPos | XPos |
| YPos | YPos |
| ZoomX | ZoomX |
| ZoomY | ZoomY |

### 6. 涉及 2D/3D 的不再支持的函数

共 4 项，涉及 3D 窗口的打开/关闭以及 2D/3D 是否打开的判断。

| 英文 | 德文 |
| --- | --- |
| close3D | beende3D |
| is2DOpen | ist2DGestartet |
| is3DOpen | ist3DGestartet |
| open3D | starte3D |

## 另请参阅（See Also）

- Colors for Syntax Highlighting（语法高亮颜色）
- Outdated SimTalk Names（过时的 SimTalk 名称）
