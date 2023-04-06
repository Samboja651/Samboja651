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
savings_acc = []

input("Welcome, press Enter to continue ")
while True:
    def Home():
        atm = int(input("1. CREATE ACCOUNT \n2. LOGIN \n3. Forgot Password \n4. EXIT \nEnter: "))

        # create account
        if atm == 1:
            name = input("Enter username: ")
            password = int(input("Enter password: "))
            #delay = random.randint(1,5)
            #wait = time.sleep(2)
            print("checking username...")
            loading()
            # not allow duplicate username or password < 4 digits
            if name not in dbusername and password >= 1000:
                dbusername.append(name)
                con_password = str(password)
                dbstrpassword.append(con_password)
                dbuserpassword.append(password)
                print("please wait as we create your account")
                loading()
                print(" ")
                #delay = random.randint(2, 9)
                #time.sleep(delay)
                
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

            elif name in dbusername and password >=1000:
                print("username not available, choose another.")
                print(" ")
            elif name not in dbusername and password < 1000:
                print("password must be atleast 4 digits")
                print(" ")
            elif name in dbusername and password < 1000:
                print("username not available, choose another.")
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
                loading()
                print("login successful")
                print("Welcome, what do you want to do? ")
                # Transactions
                Transact()
                
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
            print("verifying username...")
            loading()
            #time.sleep(3)
            if ask in dbusername:
                # get the index of ask
                index = dbusername.index(ask)
                print("Your password is",dbuserpassword[index])
            else:
                print("Username doesn't exist")
            
            print(" ")

        elif atm == 4:
            end = input("Are you sure you want to exit, Y/N: ")
            if end == "Y" or end == "y":
                #delay = random.randint(1,9)
                #time.sleep(delay)
                loading()
                print("program terminated!")
                sys.exit("Thank you for transacting with MPESA")
            else:
                print("program retained")
                print(" ")
    
        
    def Transact():
        while True:
            select = int(input("1. DEPOSIT \n2. BALANCE \n3. WITHDRAW \n4. SAVINGS ACCOUNT \n5. LOGOUT \nEnter: "))

            # deposit cash
            if select == 1:
                amount = int(input("Enter amount to deposit: "))
                account.append(amount)
                print(amount,"has been deposited to your account")
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
                balance = 0
                for money in account:
                    balance = balance + money
                # no negative withdrawal
                if balance < withdraw:
                    print("Insufficient balance!")
                    print("The amount you can withdraw is ",balance)
                    print(" ")

                else:  
                    remove = -1 * withdraw
                    # update account
                    account.append(remove)
                    print(withdraw,"withdrawn")
                    print(" ")

            # saving account
            elif select == 4:
                saving_plan = (3,5,8,0.5)
                print("Here is the savings plan\n1. 4 months = ",
                      saving_plan[0],"%""\n2. 8 months = ",saving_plan[1],"%"
                      "\n3. 12 months = ",saving_plan[2],"%""\n4. Custom plan = "
                      ,saving_plan[3],"%")
                plan = int(input("Enter saving plan: "))
                if plan == 1:
                    balance = 0
                    for money in account:
                        balance = balance + money
                    save = int(input("Enter amount to save: "))
                    if balance < save:
                        print("Insufficient account balance")
                        print("The amount you can save is ",balance)
                        print(" ")
                    else:
                        print("saved")
                        print("savings maturing...")
                        #time.sleep(4)
                        loading()
                        print("Your savings has matured,check savings balance.")
                        # increase saving amount by plan selected
                        # lets call it matured saving ->    m_saving
                        m_saving = (save * (100 + saving_plan[0])/100)
                        print(m_saving)
                        savings_acc.append(m_saving)
                        n_save = -abs(save)
                        print(n_save)
                        account.append(n_save)
                        ask = input("Do you want to check your saving account balance? Y/N: ")
                        if ask == "Y" or ask == "y":
                            print("You saved",save,"and has matured to",m_saving)
                            money = 0
                            for savings in savings_acc:
                                money = money + savings
                            print("Your total savings balance is",money)
                        # update bal by storing save as negative value
                        else:
                            print("Your patience earned you, congrats")
                        print(" ")
                        print("Note - \nTo reinvest, you have to withdraw savings and repeat saving process")
                        re_save = input("Do you want to withdraw savings to your main account? Y/N: ")
                        if re_save == "Y" or re_save == "y":
                            withdraw = int(input("Enter amount to withdraw: "))
                            money = 0
                            for savings in savings_acc:
                                money = money + savings
                            if money < withdraw:
                                print("Insufficient savings balance")
                                print("The amount you can withdraw is ",money)
                            else:
                                print(withdraw,"has been moved to main account")
                                # update savings acc to remaining amount
                                rem = -abs(withdraw)
                                savings_acc.append(rem)
                                # update the main account
                                account.append(withdraw)
                        else:
                            print("returning to menu...")
                            loading()
            elif select == 5:
                print("logging out...")
                time.sleep(2)
                print(" ")
                break
                Home()
    # lets add a loading functionality
    def loading():
        delay = random.randint(1,3)
        print("loading",end = " ")
        time.sleep(delay)
        print(".",end = " ")
        time.sleep(delay)
        print(".",end = " ")
        time.sleep(delay)
        print(".",end = " ")
        time.sleep(delay)
        print(".")

    # calling the main functions
    Home()        

# Recommendations
# TODO1 - ensure account number cannot be manipulated - hint- datatypes
# TODO2 - Upgrade ATM to store data for multiuser separately
# Hint independent account for users and a main account to store all money
# TODO3 - user can send money to another user.
# TODO4 - generate receit in real time and date
# TODO5 - Savings account
# TODO6 - prevent guest login
# TODO7 - prevent similar accounts generation
# TODO8- prevent error when password entered has character
# TODO9 - consider using patterns in loading

