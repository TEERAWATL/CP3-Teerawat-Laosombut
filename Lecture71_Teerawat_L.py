#!/usr/bin/env python
# coding: utf-8

# In[57]:


menulist = []
pricelist = []
total = 0
while True:
    menuname = input("Please Enter Menu:")
    if menuname.lower() == "exit":
        break
    else:
        menuprice = int(input("Price (THB) :"))
        menulist.append(menuname)
        pricelist.append(menuprice)
print("Bill List".center(20,"-"))

def showmenu():
    for i in range(len(menulist)):
        print(menulist[i],"--------------- ",pricelist[i]," THB")
    print("Total Price--------", sum(pricelist)," THB")

showmenu()

