#!/usr/bin/env python
# coding: utf-8

# In[69]:


menulist = []
dicmenu = {"ข้าวมันไก่":50, "ข้าวหมกไก่":45, "ข้าวไก่ย่าง":55}

    
    
while True:
    menuname = input("Please Enter Menu:")
    if menuname.lower() == "exit":
        break
    else:
        if menuname in dicmenu: 
            menulist.append([menuname,dicmenu[menuname]])
        else:
            print("ERROR please Enter Menu agian")
print("   ")        
print("Bill List".center(30,"-"))

def showmenu():
    total =0
    for i in range(len(menulist)):
        print(menulist[i][0],"                ",menulist[i][1]," THB")
        total = total+(menulist[i][1])
    print("Total Price ", total," THB")

showmenu()


# In[ ]:




