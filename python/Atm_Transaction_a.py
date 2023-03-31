# ATM transactions in a terminal
import sys
import time
import random

# database
dbusername = []
dbuserpassword = []
dbstrpassword = []
account_number = []
# all the money is stored in a list
# thats where we get balance and withdraw
account = []

input("Welcome, press Enter to continue ")
while True:
    atm = int(input("1. CREATE ACCOUNT 2. LOGIN 3. Forgot Password : "))

    # create account
    if atm == 1:
        name = input("Enter username: ")
        dbusername.append(name)
        password = int(input("Enter password: "))
        con_password = str(password)
        dbstrpassword.append(con_password)
        dbuserpassword.append(password)
        print("please wait as we create account...")
        delay = random.randint(1, 9)
        time.sleep(delay)
        print("account created successfully")

        # generate account number
        account_no_derive = "0123456789"
        length = 9
        account_num = "".join(random.sample(account_no_derive, length))
        account_number.append(account_num)
        print("Your account number is", account_num)
        time.sleep(1)
        print("go to login")
        print(" ")

    # login
    elif atm == 2:
        lgname = input("Enter your username: ")
        lgpassword = int(input("Enter your password: "))
        lg_str_password = str(lgpassword)
        # Enabling multi user functionality
        # setting default value 2 mean nul
        login_name = []
        login_password = []

        # check username
        if lgname in dbusername:
            # 0 mean found
            login_name_true = 0
            login_name.append(login_name_true)
        else:
            # 1 mean not found
            login_name_false = 1
            login_name.append(login_name_false)

        # check user password
        if lg_str_password in dbstrpassword:
            # 0 mean found
            login_password_true = 0
            login_password.append(login_password_true)
            # print(" ")
        else:
            # 1 mean not found
            login_password_false = 1
            login_password.append(login_password_false)

        # validate user
        if login_name[0] == 0 and login_password[0] == 0:
            # remove the 0's or 1's from logins
            login_name.pop()
            login_password.pop()
            print(" ")
            print("authenticating data...")
            time.sleep(3)
            print("login successful")
            print("Welcome, what do you want to do? ")
            while True:
                select = int(input("1. DEPOSIT 2. BALANCE 3. WITHDRAW 4. LOGOUT : "))

                # deposit cash
                if select == 1:
                    amount = int(input("Enter amount to deposit: "))
                    account.append(amount)
                    print("Deposit made successful")
                    print(" ")

                # get balance
                elif select == 2:
                    balance = 0
                    print(balance)
                    for money in account:
                        balance = balance + money
                        print("Your balance is Ksh.", balance)
                    print(" ")

                # withdraw cash
                elif select == 3:
                    withdraw = int(input("Enter amount to withdraw: "))
                    # store withdraw as a negative value in account
                    remove = -1 * withdraw
                    # update account
                    account.append(remove)
                    print("withrawn")
                    print(" ")

                # logout user
                elif select == 4:
                    print("logged out!")
                    sys.exit()
        # Incorrect username | password
        elif login_name[0] == 1 and login_password[0] == 1:
            print("Invalid credentials !")
            print(" ")
        # another possibility
        elif login_name[0] == 0 and login_password[0] == 1:
            print("Invalid credentials !")
            print(" ")
        # another possibility of incorrect username or password
        elif login_name[0] == 1 and login_password[0] == 0:
            print("Invalid credentials !")
            print(" ")

    # forgot password
    elif atm == 3:
        ask = input("What is your username? ")
        if ask in dbusername:
            # get the index of ask
            index = dbusername.index(ask)
            print("Your password is",dbuserpassword[index])
        else:
            print("Username doesn't exist")
        
        print(" ")

# Recommendations
# TODO1 - ensure account number cannot be manipulated - hint- datatypes
# TODO2 - Upgrade ATM to store data for multiuser
# TODO3 - user can send money to another user.
# TODO4 - prevent negative withdraw
# TODO5 - generate receit
# TODO6 - Savings account
# TODO7 - Use dots in processing
# TODO8 - prevent guest login
# TODO9 - prevent similar accounts generation
# TODO10 - Update forgot password
