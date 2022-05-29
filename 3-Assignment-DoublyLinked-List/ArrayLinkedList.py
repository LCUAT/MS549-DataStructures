import random
from timeit import default_timer as timer
arrList = []
start = timer()

def TestingAdd(limit):
    for x in range(limit):
        arrList.append(random.randrange(0,500))
    end = timer()
    print("Time to add "+str(limit)+" random elements "+str(end - start)+"s")

def TestingRemove(limit):
    for x in range(limit):
        arrList.pop()
    end = timer()
    print("Time to delete "+str(limit)+" random elements "+str(end - start)+"s\n")

TestingAdd(100)
TestingRemove(100)

TestingAdd(1000)
TestingRemove(1000)

TestingAdd(10000)
TestingRemove(10000)

