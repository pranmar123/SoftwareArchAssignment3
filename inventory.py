#Inventory

class inventory:
    def __init__(self, category, item, price):        
        self.category = category    
        self.item = item
        self.price = price


i1 = inventory("Household Goods", "Lamp", float(30.99))
i2 = inventory("Household Goods", "Broom", float(8.99))
i3 = inventory("Household Goods", "Chair", float(45.99))
i4 = inventory("Household Goods", "Candle", float(10.99))

i5 = inventory("Books", "SW Testing", float(150.99))
i6 = inventory("Books", "Algebra", float(150.99))
i7 = inventory("Books", "History", float(150.99))
i8 = inventory("Books", "Physics", float(150.99))

i9 = inventory("Toys", "Iron Man", float(21.99))
i10 = inventory("Toys", "Thor", float(21.99))
i11 = inventory("Toys", "Hulk", float(21.99))
i12 = inventory("Toys", "Spiderman", float(21.99))

i13 = inventory("Small Electronics", "Headphones", float(50.99))
i14 = inventory("Small Electronics", "Phone Charger", float(20.99))
i15 = inventory("Small Electronics", "Game Controller", float(80.99))
i16 = inventory("Small Electronics", "Speaker", float(40.99))




