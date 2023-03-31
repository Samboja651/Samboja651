# Hotel service, eat and pay

import sys
print("Welcome to Nokras Hotel")
menu = ["1.Pilau-ksh.120","2.Chips-ksh.100","3.Fish-ksh.150","4.Ugali-ksh.50","5.Coke_Soda-ksh.60"]
meal = []
bill = []

while True:
  select = int(input("1.MENU 2.BILL 3.CANCEL: "))
  if select == 1:
    for items in menu:
      print(items)
    order = int(input("What is your order? "))
    if order == 1:
      meal.append(order)
      cost = 120
      bill.append(cost)
      print("---------------")
      print("Here is your pilau ")
      print("Billed")
      print("---------------")
    elif order == 2:
      meal.append(order)
      cost = 100
      bill.append(cost)
      print("Enjoy your chips")
      print("---------------")
      print("Billed")
      print("---------------")
    elif order == 3:
      meal.append(order)
      cost = 150
      bill.append(cost)
      print("Enjoy the Fish")
      print("---------------")
      print("Billed")
      print("---------------")
    elif order == 4:
      meal.append(order)
      cost = 50
      bill.append(cost)
      print("Hmm yammy")
      print("---------------")
      print("Billed")
      print("---------------")
    elif order == 5:
      meal.append(order)
      cost = 60
      bill.append(cost)
      print("---------------")
      print("hmm refreshing")
      print("Billed")
      print("---------------")
  elif select == 2:
    total = 0
    for price in bill:
      total = total + price
    print("Your bill is ksh.",total)
    amount = int(input("To clear,enter the billed amount: "))
    if amount >= total:
      print("---------------")
      print("Bill Cleared!,Thank You, Precious customer")
      print("Welcome again")
      sys.exit()
      
    elif amount < total:
      balance = total - amount
      print("Your balance is",balance)
      clear = int(input("Please pay full balance: "))
    else:
      print("The managers has been notified, he's coming")
  elif select == 3:
    print("Welcome again")
    sys.exit()
    
    
      
    
