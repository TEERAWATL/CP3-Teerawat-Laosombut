#!/usr/bin/env python
# coding: utf-8

# In[29]:


def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
        
def showmenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
       
def select():
    userSelected = int(input(">>"))
    return userSelected
        
def vatcalculator(price):
    vat = 7
    result = price + (price * vat / 100)
    return result

def pricecalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    price = price1+price2
    
    print("Price + 7% vat=",vatcalculator(price), "THB")

a = login()
if a==True:
    print(showmenu())
    b = select()
    if b == 1:
        price = int(input("Price (THB) : "))
        
        print("Price + 7% vat=",vatcalculator(price),"THB")
    elif b == 2:
        pricecalculator()
    else:
        print("Please select number 1 and 2 only.")
        
else:
    print("Please Try Agian")
    login()

    



# In[ ]:




