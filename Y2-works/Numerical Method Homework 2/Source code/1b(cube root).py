# StudentID: 6388126
# Name: Apichaya Maneewong
# section: 2
# 1b.A program that can take a cube root of a number using Taylor Series expansion method.
# Stop the iteration of the program using stopping criterion.
# Test with the square root of the number 58.25.
import math
n_sqrt = float(input("Input the number of cube root here: "))
# from (1+x)**k -> (a+x)**k
k = 1/3 # for cube root

#TODO: calulate x to less than 1 (sqrt(i^3*(x/i^3))->i*sqrt(x/i^3)->(x/i^3)-1 
def findx(x):
    i=1
    while True:
        result = x/(i**3)
        i = i+1
        if(result>0 and result<2):
            break
    return i-1,result-1

a,x = findx(n_sqrt)
eps = 0.5*10**(2-4) # stop criterion (0.005)

def coef_k(k, n):
    result = 1
    for i in range(n):
        result = result*(k-i)
        # if i = 0, result = result*(k-0) = k
        # if i = 1, result = result*(k-1) = k*(k-1)...
    return result

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

total, prev, i, epa= 1, 1, 1, 1
while epa > eps:
    prev = total
    total += coef_k(k, i)*x**i/factorial(i)
    print("**********Step"+str(i)+"**********")
    print("prev: "+str(prev))
    print("total: "+str(total))
    print("epa: "+str(epa))
    if(i>1):
        epa = abs(total-prev)/total*100
    i += 1
total = a*total
print("**************************")
print("Program value:"+str(total))
print("Real value:"+str(n_sqrt**(1/3)))