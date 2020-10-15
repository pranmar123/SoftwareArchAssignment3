import authentication
import logout
import system
import inventory
import cart
def main():
    print("Welcome to the Online Shopping Center (OSC)")
    username, password = authentication.enterLoginInfo()
    #create a sucess boolean that returns true if authentication is sucessful
    sucess = authentication.checkLoginInfo(username,password)
    #if sucess is false then exit the program
    if sucess == False:
        raise Exception("The credentials entered are not valid. Exiting the program..")
    print("Login credentials accepted.")
    print("Restocking and initalizing inventory...")
    inventoryList = system.initalizeInventory()
    print("Initalizing cart for user: ", username)
    userCart = cart.Cart(username)

    
    #the only way this loop will break is if the user presses q
    while True:
        userChoice=int(input("Please choose an option: "))
        #if user wants to q then update quit to 1
        print("Enter 1 to display the inventory")
        print("Enter 2 to add items to the cart")
        print("Enter 3 to remove items from the cart")
        print("Enter 4 to display running total")
        print("Enter 5 to checkout")
        print("Enter 6 to see past purchase history")
        print("Enter 7 to quit the program")

        if userChoice == 7:
            break
        elif userChoice == 1:
            for i in inventoryList:
                i.display_inventory()

        #the way that adding Items and Removing Items will work is by
        #first doing everything locally, so ONLY in the cart we are going
        #to modify whenever the user adds or removes something
        #FINALLY in checkout is when we will go send the cart items to the 
        #inventory function (UPDATE INVENTORY)
        elif userChoice == 2:
            itemToAdd = input("What item would you like to add to your cart?")
            quantityToAdd = input("How many would you like to add?")
            item = inventory.Inventory(category="None",item=itemToAdd,price="None",count=quantityToAdd)
            userCart.cartContents.append(item)





    
    ## below is the start of idea on how to handle code going forward 
    ## as well as temporarily the logout function directly
    
    #while logoutNow==0:
        
    #    userChoice=input("Please choose an option (press q to logout): ")

    #    logoutNow=logout.logoutUser(userChoice)
    
        
main()
