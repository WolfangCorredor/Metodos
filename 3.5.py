
# coding: utf-8

# In[55]:

import math 
from tabulate import tabulate
n=0.0
fun1=0.0
fun2=0.0
funaux1=0.0
x=5.0
valver=math.pow(math.e, (-x))
errver=0.0
erraprox=0.0
funaux2a=0.0
fun2a=0.0
tab = []

for cont in range (0, 20):
    #funcion 1

    if(cont%2==0):
        funaux1=fun1
        fun1=fun1+(pow(x, cont)/math.factorial(cont))
        errver=(valver-fun1)
        errporver=(errver/valver)*100
        erraprox=((fun1-funaux1)/fun1)*100
        
        print erraprox
        
    else:
        funaux1=fun1
        fun1 = fun1-(pow(x, cont)/math.factorial(cont))
        errver=(valver-fun1)
        errporver=(errver/valver)*100
        erraprox=((fun1-funaux1)/fun1)*100
        print erraprox
        
    #funcion 2
    funaux2a=fun2a
    funaux2=fun2
    fun2a=fun2a+(pow(x, cont)/math.factorial(cont))
    fun2=1/fun2a
    errver2=(valver-fun2)
    errporver2=(errver2/valver)*100
    erraprox2=((fun2-funaux2)/fun2)*100
    tab.append([cont+1,fun1,errporver,erraprox,fun2,errporver2,erraprox2]) 
    #tab.append([cont,cont,cont,cont,cont,cont,cont])
      
print tabulate(tab,headers=["Valor","Aprox Fun1", "Er Porc F1", "Er Aprox F1", "Aprox Fun2", "Err. Porc2", "Er Aprox F2"])
    

