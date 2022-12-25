#!/usr/bin/env python
# coding: utf-8

# In[2]:


#practice
for i in range(1,21): 
    if i%2==0:
        print("even number",i)
    else:
        print("odd number",i)
  


# In[4]:


#sets 

a={"apple",2,3,"banana",3,5}
print(a)


# In[5]:


print("banana" in a)


# In[6]:


a.add("orange")
print(a)


# In[7]:


a.add("mango")
print(a)


# In[8]:


b={"red","black","yellow"}

a.update(b)
print(a)


# In[9]:


a.remove("orange")
print(a)


# In[11]:


a.discard("apple")
print(a)


# In[12]:


s={11,22,55,59}
f={"red","green","black"}


# In[13]:


s.update(f)
print(s)


# In[33]:


if 55 in s:
    s.remove(22)
    print(s)
else:
    print(s)


# In[25]:


print(s)


# In[34]:


m={"color1":"red","color2":"black","color3":"yellow"}
print(m)


# In[37]:


for i in m:
     print(i)


# In[39]:


print(m["color2"])


# In[40]:


c=m["color2"]
print(c)


# In[42]:


y=m.get("color1")
print(y)


# In[43]:


for i in m.values():
     print(i)


# In[44]:


z=m.copy()
print(z)


# In[47]:


z.update({"color4":"blue"})


# In[48]:


print(z)


# In[49]:


capital={"italy":"rome","england":"london","india":"delhi"}
print(capital)


# In[50]:


for i in capital.values():
    print(i)


# In[51]:


my_dict={"data1":100,"data2":54,"data3":200}
print(my_dict)


# In[57]:


print( sum(my_dict.values()))


# In[ ]:




