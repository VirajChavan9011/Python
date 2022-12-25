#!/usr/bin/env python
# coding: utf-8

# #tuples are immutable means not changable
# to change tuple we have to first convert into list

# In[2]:


x=("apple","orange",2,3.4)
print(x)


# In[3]:


for i in x:
    print(i)


# In[5]:


y=list(x)  #changing tuple to list
print(y)


# In[6]:


y[1]="kiwi"
print(y)


# In[7]:


x=tuple(y) #changing list to tuple
print(x)


# In[8]:


print(x[1::])  #slicing


# In[ ]:


t1=("red","yellow","green")  #packing
(a,b,c)=t1    #unpacking
print(a)
print(b)
print(c)


# In[10]:


p1=(4,5,"red",3.5)
s=list(p1)
s.append("orange")
p1=tuple(s)
print(p1)


# In[11]:


a,s,d,f,g=p1
print(a)
print(s)
print(d)
print(f)
print(g)


# In[12]:


p2=(5,"10",2.5,6)


# In[22]:


p3=p1+p2
print(p3)
p4=("orange",)
p5=p3+p4
print(p5)


# In[24]:


e1=(11,22)  #swaping
e2=(99,88)
e3=e1,e2=e2,e1
print(e3)


# In[32]:


r=(10,20,30,40,50)
r1=list(r)
r2=r1[::-1]
print(r2)


# In[33]:


r=(10,20,30,40,50)
print(r[::-1])


# In[36]:


o=("white",[11,22,33],[5,15,25])
o[1][1]=222
print(o)


# In[37]:


#find occurance of 50
b=(50,10,60,70,50)
b1=b.count(50)
print(b1)


# In[ ]:




