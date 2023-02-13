# StudentID: 6388126
# Name: Apichaya Maneewong
# section: 2
# 3.Find the n-term approximation of a function (T_n(x)) of sin(x) where n = 2, 4, 6, 8, 10.
# Plot T_n(x) against sin(x) in the way similar to the figure in slide 34.
#formular sin(x) = sigma(n=0 to infinity)(-1)^n*(x^2*n+1)/(2n+1)!
import matplotlib.pyplot as plt
import numpy as np
import math
nAll = [2, 4, 6, 8, 10]
# optional for the user
inn = int(input("Please choose the number of n = 2, 4, 6, 8, 10, or All(type: 1): "))
# TODO: (-1)^n*(x^2*n+1)/(2n+1)!
def findsin(n,x):
    result = 0
    for i in range(n):
        result += ((-1)**i)*(x**((2*i)+1))/math.factorial((2*i)+1)
    return result

#Plot graph session
count = 0 # to count if user type the wrong number
for i in nAll:
    # The condition for the optional that user choose 2, 4, 6, 8, or 10
    # you will got two result and line -> from real value of sin and the n-term approximation value
    if inn != 1 and inn == i: 
        x = np.arange(-10,10,0.1) #(start,stop,step)
        # line 1 points
        y = np.sin(x)       
        # plotting the line 1 points 
        plt.plot(x,y,'black')
        # line 2 points 
        # plotting the line 2 points 
        plt.plot(x, findsin(inn,x),'purple')
        #to grid
        plt.grid(True, which='Both')
        plt.xlabel('x - axis')
        # Set the y axis label of the current axis.
        plt.ylabel('y - axis')
        # Set a title of the current axes.
        plt.title('Plot T_n(x) against sin(x)')
        # show a legend on the plot
        info = 'n='+str(inn)
        plt.legend(['sin(x)', info])
        # Display a figure.
        plt.show()
    # The condition for the optional that user choose All of n include(2,4,6,8,10)
    # you will got 6 result and line -> from real value of sin and all of the n-term approximation value when n = 2 to 10
    elif inn == 1:
        x = np.arange(-10,10,0.1)   # start,stop,step
        y = np.sin(x)
        plt.plot(x,y,'black') # 
        plt.plot(x,findsin(2,x),'purple')
        plt.plot(x,findsin(4,x),'green')
        plt.plot(x,findsin(6,x),'yellow')
        plt.plot(x,findsin(8,x),'orange')
        plt.plot(x,findsin(10,x),'red')
        plt.grid(True, which='Both')
        plt.ylim(-5,5)
        plt.xlabel('x values from -10 to 10')  # string must be enclosed with quotes '  '
        plt.ylabel('sin(x) and the n-term')
        plt.title('Plot of sin and n-term from -5 to 5')
        plt.legend(['sin(x)', 'n=2','n=4','n=6','n=8','n=10'])      # legend entries as seperate strings in a list
        plt.show()
        break
    # The condition for the user who choose and type the wrong number.
    else: 
        count+=1
        if count==5:
            print("Please input the correct number!!")
            break
# !Warning!: The program will run util you close the pop-up graph.