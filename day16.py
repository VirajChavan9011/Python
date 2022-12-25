#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=lambda a:a*2
print(x(5))



# In[3]:


x=lambda a,b,c:a*b*c
print(x(2,3,4))


# In[5]:


l1=[1,2,3,4]
l2=list(map(lambda a:a*a,l1))
print(l2)


# In[7]:


l3=[12,13,1,3]
l4=list(filter(lambda a:a%3==0,l3))
print(l4)


# In[ ]:


w1=int(input("enter first number :"))
w2=int(input("Enter second number:"))


# In[10]:


w=lambda w1,w2:w1/w2
print(w(4,2))


# In[12]:


a=[4,-1,-5,15,-30]
a2=list(filter(lambda a:a>0,a))
print(a2)


# In[14]:


r=[5,8,9,12]
t=list(map(lambda r:r*3,r))
print(t)


# In[15]:


y=[8,3,11,5,9,10]
u=list(filter(lambda y:y%2==0,y))
print(u)


# In[16]:


a1=[5,6,2,3,1,4]
a2=list(map(lambda a1:a1*a1*a1,a1))
print(a2)


# In[ ]:




