#cart class
#have functgionality ot add and remove items
#and keep running total
import authentication
import system
import inventory
class Cart:
    def __init__(self,username):
        #cartID is the username
        self.cartID = username + "cart"
        self.cartContents = []


def addItemToCart(userCart):
    itemToAdd = input("What item would you like to add to your cart?: ")
    quantityToAdd = input("How many would you like to add?: ")
    #make this an instance of inventory item
    item = inventory.Inventory(category="None",item=itemToAdd,price="None",count=quantityToAdd)
    #add item to the cart
    userCart.cartContents.append(item)
    return userCart

def removeItemFromCart(userCart):
    itemToRemove = input("What item would you like to remove to your cart? (this will remove all quanitites of the item in cart): ")
    #remove the said item
    for i in userCart.cartContents:
        if i.item == itemToRemove:
            userCart.cartContents.remove(i)
            return userCart
    else:
        print("Item not found in the cart...")
        return userCart
# Calculates the cart total
def calculateRunningTotal(userCart,inventoryList):
    total = 0.00
    for i in userCart.cartContents:
        for j in inventoryList:
            if i.item == j.item:
                total+= int(i.count) * float(j.price)
    return total

    
