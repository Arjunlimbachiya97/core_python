#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Identifiers/Variable and keywords


#Identifiers/Variable
# case sensitive
name = 'Arjun'
Name = 'Arjun'

print(name)
print(Name)


# In[4]:


# contain (underscore _ , A-Z, a-z, 0-9) not start with number

_name = 'Vishal'
Empro_number = '3501'
mobile_1 = 1234567898 
mobile_2 = 9876543218

print(_name)
print(Empro_number)
print(mobile_1)
print(mobile_2)


# In[6]:


# give SyntaxError because name start with number

1_name = 'Ronak'
print(1_name)


# In[10]:


# keywords

import keyword as k
print(k.kwlist)


# In[23]:


# assert 
# if  given condition if false give AssertionError and you can give costom message.

#a = 4
#assert a > 5, 'value is small'


# In[30]:


# async, await 
# async for difine this is async function
# await sleep for given time

import asyncio

async def new_():
    print('Hello')
    await asyncio.sleep(3)
    print('world')


await new_()


# In[34]:


# raise for raise error by given condition is false

x = 2

if x < 1:
  raise Exception("Sorry, no numbers below zero")

print(x)


# In[36]:


# nonlocal for change global variable value in nested function

def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x 
    x = 'Arjun'
  myfunc2() 
  return x

print(myfunc1())


# In[45]:


# yield loop run one buy one with next(yield variable name) word

g = (2**x for x in range(100))
next(g)

