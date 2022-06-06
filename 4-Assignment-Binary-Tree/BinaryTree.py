import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir))+"\Common\\")
from Common_Functions import *

#Binary Tree Nodes
class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

#Add node into tree
def Add(param):
    node = param[0]
    key = param[1]
    # if empty
    if node is None:
        return Node(key)

    # go down left
    if key < node.key:
        node.left = Add([node.left, key])

    # go down right
    else:
        node.right = Add([node.right, key])

    return node

#delete node with value
def RemoveValue(param):
    root = param[0]
    key = param[1]

    if root is None:
        return root

    if key < root.key:
        root.left = RemoveValue([root.left, key])

    elif(key > root.key):
        root.right = RemoveValue([root.right, key])
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        temp = Minimum(root.right)

        root.key = temp

        root.right = RemoveValue([root.right, temp])

    return root

#delete node at pointer
def RemovePointer(pointer):
    return RemoveValue([pointer, pointer.key])

# find max value in tree (return rightmost node)
def Maximum(node):
    current = node
    while(current.right is not None):
        current = current.right

    print("Max Value :: " + str(current.key))
    return current.key

# find min value in tree (return leftmost node)
def Minimum(node):
    current = node
    while(current.left is not None):
        current = current.left

    print("Min Value :: " + str(current.key))
    return current.key

#traverse and print tree
def InorderTraverse(root):
	if root is not None:
		InorderTraverse(root.left)
		print (root.key,end="->")
		InorderTraverse(root.right)


# Find for value in tree
def Find(param):
    root = param[0]
    key = param[1]

    if root is None or root.key == key:
        if(root != None):
            print("Found :: " + str(root.key))
        else:
            print("Didn't find :: " + str(key))
        return root
 
    # recurce right
    if root.key < key:
        return Find(root.right,key)
   
   # recurce left
    return Find(root.left,key)


#given base node, deletes full tree
def deleteTree( base) :
  if base != None:
    deleteTree(base.left)
    deleteTree(base.right)
    del base

#testing function
def start(testingVal):
    print("Number of Nodes :: " + str(testingVal) + "\n=====================================")
    root = None
    base = None
    trange = random.sample(range(1, testingVal), 3)
    rndFind = trange[0]
    rndDelete1 = trange[1]
    rndDelete2 = trange[2]

    for x in range(testingVal):
       
        if(x == 0):
            root = Time( Add, "Time to add", [root, random.randint(0, testingVal)])[0]
            base = root
        else:
             root = Add([root, random.randint(0, testingVal)])
        if(x == rndFind):
            rndFind = root.key
        elif(x == rndDelete1):
            rndDelete1 = root
        elif(x == rndDelete2):
            rndDelete2 = root.key

    print("InorderTraverse traversal: ", end=' ')
    Time(InorderTraverse, "\nTime to transverse", root)
    print("\n")
    Time(Maximum, "Find Max Value Time", root)
    print("\n")
    Time(Minimum, "Find Min Value Time", root)
    print("\n\nFinding for " +str(rndFind), end = " :: ")
    Time(Find, "Find Time", [root, rndFind])
    print("\n\nDeleting " + str(rndDelete2), end = ":: ")
    root = Time(RemoveValue, "Time to Delete Value", [root, rndDelete2])[0]
    Time(InorderTraverse, "\nTime to transverse", root)
    print("\n\n")
    root = Time(RemovePointer, "Delete By Reference :: " + str(rndDelete1.key), rndDelete1)[0]
    Time(InorderTraverse, "\nTime to transverse", root)
    print("\n\nDeleting old tree...\n\n")
    deleteTree(base)
    root = None

#run with 100
start(100)

#run with 1000
start(1000)

#run with 10000
start(10000)

#run with 
start(100000)