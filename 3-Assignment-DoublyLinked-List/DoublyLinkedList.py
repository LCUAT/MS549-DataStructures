import random
from timeit import default_timer as timer

#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

#Doubly linked List Class
class doublyLinkedList:
    def __init__(self):
        self.start_node = None
#find value
    def Find(self, data):
        n = self.start_node
        while n.next is not None:
            if(n.data == data):
                print(str(data) + " found at " + str(n))
                return n
            n = n.next
        if(n.data == data):
                print(str(data) + " found at " + str(n))
                return n
        print(str(data) + " Not found")
        return

#delete at the given data value
    def delete_at_data(self, data):
        n = self.start_node
        while n.next is not None:
            if(n.data == data):
                if(n.next != None):
                    n.next.prev = None
                if(n.prev != None):
                    n.prev.next = None
            n = n.next
        if(n.data == data):
            if(n.next != None):
                n.next.prev = None
            if(n.prev != None):
                n.prev.next = None
            if(n.next == None and n.prev == None):
                 self.start_node = None

#delete at the given ref
    def delete_at_ref(self, ref):
        n = self.start_node
        while n.next is not None:
            if(n == ref):
                if(n.next != None):
                    n.next.prev = None
                if(n.prev != None):
                    n.prev.next = None
            n = n.next
        if(n == ref):
            if(n.next != None):
                n.next.prev = None
            if(n.prev != None):
                n.prev.next = None
            if(n.next == None and n.prev == None):
                 self.start_node = None

#Insert element at the end
    def InsertToEnd(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return self.start_node
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
        return n

#Delete the element from the end
    def delete_at_end(self):
        if self.start_node is None:
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None

#Print List
    def Print(self):
            printStr = "["
            n = self.start_node
            while n is not None:
                printStr += str(n.data)
                n = n.next
                printStr += "-->"
            printStr += "None]"
            print(printStr)

#Create a new Doubly Linked List
doublyLinkedList = doublyLinkedList()

#Testing adding values to list
def TestingAdd(limit):
    print("Adding "+str(limit)+" random elements to linked list")
    start = timer()
    for x in range(100):
        doublyLinkedList.InsertToEnd(random.randrange(0,500))
    end = timer()
    print("Time to add "+str(limit)+" random elements "+str(end - start)+"s\n")

    # Print Data
    doublyLinkedList.Print()

#Testing remoing values from list
def TestingRemove(limit):
    print("Removing "+str(limit)+" random elements to linked list")
    start = timer()
    for x in range(100):
        doublyLinkedList.delete_at_end()
    end = timer()
    print("Time to remove "+str(limit)+" random elements "+str(end - start)+"s\n")

    # Print Data
    doublyLinkedList.Print()

#Testing finding values in list
def TestingFind():
    print("finding element 1")
    start = timer()
    doublyLinkedList.InsertToEnd(1)
    doublyLinkedList.Print()
    doublyLinkedList.Find(1)
    end = timer()
    print("Time to find 1: "+str(end - start)+"s\n")

#Testing deleting value at data
def TestingDeleteAt():
    print("Deleting Element 1")
    doublyLinkedList.Print()
    start = timer()
    doublyLinkedList.delete_at_data(1)
    end = timer()
    doublyLinkedList.Print()
    print("Time to delete element 1: "+str(end - start)+"s\n")

#Testing deteting value at reference
def TestingDeleteAtRef():
    ref = doublyLinkedList.InsertToEnd(1)
    print("\nDeleting at ref: " + str(ref))
    doublyLinkedList.Print()
    start = timer()
    doublyLinkedList.delete_at_ref(ref)
    end= timer()
    doublyLinkedList.Print()
    print("Time to delete at ref: "+str(end - start)+"s\n")

#Testing full Suite
def TestingSuite():

    TestingAdd(100)
    TestingRemove(100)

    TestingAdd(1000)
    TestingRemove(1000)

    TestingAdd(10000)
    TestingRemove(10000)

    TestingFind()

    TestingDeleteAt()

    TestingDeleteAtRef()

#Menu for custom user
userInput = -1
while(True):
    userInput = input("\n\nMenu\n==========================\n1) Run full testing suite\n2)Add Value\n3)Remove Value with data\n4)Print list\n5)Exit\n==========================\nSelection:")
    if (userInput == "1"):
        TestingSuite()
    elif(userInput == "2"):
        value = input("Enter Value to add ")
        print("Before:")
        doublyLinkedList.Print()
        doublyLinkedList.InsertToEnd(value)
        print("After:")
        doublyLinkedList.Print()
    elif(userInput == "3"):
        print("Before:")
        doublyLinkedList.Print()
        doublyLinkedList.delete_at_data(input("Enter Data "))
        print("After:")
        doublyLinkedList.Print()
    elif(userInput =="4"):
        doublyLinkedList.Print()
    elif(userInput == "5"):
        break
    else:
        print("Invalid Option")