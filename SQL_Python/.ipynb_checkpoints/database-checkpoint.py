#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[3]:


def create_table():
    pms = input('create new table? Enter y/n: ')
    if pms == 'y':
        conn = sqlite3.connect('customer_list.db')
        cur = conn.cursor()
        table = input('Enter table name: ')
        requires = input('Enter columns and datatypes. Ex "first_name text, last_name text, age integer": ')
        
        try:
            cur.execute('CREATE TABLE {} ({})'.format(table, requires))
        except:
            pass
    elif pms == 'n':
        pass
    conn.commit()
    conn.close()


# In[6]:


def show_all(self):
    conn = sqlite3.connect('customer_list.db')
    cur = conn.cursor()
    #name = input('Enter table name to query: ')
    cur.execute('SELECT rowid, * FROM {}'.format(str(self)))
    items = cur.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()


# In[7]:


def add_one(table, value):
    conn = sqlite3.connect('customer_list.db')
    cur = conn.cursor()
    value = input('Enter customer information: ')
    cur.execute('INSERT INTO {} VALUES({})'.format(table, value))
    conn.commit()
    conn.close()


# In[9]:


def delete_one(table):
    conn = sqlite3.connect('customer_list.db')
    cur = conn.cursor()
    pms = input('You really want to delete data? Enter y/n: ')
    if pms == 'y':
        condition = input('Add conditions. Ex "rowid > 3"')
        pms2 = input('Are you ready? Enter y/n: ')
        if pms2 == 'y':
            cur.execute('DELETE FROM {} WHERE {}'.format(table, condition))
        elif pms2 == 'n':
            pass
    elif pms == 'n':
        pass
    conn.commit()
    conn.close()


# In[ ]:




