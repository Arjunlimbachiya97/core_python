#!/usr/bin/env python
# coding: utf-8

# In[8]:


"""
1) Type Conversion
2) I/O and import
3) Operators
4) Namespace
"""

# 1) Type Conversion

# Implicit Type Conversion
# convert datatype autometicaly lower data type to the higher data type
number_1 = 20
number_2 = 20.73

sum = number_1 + number_2
print(sum)

# Explicit Type Conversion
mobile = "6354020482"
mobile = int(mobile)
print(type(mobile))


# In[18]:


# print function parameters
value = 12
print("this is value of ",value, sep = '  ')


# In[20]:


print('Hello', end = ' ')
print('hyperlink')


# In[28]:


# Operators

# Arithmetic Operators
a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a//b)
print(a**b)


# In[39]:


# Assignment Operators

c = 50
a = 11
c //= a
print(c)
print(c)
c += a
print(c)
c -= a
print(c)
c *= a
print(c)
c /= a
print(c)
c %= a
print(c)
c **= a
print(c)


# In[41]:


# Comparison Operators

d = 14
e = 39

print(d == e)
print(d > e)
print(d >= e)
print(d < e)
print(d <= e)
print(d != e)


# In[49]:


# Logical Operators
f = 10 
g = 20

print((f < g) and (f == 10))
print((f < g) or (f == 11))
print(not(f < g))


# In[50]:


# Bitwise operators


# In[54]:


# Special operators

list_1 = [1, 23, 4, 5, 6, 7, "Arjun"]
list_2 = [1, 23, 4, 5, 6, 7, "Arjun"]

# check value memory location
print(list_1 is list_2)
print(list_1 is not list_2)


# In[58]:


# Membership operators

list_3 = ['Bhabhar', 1, 23, 4, 5, 6, 7, "Arjun"]

print('Bhabhar' in list_3)
print('sdkjb' not in list_3)


# In[59]:


# Namespace

# global_var is in the global namespace
global_var = 10

def outer_function():
    #  outer_var is in the local namespace 
    outer_var = 20

    def inner_function():
        #  inner_var is in the nested local namespace 
        inner_var = 30

        print(inner_var)

    print(outer_var)

    inner_function()

# print the value of the global variable
print(global_var)

# call the outer function and print local and nested local variables
outer_function()

