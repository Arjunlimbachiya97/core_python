#!/usr/bin/env python
# coding: utf-8

# In[2]:


# comment
'''
variable
datatype
'''

name = "Arjun"
print(name)


# In[4]:


name = "Vishal"
print(name)


# In[7]:


# give maltipal variable and values

first_name, last_name, surname = "Arjunkumar", "A.", "Limbachiya"
print(surname,first_name,last_name)


# In[15]:


# give maltipal variable one value

arjun = yogesh = "shreenath nagar society"
print(arjun)
print(yogesh)

del yogesh

print(arjun)


# In[16]:


# variable Constants variable value is not change

PAI = 11.24


# In[4]:


# Datatype

dt_1 = 'Arjun' # string
dt_2 = 12   # intiger
dt_3 = 2.4  # float
dt_4 = True # bool
dt_5 = False # bool
dt_6 = 1 + 3j # complex
list_1 = [1, 'name']
print(dt_6)

# List items are Ordered,Changeable,indexed,Allow Duplicates values
dt_7 = [1, 'Arjun', 2.5, True, dt_5, list_1]
print(dt_7)


# Tuple items are Ordered,Not Changeable,indexed,Allow Duplicates values
dt_8 = (1, 4, 'Ronak', 2.5, True, 1)
print(dt_8)


# Set items are not Ordered,not changeable,not indexing,not allow duplicates values
# but you can add or remove
dt_9 = {'arjun', 54, 'bhabhr', 'arjun'}
print(dt_9)


# Dictionary items are ordered,not indexing,keys not allow duplicates values
dt_10 = {'arjun' : 'mca', 'ronak' : 10, 'bhavin' : 10, 'ronak' : 28}
print(dt_10)


# In[ ]:




