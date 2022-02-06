#!/usr/bin/env python
# coding: utf-8

# In[36]:



print("Please, Enter your Username and Password")
user = input("Username :")
password = int(input("Password :"))
if user.upper() == "CUSTOMER" and password == 1234:
    print("----------------------")
    print("---Welcom To A shop---")
    print("please select an option below")
    water = 10
    egg = 5
    apple = 15
    print("----------------------")
    print("option 1 = Water x 1  :", water, "BTH")
    print("option 2 = Egg   x 1  :", egg,   "BTH")
    print("option 3 = Apple x 1  :", apple, "Baht")
    select = int(input("Option :"))
    
    if select == 1:
        item = "Water"
        number = int(input("Enter number of item :"))
        total = water*number
        
    elif select == 2:
        item = "Egg"
        number = int(input("Enter number of item :"))
        total = egg*number
        
        
    elif select == 3:
        item = "Apple"
        number = int(input("Enter number of item :"))
        total = apple*number
        
    else:
        item = "Not found"
        number = 0
        total = 0
    print("-----------------------")    
    
    print(item,"---------------","x", number, "\ntotal =", total, "BTH")
    
        
elif user.upper() == "CUSTOMER" and password != 1234:
    print("Your password is incorrect.\n Please try again")
else: 
    print("Your username is incorrect. \n Please try again")


# In[ ]:




