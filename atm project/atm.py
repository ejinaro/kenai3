from ctypes.wintypes import PINT


def add_user():
    #Function to add user
    username = input("Enter username: ")
    pin = input("Enter Pin: ")
    user_usd_balance = 0.0
    user_kes_balance = 0.0
    user_details ={"name": username, "user_pin": pin, "balance" :{"USD" : user_usd_balance, "KES" : user_kes_balance} } 
    
    #Create a file and write to the file
    usersDB = open('Users.txt', 'a')
    usersDB.write(str(user_details))
    #print(user_details)



add_user()

    

