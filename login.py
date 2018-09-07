defuser = "YeoluXX" #Define User
defpass = "YeoluXX" #Define Password


user =input("User:") #İnput User
password =input("Password:") #İnput Password


if ((defuser == user) and (defpass == password)):
    print("Login Successful")
elif((defuser != user) and (defpass == password)):
    print("Your username is false.")
    print("Please try again")
elif ((defuser == user) and (defpass != password)):
    print("Your password is false.")
    print("Please try again")
elif ((defuser != user) and (defpass != password)):
    print("Your username and password is false")
    print("Please try again")