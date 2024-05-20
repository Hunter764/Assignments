#Returns true if the linked list is empty, false otherwise.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isempty(self):    #check for empty
        return self.head is None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
print("empty? :",ll.isempty())  #empty? : True

ll.head = Node(1)  
print("empty? :",ll.isempty())  #empty? : False

ll.head.next = Node(2)
ll.head.next.next = Node(3)  #list: 1 -> 2 -> 3 -> None
print("empty? :",ll.isempty())  # empty? False
