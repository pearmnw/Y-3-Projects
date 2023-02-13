# StudentID: 6388126
# Name: Apichaya Maneewong
# section: 2
# 2.A program that can evaluate the value of natural log of 11025 using Taylor Series expansion method.
# Then apply basic log property: log(a * b) = log(a) + log(b) and log(exp(k)) = k
# Formular
# ln(x) -> ln((e**i)*(x/e**i)) -> ln(e**i)+ln(x/e**i) which x/e**i < 1 -> ln(e**i)+ln(1+(x/e**i)-1)
# ln(e**i) = i ; ln(1+x) = ((-1)**n/(n+1))*(x**(n+1))
# i+ln(1+x) while x = ((x/e**i)-1)

import numpy as np
import math
num = int(input("please input the number of the natural log: "))
e = math.e
eps = 0.5*10**(2-4) # stop criterion (0.005)
#TODO: calulate x to less than 1 -> x = ((x/e**i)-1)
def findx(n):
    i=1
    while True:
        result = n/e**i 
        i = i+1
        if(result>0 and result<2):
            break
    return result-1,i-1

#TODO: ln(1+x) = ((-1)**n/(n+1))*(x**(n+1))
def findln(x):
    total,prev,epa,n = 0,0,1,0
    while epa > eps:
        prev = total
        total += ((-1)**n/(n+1))*(x**(n+1))
        print("**********Step"+str(n+1)+"**********")
        print("prev: "+str(prev))
        print("total: "+str(total))
        print("epa: "+str(epa))
        epa = abs(total-prev)/total*100 # approximation error % 
        n+=1
    return total

realn, r = findx(num)
result = r + findln(realn)
print("**************************")
print("Program value:"+str(result))
print("Real value:"+str(np.log(num)))
print(r)