#Rotates the linked list by k positions to the right.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def rotate_right(self, k):
        if not self.head or k == 0:
            return
        #length calculation
        length = 1
        tail = self.head
        while tail.next:
            tail = tail.next
            length += 1

        #adjust k if it greater than length of linkedlist 
        k %= length

        if k == 0:
            return

        #find the new tail (the node at position length - k - 1)
        new_tail = self.head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        #pointer update
        new_head = new_tail.next
        new_tail.next = None
        tail.next = self.head
        self.head = new_head

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

print("original list :")
ll.print_list()  #1=>2=>3=>4=>5=>None

k = 3
ll.rotate_right(k)

print(f"After {k} rotation :")
ll.print_list()  #3 => 4 => 5 => 1 => 2 => None 
