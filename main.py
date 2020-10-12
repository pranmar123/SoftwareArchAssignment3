import authentication

def main():
    print("Welcome to the Online Shopping Center (OSC)")
    username, password = authentication.enterLoginInfo()
    #create a sucess boolean that returns true if authentication is sucessful
    sucess = authentication.checkLoginInfo(username,password)
    #if sucess is false then exit the program
    if sucess == False:
        raise Exception("The credentials entered are not valid. Exiting the program..")
    print("Login credentials accepted.")
    ##FINISHED the first part bullet of the requirements.
main()