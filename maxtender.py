class Property:
    def __init__(self, property_type, property_value, max_bid_price):
        self.property_value = property_value
        self.property_type = property_type
        self.max_bid_price = max_bid_price


class Tender:
    def __init__(self, buyerName, property_type, bidPrice):
        self.buyerName = buyerName
        self.property_type = property_type
        self.bidPrice = bidPrice


def bidProperty(properties, tenders):
    for listedproperty in properties:
        for tender in tenders:
            if listedproperty.property_type == tender.property_type:
                if tender.bidPrice >= listedproperty.property_value and tender.bidPrice <= listedproperty.max_bid_price:
                    return tender


properties = []
tenders = []

# input
noOfProperty = int(input())
for i in range(noOfProperty):
    property_type = input()
    property_value = int(input())
    max_bid_price = int(input())
    properties.append(Property(property_type, property_value, max_bid_price))

noOfTenders = int(input())
print(noOfTenders)
for j in range(noOfTenders):
    buyerName = input()
    property_type = input()
    bidPrice = int(input())
    tenders.append(Tender(buyerName, property_type, bidPrice))

bid = bidProperty(properties, tenders)
print(bid.buyerName)
for i in range(noOfProperty):
    if properties[i].property_type == bid.property_type:
        continue
    print(properties[i].property_type)
