#Inserts an element at the specified index.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, index, data):
        if index < 0:
            print("Index must be a non-negative integer.")
            return
        
        new_node = Node(data)
        
        #insert at head
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        count = 0
        
        while current is not None and count < index - 1:
            current = current.next
            count += 1
        
        if current is None:
            print("Index out of range.")
            return
        
        #new node insertion
        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.insert_at_index(0,3)  #Insertion(index,data)
ll.insert_at_index(1,5) 
ll.insert_at_index(1,4)  
ll.insert_at_index(0,2)

ll.print_list()   #2 -> 3 -> 4 -> 5 -> None
