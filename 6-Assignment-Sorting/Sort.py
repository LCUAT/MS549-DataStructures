#References (as prompted for in assignment)
#   https://www.geeksforgeeks.org/iterative-selection-sort-for-linked-list/
#   https://www.geeksforgeeks.org/insertion-sort-for-singly-linked-list/

import random
from timeit import default_timer as timer
import numpy as np
import sys

# Linked List Node
class Node:
	
	def __init__(self, val, next):
		self.data = val
		self.next = next

iterations = [100, 1000, 10000]
SelectionTimes = []
InsertionTimes = []

# Function to sort a linked list
# using selection sort algorithm
# by swapping the next pointers
def selectionSort(head):
    start = timer()
    a = b = head

    # While b is not the last node
    while b.next:

        c = d = b.next

        # While d is pointing to a valid node
        while d:

            if b.data > d.data:

                # If d appears immediately after b
                if b.next == d:

                    # Case 1: b is the head
                    # of the linked list
                    if b == head:

                        # Move d before b
                        b.next = d.next
                        d.next = b

                        # Swap b and d pointers
                        b, d = d, b
                        c = d

                        # Update the head
                        head = b

                        # Skip to the next element
                        # as it is already in order
                        d = d.next
                    
                    # Case 2: b is not the head
                    # of the linked list
                    else:

                        # Move d before b
                        b.next = d.next
                        d.next = b
                        a.next = d

                        # Swap b and d pointers
                        b, d = d, b
                        c = d

                        # Skip to the next element
                        # as it is already in order
                        d = d.next
                    
                # If b and d have some non-zero
                # number of nodes in between them
                else:

                    # Case 3: b is the head
                    # of the linked list
                    if b == head:

                        # Swap b.next and d.next
                        r = b.next
                        b.next = d.next
                        d.next = r
                        c.next = b

                        # Swap b and d pointers
                        b, d = d, b
                        c = d

                        # Skip to the next element
                        # as it is already in order
                        d = d.next

                        # Update the head
                        head = b
                    
                    # Case 4: b is not the head
                    # of the linked list
                    else:

                        # Swap b.next and d.next
                        r = b.next
                        b.next = d.next
                        d.next = r
                        c.next = b
                        a.next = d

                        # Swap b and d pointers
                        b, d = d, b
                        c = d

                        # Skip to the next element
                        # as it is already in order
                        d = d.next
                    
            else:

                # Update c and skip to the next element
                # as it is already in order
                c = d
                d = d.next

        a = b
        b = b.next

    end=timer()
    SelectionTimes.append((end - start))
    return head


# function to sort a singly linked list using insertion sort
def insertionSort(head_ref):
    start = timer()
    # Initialize sorted linked list
    sorted = None
  
    # Traverse the given linked list and insert every
    # node to sorted
    current = head_ref
    while (current != None):
      
        # Store next for next iteration
        next = current.next
  
        # insert current in sorted linked list
        sorted = sortedInsert(sorted, current)
  
        # Update current
        current = next
      
    # Update head_ref to point to sorted linked list
    head_ref = sorted
    end=timer()
    InsertionTimes.append((end - start))
    return head_ref
  
# function to insert a new_node in a list. Note that this
# function expects a pointer to head_ref as this can modify the
# head of the input linked list (similar to push())
def sortedInsert(head_ref, new_node):
  
    current = None
      
    # Special case for the head end */
    if (head_ref == None or (head_ref).data >= new_node.data):
      
        new_node.next = head_ref
        head_ref = new_node
      
    else:
      
        # Locate the node before the point of insertion 
        current = head_ref
        while (current.next != None and
            current.next.data < new_node.data):
          
            current = current.next
          
        new_node.next = current.next
        current.next = new_node
          
    return head_ref

def exportResults(title):
    print("Exporting Results...", end = '')
    a = np.array(iterations)
    b = np.array(SelectionTimes)
    c = np.array(InsertionTimes)
    with open(title+'.csv','w') as f:
        f.write('Number of Iterations, Selection Sort Times (s),Insertion Sort Times (s)\n')
        np.savetxt(f, list(zip(a,b,c)), delimiter=',', fmt='%1.10f')
    print("Successful!")


def test(numIterations):
    keys = np.random.randint(1,100,numIterations)
    savedKeys = keys
    head = None
    for key in keys:
        head = Node(key, head)
    
    print(f"Unsorted list :: {keys}\nLength :: {len(keys)}")
    # sort the list
    head = insertionSort(head)
    # print the sorted list
    print('\n\nInsertion Sort')
    print(f"Sorted list :: {keys}\nLength :: {len(keys)}")

    head = None
    for key in savedKeys:
        head = Node(key, head)
    head = selectionSort(head)
    print("\n\nSelection Sort")
    print(f"Sorted list :: {keys}\nLength :: {len(keys)}\n\n")



for x in iterations:
    test(x)



exportResults("Sort-Results")