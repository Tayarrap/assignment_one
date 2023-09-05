#!/usr/bin/env python
# coding: utf-8

# In[15]:


#create a class called Book
class Book:
    def __init__(x, author, title):   #set to object variables
        x.author = author
        x.title = title
        
    def display(x):                   #create a function called display
        print(f"'{x.title}', written by {x.author}") #format string 
        
Book1 = Book ("J.K. Rowling", "Harry Potter and the Goblet of Fire") 
Book2 = Book ("Walter Scott", "Ivanhoe: A Romance")

Book1.display() #call display functions
Book2.display()


# In[ ]:





# In[ ]:





# In[ ]:




