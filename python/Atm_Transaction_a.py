# ATM transactions in a terminal
import sys
import random
from datetime import datetime
import time

# database
dbusername = []
dbuserpassword = []
dbstrpassword = []
account_number = []
# all the money is stored in a list
# thats where we get balance and withdraw
account = []
savings_acc = []

# date and time
sahii = datetime.now()
current_time = sahii.strftime("%H:%M:%S")
now = datetime.now()
today = now.strftime("%Y-%m-%d ")

input("Welcome, press Enter to continue ")
while True:
    def home():
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
                #loading()
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
                #time.sleep(1)
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
                #loading()
                print("login successful")
                print("Welcome, what do you want to do? ")
                # Transactions
                transact()
                
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
            #loading()
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
                #loading()
                print("program terminated!")
                sys.exit("Thank you for transacting with MPESA")
            else:
                print("program retained")
                print(" ")
    
        
    def transact():
        while True:
            select = int(input("1. DEPOSIT \n2. BALANCE \n3. WITHDRAW \n4. SAVINGS ACCOUNT \n5. LOGOUT \nEnter: "))

            # deposit cash
            if select == 1:
                amount = int(input("Enter amount to deposit: "))
                account.append(amount)             
                print("-----------------------------------------------------------------")
                print("Succeded, amount deposited to your account on",today,"\nis Ksh.",amount,"as at",current_time)
                print("-----------------------------------------------------------------")
                print(" ")

            # get balance
            elif select == 2:
                balance = 0
                #print(balance)
                for money in account:
                    balance = balance + money
                print("------------------------------------------------------------------")
                print("Your balance on",today,"is Ksh.", balance,"as at",current_time)
                print("------------------------------------------------------------------")
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
                    print("-------------------------------------------------")
                    print("Insufficient balance!")
                    print("The amount you can withdraw is Ksh.",balance)
                    print("-------------------------------------------------")
                    print(" ")

                else:  
                    remove = -1 * withdraw
                    # update account
                    account.append(remove)
                    print("------------------------------------------------")
                    print("Succeded, you have withdrawn Ksh.",withdraw,"\non",today,"as at",current_time)
                    print("------------------------------------- ----------")
                    print(" ")

            # saving account
            elif select == 4:
                saving_plan = (3,5,8,0.8,1)
                print("Here is the savings plan\n1. 4 months = ",
                      saving_plan[0],"%""\n2. 8 months = ",saving_plan[1],"%"
                      "\n3. 12 months = ",saving_plan[2],"%""\n4. Custom plan = "
                      ,saving_plan[3],"%""\n5. Compounding Interest = ",saving_plan[4],"%")
                plan = int(input("Enter saving plan: "))
                if plan == 1:
                    balance = 0
                    for money in account:
                        balance = balance + money
                    save = int(input("Enter amount to save: "))
                    if balance < save:
                        print("Insufficient account balance")
                        print("The amount you can save is Ksh.",balance)
                        print(" ")
                    else:
                        print("saved")
                        print("savings maturing...")
                        #time.sleep(4)
                        #loading()
                        print("Your savings has matured,check savings balance.\n")
                        # increase saving amount by plan selected
                        # lets call it matured saving ->    m_saving
                        m_saving = (save * (100 + saving_plan[0])/100)
                        #print(m_saving)
                        savings_acc.append(m_saving)
                        n_save = -abs(save)
                        #print(n_save)
                        account.append(n_save)
                        ask = input("Do you want to check your saving account status? Y/N: ")
                        if ask == "Y" or ask == "y":
                            print("---------------------------------------------------")
                            print("You saved Ksh.",save,"and has matured to Ksh.",m_saving)
                            money = 0
                            for savings in savings_acc:
                                money = money + savings
                            print("Your total savings balance is Ksh.",money)
                            print("----------------------------------------------------")
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
                                print("------------------------------------------------")
                                print("Insufficient savings balance")
                                print("The amount you can withdraw is Ksh.",money)
                                print("------------------------------------------------")
                            else:
                                print("----------------------------------------------")
                                print("Ksh.",withdraw,"has been moved to main account")
                                print("----------------------------------------------")
                                # update savings acc to remaining amount
                                rem = -abs(withdraw)
                                savings_acc.append(rem)
                                # update the main account
                                account.append(withdraw)
                        else:
                            print("returning to menu...")
                            #loading()
                            print("___________________")
                elif plan == 2:
                    balance = 0
                    for money in account:
                        balance = balance + money
                    save = int(input("Enter amount to save: "))
                    if balance < save:
                        print("----------------------------------------------")
                        print("Insufficient account balance")
                        print("The amount you can save is Ksh", balance)
                        print("----------------------------------------------")
                        print(" ")
                    else:
                        print("saved")
                        print("savings maturing...")
                        # time.sleep(4)
                        # loading()
                        print("Your savings has matured,check savings balance.\n")
                        # increase saving amount by plan selected
                        # lets call it matured saving ->    m_saving
                        m_saving = (save * (100 + saving_plan[1]) / 100)
                        # print(m_saving)
                        savings_acc.append(m_saving)
                        n_save = -abs(save)
                        # print(n_save)
                        account.append(n_save)
                        ask = input("Do you want to check your saving account balance? Y/N: ")
                        if ask == "Y" or ask == "y":
                            print("----------------------------------------------------------")
                            print("You saved Ksh.", save, "and has matured to Ksh.", m_saving)
                            money = 0
                            for savings in savings_acc:
                                money = money + savings
                            print("Your total savings balance is Ksh.", money)
                            print("----------------------------------------------------------")
                        # update bal by storing save as negative value
                        else:
                            print("______________________________")
                            print("Your patience earned you, congrats")
                            print("______________________________")
                        print(" ")
                        # use \033[34m to color code
                        print("Note - \nTo reinvest, you have to withdraw savings and repeat saving process")
                        re_save = input("Do you want to withdraw savings to your main account? Y/N: ")
                        if re_save == "Y" or re_save == "y":
                            withdraw = int(input("Enter amount to withdraw: "))
                            money = 0
                            for savings in savings_acc:
                                money = money + savings
                            if money < withdraw:
                                print("---------------------------------------------------")
                                print("Insufficient savings balance")
                                print("The amount you can withdraw is Ksh. ", money)
                                print("---------------------------------------------------")
                            else:
                                print("---------------------------------------------------")
                                print("Ksh.",withdraw,"has been moved to main account")
                                print("---------------------------------------------------")
                                # update savings acc to remaining amount
                                rem = -abs(withdraw)
                                savings_acc.append(rem)
                                # update the main account
                                account.append(withdraw)
                        else:
                            print("returning to menu...")
                            # loading()
                            print("___________________")

                elif plan == 3:
                    balance = 0
                    for money in account:
                        balance = balance + money
                    save = int(input("Enter amount to save: "))
                    if balance < save:
                        print("----------------------------------------------")
                        print("Insufficient account balance")
                        print("The amount you can save is Ksh.", balance)
                        print("----------------------------------------------")
                        print(" ")
                    else:
                        print("saved")
                        print("savings maturing...")
                        # time.sleep(4)
                        # loading()
                        print("Your savings has matured,check savings balance.\n")
                        # increase saving amount by plan selected
                        # lets call it matured saving ->    m_saving
                        m_saving = (save * (100 + saving_plan[2]) / 100)
                        # print(m_saving)
                        savings_acc.append(m_saving)
                        n_save = -abs(save)
                        # print(n_save)
                        account.append(n_save)
                        ask = input("Do you want to check your saving account balance? Y/N: ")
                        if ask == "Y" or ask == "y":
                            print("------------------------------------------------------------")
                            print("You saved Ksh.", save, "and has matured to Ksh.", m_saving)
                            money = 0
                            for savings in savings_acc:
                                money = money + savings
                            print("Your total savings balance is Ksh.", money)
                            print("------------------------------------------------------------")
                        # update bal by storing save as negative value
                        else:
                            print("______________________________")
                            print("Your patience earned you, congrats")
                            print("______________________________")
                        print(" ")
                        # use \033[34m to color code
                        print("Note - \nTo reinvest, you have to withdraw savings and repeat saving process")
                        re_save = input("Do you want to withdraw savings to your main account? Y/N: ")
                        if re_save == "Y" or re_save == "y":
                            withdraw = int(input("Enter amount to withdraw: "))
                            money = 0
                            for savings in savings_acc:
                                money = money + savings
                            if money < withdraw:
                                print("--------------------------------------------------")
                                print("Insufficient savings balance")
                                print("The amount you can withdraw is Ksh.", money)
                                print("--------------------------------------------------")
                            else:
                                print("--------------------------------------------------")
                                print("Ksh",withdraw, "has been moved to main account")
                                print("--------------------------------------------------")
                                # update savings acc to remaining amount
                                rem = -abs(withdraw)
                                savings_acc.append(rem)
                                # update the main account
                                account.append(withdraw)
                        else:
                            print("returning to menu...")
                            # loading()
                            print("___________________")

                elif plan == 4:
                    balance = 0
                    for money in account:
                        balance = balance + money
                    save = int(input("Enter amount to save: "))

                    duration = int(input("How many months do you want to save? "))
                    if balance < save:
                        print("----------------------------------------------")
                        print("Insufficient account balance")
                        print("The amount you can save is Ksh.", balance)
                        print("----------------------------------------------")
                        print(" ")
                    else:
                        print("saved")
                        print("savings maturing...")
                        # time.sleep(4)
                        # loading()
                        print("Your savings has matured,check savings balance.\n")
                        # increase saving amount by plan selected
                        # lets call it matured saving ->    m_saving
                        m_saving = (save * (100 + (duration * saving_plan[3])) / 100)
                        # print(m_saving)
                        savings_acc.append(m_saving)
                        n_save = -abs(save)
                        # print(n_save)
                        account.append(n_save)
                        ask = input("Do you want to check your saving account balance? Y/N: ")
                        if ask == "Y" or ask == "y":
                            print("---------------------------------------------------------")
                            print("You saved Ksh.", save, "and has matured to Ksh.", m_saving)
                            money = 0
                            for savings in savings_acc:
                                money = money + savings
                            print("Your total savings balance is Ksh.", money)
                            print("---------------------------------------------------------")
                        # update bal by storing save as negative value
                        else:
                            print("______________________________")
                            print("Your patience earned you, congrats")
                            print("______________________________")
                        print(" ")
                        # use \033[34m to color code
                        print("Note - \nTo reinvest, you have to withdraw savings and repeat saving process")
                        re_save = input("Do you want to withdraw savings to your main account? Y/N: ")
                        if re_save == "Y" or re_save == "y":
                            withdraw = int(input("Enter amount to withdraw: "))
                            money = 0
                            for savings in savings_acc:
                                money = money + savings
                            if money < withdraw:
                                print("-------------------------------------------------")
                                print("Insufficient savings balance")
                                print("The amount you can withdraw is Ksh.", money)
                                print("-------------------------------------------------")
                            else:
                                print("----------------------------------------------------")
                                print("Ksh.",withdraw, "has been moved to main account")
                                print("----------------------------------------------------")
                                # update savings acc to remaining amount
                                rem = -abs(withdraw)
                                savings_acc.append(rem)
                                # update the main account
                                account.append(withdraw)
                        else:   
                            print("returning to menu...")
                            # loading()
                            print("___________________")

                elif plan == 5:
                    print("Note - Compound interest is 1% compounded on monthly basis")
                    print("---------------------------------------------------------------------")
                    balance = 0
                    for money in account:
                        balance = balance + money
                    save = int(input("Enter amount to save: "))

                    duration = int(input("How many months do you want to save? "))
                    if balance < save:
                        print("----------------------------------------------")
                        print("Insufficient account balance")
                        print("The amount you can save is Ksh.", balance)
                        print("----------------------------------------------")
                        print(" ")
                    else:
                        print("saved")
                        print("savings maturing...")
                        # time.sleep(4)
                        # loading()
                        print("Your savings has matured,check savings balance.\n")
                        # increase saving amount by plan selected
                        # lets call it matured saving ->    m_saving
                        m_saving = save
                        for period in range(0, duration):
                            m_saving *= (100 + saving_plan[4])/100
                        # print(m_saving)
                        savings_acc.append(m_saving)
                        n_save = -abs(save)
                        # print(n_save)
                        account.append(n_save)
                        ask = input("Do you want to check your saving account balance? Y/N: ")
                        if ask == "Y" or ask == "y":
                            print("---------------------------------------------------------")
                            print("You saved Ksh.", save, "and has matured to Ksh.", m_saving)
                            money = 0
                            for savings in savings_acc:
                                money = money + savings
                            print("Your total savings balance is Ksh.", money)
                            print("---------------------------------------------------------")
                        # update bal by storing save as negative value
                        else:
                            print("______________________________")
                            print("Your patience earned you, congrats")
                            print("______________________________")
                        print(" ")
                        # use \033[34m to color code
                        print("Note - \nTo reinvest, you have to withdraw savings and repeat saving process")
                        re_save = input("Do you want to withdraw savings to your main account? Y/N: ")
                        if re_save == "Y" or re_save == "y":
                            withdraw = int(input("Enter amount to withdraw: "))
                            money = 0
                            for savings in savings_acc:
                                money = money + savings
                            if money < withdraw:
                                print("-------------------------------------------------")
                                print("Insufficient savings balance")
                                print("The amount you can withdraw is Ksh.", money)
                                print("-------------------------------------------------")
                            else:
                                print("----------------------------------------------------")
                                print("Ksh.",withdraw, "has been moved to main account")
                                print("----------------------------------------------------")
                                # update savings acc to remaining amount
                                rem = -abs(withdraw)
                                savings_acc.append(rem)
                                # update the main account
                                account.append(withdraw)
                        else:   
                            print("returning to menu...")
                            # loading()
                            print("___________________")
                           
                            
                           
            elif select == 5:
                print("_____________")
                print("logging out...")
                time.sleep(2)
                print(" ")
                break
                home()
    # lets add a loading functionality 
    def loading():
        import time
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

    # datetime
    def date():
        today = date.today()
        print(today)
        
    def time():
        current_time = time.strftime("%H:%M:%S")
        print(current_time)

    # calling the main functions
    home()        

# Recommendations
# TODO1 - ensure account number cannot be manipulated - hint- datatypes
# TODO2 - Upgrade ATM to store data for multiuser separately
# Hint independent account for users and a main account to store all money
# TODO3 - user can send money to another user.
# TODO6 - prevent guest login
# TODO7 - prevent similar accounts generation
# TODO8- prevent error when password entered has character
# TODO10 - improve security, how can we verify the person when forgot password is used
# TODO11 - SET MONEY AND OTHERS TO 2 DECIMAL PLACES

