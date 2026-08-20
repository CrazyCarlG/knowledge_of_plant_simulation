# Factory51 SimTalk 代码样例

> 模型来源：`02-offcial-psfm-model/Factory51/Factory51.psfm`（Folder Model，PSFM 文本格式）
> 提取依据：`Models/Factory51/**`、`UserObjects/**` 中对象的 `$CustomAttributes`（`DataType: method` 的自定义属性方法）与 `Method` 对象的 `Program` 字段；外部库 `ApplicationObjects/HBW3D/WMS/**` 与 `ApplicationObjects/CranesAndMore/StorageArea.yaml` 的 `Program` 源码。
>
> 说明：`.jt` 文件（如 `StoreEntry.jt`、`TruckArrivals.jt`）是 Siemens JT 二进制格式（3D 图形 + 编译后源码），非明文 SimTalk，无法直接解析，本清单不纳入；其对应的明文源码位于对象 `.yaml` 的 `$CustomAttributes` 或 `Program` 字段中。

---

## 一、代码清单

### 1.1 进货（卡车到达 / 装载 / 卸货）

#### 代码块名称：Source.OnEntrance（所属Frame：Models/Factory51）
- 触发/调用方式：由 `Source` 的 `EntranceCtrl = "self.OnEntrance"` 绑定，当 Source 按 `Number=120` 生成 MU 进入自身时触发，每件触发一次。
- 功能说明：为每件产品创建 4 个 Box（箱），每箱内按 `Box.Capacity` 创建 DummyPart（零件）；按已产出数量将前一半零件命名/着色为 Aubergine（紫色），后一半为 Strawberry（粉红），并设置三维材质。

```simtalk
// Create 4 boxes on each palette
for var j := 1 to 4
	var container := .UserObjects.MUs.Box.create(@)

	// Create 4 parts in each box
	for var k := 1 to .UserObjects.MUs.Box.Capacity
		var part := .UserObjects.MUs.DummyPart.create(container)
		
		part._3D.VisibleGraphicGroups := ["Finished"]
		
		var color:integer
												
		if ?.statNumOut < ?.Number/2
			part.Name := "Aubergine0"
			color := makeRGBValue(107, 0, 128)
		else
			part.Name := "Strawberry0"
			color := makeRGBValue(255, 0, 128)
		end

		part._3D.activateMaterialWithColor(color)
		part._3D.MaterialSpecularColor := color
		part._3D.MaterialShininess := 0.2
	next
next

@.ConveyingDirection := 3
```

#### 代码块名称：TruckArrivals.OnEntrance（所属Frame：Models/Factory51）
- 触发/调用方式：由 `TruckArrivals`（Source）的 `EntranceCtrl = "self.OnEntrance"` 绑定，按 `Interval=[Normal,15:00,4:00,2:00,30:00]` 生成卡车 MU 进入时触发。
- 功能说明：限制等待卡车数量（`SupplyRoad.NumMU > 1` 时拒入并统计 `TrucksMissed`）；否则为卡车装载托盘 → 箱 → 零件，并计算托盘含内容高度 `MUHeightWithContent`。

```simtalk
// Don't allow more than 2 waiting trucks
if SupplyRoad.NumMU > 1
	TrucksMissed += 1
	@.delete
	return
end

// Load Truck with parts
for var i := 1 to @.Capacity
	var palette := .UserObjects.MUs.Pallet.create(@)

	// Create boxes on each palette
	for var j := 1 to palette.Capacity
		var container := .UserObjects.MUs.Box.create(palette)
	
		// Create parts in each box
		for var k := 1 to container.Capacity
			.UserObjects.MUs.Part.create(container)
		next
	next
	
	palette.MUHeightWithContent := palette.MUHeight + palette.ZDim*palette.Cont.MUHeight
next
```

#### 代码块名称：TruckArrivals.Init（所属Frame：Models/Factory51）
- 触发/调用方式：仿真初始化时由 Plant Simulation 自动调用 `Init` 控制。
- 功能说明：为卡车源创建路径对象 `Path`。

```simtalk
self.~.Path.create(self.~)
```

#### 代码块名称：UnloadTruck（Method，所属Frame：Models/Factory51）
- 触发/调用方式：卡车到达卸货点后由上游触发（外部调用，参数传入卡车 `CurrentTruck`）。
- 功能说明：从 `AGVPool` 取叉车，循环将卡车上的托盘经标记点 `M_RoadTurn → M_Road → M_Truck` 搬运到 `StoreEntry` 入库缓冲，叉臂升降与前进后退配合，直到卡车清空后释放卡车。

```simtalk
param CurrentTruck:object

TrucksArrived += 1

var forklift := AGVPool.Cont

while not CurrentTruck.Empty
	forklift.Backwards := true
	forklift.setRoute([M_RoadTurn,M_Road])
	forklift.moveFork(0.4)
	waituntil forklift.DestinationWasReached

	forklift.Backwards := false
	forklift.setRoute([M_Truck])
	forklift.moveFork(1.5)
	waituntil forklift.DestinationWasReached

	wait 3
	CurrentTruck.Cont.move(forklift)

	forklift.Backwards := true
	forklift.setRoute([M_Road])
	waituntil forklift.DestinationWasReached

	forklift.Backwards := false
	waituntil not StoreEntry.Full
	forklift.setRoute([M_RoadTurn,M_StoreEntry])
	forklift.moveFork(0.5)
	waituntil forklift.DestinationWasReached

	wait forklift.moveFork(0.05)
	forklift.cont.move(StoreEntry)
end

CurrentTruck.Stopped := false
```

### 1.2 入库与立体仓库（HBW3D WMS + CranesAndMore StorageArea）

#### 代码块名称：StorageArea.storing（Method，所属Frame：ApplicationObjects/CranesAndMore/StorageArea）
- 触发/调用方式：由 `StoreEntry.ExitCtrl = "StorageArea.storing"` 绑定，当 MU 离开 `StoreEntry`（入库缓冲）时触发。
- 功能说明：从入库缓冲取产品，调用 `getFreePlace` 找空位、`occupyPlace` 占用，然后控制 `MultiPortalCrane` 堆垛机（`portal`）移动钩子、抓取产品、移动到目标货位放下。

```simtalk
var Store : object := self.~
var portal := Store.storingPortal
var crane := Portal.~

waituntil not Store.Full and portal.state="idle" and Store.StoreEntrance.occupied

var step : integer := 1

// get the height of the MU on StoreEntrance
var Product :object := Store.StoreEntrance.cont
if Product.MuHeightWithContent>0 then
	var productHeight : length := Product.MuHeightWithContent
else
	productHeight := Product.MuHeight
end

// get a free place in the store
var place : integer[2] := Store.getFreePlace
if place.x>0 and place.y>0 then
	// a free place was found for the product, occupy the place
	Store.occupyPlace(place, product.name)

	// calculate the target position in crane coordinates
	var TargetPosition := crane._3D.getPositionOfObject(Store, Store._3D.getMUAnimationPosition(place.x, place.y))

	var upperPart := Store[place[1], place[2]].cont
	if upperPart=void then
		// no part at  this place
		var position : length[3] := [0.0, 0.0, 0.0]
		TargetPosition.z := Position.z
	else
		position := upperPart._3D.Position
		if upperPart.MuHeightWithContent>0 then
			TargetPosition.z := Position.z + upperPart.MuHeightWithContent
		else
			TargetPosition.z := Position.z + upperPart.MUHeight
		end
	end

	TargetPosition.z += Store.Coordinate3D.z

	// move hook up
	portal.moveHook(crane.DefaultHookHeight)
	waituntil portal.state="waiting"

	// move to the entrance object
	portal.moveToObject(Store.StoreEntrance.cont)
	waituntil portal.state="waiting"

	// move hook down to the object
	var height : length := crane.~._3D.getPositionOfObject(Product).z + productHeight
	portal.moveHookAbs(height)
	waituntil portal.state="waiting"

	// pick the product
	Portal._3D.MuSideToAttach := "Top"
	Product.move(Portal)
	waituntil not portal.empty and portal.state="waiting"

	// move hook up
	portal.moveHook(crane.DefaultHookHeight)
	waituntil portal.state="waiting"

	// move portal to the target position
	portal.moveToCranePosition(TargetPosition.x,TargetPosition.y)
	waituntil portal.state="waiting"

	// move hook down so that we can place the product onto the floor
	portal.moveHookabs(TargetPosition.z + ProductHeight)
	waituntil portal.state="waiting"

	// release the product
	Product.move(Store[place.x, place.y])
	waituntil portal.empty and portal.state="waiting"

	// move hook up
	portal.moveHook(crane.DefaultHookHeight)
	waituntil portal.state="waiting"

	// now the sequence is finished
	portal.endSequence
end
```

#### 代码块名称：WMS.placeIntoStock（Method，所属Frame：ApplicationObjects/HBW3D/WMS）
- 触发/调用方式：由模型内的 `userSetTarget` 方法显式调用 `Warehouse.WMS.placeIntoStock(@, @.Cont.Cont.Name, 12)`。
- 功能说明：根据托盘/零件确定产品名与数量，调用 `getFreePlace` 搜索空位；找到后 `reserveBox` 预留货位、关闭 `AutomaticRouting` 并把货位设为托盘 `Destination`，再写入 `HBW_ProductName`/`HBW_ProductQuantity` 自定义属性。

```simtalk
param Pallet: object := void, product: string := "", quantity: integer := 0 -> boolean

if pallet = void then
	pallet := @
end

if product = "" then
	// determine the product and the quantity
	if pallet.InternalClassName="Piece" then
		product := pallet.Name
	else
		product := when pallet.empty then pallet.name else pallet.cont.name
	end
end

if quantity = 0 then
	if pallet.InternalClassname="Piece" then
		quantity := 1
	else
		quantity := when pallet.empty then 1 else pallet.numMu
	end
end

var Racklane: object
var Side: string
var Column, Row: integer

getFreePlace(Racklane, Side, Column, Row, Product)

if Racklane = void or Column = 0 or Row = 0 then
	return false
else
	// free place found, make a reservation for this place
	reserveBox(Racklane, Side, Column, Row)
	// Set the place in the rack returned above as destination for the pallet
	Pallet.AutomaticRouting := false
	if Side ~= "left"
		Pallet.Destination := RackLane.RackLeft[Column,Row]
	else
		Pallet.Destination := RackLane.RackRight[Column,Row]
	end

	// Assign product name to user-defined attribute HBW_ProductName
	if pallet.getAttrNo("HBW_ProductName") <= 0 then
		pallet.createAttr("HBW_ProductName", "string")
	end
	pallet.HBW_ProductName := product

	// Assign quantity to user-defined attribute HBW_ProductQuantity
	if quantity > 1
		if pallet.getAttrNo("HBW_ProductQuantity") <= 0 then
			pallet.createAttr("HBW_ProductQuantity", "integer")
		end
		pallet.HBW_ProductQuantity := quantity
	end
	return true
end
```

#### 代码块名称：WMS.getFreePlace（Method，所属Frame：ApplicationObjects/HBW3D/WMS）
- 触发/调用方式：被 `placeIntoStock` 调用。
- 功能说明：按 `StrategyIndex`（入库策略编号）分派到对应的选位策略方法（`OneByOne`/`Random`/`Predefined`/`XYZ`）。

```simtalk
param byRef Racklane: object, byRef Side: string, byRef Column, Row: integer,
	product: string := ""
	
switch StrategyIndex
case 1
	OneByOne(Racklane, Side, Column, Row, product)
case 2
	Random(Racklane, Side, Column, Row)
case 3
	Predefined(Racklane, Side, Column, Row, product)
case 4
	XYZ(Racklane, Side, Column, Row, product)	
else
	debug
end
```

#### 代码块名称：WMS.OneByOne（Method，所属Frame：ApplicationObjects/HBW3D/WMS）
- 触发/调用方式：由 `getFreePlace` 在 `StrategyIndex=1` 时调用。
- 功能说明：按 `lastIndex` 轮询各巷道（RackLane），先找左货架 `OccupancyLeft` 中第一个 0 值（空位），找不到再找右货架；用 `setCursor`/`find` 在占用表中定位空位并回传行列号与左右侧。

```simtalk
param byRef Racklane: object, byRef Side: string, byRef Column, Row: integer,
	product: string

var found: boolean    := false
var finished: boolean := false

// just to make sure all racklanes have same utilization 
var index: integer := lastIndex + 1
var count: integer := 1

if index > RackLanes.Dim then
	index := 1
end
	
repeat
	racklane := RackLanes[index]

	if racklane = void
		continue
	end
	
	// get the first free place of the left rack
	var rack: object := racklane.OccupancyLeft
	
	rack.setCursor(1,1)
	if rack.find(0) then
		Column    := rack.CursorX
		Row       := rack.CursorY
		Side      := "left"
		found     := true
		lastIndex := Index
	else
		// get the first free place of the right rack
		rack := racklane.OccupancyRight
		
		rack.setCursor(1,1)
		if rack.find(0) then
			Column    := rack.CursorX
			Row       := rack.CursorY
			Side      := "right"
			found     := true
			lastIndex := Index
		else
			Racklane := void
		end
	end
	
	index += 1
until found or index>RackLanes.Dim
```

#### 代码块名称：WMS.reserveBox（Method，所属Frame：ApplicationObjects/HBW3D/WMS）
- 触发/调用方式：被 `placeIntoStock` 调用。
- 功能说明：在对应侧占用表（`OccupancyLeft`/`OccupancyRight`）中把目标货位标记为 1（占用），并更新 `NumFreePlaces`/`NumOccupiedPlaces` 全局计数。

```simtalk
param RackLane: object, Side: string, Column, Row: integer -> boolean

var OccupancyTable: object

if Side ~= "left"
	OccupancyTable := Racklane.OccupancyLeft
else
	OccupancyTable := Racklane.OccupancyRight
end

if OccupancyTable[Column, Row] = 0 then
	OccupancyTable[Column, Row] := 1
	// Decrease number of available places in all registered racklanes
	NumFreePlaces -= 1
	NumOccupiedPlaces += 1
	return true
else
	return false // Box is not free
end
```

#### 代码块名称：WMS.removeProduct（Method，所属Frame：ApplicationObjects/HBW3D/WMS）
- 触发/调用方式：被 `removeProducts` 调用。
- 功能说明：在 `Content` 库存表中按产品名找到行，扣减对应数量。

```simtalk
param product: string, Quantity: integer

var row: integer := Content.getRowNo(Product)

if row > 0 then
	Content[1,row] -= Quantity
else
	debug --Product not found in table Content
end
```

#### 代码块名称：WMS.removeProducts（Method，所属Frame：ApplicationObjects/HBW3D/WMS）
- 触发/调用方式：由出库订单（外部调用）或 `autoRemove` 触发。
- 功能说明：先校验库存是否满足数量，再在 `Inventory` 表中查找持有该产品的托盘列表，用 `findCeil` 找到数量最接近需求且足够的托盘，调用 `getPalletLocation` 定位、`appendOrder` 生成出库任务、`removeProduct` 扣减库存并 `cutRow` 删除 Inventory 记录，循环直至满足需求。

```simtalk
param OrderNo: string, product: string, quantity: integer

// check if the requested quantity is at stock
var StockRow: integer := Content.getRowNo(Product)
if StockRow <= 0 then
	debug -- The requested product could not be found in the warehouse
else
	if Content[1, StockRow] < quantity then
		debug -- Not enough parts at stock
	else
		// look for a pallet which fits the requested quantity
		var ProductRow: integer := Inventory.getRowNo(Product)

		if ProductRow <= 0 then
			debug -- Product not in warehouse
		else
			var done: boolean := false
			var Rest: integer := Quantity
			var PalletList:= Inventory["Pallets", ProductRow]

			repeat
				// find a pallet with the number of parts close to the requested quantity
				PalletList.setCursor(1,1)
				var found: boolean := PalletList.findCeil({2,1}..{2,*}, Rest)
				if PalletList.CursorY > 0 then
					var PalletRow := PalletList.CursorY

					// remove the pallet
					var Pallet: object := PalletList["Pallet", PalletRow]
					var numProducts: integer := PalletList["Quantity", PalletRow]

					var Racklane: object
					var Side: string
					var column, row: integer

					getPalletLocation(Pallet, Racklane, Side, Column, Row)

					if Racklane /= void then
						Racklane.appendOrder(Column, Row, side, OrderNo)

						// remove the quantity in stock
						removeProduct(Product, numProducts)

						// remove the entry in table Inventory
						PalletList.cutRow(PalletRow)

						// calculate the rest
						Rest -= numProducts
					else
						debug -- No racklane found for product
						done := true
					end
				else
					debug -- No entry found in table Inventory for product
					done := true
				end
			until Rest<=0 or done
		end
	end
end
```

#### 代码块名称：WMS.autoRemove（Method，所属Frame：ApplicationObjects/HBW3D/WMS）
- 触发/调用方式：由 `WMS_Init` 通过 `&autoremove.executeIn(startRemoveTime)` 定时启动，并自递归 `self.executeIn(RemoveInterval)` 周期执行。
- 功能说明：在 `Content` 中随机选一种有库存的产品，随机确定本次出库数量（不超过 `MaxAmount`），调用 `removeProducts` 出库。

```simtalk
if Content.YDim>0 then
	// get one of the products
	var row : integer := ceil(z_uniform(87, 0, Content.YDim))

	var product := Content[0, row]

	if Content[1,row]>0 then
		// get the number of products to remove from stock
		var quantity : integer := min(round(z_uniform(1, MaxAmount)), Content[1,row])

		// remove the product
		removeProducts("0", product, quantity)
	end
end

self.executeIn(RemoveInterval)
```

#### 代码块名称：WMS.WMS_Init（Method，所属Frame：ApplicationObjects/HBW3D/WMS）
- 触发/调用方式：由 `INIT` 方法 `&WMS_init.executeIn(0)` 在所有 Init 执行完后触发。
- 功能说明：若启用 `activateAutoRemove` 则定时启动 `autoRemove`；并遍历所有巷道设置货架 MU 以立方体方式显示的 3D 开关。

```simtalk
if activateAutoRemove then
	&autoremove.executeIn(startRemoveTime)
end

for var i := 1 to RackLanes.dim
	var Racklane := RackLanes[i]
	if ShowMUsAsCuboids
		Racklane.RackLeft._3D.MUAnimationAreaShowMUsAsCuboids := true
		Racklane.RackRight._3D.MUAnimationAreaShowMUsAsCuboids := true
	else
		Racklane.RackLeft._3D.MUAnimationAreaShowMUsAsCuboids := false
		Racklane.RackRight._3D.MUAnimationAreaShowMUsAsCuboids := false
	end
next
```

#### 代码块名称：WMS.INIT（Method，所属Frame：ApplicationObjects/HBW3D/WMS）
- 触发/调用方式：仿真初始化时自动调用 `Init` 控制。
- 功能说明：延迟到所有 Init 方法执行完毕后再执行 `WMS_Init`。

```simtalk
&WMS_init.executeIn(0) // Execute WMS_init after all Init methods are executed
```

### 1.3 出库与配送（拉式）

#### 代码块名称：StoreExit.Init（所属Frame：Models/Factory51）
- 触发/调用方式：仿真初始化后循环执行（`while true` 无限循环）。
- 功能说明：拉式补料核心——当仓库非空且自身为空时，调用 `StorageArea.removeProductTo` 从仓库拉一件产品到 StoreExit，再等待自身满。

```simtalk
while true
	stopuntil not StorageArea.Empty and self.~.Empty

	StorageArea.&removeProductTo.executeNewCallChain(1, @) // Order one part for the object which has the Init control
		
	stopuntil self.~.Full
end
```

#### 代码块名称：StoreExit.OnExit（所属Frame：Models/Factory51）
- 触发/调用方式：由 `StoreExit`（Buffer）的 `ExitCtrl = "self.OnExit"` 绑定，MU 离开时触发。
- 功能说明：并行启动两个 `Unload` 子方法，分别向上/下两个 `PickAndPlace`（Top/Bottom）分发箱体；等待托盘清空后删除空托盘。

```simtalk
self.~.&Unload.executeNewCallChain(1, PickAndPlaceTop, @, ?)
self.~.&Unload.executeNewCallChain(2, PickAndPlaceBottom, @, ?)

stopuntil @.Empty
wait 4
@.delete
```

#### 代码块名称：StoreExit.Unload（所属Frame：Models/Factory51）
- 触发/调用方式：由 `StoreExit.OnExit` 通过 `executeNewCallChain` 并行调用，参数 `ypos` 为托盘行号、`target` 为目标 PickAndPlace。
- 功能说明：按坐标 `@[行, 列]` 从托盘逐箱取出（`cont` 为内容物），`move` 到目标位置并等待其离开托盘。

```simtalk
param ypos:integer, target:object

var box:object

for var i := 1 to 2
	box := @[2, ypos].cont
	box.move(target)
	stopuntil box.Location /= @
																
	box := @[1, ypos].cont
	box.move(target)
	stopuntil box.Location /= @
next
```

#### 代码块名称：StorageArea.removeProductTo（Method，所属Frame：ApplicationObjects/CranesAndMore/StorageArea）
- 触发/调用方式：由 `StoreExit.Init` 调用。
- 功能说明：在 `Content` 表中定位要出库的产品，`getPlaceOfProduct` 找货位，控制 `RemovingPortal` 堆垛机移动到货位、抓取产品、`freePlace` 释放货位、搬运到目标工位（ToStation）。

```simtalk
param Quantity : integer, ToStation : object, Product : string := ""  -> boolean

var store := self.~
var portal := store.RemovingPortal
var crane := Portal.~

waituntil portal.state="idle"

// determine the product which should be removed
if product="" then
	var index : integer := 1
	Product := store.Content[1,1]
	if Product="" then
		return
	end

else
	store.content.setCursor(1,1)
	If store.content.find({1,1}..{1,*}, Product) then
		index := store.Content.CursorY
	else
		// product not found
		return false
	end
end

// check for the reqiested quantity
var removeQuantity : integer := min(store.Content["Quantity", index], Quantity)
if removeQuantity<=0 then
	return false
end

// determine the target position of the exit station
var TargetPosition := rootfolder.Internal.Methods.getTargetPosition(Crane, ToStation)
var TargetCranePosition : real[3] := crane.calculateTargetPosition(Portal, TargetPosition)


var step : integer := 1
var partsRemoved : integer := 0


// move hook up
portal.moveHook(crane.DefaultHookHeight)

// determine the location from which we want to remove the product
var place := store.getPlaceOfProduct(Product)

// calculate the target position in world coordinates
var StorePosition : real[3] := crane._3D.getPositionOfObject(Store, Store._3D.getMUAnimationPosition(place.x, place.y))
var CranePosition : real[3] := crane.calculateTargetPosition(Portal, StorePosition)

var part : object := store[place[1], place[2]].cont
if part=void then
	return
end

var pickHeight : length
if part.MuHeightWithContent>0 then
	pickHeight := part.MuHeightWithContent
else
	pickHeight := part.MuHeight
end
waituntil portal.state="waiting"

// move to the position of the product
portal.movePortalTo(CranePosition)
waituntil portal.state="waiting"

// move hook down
var position := part._3D.Position
portal.moveHookAbs(position.z + pickHeight)
waituntil portal.state="waiting"

// pick the part
Portal._3D.MuSideToAttach := "Top"
part.move(Portal)
waituntil not portal.empty

store.freePlace(place, product)
waituntil portal.state="waiting"

// move hook up
portal.moveHook(crane.DefaultHookHeight)
waituntil portal.state="waiting"

// move portal to the exit location
portal.moveToCranePosition(TargetPosition.x,TargetPosition.y)
waituntil portal.state="waiting"

// move hook down to the object
portal.moveHookAbs(TargetPosition[3] + pickHeight)
waituntil portal.state="waiting"

// unload the hook
portal.cont.move(ToStation)

waituntil portal.empty
partsRemoved += 1
if partsRemoved<removeQuantity then
	step := 0	// step will be incrementd at the end of the case statement
end
waituntil portal.state="waiting"

// move hook up
portal.moveHook(crane.DefaultHookHeight)
waituntil portal.state="waiting"

// now the sequence is finished
portal.endSequence

return true
```

### 1.4 生产线内部（P1/P2）

#### 代码块名称：Production.Init（Method，所属Frame：UserObjects/Production）
- 触发/调用方式：Production Frame（P1/P2）初始化时自动调用。
- 功能说明：按 `NumAGVs` 数量在 `Track` 上等间距创建 AGV 车队，`startPos` 从 12 开始每次减去 `AGV.Length + 0.1`。

```simtalk
var startPos:length := 12

for var i := 1 to NumAGVs
	var agv := .UserObjects.MUs.AGV.create(Track, startPos)
	startPos -= agv.Length + 0.1
next
```

#### 代码块名称：Production.Line.OnExit（所属Frame：UserObjects/Production）
- 触发/调用方式：由 `Line`（Conveyor）的 `ExitCtrl = "self.OnExit"` 绑定，板件离开主线传送带时触发。
- 功能说明：累计在制品数 `PlatesInProduction`；按下游 `Polishing1.Polishing.Empty`（抛光站是否为空）动态选出口——空走出口 2（抛光分支），忙走出口 1（其它分支），实现拉式分流。

```simtalk
PlatesInProduction += 1

if Polishing1.Polishing.Empty
	@.move(2)
else
	@.move(1)
end
```

#### 代码块名称：Milling.OnEntrance（所属Frame：UserObjects/Milling）
- 触发/调用方式：由 `Milling`（Station）的 `EntranceCtrl = "self.OnEntrance"` 绑定，MU 进入时触发（`EntranceCtrlBeforeActions=true`）。
- 功能说明：先播放关门姿态 `DoorClosed`，等待姿态完成后 `startProcessing` 开始加工；若对象在 3D 中存在且有动画，则播放刀具 `Tool.Work` 动画与转台 `TurnPlate` 旋转动画（转速与 `procTime` 挂钩）。

```simtalk
var poses := ?._3D.Poses
poses.moveTo("DoorClosed")
waituntil poses.EndPoseWasReached
?.startProcessing

// We only start the animation if the object exists in 3D and we are not in fast-forward
if ?._3D.ExistsWithAnimation
	?._3D.getObject("Tool").SelfAnimations.Work.play
	?._3D.getObject("TurnPlate").SelfAnimations.playRotation(0, 360, 360/?.procTime)
end
```

#### 代码块名称：Milling.OnExit（所属Frame：UserObjects/Milling）
- 触发/调用方式：由 `Milling` 的 `ExitCtrl = "self.OnExit"` 绑定（`ExitCtrlFront=true`、`ExitCtrlRear=true`、`ExitCtrlOnce=true`），MU 离开/阻塞解除/后置触发时调用。
- 功能说明：三分支处理——若因前置阻塞方 `sender` 释放而触发，则将 MU `move` 到 sender；若是后置触发（MU 不在本站），播放姿态复位并标记 `IsAvailable=true`；正常出料则切换图形组 `Milled` 并 `move` 离开。

```simtalk
param sender: object

if sender /= void
	// We were in the forward blocking list of sender which became free
	@.move(sender)
elseif @.Location /= ?
	// Rear triggered exit control call?
	var poses := ?._3D.Poses
	poses.moveTo("PlateCenter")
	poses.moveTo("DoorOpen")
	waituntil poses.EndPoseWasReached
	self.~.IsAvailable := true
else
	@._3D.VisibleGraphicGroups := ["Milled"]
	poses := ?._3D.Poses
	poses.moveTo("PlateRight")
	waituntil poses.EndPoseWasReached
	@.move
end
```

#### 代码块名称：Milling.Reset（所属Frame：UserObjects/Milling）
- 触发/调用方式：仿真复位时调用。
- 功能说明：将自定义布尔属性 `IsAvailable` 复位为 `true`。

```simtalk
self.~.IsAvailable := true
```

### 1.5 成品入库触发

#### 代码块名称：userSetTarget（Method，所属Frame：Models/Factory51）
- 触发/调用方式：由成品托盘/箱到达仓库入口时触发（外部/接口调用）。
- 功能说明：设定托盘含内容高度为 0.84，并调用 `Warehouse.WMS.placeIntoStock` 将产品（`@.Cont.Cont.Name`）以数量 12 入库。

```simtalk
@.MUHeightWithContent = 0.84
Warehouse.WMS.placeIntoStock(@, @.Cont.Cont.Name, 12)
```

---

## 二、逐段注释解读

### 2.1 Source.OnEntrance —— 产品生成与颜色区分

```simtalk
for var j := 1 to 4
    var container := .UserObjects.MUs.Box.create(@)   // 在 Source(@) 中创建自定义 Box 类实例
    for var k := 1 to .UserObjects.MUs.Box.Capacity   // 每箱按 Box.Capacity 填满
        var part := .UserObjects.MUs.DummyPart.create(container) // 在 Box 容器内创建 DummyPart
        part._3D.VisibleGraphicGroups := ["Finished"]  // 显示 "Finished" 图形组
        if ?.statNumOut < ?.Number/2                   // `?.` 指当前调用方法的对象(Source)；statNumOut=已产出数
            part.Name := "Aubergine0"                  // 前一半命名 Aubergine0
            color := makeRGBValue(107, 0, 128)         // 紫色 RGB
        else
            part.Name := "Strawberry0"                 // 后一半命名 Strawberry0
            color := makeRGBValue(255, 0, 128)         // 粉红 RGB
        end
        part._3D.activateMaterialWithColor(color)      // 激活材质并着色
        part._3D.MaterialSpecularColor := color        // 高光颜色
        part._3D.MaterialShininess := 0.2              // 光泽度
    next
next
@.ConveyingDirection := 3                             // 设定 Source 的传送方向
```

- **`@`**：指当前 MU（在 Entrance/Exit 控制中为进入/离开的 MU）。
- **`?`**：指当前被调方法的对象（即 Source 本身），用于访问 `statNumOut`/`Number`。
- **`.UserObjects.MUs.Box.create(@)`**：绝对路径访问自定义类并用 `create(Location)` 在其位置创建实例。

### 2.2 TruckArrivals.OnEntrance —— 卡车限流与装载

```simtalk
if SupplyRoad.NumMU > 1          // 若道路已有 >1 辆等待卡车
    TrucksMissed += 1            // 统计错过卡车数
    @.delete                     // 删除刚生成的卡车 MU
    return                       // 拒绝进入
end
for var i := 1 to @.Capacity     // @.Capacity 为卡车装载容量
    var palette := .UserObjects.MUs.Pallet.create(@)      // 在卡车(@)内创建 Pallet
    for var j := 1 to palette.Capacity                    // 每托盘容量
        var container := .UserObjects.MUs.Box.create(palette) // 托盘内创建 Box
        for var k := 1 to container.Capacity              // 每箱容量
            .UserObjects.MUs.Part.create(container)       // 箱内创建 Part（注意此处用 Part 而非 DummyPart）
        next
    next
    palette.MUHeightWithContent := palette.MUHeight + palette.ZDim*palette.Cont.MUHeight
    // 含内容高度 = 托盘自身高度 + Z向层数 × 内容物高度
next
```

- **`return`**：立即退出方法，实现"拒入"。
- **`MUHeightWithContent`**：MU 含内容总高度属性，后续入库堆垛时用于计算堆叠高度。

### 2.3 UnloadTruck —— 叉车路径点搬运

```simtalk
param CurrentTruck:object          // 传入待卸货卡车
TrucksArrived += 1                 // 累计到达卡车
var forklift := AGVPool.Cont       // 从 AGVPool 资源池取叉车(Transporter)
while not CurrentTruck.Empty       // 卡车非空循环
    forklift.Backwards := true     // 叉车倒车
    forklift.setRoute([M_RoadTurn,M_Road])  // 沿标记点 M_RoadTurn→M_Road 设定路径
    forklift.moveFork(0.4)         // 调整叉臂高度
    waituntil forklift.DestinationWasReached  // 等待到达目的地
    ...
    CurrentTruck.Cont.move(forklift)  // 卡车内容物移动到叉车上
    ...
    waituntil not StoreEntry.Full  // 等待入库缓冲非满
    forklift.setRoute([M_RoadTurn,M_StoreEntry])
    forklift.moveFork(0.5)
    waituntil forklift.DestinationWasReached
    wait forklift.moveFork(0.05)   // wait + 表达式：等待一段时间后执行叉臂微调
    forklift.cont.move(StoreEntry) // 叉车内容物移动到 StoreEntry
end
CurrentTruck.Stopped := false      // 释放卡车（恢复行驶）
```

- **`setRoute([...])`**：为 Transporter 设定由标记点（Marker）组成的路径。
- **`moveFork`**：叉车专用，升降叉臂。
- **`waituntil`**：阻塞等待条件成立（同步点，避免竞态）。
- **`move`**：移动 MU 到目标对象。

### 2.4 StoreExit.Init / OnExit / Unload —— 拉式出库与并行分发

```simtalk
// Init
while true
    stopuntil not StorageArea.Empty and self.~.Empty   // 等待仓库非空且自身空
    StorageArea.&removeProductTo.executeNewCallChain(1, @) // 异步执行链调用 removeProductTo 拉一件产品
    stopuntil self.~.Full                              // 等待自身满
end

// OnExit
self.~.&Unload.executeNewCallChain(1, PickAndPlaceTop, @, ?)
self.~.&Unload.executeNewCallChain(2, PickAndPlaceBottom, @, ?)
// 并行启动两条 Unload 调用链，分别给上下两个 PickAndPlace
stopuntil @.Empty          // 等待托盘清空
wait 4                     // 等 4 秒
@.delete                   // 删除空托盘

// Unload
param ypos:integer, target:object
for var i := 1 to 2
    box := @[2, ypos].cont  // @[行,列] 索引托盘坐标取内容箱
    box.move(target)        // 箱移动到目标
    stopuntil box.Location /= @  // 等待箱离开托盘
    box := @[1, ypos].cont
    box.move(target)
    stopuntil box.Location /= @
next
```

- **`self.~`**：`self` 为当前方法的对象，`~` 取上一级（父 Frame 或上级位置）。此处 `self.~` 指 StoreExit 自身所在位置。
- **`&removeProductTo` / `&Unload`**：方法引用（`&` 取方法对象），配合 `executeNewCallChain` 实现异步并发调用。
- **`executeNewCallChain(n, ...)`**：启动第 n 条并发调用链，多个链可并行执行。
- **`@[2, ypos]`**：用二维下标访问托盘（Container）内指定行列的 MU。

### 2.5 Production.Init / Line.OnExit —— AGV 车队与拉式分流

```simtalk
// Init
var startPos:length := 12
for var i := 1 to NumAGVs
    var agv := .UserObjects.MUs.AGV.create(Track, startPos)  // 在 Track 指定位置创建 AGV
    startPos -= agv.Length + 0.1                             // 递减位置
next

// Line.OnExit
PlatesInProduction += 1                 // 在制品计数 +1
if Polishing1.Polishing.Empty           // 判断抛光站是否为空
    @.move(2)                           // 空 → 走出口 2（抛光分支）
else
    @.move(1)                           // 忙 → 走出口 1（其它分支）
end
```

- **`@.move(n)`**：将 MU 从当前对象第 n 个后继出口移出，实现分流选路。

### 2.6 Milling.OnEntrance / OnExit / Reset —— 3D 动画 + 加工 + 阻塞处理

```simtalk
// OnEntrance
var poses := ?._3D.Poses          // 获取姿态对象(Poses)
poses.moveTo("DoorClosed")        // 播放关门姿态
waituntil poses.EndPoseWasReached // 等待姿态到位
?.startProcessing                 // 开始加工
if ?._3D.ExistsWithAnimation      // 3D 存在且有动画
    ?._3D.getObject("Tool").SelfAnimations.Work.play        // 播放刀具 Work 动画
    ?._3D.getObject("TurnPlate").SelfAnimations.playRotation(0, 360, 360/?.procTime)  // 转台旋转，转速与加工时间挂钩
end

// OnExit
param sender: object
if sender /= void                 // 因前置阻塞方释放而触发
    @.move(sender)                // 把 MU 移到刚释放的阻塞方
elseif @.Location /= ?            // 后置触发（MU 已不在本站）
    poses.moveTo("PlateCenter"); poses.moveTo("DoorOpen")   // 姿态复位
    waituntil poses.EndPoseWasReached
    self.~.IsAvailable := true    // 标记可用
else                              // 正常出料
    @._3D.VisibleGraphicGroups := ["Milled"]  // 切换为已铣削图形组
    poses.moveTo("PlateRight")
    waituntil poses.EndPoseWasReached
    @.move                         // 无参 move：默认出口移出
end

// Reset
self.~.IsAvailable := true
```

- **`poses.moveTo("...")`**：姿态动画切换（Milling 定义了 `DoorOpen`/`DoorClosed`/`PlateCenter`/`PlateRight` 等 Poses）。
- **`SelfAnimations.play / playRotation`**：子对象自动画播放。
- **`sender`**：`ExitCtrl` 可传参，当因前向阻塞解除时系统传入阻塞方对象。

### 2.7 WMS 系列 —— 立体仓库库存管理

```simtalk
// placeIntoStock
param Pallet: object := void, product: string := "", quantity: integer := 0 -> boolean
if pallet = void then pallet := @ end
if product = "" then
    if pallet.InternalClassName="Piece" then product := pallet.Name
    else product := when pallet.empty then pallet.name else pallet.cont.name end
end
if quantity = 0 then
    if pallet.InternalClassname="Piece" then quantity := 1
    else quantity := when pallet.empty then 1 else pallet.numMu end
end
getFreePlace(Racklane, Side, Column, Row, Product)  // 找空位（返回 Racklane/Side/Column/Row）
if Racklane = void or Column = 0 or Row = 0 then return false
else
    reserveBox(Racklane, Side, Column, Row)         // 预留货位
    Pallet.AutomaticRouting := false                // 关闭自动路由
    if Side ~= "left"
        Pallet.Destination := RackLane.RackLeft[Column,Row]   // 设定目标货位（左）
    else
        Pallet.Destination := RackLane.RackRight[Column,Row]  // 右
    end
    if pallet.getAttrNo("HBW_ProductName") <= 0 then
        pallet.createAttr("HBW_ProductName", "string")  // 动态创建自定义属性
    end
    pallet.HBW_ProductName := product
    ...
    return true
end
```

- **`-> boolean`**：方法返回值类型声明（返回 `true`/`false`）。
- **`when <cond> then A else B`**：SimTalk 条件表达式（三元运算）。
- **`getAttrNo` / `createAttr`**：查询/创建自定义属性编号。
- **`byRef` 参数**（getFreePlace/OneByOne 中）：引用传递，用于回传多个结果。

```simtalk
// getFreePlace + OneByOne
switch StrategyIndex      // 按策略编号分派
case 1 OneByOne(...)
case 2 Random(...)
case 3 Predefined(...)
case 4 XYZ(...)
else debug
end

// OneByOne 中
rack.setCursor(1,1)       // 光标定位到 (1,1)
if rack.find(0) then      // 在占用表中查找值 0（空位）
    Column := rack.CursorX; Row := rack.CursorY; Side := "left"
end
```

- **`setCursor` / `find` / `CursorX` / `CursorY`**：DataTable 光标查找机制，定位第一个匹配单元格。

```simtalk
// reserveBox
if OccupancyTable[Column, Row] = 0 then
    OccupancyTable[Column, Row] := 1   // 标记占用
    NumFreePlaces -= 1                 // 全局空闲数 -1
    NumOccupiedPlaces += 1             // 全局占用数 +1
    return true
else return false end
```

```simtalk
// removeProducts
var PalletList := Inventory["Pallets", ProductRow]   // 取产品对应的托盘列表
PalletList.findCeil({2,1}..{2,*}, Rest)              // 在数量列查找 ≥Rest 的最小值
if PalletList.CursorY > 0 then
    var Pallet := PalletList["Pallet", PalletRow]
    ...
    Racklane.appendOrder(Column, Row, side, OrderNo) // 生成出库任务
    removeProduct(Product, numProducts)              // 扣减库存
    PalletList.cutRow(PalletRow)                     // 删除 Inventory 行
    Rest -= numProducts
end
```

- **`findCeil({2,1}..{2,*}, Rest)`**：在指定范围内查找大于等于目标值的最小值所在位置。
- **`cutRow`**：删除 DataTable 行。
- **`z_uniform(seed, low, high)`**（autoRemove 中）：均匀分布随机数生成函数（`seed=87`）。

---

## 三、依赖关系

> 每个代码块正常运行所依赖的外部对象 / 变量 / 表格 / 方法。

### 3.1 进货环节

| 代码块 | 依赖对象 / 方法 | 依赖变量 / 属性 | 依赖类 |
| --- | --- | --- | --- |
| Source.OnEntrance | `makeRGBValue`（内置函数） | `?.Number`、`?.statNumOut` | `.UserObjects.MUs.Box`、`.UserObjects.MUs.DummyPart` |
| TruckArrivals.OnEntrance | — | `SupplyRoad`（Conveyor）的 `NumMU`、`TrucksMissed`（Variable）、`@.Capacity` | `.UserObjects.MUs.Pallet`、`.UserObjects.MUs.Box`、`.UserObjects.MUs.Part` |
| TruckArrivals.Init | `self.~.Path.create` | — | 内置 Path |
| UnloadTruck | `AGVPool.Cont`、`forklift.setRoute/moveFork/move` | `TrucksArrived`、`M_RoadTurn`/`M_Road`/`M_Truck`/`M_StoreEntry`（Marker）、`StoreEntry`（Buffer） | Forklift（Transporter） |

### 3.2 入库与立体仓库

| 代码块 | 依赖对象 / 方法 | 依赖变量 / 表格 / 属性 |
| --- | --- | --- |
| StorageArea.storing | `Store.getFreePlace`、`Store.occupyPlace`、`portal.moveHook/moveToObject/moveToCranePosition/moveHookAbs/endSequence` | `Store.storingPortal`、`Store.StoreEntrance`、`crane.DefaultHookHeight`、`Store.Full`、`portal.state` |
| WMS.placeIntoStock | `getFreePlace`、`reserveBox` | `pallet.InternalClassName/Name/numMu/empty/cont.name`、`RackLane.RackLeft/RackRight`、`HBW_ProductName`/`HBW_ProductQuantity` 自定义属性 |
| WMS.getFreePlace | `OneByOne`/`Random`/`Predefined`/`XYZ` | `StrategyIndex` |
| WMS.OneByOne | — | `RackLanes`（DataList）、`lastIndex`、`racklane.OccupancyLeft/OccupancyRight` |
| WMS.reserveBox | — | `Racklane.OccupancyLeft/OccupancyRight`、`NumFreePlaces`、`NumOccupiedPlaces` |
| WMS.removeProduct | — | `Content`（DataTable）、`Content.getRowNo` |
| WMS.removeProducts | `getPalletLocation`、`removeProduct`、`Racklane.appendOrder` | `Content`、`Inventory`（DataTable，含 "Pallets"/"Pallet"/"Quantity" 列）、`PalletList.findCeil/cutRow` |
| WMS.autoRemove | `removeProducts` | `Content`、`MaxAmount`、`RemoveInterval`、`z_uniform` |
| WMS.WMS_Init | `&autoremove.executeIn` | `activateAutoRemove`、`startRemoveTime`、`RackLanes.dim`、`ShowMUsAsCuboids`、`_3D.MUAnimationAreaShowMUsAsCuboids` |
| WMS.INIT | `&WMS_init.executeIn` | — |

### 3.3 出库与配送

| 代码块 | 依赖对象 / 方法 | 依赖变量 / 属性 |
| --- | --- | --- |
| StoreExit.Init | `StorageArea.&removeProductTo.executeNewCallChain` | `StorageArea.Empty`、`self.~.Empty/Full` |
| StoreExit.OnExit | `self.~.&Unload.executeNewCallChain` | `PickAndPlaceTop`/`PickAndPlaceBottom`、`@.Empty` |
| StoreExit.Unload | `box.move` | `@[行,列]` 托盘坐标、`box.Location` |
| StorageArea.removeProductTo | `store.getPlaceOfProduct`、`rootfolder.Internal.Methods.getTargetPosition`、`crane.calculateTargetPosition`、`portal.movePortalTo/moveHookAbs/moveToCranePosition/endSequence`、`store.freePlace` | `store.Content`（含 "Quantity" 列）、`RemovingPortal`、`portal.state`、`_3D.getMUAnimationPosition` |

### 3.4 生产线内部

| 代码块 | 依赖对象 / 方法 | 依赖变量 / 属性 |
| --- | --- | --- |
| Production.Init | `.UserObjects.MUs.AGV.create` | `NumAGVs`、`Track`、`agv.Length` |
| Production.Line.OnExit | `@.move` | `PlatesInProduction`、`Polishing1.Polishing.Empty` |
| Milling.OnEntrance | `?._3D.Poses.moveTo`、`?.startProcessing`、`getObject("Tool"/"TurnPlate").SelfAnimations` | `?._3D.ExistsWithAnimation`、`?.procTime` |
| Milling.OnExit | `@.move`、`poses.moveTo` | `sender`、`@.Location`、`self.~.IsAvailable`、`@._3D.VisibleGraphicGroups` |
| Milling.Reset | — | `self.~.IsAvailable` |
| userSetTarget | `Warehouse.WMS.placeIntoStock` | `@.MUHeightWithContent`、`@.Cont.Cont.Name` |

### 3.5 跨模块依赖链总结

```
Source.OnEntrance ──创建──> Box / DummyPart（Aubergine/Strawberry）
TruckArrivals.OnEntrance ──创建──> Truck > Pallet > Box > Part
UnloadTruck ──AGVPool 取叉车──> 搬运到 StoreEntry
StoreEntry.ExitCtrl ──> StorageArea.storing ──> getFreePlace/occupyPlace + MultiPortalCrane
StoreExit.Init ──> StorageArea.removeProductTo ──> getPlaceOfProduct/freePlace + RemovingPortal
StoreExit.OnExit ──> Unload ──> PickAndPlaceTop/Bottom（进入生产线）
Production.Init ──> AGV.create（线内车队）
Production.Line.OnExit ──> 分流到 Polishing/其它
Milling.OnEntrance/OnExit ──> 3D 姿态 + startProcessing + VisibleGraphicGroups
userSetTarget ──> Warehouse.WMS.placeIntoStock ──> getFreePlace/reserveBox/OneByOne
```

---

## 附注：无法解析的片段

- 各对象的 `.jt` 文件（如 `Models/Factory51/StoreEntry.jt`、`StoreExit.jt`、`TruckArrivals.jt`、`TruckDepartures.jt`、`UpperStoreExit.jt`，以及 `UserObjects/**`、`ApplicationObjects/**` 下大量 `.jt`）为 Siemens JT 二进制格式（头部 `Version 10.8 JT DM 10.6.1.10`，内含 LZMA 压缩的 3D 图形与编译后源码），非明文 SimTalk，无法直接解析，故未纳入清单；其对应明文源码位于同目录 `.yaml` 的 `$CustomAttributes`/`Program` 字段。
- `Models/Factory51/$.jt` 为根 Frame 的 3D 场景二进制数据（588 行），同样无法解析为 SimTalk。
- `UserObjects/Warehouse/WMS/placeIntoStock.yaml`、`WMS_Init.yaml` 等派生 Method 仅含 `Origin`/`RandomSeed`/`UUID`，无 `Program`（其逻辑继承自 `ApplicationObjects/HBW3D/WMS/placeIntoStock.yaml` 等库内同名方法），本清单已引用库内原始源码。
