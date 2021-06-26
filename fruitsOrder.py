class FruitsOrder:
    def __init__(self, itemId, fruitName, fruitType, unitQtyOrdered, pricePerUnit):
        self.itemId = itemId
        self.fruitName = fruitName
        self.fruitType = fruitType
        self.unitQtyOrdered = unitQtyOrdered
        self.pricePerUnit = pricePerUnit

    def TotalPrice(self):
        return self.unitQtyOrdered*self.pricePerUnit

class FruitsStore:
    def __init__(self, fList, avFruitist):
        self.fList = fList
        self.avFruitist = avFruitist

    def getTotalPriceOfAvailableOrderedFruit(self, itemId):
        for item in self.fList:
            if itemId == item.itemId:
                avfruit = item.fruitName+"-"+item.fruitType
                if avfruit in self.avFruitist:
                    return item.TotalPrice()
        return None

    def getFruitWithLeastPrice(self):
        LeastPriceObject = self.fList[0]
        for i in range(len(self.fList)):
            if self.fList[i].TotalPrice() < LeastPriceObject.TotalPrice():
                LeastPriceObject = self.fList[i]
        return LeastPriceObject

noOfFruitsOrder = int(input())
FruitsOrderObjects = []

for i in range(noOfFruitsOrder):
    itemId = int(input())
    fruitName = input()
    fruitType = input()
    unitQtyOrdered = int(input())
    pricePerUnit = float(input())
    FruitsOrderObjects.append(FruitsOrder(
        itemId, fruitName, fruitType, unitQtyOrdered, pricePerUnit))
noOfAvFruits = int(input())
AvFruitsList = []

for i in range(noOfAvFruits):
    avFriuts = input()
    AvFruitsList.append(avFriuts)

FruitsStoreobject = FruitsStore(FruitsOrderObjects, AvFruitsList)
itemId = int(input())
totalPrice = FruitsStoreobject.getTotalPriceOfAvailableOrderedFruit(itemId)
LeastPrice = FruitsStoreobject.getFruitWithLeastPrice()

if totalPrice is None:
    print("itemID OR fruit not fount")
else:
    print(totalPrice)
print(LeastPrice.itemId)
print(LeastPrice.fruitName)
print(LeastPrice.fruitType)
print(LeastPrice.TotalPrice)