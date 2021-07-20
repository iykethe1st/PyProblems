#!/usr/bin/env python
# coding: utf-8

# In[5]:


#import multp-precision module
from mpmath import mp
#define PI function
def pi_func():
    while True:
        #request input from user
        try:
            entry = input("Please enter an number of decimal places to which the value of PI should be calculated\nEnter 'quit' to cancel: ")
            #condition for quit
            if entry == 'quit':
                break
            #modify input for computation
            mp.dps = int(entry) +1
        #condition for input error
        except:
            print("Looks like you did not enter an integer!")
            continue
        #execute and print result
        else:
            print(mp.pi)
            continue
        


# In[ ]:




