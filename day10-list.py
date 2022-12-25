#!/usr/bin/env python
# coding: utf-8

# In[3]:


w=input("Enter one word:")
z=w.upper()
print(z)


# In[4]:


a=["apple","red","banana"]
b=["red","green"]

c=zip(a,b) #will match two list
print(list(c))


# In[5]:


for x,y in zip(a,b):
    print(x,y)


# In[11]:


list1=[1,2,3,4]
list2=[]
for i in list1:
    list2.append(i*i)
print(list2)


# In[9]:


l1=["mango","","apple","orange"]
v=list(filter(None,l1))
print(v)


# In[10]:


list1=["hello","tech"]
list2=["priya","rahul"]
for x,y in zip(list1,list2):
    print(x,y)


# In[12]:


l1=[40,30,10,15,40]
l2=l1.count(40)
print(l2)


# In[22]:


r1=[10,15,20,30,35]
roll_no=int(input("Enter roll no:"))
for i in r1:
    if roll_no==i:
        print("present")
    else:
        print("Absent")


# In[26]:


r1=[10,15,20,30,35]
roll_no=int(input("Enter roll no:"))
if roll_no in r1:
     print("present")
else:
    print("Absent")


# In[28]:


k1=[12,75,150,180,145,525,50]
for i in k1:
    if i>500:
        break
    elif i>150:
        continue
    elif i%5==0:
        print(i)


# In[29]:


e1=[4,6,8,12,16]
print(min(e1))
print(max(e1))


# In[31]:


x=[23,25,12,16,25]
if x[0]==x[-1]:
    print("first and last values are same")
else:
    print("first and last values are not same")


# In[38]:


print(list(range(4,30,2)))


# In[ ]:




