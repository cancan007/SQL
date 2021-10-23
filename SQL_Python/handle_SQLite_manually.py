#!/usr/bin/env python
# coding: utf-8

# In[1]:


import database as db


# In[2]:


print('Welcome!')


# In[3]:


table = input('Enter table name: ')


# In[4]:


db.create_table(table)


# In[ ]:


pms1 = input('insert new value to table? Enter y/n: ')
if pms1 == 'y':
    db.add_one(table)
    while pms1 == 'y':
        pms1 = input('insert new value to table again? Enter y/n: ')
        if pms1 == 'y':
            db.add_one(table)
        elif pms1 == 'n':
            pass
elif pms1 == 'n':
    pass


# In[ ]:


pms2 = input('Do you want to query the table? Enter y/n: ')
if pms2 == 'y':
    db.show_all(table)
elif pms2 == 'n':
    pass


# In[ ]:


pms3 = input('Do you want to delete a value in the table? Enter y/n: ')
if pms3 == 'y':
    db.delete_one(table)
elif pms3 == 'n':
    pass


# In[ ]:


print('Congratulations! You are successful creating new table')


# In[ ]:


db.show_all(table)


# In[ ]:


#!jupyter nbconvert --to python handle_SQLite_manually.ipynb


# In[ ]:




