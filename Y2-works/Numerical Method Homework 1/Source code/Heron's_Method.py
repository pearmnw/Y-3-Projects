# StudentID: 6388126
# Name: Apichaya Maneewong
# section: 2
# 1.take a square-root of a number n using the heron's method and digit adding method taught in class
# test with the square root of 19 (n = 19).  Use stopping criterion to stop your program.
import math
usernum = input("Enter number of square root: ")
stopcri = 0.005
n = int(usernum)
# formular = 1/2*(a+x/a)
# x = number of nonperfect sqrt, a = the perfect sqrt that nearest to x
# first a = guess but next a = result from the first calculate
# TODO: the calculation of heron's method
def sqrt_Heron(n_sqrt, stopcri): 
    guess = round(math.sqrt(n_sqrt))
    prev = 1    # previous num
    current = guess # current num
    count = 0 # To receive the step
    while(abs(current-prev)>stopcri):
        count += 1
        print("Step"+str(count)+ ": "+str(current))
        prev = current #(current from previous loop)
        current = (1/2)*(prev+(n_sqrt/prev))     # calulate the new value
    return current,count

result,count = sqrt_Heron(n,stopcri)
print("Step"+str(count+1)+ ": "+str(result))
print("The answer of Heron's method: "+str(result))
print("The answer of square root: "+ str(math.sqrt(n)))