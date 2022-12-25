#!/usr/bin/env python
# coding: utf-8

# In[5]:


for i in range(1,11):
    if i%2==0:
        print("even number:",i)
    else:
        print("odd number",i)


# In[7]:


a=int(input("enter number: "))
for i in range(1,a+1):
    if i%2==0:
        print("even number:",i)
    else:
        print("odd number",i)


# In[11]:


a=int(input("enter number: "))
for i in range(1,a+1):
       print("Square:",i*i)
  
      


# In[13]:


a=int(input("enter number: "))
for i in range(1,a+1):
    if i%2==0:
        print("Suare:",i*i)
    else:
        print("cube:",i*i*i)


# In[23]:


a="apple"
for i in (a):
    if i=="l":
         break
    print(i)


# In[26]:


a = "abc"
for i in a:
    print(i*2,end=" ")


# In[5]:


a=int(input("enter number: "))
for i in range(1,a+1):
    if i>0:
        print("Positive",i)
for i in range(-1,-a):
    if -i<0:
        print("Negative",i)


# In[ ]:




