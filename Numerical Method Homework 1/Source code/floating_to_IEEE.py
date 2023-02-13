# StudentID: 6388126
# Name: Apichaya Maneewong
# section: 2
# 2.convert a floating point number (base-10) into IEEE-754
# test with the floating point number (base-10) 58.5625.
# s = sign bit, e = exponent, f,m = mantissa
import math
usernumber = input("input your number: ")
string_split = usernumber.split(".") # 58 , 0.5625
number = int(string_split[0])
floatnum = float("0."+string_split[1])

def inttobi(num):
#TODO: TO convert the decimal to binary
# divided the number by 2 until the number left 0
# The mod is the binary
    if(num<0): # for the negative number
        num = abs(num) 
    prev = 0
    current = num #(first current'58')
    listofmod = []
# do the loop for calculat (num/2)
    while(current > 0): 
        prev = current #prev is the current from previous loop
        current = math.floor(prev/2) 
        mod = prev%2
        listofmod.append(str(mod))
    # !!reminding: the correct answer is the reverse version
    #TODO: reverse version
    listrealbi = []
    for i in range(len(listofmod)):
        listrealbi.append(listofmod[len(listofmod)-i-1])

    return listrealbi

#TODO: stop the calculation of floating
# let float value * 2 until the answer is 1.0
# the answer is the same number as previous numbers
def tostopcalfloatpart(list,fnum):
    count = 0
    for i in list:
        if(fnum == i):
            count += 1
            if(count > 13): #will make binary have 32 bit by ignore the same result untill 13
                return True
    return False

# TODO: covert the floating part
def floattobi(fnum):
    prev = 0
    current = fnum
    listofnum = [] # keep binary part ex. '0'.5, '1'.6
    keepprev = [] # keep all answer that will use to compare in tostopcalfloatpart
    while (tostopcalfloatpart(keepprev,current)==False):
        prev = current
        current = prev*2
        keepprev.append(prev)
        string_split = str(current).split(".")        
        listofnum.append(string_split[0])
        current = float("0."+string_split[1])
        # keep the calculate part ex. 0.5, '1'.6 = 0.6
    return listofnum

#TODO: call all previous function and covert binary to IEEE format 
def convertbitoIEEE(number,floatnum):
    listbinum =inttobi(number) #call inttobi
    listbifloat = floattobi(floatnum) #call floattobi
    #TODO: condition and the format of positive number
    if(number>0):
        s = '0'
        #formula to find e = 127+e(from 1.110...*2^'e')
        expdec = 127+(len(inttobi(number))-1) #decimal version
        expbias = ''.join(inttobi(expdec)) #keep the bi version
        listbinum.remove(listbinum[0]) #remove this '1'.110...
        fraction = ''.join(listbinum) + ''.join(listbifloat)
    else: 
        s = '1'
        expdec = 127+(len(inttobi(number))-1)
        expbias = ''.join(inttobi(expdec))
        listbinum.remove(listbinum[0])
        fraction = ''.join(listbinum) + ''.join(listbifloat)
    print("s = "+s)
    print("e = "+expbias)
    print("f = "+fraction+"...")

convertbitoIEEE(number,floatnum)

