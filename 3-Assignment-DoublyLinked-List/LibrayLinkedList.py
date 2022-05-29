import collections
import random
from timeit import default_timer as timer

linked_lst = collections.deque()
 
#Testing adding values to list
def TestingAdd(limit):
    print("Adding "+str(limit)+" random elements to linked list")
    start = timer()
    for x in range(100):
        linked_lst.append(random.randrange(0,500))
    end = timer()
    print("Time to add "+str(limit)+" random elements "+str(end - start)+"s\n")

#Testing remoing values from list
def TestingRemove(limit):
    print("Removing "+str(limit)+" random elements to linked list")
    start = timer()
    for x in range(100):
        linked_lst.pop()
    end = timer()
    print("Time to remove "+str(limit)+" random elements "+str(end - start)+"s\n")

TestingAdd(100)
TestingRemove(100)

TestingAdd(1000)
TestingRemove(1000)

TestingAdd(10000)
TestingRemove(10000)