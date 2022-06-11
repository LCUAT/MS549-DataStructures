import random
import sys
import os
from tkinter import N
from typing import Hashable
import numpy as np
import sympy
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir))+"\Common\\")
from Common_Functions import *
from timeit import default_timer as timer

insertTimes = []
RemoveTimes = []
findTimes = []
keys =[]
hashTable = {}

def Retrieve(key):
    start = timer()
    if key in hashTable: 
        end = timer()
        findTimes.append((end - start))
        return True
    else:
        end = timer()
        findTimes.append((end - start))
        return False

def insert(key, value):
    start = timer()
    #Linear Probing
    hashKey = hash(key)
    if(Retrieve(hashKey) == False):
        hashTable[hashKey] = value
        end = timer()
        insertTimes.append((end - start))
        return hashKey
    else:
        #print("WARN :: Duplicate Key found :: " + str(hashKey))
        n = 1
        while(Retrieve(hashKey)):
            hashKey = (hash(key) + n * n)
            if (Retrieve(hashKey) == False):
                hashTable[hashKey] = value
                end = timer()
                insertTimes.append((end - start))
                return hashKey
            n = n+1

def insertLinearly(key, value):
    start = timer()
    #Linear Probing
    n = 1
    hash1 = hash(key)
    lenTable = len(hashTable)+1
    while(True):
        hashKey = (hash1 + n) % (lenTable)
        if(Retrieve(hashKey) == False):
            hashTable[hashKey] = value
            end = timer()
            insertTimes.append((end - start))
            return hashKey
        n = n +1

def insertQuadradic(key, value):
    start = timer()
    #Linear Probing
    n = 1
    lenTable = len(hashTable)+1
    hash1 = hash(key)
    while(True):
        hashKey = (hash1%(lenTable) + n^2)%(lenTable)
        if(Retrieve(hashKey) == False):
            hashTable[hashKey] = value
            end = timer()
            insertTimes.append((end - start))
            return hashKey
        n = n +1

def insertDouble(key, value):
    start = timer()
    n = 1
    tblLength = len(hashTable)+1
    hashKeyVal = hash(key)
    rndPrime1 = random.randint(1,tblLength)
    hash1 = (hashKeyVal % rndPrime1)
    while(True):
        rndPrime2 = random.randint(1,tblLength)
        hash2= rndPrime2 - (hashKeyVal % rndPrime2)
        hashKey = (hash1 + n * hash2 ) % (tblLength)
        if(Retrieve(hashKey) == False):
            hashTable[hashKey] = value
            end = timer()
            insertTimes.append((end - start))
            return hashKey
        n = n +1

def Remove(key):
    start = timer()
    try:
         del hashTable[key]
    except:
        print("ERROR :: unable to Remove key; key not found :: " + str(key))

    end = timer()
    RemoveTimes.append((end - start))

def printHashTable():
    print(hashTable)
    print("Number of elements :: " + str(len(hashTable)))

values = ["Thankful Feet", 1, "Mundane Afternoon", 42.290, " Uninterested Cup"," Delicious Cows"," Devilish Calculator"," Victorious Toy"," Third Meeting"," Narrow Boundary", "Dynamic Button", "Miscreant Boats"," Bent Kite"," Unadvised Glass","Onerous Quince"," Uneven Plate"," Gainful Pin"," Diligent Seed"," Elite Twig"," Gusty Sleet"]

def test(numInterations, type):
    insertTimes = []
    RemoveTimes = []
    findTimes = []
    keys =[]
    hashTable = {}
    print("\n\nTESTNG :: " + type + " :: " + str(numInterations))
    for num in range(numInterations):
        key = random.randint(0,numInterations)
        value = values[random.randint(0, len(values)-1)]
        #print("Attempting to insert: {key: " +str(key)+", value: " + str(value)+"}")
        if(type == "linear"):
            keys.append(insertLinearly(key,value))
        elif(type == "quadratic"):
            keys.append(insertQuadradic(key,value))
        elif(type == "double"):
            keys.append(insertDouble(key,value))
        sys.stdout.write("\rInserting Values: {0}".format((float(num)/numInterations)*100))
        sys.stdout.flush()
        #print("inserting: {key: " +str(keys[len(keys)-1])+", value: " + str(value)+"}")
    print("")
    printHashTable()
        
    print("\n\ninsterting dublicate key to show functionaliy")
    val2 = values[random.randint(0, len(values)-1)]
    #print("inserting: {key: 0"+", value: " + str(val2)+"}")
    if(type == "linear"):
        keys.append(insertLinearly(0, val2))
    elif(type == "quadratic"):
        keys.append(insertQuadradic(key,value))
    elif(type == "double"):
        keys.append(insertDouble(key,value))
    printHashTable()

    print("\n\n Searching for each value")
    found = True
    for x in keys:
        if(Retrieve(x) == False):
            print("ERROR :: Something went wrong, key not found")
            found = False
            break
        sys.stdout.write("\rSarching for values: {0}".format(x/len(keys))*100)
        sys.stdout.flush()
    if(found):
        print("All keys Found!")

    print("\n\nSearching for non-esistant key")
    if(not Retrieve(";lkj")):
        print("Key not found :: ;lkj")
    else:
        print("Something went wrong, found key ;lkj")

    print("\n\nDeleting all values")
    for x in keys:
        Remove(x)
        sys.stdout.write("\rDeleting values: {0}".format(x/len(keys))*100)
        sys.stdout.flush()
    printHashTable()

    print("\n\n Deleting key that doesn't exit to show functionality")
    Remove("al;skdjf;alskdjf;lakdsjf;lkaksjdf")
    
    print("\n\nExporting Results...")
    exportResults(type + "-",numInterations)

def exportResults(title,numInterations):
    a = np.array(insertTimes)
    b = np.array(RemoveTimes)
    c = np.array(findTimes)
    with open(title+str(numInterations)+'.csv','w') as f:
        f.write('# Results for '+str(numInterations)+'\n')
        f.write('Insert Times (s),Remove Times (s),Find Times (s)\n')
        np.savetxt(f, list(zip(a,b,c)), delimiter=',', fmt='%1.10f')

#test(100, "linear")
#test(100, "double")
#test(100, "quadratic")

test(1000, "linear")
test(1000, "double")
test(1000, "quadratic")

#test(10000, "linear")
#test(10000, "double")
#test(10000, "quadratic")