#Prepends an element to the beginning of the linked list.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):   # Prepending (making new node at head)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" => ")
            current = current.next
        print("None")


ll = LinkedList()
ll.prepend(3) 
ll.prepend(2)  
ll.prepend(1)  

ll.print_list() # 1 => 2 => 3 => None
