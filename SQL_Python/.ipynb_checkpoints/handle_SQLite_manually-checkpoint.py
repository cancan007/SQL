#!/usr/bin/env python
# coding: utf-8

# In[3]:


import database as db


# In[2]:


print('Welcome!')


# In[5]:


table = input('Enter table name: ')


# In[4]:


db.create_table()


# In[9]:


pms1 = input('insert new value to table? Enter y/n: ')
if pms1 == 'y':
    db.add_one(table)
    pms1 = input('insert new value to table again? Enter y/n: ')
elif pms1 == 'n':
    pass


# In[10]:


pms2 = input('Do you want to query the table? Enter y/n: ')
if pms2 == 'y':
    db.show_all(table)
elif pms2 == 'n':
    pass


# In[11]:


pms3 = input('Do you want to delete a value in the table? Enter y/n: ')
if pms3 == 'y':
    db.delete_one(table)
elif pms3 == 'n':
    pass


# In[ ]:




