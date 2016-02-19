
# coding: utf-8

# In[1]:

import math
e=0.0
n=0
Et=0.0
et=0.0
ea=0.0
es=0.05
e=0
while True: 
    e2=e
    e += ((1/2)**n)/math.factorial(n)
    Et=(math.exp(1/2))-e
    et=(Et/e)*100
    ea=((e-e2)/e)*100
    n = n+1
    cont =n-1
    print (str(cont)+"\t"+str(e)+"\t"+str(et)+"\t\t"+str(ea))
    if str(ea)<=str(es):
        break


# In[ ]:



