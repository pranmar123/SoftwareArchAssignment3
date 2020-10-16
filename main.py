import authentication
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
        print("Enter 1 to display the inventory")
        print("Enter 2 to add items to the cart")
        print("Enter 3 to remove items from the cart")
        print("Enter 4 to display running total")
        print("Enter 5 to checkout")
        print("Enter 6 to see past purchase history")
        print("Enter 7 to quit the program")
        userChoice=int(input("Please choose an option: "))
        #if user wants to q then update quit to 1
        
        if userChoice == 7:
            print("Exiting the program...")
            break
        elif userChoice == 1:
            print("Category: \t Item: \t Price: Count: ")
            for i in inventoryList:
                i.display_inventory()

        #the way that adding Items and Removing Items will work is by
        #first doing everything locally, so ONLY in the cart we are going
        #to modify whenever the user adds or removes something
        #FINALLY in checkout is when we will go send the cart items to the 
        #inventory function (UPDATE INVENTORY)
        elif userChoice == 2:
            userCart = cart.addItemToCart(userCart)
            total = cart.calculateRunningTotal(userCart, inventoryList)
            print("The current total of the cart is: $",total)
        
        elif userChoice == 3:
            userCart = cart.removeItemFromCart(userCart)
            total = cart.calculateRunningTotal(userCart, inventoryList)
            print("The current total of the cart is: $",total)

        elif userChoice == 4:
            total = cart.calculateRunningTotal(userCart, inventoryList)
            print("The current total of the cart is: $",total)

        elif userChoice == 5:
            confirm = system.checkout(total)
            if confirm == "Y":    
            #update inventory
                for i in userCart.cartContents:
                    for j in inventoryList:
                        if i.item == j.item:
                            j.update_inventory(i.count)
                #dispaly updated inventory
                print("Printing updated inventory...")
                print("Category: \t Item: \t Price: Count: ")
                for i in inventoryList:
                    i.display_inventory()
                #store past purchases
                system.storePastPurchases(userCart,username)
                #reset cart
                userCart.cartContents = []
            else:
                pass

        elif userChoice == 6:
            system.viewPastPurchases()

            
    
        
main()
