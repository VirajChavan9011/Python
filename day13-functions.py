#!/usr/bin/env python
# coding: utf-8

# In[1]:


def demo():
    print("hello")
    
demo()


# In[2]:


def add_num(no1,no2):
    sum=no1+no2
    print(sum)
    
add_num(2,4)


# In[4]:


def add_num1():
    no1=int(input("enter 1 no"))
    no2=int(input("enter 1 no"))
    sum=no1+no2
    print(sum)
    
add_num1()


# In[5]:


def square_number():
    n1=int(input("enter number: "))
    square=n1*n1
    print(square)
    
square_number()
    


# In[6]:


def sq_number(n1):
    square=n1*n1
    print(square)
    
sq_number(4)


# In[8]:


def radius1():
    rad=float(input("enter radius: "))
    cir=3.142*rad*rad
    print(cir)

radius1()


# In[10]:


def word1(word):
    w=word.upper()
    print(w)
    
word1("omkar")


# In[13]:


def name1():
    fname=input("enter your first name :")
    lname=input("Enter your Last name :")
    tname=fname + " " + lname
    print(tname)
    
name1()


# In[16]:


def nam(fname,lname):
    tname=fname+ " " +lname
    print(tname)
    
nam("nick","roy")
    


# In[18]:


def side1(side):
    cube=side*side*side
    surface_area=6*side*side
    print("cube: ",cube)
    print("surface_area: ",surface_area)
    
side1(4)


# In[24]:


def vot(name,age):
    if age>18:
        print(name,"you can vote")
    else:
        print(name,"you can't vote")
    
vot("sam",20)


# In[32]:


def total_sal():
    salary=int(input("enter salary"))
    DA=(salary*10)/100
    HRA=(salary*5)/100
    print("your salary: ",salary) 
    print("DA:",DA) 
    print("HRA:",HRA)

total_sal()


# In[ ]:




