#Reverses the linked list.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self): # reverse Method
        previous = None
        current = self.head
        while current:
            next_node = current.next  #save the next node
            current.next = previous  #reverse the pointer
            previous = current  #move previous to current
            current = next_node  #move current to next node
        self.head = previous  #set the new head

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" => ")
            current = current.next
        print("None")

ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)

print("Original List:")
ll.print_list()  #1 => 2 => 3 => 4 => 5 => None

ll.reverse()

print("Reversed List:")
ll.print_list()  #5 => 4 => 3 => 2 => 1 => None
