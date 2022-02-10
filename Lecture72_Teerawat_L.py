#!/usr/bin/env python
# coding: utf-8

# In[64]:


menulist = []


while True:
    menuname = input("Please Enter Menu:")
    if menuname.lower() == "exit":
        break
    else:
        menuprice = int(input("Price (THB) :"))
        menulist.append([menuname,menuprice])
        
print("Bill List".center(20,"-"))

def showmenu():
    total =0
    for i in range(len(menulist)):
        print(menulist[i][0],"                 ",menulist[i][1]," THB")
        total = total+(menulist[i][1])
    print("Total Price--------", total," THB")

showmenu()


# In[ ]:




