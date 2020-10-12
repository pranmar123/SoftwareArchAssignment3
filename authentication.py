def enterLoginInfo():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    return username,password

def checkLoginInfo(username, password):
    sucess = False
    #concatenate user and password to textfile format
    loginDetails = username + '@' + password
    with open("credentials.txt","r") as credentials:
        for line in credentials:
            #stripping the \n
            line = line.rstrip("\n")
            if loginDetails == line:
                sucess = True
                break
    return sucess