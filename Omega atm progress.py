from datetime import* 
from time import strftime 
user_details = {
             0:  {'Username': 'Edwin', 'pin': '1111', 'balance': {'ksh': 140, 'usd': 0}},
             1:  {'Username': 'George',   'pin': '2222', 'balance': {'ksh': 240, 'usd': 0}},
             2:  {'Username': 'Evah',     'pin': '3333', 'balance': {'ksh': 340, 'usd': 0}},
             3:  {'Username': 'Favour',   'pin': '4444', 'balance': {'ksh': 440, 'usd': 0}},
             4:  {'Username': 'Ellan',    'pin': '5555', 'balance': {'ksh': 540, 'usd': 0}},
             5:  {'Username': 'Ririmba', 'pin': '6666', 'balance': {'ksh': 640, 'usd': 0}}
                }


def login_details():
    print('Insert your card')
    login = input('Please enter your username: ')
    password = int(input('Enter your password: '))
    len = (user_details.__len__())
    global count
    count = 0
    success = False
    while count < len:
        if user_details[count]['Username'] == login and int(user_details[count]['pin']) == password:
            success = True
            print('successful login')
            menu1()
            break
        count += 1
    person = 0
    if success != True:
            print('Invalid Password, try again ')
    password = int(input('Please enter your Password again: '))
    login_details()


def menu1():
    success = True
    if success == True:
        print('Check balance -- 1')
        print('Deposit click -- 2')
        print('Withdraw click -- 3')
        print('Mini Statement click -- 4')
        print('Quit Click 5')
    menu = int(input('1, 2, 3, 4, or 5 '))
    if menu == 1:
        check_balance()
    elif menu == 2:
        deposit()
    elif menu == 3:
        withdraw()
    elif menu == 4:
        global username 
        username = user_details[count]['Username']
        global balance_kes 
        balance_kes = int(user_details[count]['balance']['ksh'])
        global balance_usd 
        balance_usd = int(user_details[count]['balance']['usd'])
        printreceipt()
    elif menu == 5:
            print('Are you sure you want to quit : Yes/ No')
    menu2 = input('Yes / No: ')
    if menu2 == 'Yes':
            print('Thank You for banking with us')
            login_details()
    elif menu == 'No':
            menu1()
        
    menu1()


def check_balance():
    global balance
    balance = user_details[count]['balance']['ksh']
    print('Your balance is: ' + str(balance))
    menu1()
    check_balance()


def deposit():
    balance = user_details[count]['balance']['ksh']
    amount1 = int(input('Enter the amount to deposit:'))
    bal1 = balance + amount1
    user_details[count]['balance']['ksh']=bal1
    user_name = user_details[count]['Username']
    print('Hurray! Deposit Successful')
    f = open ("%s.txt" %user_name, 'a')
    f.write ('\n ********OMEGA BANK LTD********** ' +  '\n  Deposit' + str(amount1))
    f.close()
    menu1()
    deposit()

 
def withdraw():
    balance = user_details[count]['balance']['ksh']
    amount2 = int(input('Enter the amount to withdraw: '))
    if amount2 > balance:
        print('Insufficient Funds: Work Harder :)')
    else:
        print('success')
    bal2=balance - amount2
    user_details[count]['balance']['ksh'] = bal2
    user_name = user_details[count]['Username']
    f = open ("%s.txt" %user_name, 'a')
    f.write ("\n Withdraw"+ str(amount2))
    f.close()
    menu1()
    withdraw()


#Function to printreceipt -- Creates a file with the username as a receipt.
def printreceipt():
    currentTime = datetime.now()
    readableTime = currentTime.strftime("%H:%M:%S") 
    print(readableTime)

    print("********OMEGA BANK LTD********** \n")
    print("Dear {}", username, "Your balance is as below: \n")
    print("\t \t Name: ", username + " \n")
    print("\t \t Balance in KES: ", str(balance_kes) + " \n")
    print("\t \t Balance in USD: ", str(balance_usd) + " \n")

    receiptFile = open("%s.txt" %username, "r")
    print(receiptFile.read())
    receiptFile.close
    # receiptFile.write("\n ********OMEGA BANK LTD********** \n")
    # receiptFile.write("Dear " + username + ", Your balance is as below: \n")
    # receiptFile.write("\t \t Name: " + username + " \n")
    # receiptFile.write("\t \t Balance in KES: " + str(balance_kes) + " \n")
    # receiptFile.write("\t \t Balance in USD: " + str(balance_usd) + " \n")
    # receiptFile.write("\n \t \t Time: " + str(readableTime) + " \t \t \n")
    # receiptFile.write("\t \t Thank You For banking with Us:) \t \t")
    menu1()
    printreceipt()
login_details()

