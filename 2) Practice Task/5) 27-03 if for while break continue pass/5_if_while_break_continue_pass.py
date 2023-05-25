#!/usr/bin/env python
# coding: utf-8

# In[6]:


number = int(input("Enter the number = "))

if number % 2 == 1:
    print("This is odd number")
else:
    print("This is even number")


# In[3]:


value = input("Enter the number = ")


if value.isdigit() == True:
    value = int(value)
    if (value >=0 and value <= 9):
        print("This value is number")

elif value.isdigit() == False:
    if (value >= 'a' and value <= 'z') or (value >= 'A' and value <= 'Z'):
        print("This values is charecter")
    else:
        print("This value is special cherecter")


# In[44]:


# Print First 10 natural numbers using while loop

digit = 1
while digit <= 10:
    print(digit)
    digit += 1


# In[46]:


# Print the following pattern 

for i in range(1,10):
    for j in range(1,i+1):
        print(j,end = '')
    print('')


# In[54]:


# Calculate the sum of all numbers from 1 to a given number

number_1 = int(input('Enter the number : '))
sum = 0
for i in range(1,number_1+1):
    sum += i
print(f'sum of 1 to {number_1} = ',sum)


# In[60]:


numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    print(i, end=", ")


# In[65]:


a = 23456
   
count = 0

while a !=0:
   print(a)
   a //= 10
   count += 1
print(count)


# In[79]:


for q in range(10,0,-1):
    for r in range(q,0,-1):
        print(r,end=" ")
    print(" ")


# In[3]:


for i in range(1,5):
    for j in range(1,i+1):
        print("*",end='')
    for k in range(5,1,-1):
        print(k,end='')
    print('')
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print('')
      

