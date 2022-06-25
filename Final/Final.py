import random
import networkx
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


doublyLinkedList = doublyLinkedList()

# custom graph
custom_graph = networkx.Graph()
# non-directional weighted edges for custom graph based on 'power grid' board game
custom_edges = [('Transistor C', 'Transistor B', 6), ('Transistor B', 'Transistor C', 6), ('Transistor D', 'Transistor B', 6), ('Transistor B', 'Transistor D', 6), ('Transistor D', 'Transistor C', 25), ('Transistor C', 'Transistor D', 25), ('Transistor E', 'Transistor B', 5), ('Transistor B', 'Transistor E', 5), ('Transistor E', 'Transistor C', 19), ('Transistor C', 'Transistor E', 19), ('Transistor E', 'Transistor D', 11), ('Transistor D', 'Transistor E', 11), ('Transistor F', 'Transistor B', 10), ('Transistor B', 'Transistor F', 10), ('Transistor F', 'Transistor C', 5), ('Transistor C', 'Transistor F', 5), ('Transistor F', 'Transistor D', 12), ('Transistor D', 'Transistor F', 12), ('Transistor F', 'Transistor E', 21), ('Transistor E', 'Transistor F', 21), ('Transistor G', 'Transistor B', 22), ('Transistor B', 'Transistor G', 22), ('Transistor G', 'Transistor C', 25), ('Transistor C', 'Transistor G', 25), ('Transistor G', 'Transistor D', 12), ('Transistor D', 'Transistor G', 12), ('Transistor G', 'Transistor E', 15), ('Transistor E', 'Transistor G', 15), ('Transistor G', 'Transistor F', 15), ('Transistor F', 'Transistor G', 15), ('Transistor H', 'Transistor B', 20), ('Transistor B', 'Transistor H', 20), ('Transistor H', 'Transistor C', 23), ('Transistor C', 'Transistor H', 23), ('Transistor H', 'Transistor D', 23), ('Transistor D', 'Transistor H', 23), ('Transistor H', 'Transistor E', 9), ('Transistor E', 'Transistor H', 9), ('Transistor H', 'Transistor F', 20), ('Transistor F', 'Transistor H', 20), ('Transistor H', 'Transistor G', 9), ('Transistor G', 'Transistor H', 9), ('Transistor I', 'Transistor B', 10), ('Transistor B', 'Transistor I', 10), ('Transistor I', 'Transistor C', 18), ('Transistor C', 'Transistor I', 18), ('Transistor I', 'Transistor D', 13), ('Transistor D', 'Transistor I', 13), ('Transistor I', 'Transistor E', 22), ('Transistor E', 'Transistor I', 22), ('Transistor I', 'Transistor F', 9), ('Transistor F', 'Transistor I', 9), ('Transistor I', 'Transistor G', 15), ('Transistor G', 'Transistor I', 15), ('Transistor I', 'Transistor H', 14), ('Transistor H', 'Transistor I', 14), ('Transistor J', 'Transistor B', 24), ('Transistor B', 'Transistor J', 24), ('Transistor J', 'Transistor C', 10), ('Transistor C', 'Transistor J', 10), ('Transistor J', 'Transistor D', 16), ('Transistor D', 'Transistor J', 16), ('Transistor J', 'Transistor E', 24), ('Transistor E', 'Transistor J', 24), ('Transistor J', 'Transistor F', 11), ('Transistor F', 'Transistor J', 11), ('Transistor J', 'Transistor G', 7), ('Transistor G', 'Transistor J', 
7), ('Transistor J', 'Transistor H', 12), ('Transistor H', 'Transistor J', 12), ('Transistor J', 'Transistor I', 17), ('Transistor I', 
'Transistor J', 17), ('Transistor K', 'Transistor B', 6), ('Transistor B', 'Transistor K', 6), ('Transistor K', 'Transistor C', 16), ('Transistor C', 'Transistor K', 16), ('Transistor K', 'Transistor D', 23), ('Transistor D', 'Transistor K', 23), ('Transistor K', 'Transistor E', 25), ('Transistor E', 'Transistor K', 25), ('Transistor K', 'Transistor F', 19), ('Transistor F', 'Transistor K', 19), ('Transistor K', 'Transistor G', 22), ('Transistor G', 'Transistor K', 22), ('Transistor K', 'Transistor H', 23), ('Transistor H', 'Transistor K', 23), ('Transistor K', 'Transistor I', 17), ('Transistor I', 'Transistor K', 17), ('Transistor K', 'Transistor J', 8), ('Transistor J', 'Transistor K', 8), ('Transistor L', 'Transistor B', 10), ('Transistor B', 'Transistor L', 10), ('Transistor L', 'Transistor C', 
24), ('Transistor C', 'Transistor L', 24), ('Transistor L', 'Transistor D', 22), ('Transistor D', 'Transistor L', 22), ('Transistor L', 'Transistor E', 6), ('Transistor E', 'Transistor L', 6), ('Transistor L', 'Transistor F', 23), ('Transistor F', 'Transistor L', 23), ('Transistor L', 'Transistor G', 17), ('Transistor G', 'Transistor L', 17), ('Transistor L', 'Transistor H', 18), ('Transistor H', 'Transistor L', 18), ('Transistor L', 'Transistor I', 25), ('Transistor I', 'Transistor L', 25), ('Transistor L', 'Transistor J', 6), ('Transistor J', 'Transistor L', 6), ('Transistor L', 'Transistor K', 25), ('Transistor K', 'Transistor L', 25), ('Transistor M', 'Transistor B', 21), ('Transistor B', 'Transistor M', 21), ('Transistor M', 'Transistor C', 10), ('Transistor C', 'Transistor M', 10), ('Transistor M', 'Transistor D', 14), ('Transistor D', 'Transistor M', 14), ('Transistor M', 'Transistor E', 18), ('Transistor E', 'Transistor M', 18), ('Transistor M', 'Transistor F', 23), ('Transistor F', 'Transistor M', 23), ('Transistor M', 'Transistor G', 25), ('Transistor G', 'Transistor M', 25), ('Transistor M', 'Transistor H', 19), ('Transistor H', 'Transistor M', 19), ('Transistor M', 'Transistor I', 16), ('Transistor I', 'Transistor M', 16), ('Transistor M', 'Transistor J', 13), ('Transistor J', 'Transistor M', 13), ('Transistor M', 'Transistor K', 20), ('Transistor K', 'Transistor M', 20), ('Transistor M', 'Transistor L', 9), ('Transistor L', 'Transistor M', 9), ('Transistor N', 'Transistor B', 22), ('Transistor B', 'Transistor N', 22), ('Transistor N', 'Transistor C', 18), ('Transistor C', 'Transistor N', 18), ('Transistor N', 'Transistor D', 19), ('Transistor D', 'Transistor N', 19), ('Transistor N', 'Transistor E', 17), ('Transistor E', 'Transistor N', 17), ('Transistor N', 'Transistor F', 5), ('Transistor F', 'Transistor N', 5), ('Transistor N', 'Transistor G', 10), ('Transistor G', 'Transistor N', 10), ('Transistor N', 'Transistor H', 22), ('Transistor H', 'Transistor N', 22), ('Transistor N', 'Transistor I', 16), ('Transistor I', 'Transistor N', 16), ('Transistor N', 'Transistor J', 11), ('Transistor J', 'Transistor N', 11), ('Transistor N', 'Transistor K', 11), ('Transistor K', 'Transistor N', 11), ('Transistor N', 'Transistor L', 12), ('Transistor L', 'Transistor N', 12), ('Transistor N', 'Transistor M', 10), ('Transistor M', 'Transistor N', 10), ('Transistor O', 'Transistor B', 16), ('Transistor B', 'Transistor O', 16), ('Transistor O', 'Transistor C', 19), ('Transistor C', 'Transistor O', 19), ('Transistor O', 'Transistor D', 21), ('Transistor D', 'Transistor O', 21), ('Transistor O', 'Transistor E', 17), ('Transistor E', 'Transistor O', 17), ('Transistor O', 'Transistor F', 20), ('Transistor F', 'Transistor O', 20), ('Transistor O', 'Transistor G', 19), ('Transistor G', 'Transistor O', 19), ('Transistor O', 'Transistor H', 11), ('Transistor H', 'Transistor O', 11), ('Transistor O', 'Transistor I', 20), ('Transistor I', 'Transistor O', 20), ('Transistor O', 'Transistor J', 9), ('Transistor J', 'Transistor O', 9), ('Transistor O', 'Transistor K', 14), ('Transistor K', 'Transistor O', 14), ('Transistor O', 'Transistor L', 17), ('Transistor L', 'Transistor O', 17), ('Transistor O', 'Transistor M', 16), ('Transistor M', 'Transistor O', 16), ('Transistor O', 'Transistor N', 5), ('Transistor N', 'Transistor O', 5), 
('Transistor P', 'Transistor B', 11), ('Transistor B', 'Transistor P', 11), ('Transistor P', 'Transistor C', 10), ('Transistor C', 'Transistor P', 10), ('Transistor P', 'Transistor D', 25), ('Transistor D', 'Transistor P', 25), ('Transistor P', 'Transistor E', 9), ('Transistor E', 'Transistor P', 9), ('Transistor P', 'Transistor F', 23), ('Transistor F', 'Transistor P', 23), ('Transistor P', 'Transistor G', 5), ('Transistor G', 'Transistor P', 5), ('Transistor P', 'Transistor H', 17), ('Transistor H', 'Transistor P', 17), ('Transistor P', 'Transistor I', 12), ('Transistor I', 'Transistor P', 12), ('Transistor P', 'Transistor J', 6), ('Transistor J', 'Transistor P', 6), ('Transistor P', 'Transistor K', 20), ('Transistor K', 'Transistor P', 20), ('Transistor P', 'Transistor L', 14), ('Transistor L', 'Transistor P', 14), ('Transistor P', 'Transistor M', 17), ('Transistor M', 'Transistor P', 17), ('Transistor P', 'Transistor N', 21), ('Transistor N', 'Transistor P', 21), ('Transistor P', 'Transistor O', 16), ('Transistor O', 'Transistor P', 16), ('Transistor Q', 'Transistor B', 21), ('Transistor B', 'Transistor Q', 21), ('Transistor Q', 'Transistor C', 8), ('Transistor C', 'Transistor Q', 8), ('Transistor Q', 'Transistor D', 11), ('Transistor D', 'Transistor Q', 11), ('Transistor Q', 'Transistor E', 7), ('Transistor E', 'Transistor Q', 7), ('Transistor Q', 'Transistor F', 16), ('Transistor F', 'Transistor Q', 16), ('Transistor Q', 'Transistor G', 17), ('Transistor G', 'Transistor Q', 17), ('Transistor Q', 'Transistor H', 9), ('Transistor H', 'Transistor Q', 9), ('Transistor Q', 'Transistor I', 6), ('Transistor I', 'Transistor Q', 6), ('Transistor Q', 'Transistor J', 19), ('Transistor J', 'Transistor Q', 19), ('Transistor Q', 'Transistor K', 24), ('Transistor K', 'Transistor Q', 24), ('Transistor Q', 'Transistor L', 13), ('Transistor L', 'Transistor Q', 13), ('Transistor Q', 'Transistor M', 24), ('Transistor M', 'Transistor Q', 24), ('Transistor Q', 'Transistor N', 19), ('Transistor N', 'Transistor Q', 19), ('Transistor Q', 'Transistor O', 8), ('Transistor O', 'Transistor Q', 8), ('Transistor Q', 'Transistor P', 14), ('Transistor P', 'Transistor Q', 14), ('Transistor R', 'Transistor B', 25), ('Transistor B', 'Transistor R', 25), ('Transistor R', 'Transistor C', 19), ('Transistor C', 'Transistor R', 19), ('Transistor R', 'Transistor D', 9), ('Transistor D', 'Transistor R', 9), ('Transistor R', 'Transistor E', 13), ('Transistor E', 'Transistor R', 13), ('Transistor R', 'Transistor F', 8), ('Transistor F', 'Transistor R', 8), ('Transistor R', 'Transistor G', 18), ('Transistor G', 'Transistor R', 18), ('Transistor R', 'Transistor H', 11), ('Transistor H', 'Transistor R', 11), ('Transistor R', 'Transistor I', 10), ('Transistor I', 'Transistor R', 10), ('Transistor R', 'Transistor J', 16), ('Transistor J', 'Transistor R', 16), ('Transistor R', 'Transistor K', 15), ('Transistor K', 'Transistor R', 15), ('Transistor R', 'Transistor L', 5), ('Transistor L', 'Transistor R', 5), ('Transistor R', 'Transistor M', 11), ('Transistor M', 'Transistor R', 11), ('Transistor R', 'Transistor N', 11), ('Transistor N', 'Transistor R', 11), ('Transistor R', 'Transistor O', 13), ('Transistor O', 'Transistor R', 13), ('Transistor R', 'Transistor P', 19), ('Transistor P', 'Transistor R', 19), ('Transistor R', 'Transistor Q', 11), ('Transistor Q', 'Transistor R', 11), ('Transistor S', 'Transistor B', 17), ('Transistor B', 'Transistor S', 17), ('Transistor S', 'Transistor C', 12), ('Transistor C', 'Transistor S', 12), ('Transistor S', 'Transistor D', 9), ('Transistor D', 'Transistor S', 9), ('Transistor S', 'Transistor E', 20), ('Transistor E', 'Transistor S', 20), ('Transistor S', 'Transistor F', 5), ('Transistor F', 'Transistor S', 5), ('Transistor S', 'Transistor G', 10), ('Transistor G', 'Transistor S', 10), ('Transistor S', 'Transistor H', 7), ('Transistor H', 'Transistor S', 7), ('Transistor S', 'Transistor I', 9), ('Transistor I', 'Transistor S', 9), ('Transistor S', 'Transistor J', 21), ('Transistor J', 'Transistor S', 21), ('Transistor S', 'Transistor K', 21), ('Transistor K', 'Transistor S', 21), ('Transistor S', 'Transistor L', 12), ('Transistor L', 'Transistor S', 12), ('Transistor S', 'Transistor M', 16), ('Transistor M', 'Transistor S', 16), ('Transistor S', 'Transistor N', 13), ('Transistor N', 'Transistor S', 13), ('Transistor S', 'Transistor O', 18), ('Transistor O', 'Transistor S', 18), ('Transistor S', 'Transistor P', 13), ('Transistor P', 'Transistor S', 13), ('Transistor S', 'Transistor Q', 23), ('Transistor Q', 'Transistor S', 23), ('Transistor S', 'Transistor R', 20), ('Transistor R', 'Transistor S', 20), ('Transistor T', 'Transistor B', 8), ('Transistor B', 'Transistor T', 8), ('Transistor T', 'Transistor C', 7), ('Transistor C', 'Transistor T', 7), ('Transistor T', 'Transistor D', 25), ('Transistor D', 'Transistor T', 25), ('Transistor T', 'Transistor E', 14), ('Transistor E', 'Transistor T', 14), ('Transistor T', 'Transistor F', 20), ('Transistor F', 'Transistor T', 20), ('Transistor T', 'Transistor G', 19), ('Transistor G', 'Transistor T', 19), ('Transistor T', 'Transistor H', 19), ('Transistor H', 'Transistor T', 19), ('Transistor T', 'Transistor I', 7), ('Transistor I', 'Transistor T', 7), ('Transistor T', 'Transistor J', 14), ('Transistor J', 'Transistor T', 14), ('Transistor T', 'Transistor K', 6), ('Transistor K', 'Transistor T', 6), ('Transistor T', 'Transistor L', 17), ('Transistor L', 'Transistor T', 17), ('Transistor T', 'Transistor M', 15), ('Transistor M', 'Transistor T', 15), ('Transistor T', 'Transistor N', 19), ('Transistor N', 'Transistor T', 19), ('Transistor T', 'Transistor O', 14), ('Transistor O', 'Transistor T', 14), ('Transistor T', 'Transistor P', 6), ('Transistor P', 'Transistor T', 6), ('Transistor T', 'Transistor Q', 24), ('Transistor Q', 'Transistor T', 24), ('Transistor T', 'Transistor R', 12), ('Transistor R', 'Transistor T', 12), ('Transistor T', 'Transistor S', 11), ('Transistor S', 'Transistor T', 11), ('Transistor U', 'Transistor B', 5), ('Transistor B', 'Transistor U', 5), ('Transistor U', 'Transistor C', 8), ('Transistor C', 'Transistor U', 8), ('Transistor U', 'Transistor D', 12), ('Transistor D', 'Transistor U', 12), ('Transistor U', 'Transistor E', 12), ('Transistor E', 'Transistor U', 12), ('Transistor U', 'Transistor F', 21), ('Transistor F', 'Transistor U', 21), ('Transistor U', 'Transistor G', 6), ('Transistor G', 'Transistor U', 6), ('Transistor U', 'Transistor H', 8), ('Transistor H', 'Transistor U', 8), ('Transistor U', 'Transistor I', 5), ('Transistor I', 'Transistor U', 5), ('Transistor U', 'Transistor J', 17), ('Transistor J', 'Transistor U', 17), ('Transistor U', 'Transistor K', 6), ('Transistor K', 'Transistor U', 6), ('Transistor U', 'Transistor L', 24), ('Transistor L', 'Transistor U', 24), ('Transistor U', 'Transistor M', 16), ('Transistor M', 'Transistor U', 16), ('Transistor U', 'Transistor N', 17), ('Transistor N', 'Transistor U', 17), ('Transistor U', 'Transistor O', 8), ('Transistor O', 'Transistor U', 8), ('Transistor U', 'Transistor P', 19), ('Transistor P', 'Transistor U', 19), ('Transistor U', 'Transistor Q', 9), ('Transistor Q', 'Transistor U', 9), ('Transistor U', 'Transistor R', 11), ('Transistor R', 'Transistor U', 11), ('Transistor U', 'Transistor S', 6), ('Transistor S', 'Transistor U', 6), ('Transistor U', 'Transistor T', 6), ('Transistor T', 'Transistor U', 6)]
# create nodes and graph based on board game edges with weights
custom_graph.add_weighted_edges_from(custom_edges)

for x in (list(networkx.bfs_edges(custom_graph,'Transistor Q'))):
    doublyLinkedList.InsertToEnd(x)

doublyLinkedList.Print()

