# import common functions
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir))+"\Common\\")
from Common_Functions import *


def Fibonacci(num):
    n = int(num)
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

num = 10
if(len(sys.argv) > 0):
    num = sys.argv[1]
time = Time(Fibonacci, "Fibinachi Time: ", num)
#show processor useage for program
processorInfo(time[1])

#show program output
print("{}th of fibonaccci: {}".format(num,time[0]))
