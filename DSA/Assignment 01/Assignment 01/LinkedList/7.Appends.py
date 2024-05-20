#Appends an element to the end of the linked list.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):  #appending method
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" => ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(1)  
ll.append(2) 
ll.append(3)  

ll.print_list()  #1 => 2 => 3 => None
