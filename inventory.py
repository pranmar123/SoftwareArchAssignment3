#Inventory

class Inventory:
    def __init__(self, category, item, price, count):        
        self.category = category    
        self.item = item
        self.price = price
        self.count = count

    #inventory list is a list of objects that are part of the inventory class
    def display_inventory(self):
        print(self.category + "\t" + self.item + "\t" + self.price + "\t"+ self.count)
        
    def update_inventory(self,quantityToSubtract):
        #integer version of self.count
        intSelfCount = int(self.count)
        intQuantityToSubstract = int(quantityToSubtract)
        self.count = str(intSelfCount-intQuantityToSubstract)

    

