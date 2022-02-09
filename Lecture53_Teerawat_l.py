#!/usr/bin/env python
# coding: utf-8

# In[14]:


total_p = int(input("Enter your total price (THB):"))

def vat_calculation(total_p):
    result = total_p+(total_p*(7/100))
    return result

result = vat_calculation(total_p)
print("That comes to ",result," THB")


# In[ ]:




