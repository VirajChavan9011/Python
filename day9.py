#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=["apple","mango","banana"]


# In[4]:


print(a)


# In[5]:


z=[5,6,2,3,"black","red","green"]
print(z)


# In[8]:


for i in z:
    print(i)


# In[11]:


z.insert(2,"white")
print(z)


# In[21]:


for i in z:
    if i=="red":
        break
    print(i)


# In[22]:


z.remove("black")
print(z)


# In[24]:


L2=[4.3,2.3,7.8,"orange"]
z.extend(L2)
print(z)


# In[41]:


for  i in z:
    if i=="white":
        z.insert(3,"yellow")
    print(i)


# In[33]:


del z[5]


# In[48]:


print(z)


# In[35]:


z.insert(4,2)


# In[51]:


print(z)


# In[47]:


del z["yellow"==2]


# In[50]:





# In[54]:


for i in z:
    if i=="green":
        z.pop()
    print(i)


# In[ ]:




