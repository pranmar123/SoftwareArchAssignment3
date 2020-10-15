#system class
#ask payment
#complete purchase then updatE inventory
#do after inventory class
import inventory

def initalizeInventory():
    i1 = inventory.Inventory("Household Goods", "Lamp", "30.99", "10")
    i2 = inventory.Inventory("Household Goods", "Broom", "8.99", "20")
    i3 = inventory.Inventory("Household Goods", "Chair", "45.99", "30")
    i4 = inventory.Inventory("Household Goods", "Candle", "10.99", "40")

    i5 = inventory.Inventory("Books", "SW Testing", "150.99","10")
    i6 = inventory.Inventory("Books", "Algebra", "150.99","20")
    i7 = inventory.Inventory("Books", "History", "150.99", "30")
    i8 = inventory.Inventory("Books", "Physics", "150.99", "40")

    i9 = inventory.Inventory("Toys", "Iron Man", "21.99", "10")
    i10 = inventory.Inventory("Toys", "Thor", "21.99", "20")
    i11 = inventory.Inventory("Toys", "Hulk", "21.99", "30")
    i12 = inventory.Inventory("Toys", "Spiderman", "21.99", "40")

    i13 = inventory.Inventory("Small Electronics", "Headphones", "50.99", "10")
    i14 = inventory.Inventory("Small Electronics", "Phone Charger", "20.99", "30")
    i15 = inventory.Inventory("Small Electronics", "Game Controller", "80.99", "30")
    i16 = inventory.Inventory("Small Electronics", "Speaker", "40.99", "40")

    #moving all items to a list that contains the inventory objects
    inventoryList = []
    inventoryList.append(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16)
    return inventoryList


def purchase():
    #call cardNumber function
    #call system  inventory update
    pass
