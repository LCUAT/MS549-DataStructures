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
        print("\tUnable to peek on empty stackValay")
        return -1
    else:
        return stackVal[-1]

def push(val):
    if(len(stackVal) <= 10):
        return stackVal.append(val)
    else:
        print(("\t- Stack Full, unable to add value: " + str(val)))
        return -1

def pop():
    if(len(stackVal) == 0):
        print("\t-Unable to pop on an empty stack")
    else:
        return stackVal.pop()


#main functionality
def main():

    #print the inital stack values
    print("Stack Initial values:")
    print(stackVal)

    #push to full stack
    print("\nPushing to full stack:")
    print(Time(push,"pushing to stack",1)[0])

    #Pop an element from the statck and show the emement
    print("\nPopping All Elements from stack:")
    while(len(stackVal) > 0):
        print(Time(stackVal.pop,"Time to Pop:")[0])

    #pop on an empty stack
    print("\nPopping an empty stack:")
    Time(pop,"Time to Pop:")[0]

    #push to stack
    print("\nPushing to stack:")
    Time(push,"pushing to stack",1)[0]

    #Peek at the next element in the stack
    print("\nPeeking Elements from stack:")
    print(Time(peek,"Time to peek:")[0])

#time and call main function
totalTime = Time(main,"\n=========================\nWhole program Time:")

#show processor useage for program
processorInfo(totalTime[1])