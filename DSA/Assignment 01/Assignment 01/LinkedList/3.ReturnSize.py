#Returns the size of the linked list.

class Node:  #Node creating
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def size(self):  #size method
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def print_list(self): #print output method
        current = self.head
        while current:
            print(current.data, end="=>")
            current = current.next
        print("None")

ll = LinkedList()
print('size :',ll.size())  #size : 0

ll.head = Node(1)  
print('size :',ll.size())  #size : 1

ll.head.next = Node(2)
ll.head.next.next = Node(3)  #lsit :1=>