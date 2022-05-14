# Luke Coddington
# Data Structues MS 549
# Assignment 1: Test Driven Development
# Description:
#   This project shows a basic implementation of the test driven developement through the timiing of the pogram and it's functions as well as monitoring the cpu usage for the duration of the program.

# import common functions
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir))+"\Common\\")
from Common_Functions import *

#simulated stack
stackVal = [1,3,5,7,9,11,13,15,17,19,21]

# define peek function for stackValay in python
def peek():
    if(len(stackVal) == 0):
        printc("Unable to peek on empty stackValay", "red")
        return -1
    else:
        return stackVal[-1]

def push(val):
    if(len(stackVal) <= 10):
        return stackVal.append(val)
    else:
        printc(("stack Full, unable to add value: " + str(val)), "red")
        return -1

def pop():
    if(len(stackVal) == 0):
        printc("Unable to pop on an empty stackValay", "red")
    else:
        return stackVal.pop()


#main functionality
def main():

    #print the inital stack values
    printc("Stack Initial values:", "green")
    print(stackVal)

    #push to full stack
    printc("\nPushing to full stack:", "green")
    print(Time(push,"pushing to stack",1)[0])

    #Pop an element from the statck and show the emement
    printc("\nPopping All Elements from stack:", "green")
    while(len(stackVal) > 0):
        print(Time(stackVal.pop,"Time to Pop:")[0])

    #pop on an empty stack
    printc("\nPopping an empty stack:", "green")
    Time(pop,"Time to Pop:")[0]

    #push to stack
    printc("\nPushing to stack:", "green")
    Time(push,"pushing to stack",1)[0]

    #Peek at the next element in the stack
    printc("\nPeeking Elements from stack:", "green")
    print(Time(peek,"Time to peek:")[0])

#time and call main function
totalTime = Time(main,"\n=========================\nWhole program Time:")

#show processor useage for program
processorInfo(totalTime[1])