#Splits the linked list into two linked lists at the specified index.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def split_at_index(self, index):
        if not self.head:
            return None, None

        current = self.head
        prev = None
        count = 0

        # Traverse to the node at the specified index
        while current and count != index:
            prev = current
            current = current.next
            count += 1

        if not current:
            #if index is out of range
            return self, None
         #adjust ptr
        if prev:
            prev.next = None  # Cut off the first list at the node before the specified index
        second_list = LinkedList()
        second_list.head = current  #set index as a head of breaked list

        return self, second_list

    def append(self, data):
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
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original List :")
ll.print_list()  #Original List :1 -> 2 -> 3 -> 4 -> 5 -> None

index = 2
first_half, second_half = ll.split_at_index(index)
print("1st Half :")
first_half.print_list()  #1st Half :1 -> 2 -> None

print("2nd Half :")
second_half.print_list()  #2nd Half :3 -> 4 -> 5 -> None
