#!/usr/bin/env python
# coding: utf-8

# # 1st Project
# 

# In[2]:


a=int(input("Enter your age: "))
b=int(input("Enter your income: "))
if a<18:
    print("No tax")
elif(a>=18):
    if(b<500000):
        print((b*10)/100)
    else:
        print((b*20)/100)
        


# # 2nd project

# In[3]:


a=input("Enter the name of employee: ")
b=input("Enter the grade of employee(A\B\C): ")
c=int(input("Enter the salary of employee: "))
d=input("Enter the address of employye: ")
e=int(input("Enter the age of employee: "))
if b=="A":
    f=(5/100*c)
elif b=="B":
    f=(3/100)*c
else:
    f=(1/100)*c
#print("Bonus is ",f)   

# Bonus after salary
if c>50000:
    h=(10/100)*c
else:
    h=(5/100)*c
print("Total BONUS IS:",f+h )    

# tax

if c>50000:
    g=5/100*c
else:
    g=2/100*c
print("TOTAL TAX is ",g)    
    


# In[ ]:




