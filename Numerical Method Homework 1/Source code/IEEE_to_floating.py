# StudentID: 6388126
# Name: Apichaya Maneewong
# section: 2
# 3.convert a 32-bit binary string in IEEE-754 format into a decimal floating point number (base-10)
# test with the floating point number (base-10) 58.5625
# s = sign bit, e = exponent, f,m = mantissa
import math
in_s = input("input s: ") #String
in_e = input("input e: ")
in_f = input("input f: ")

#TODO: covert string to list
def convert(string):
    list1=[]
    list1[:0]=string
    return list1

#TODO: Convert e part = exponent = decimal - 127
# convert binary to decimal
# by find the position that being '1' and let sum all of 2^position
def convertE(e):
    listofe = convert(e)
    total = 0
    keepposof1 = []
    #TODO: find the position that being '1'
    for i in range(len(listofe)):
        if(listofe[i] == '1'):
            #first position is on the right side
            keepposof1.append((len(listofe)-1)-i)
    #TODO: do summation
    for y in keepposof1:
        total += 2**y
    total = total - 127
    return total

#TODO: convert f,m part 
# convert binary to floating point
# by find the position that being '1' and let sum all of 2^(-position)
def convertM(f):
    listofm = convert(f)
    total_m = 0.0
    keepposof1 = []
    for i in range(len(listofm)):
        if(listofm[i] == '1'):
            keepposof1.append(i+1)
    for y in keepposof1:
        total_m += (2**-y)
    return total_m

#TODO: calculate all of number the answer will be the decimal value
#formula = ((-1)**s)*(1+m)*(2**e)
s = int(in_s)
e = convertE(in_e)
m = convertM(in_f)
dec = ((-1)**s)*(1+m)*(2**e)
print("The decimal floating point number is: " + str(dec))