#!/usr/bin/env python
# coding: utf-8

# In[18]:


def word1(key):
    d1={"a":100,"b":200,"c":300}
    if key in d1:
        print("this is present",key)
    else:
        print("this is not present",key)
        
word1("z")
   


# In[25]:


def ques():
    ans=str(input("Do you want to shutdown?(yes/No)"))
    if ans=="Yes" or ans=="yes":
            print("shutdown started")
    elif ans=="No" or ans=="no":
            print("shutdown Aborted")
    else:
            print("something is wrong! Answer correctly")
ques()


# In[47]:


def sum1():
    o=[1,2,3,4,5,6]
    sum=0
    for i in o:
        sum=sum+i
     
    print(sum)
           
sum1()



# In[39]:





# In[63]:


def sqre():
    o=[1,2,3,4,5,6]
    m=[]
    for i in o:
        square=i*i
        m.append(square)
       
    print(m)
sqre()


# In[ ]:




