# StudentID: 6388126
# Name: Apichaya Maneewong
# section: 2
# 1a.square root of a number using Taylor Series expansion method.
# Test with the square root of the number 58.25.
import math
n_sqrt = float(input("Input the number of square root here: "))
# from (1+x)**k -> (a+x)**k
k = 0.5 #1/2 from the square root
#TODO: calulate x to less than 1 (sqrt(i^2*(x/i^2))->i*sqrt(x/i^2)->(x/i^2)-1
def findx(x):
    i=1
    while True:
        result = x/(i**2) 
        i = i+1
        if(result>0 and result<2):
            break
    return i-1,result-1

a,x = findx(n_sqrt)
eps = 0.5*10**(2-4) # stop criterion (0.005)

#Formular is sigma(n=0) to infinity(k,n)*(x**n)
# = 1 + kx + (k*(k-1)/2!)(x**2) + (k*(k-1)*(k-2)/3!)(x**3)...
def coef_k(k, n):
    result = 1
    for i in range(n):
        result = result*(k-i)
        # if i = 0, result = result*(k-0) = k
        # if i = 1, result = result*(k-1) = k*(k-1)...
    return result

#TODO: factorial 
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
        epa = abs(total-prev)/total*100 # approximation error % 
    i += 1
total = a*total 
print("**************************")
print("Program value:"+str(total))
print("Real value:"+str(math.sqrt(n_sqrt)))