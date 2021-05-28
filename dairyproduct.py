class DairyProduct:
    def __init__(self, dairyId, dairyBrand, producttype, price, grade):
        self.dairyId = dairyId
        self.dairyBrand = dairyBrand
        self.producttype = producttype
        self.price = price
        self.grade = grade
        
class ProductGrade:
    def __init__(self, dairyList, weightDict):
        self.dairyList = dairyList
        self.weightDict = weightDict

    def priceBasedOnBrandAndType(self, brand, type):
        for i in range(len(self.dairyList)):
            object = dairyList[i]
            if object.dairyBrand == brand and object.producttype == type:
                updateedPrice = object.price + \
                    object.price* self.weightDict[object.grade]/100
                result = object.dairyBrand + " : "+updateedPrice
                return result
            else:
                return None

NoOfProds = int(input())
dairylist = []
for i in range(NoOfProds):
    did = int(input())
    brand = input()
    ptype = input()
    price = int(input())
    grade = input()
    dairylist.append(DairyProduct(did, brand, ptype, price, grade))
wDict = {}
NoOfGrade = int(input)
for i in range(NoOfGrade):
    grade = input()
    value = input()
    wDict[grade] = value
brand = input()
btype = input()

ProductGrade(dairylist, wDict)
print(ProductGrade.priceBasedOnBrandAndType(brand, btype))
