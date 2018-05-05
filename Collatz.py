#Imports
from scipy.stats import linregress
import matplotlib.pyplot as plt
import numpy as np
import random
import sys
from math import *
from PrimesArray import primes
na = np.array


#Collatz Function
def c(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

#Collatz Sequence generating function :!!! RETURNS PATH LEN
def cs(s):
    count = 0
    prev = s
    while True:
        x = c(prev)
        # print(x)
        if x == 2:
            #print("[COUNT] %s" % count)
            break
        else:
            count += 1
            prev = x
    return count

# Progress Bar: DIRECTLY from stack overflow ALL credit for this function to the author at https://stackoverflow.com/questions/3160699/python-progress-bar
def update_progress(progress):

    barLength = 10 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()

#Generate Points based off of a function of x

baseRule= lambda a : a #identity

# Generate Points up to a quantity= upperLim, based off of a function
def genPoints(upperLim,collatzSequenceFunction=cs,statusFunction=update_progress,silent=False,x_rule=baseRule,y_rule=baseRule):
    #Note the calculation may run faster if it is silent...
    y = []
    x = []
    for i in range(2, upperLim): ## 2!! o is not in the range of cs
        x.append(x_rule(i))
        y.append(collatzSequenceFunction(y_rule(i)))
        if not silent:
            statusFunction(round((i / (upperLim)) * 100) / 100)
    return [np.array(x), np.array(y)]


if __name__ == "__main__":

    #settings
    Points_Quantity=1000
    print("[Begin Generation]")

    #Maping rules for expiramentation
    yr = lambda y: primes[y]
    xr = lambda x : x/primes[x]

    #Generate Points
    points = genPoints(Points_Quantity,x_rule=xr,y_rule=yr)
    print("[End Generation]")

    #Graph Setup
    plt.title('Collatz of 2*n +1 numbers')
    plt.xlabel('x-Axis: x')
    plt.ylabel('y-Axis: Path Length to 2')

    #Plot the points
    print("[Plotting]")
    plt.scatter(points[0], points[1], c=(random.random(),random.random(),random.random()), s=np.pi * 3, alpha=0.5)
    plt.show()
    print("[Finished]")