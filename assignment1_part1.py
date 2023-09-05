#!/usr/bin/env python
# coding: utf-8

# In[19]:


class ListDivideException(Exception):
    pass

def list_divide(numbers, divide=2):
    count = 0
    for num in numbers:
        if num % divide == 0:
            count += 1
    return count


def test_list_divide(test):
    if list_divide([1,2,3,4,5])!=2:
        return "Exception"
    elif list_divide([2,4,6,8,10])!=5:
        return "Exception"
    elif list_divide([30,54,63,98,100],divide=10)!=2:
        return "Exception"
    elif list_divide([])!=0:
        return "Exception"
    elif list_divide([1,2,3,4,5],divide=1)!=5:
        return "Exception"
    


    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




