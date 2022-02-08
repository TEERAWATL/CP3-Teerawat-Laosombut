#!/usr/bin/env python
# coding: utf-8

# In[9]:


def plus(a,b):
    c = a+b
    print(a,"+",b,"=",c)
    
def minus(a,b):
    c = a-b
    print(a,"-",b,"=",c)
    
def multiply(a,b): 
    c = a*b
    print(a,"*",b,"=",c)
    
def divide(a,b): 
    c = a/b
    print(a,"/",b,"=",c)
    
a = int(input("1_number="))
b = int(input("2_number="))

print("please select option to operate numbers.")
print("1=plus   2=minus   3=multiply   4=divide")
select = int(input("Enter the option:"))
if select == 1:
    plus(a,b)
elif select == 2:
    minus(a,b)
elif select == 3:
    multiply(a,b)
elif select == 4:
    divide(a,b)
else:
    print("Error, please try again")


# In[ ]:




