#Interleaves two linked lists into a single linked list.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def interleave(self, other_list): #Interleave
        interleaved = LinkedList()
        current_self = self.head
        current_other = other_list.head

        while current_self and current_other:
            interleaved.append(current_self.data)
            interleaved.append(current_other.data)
            current_self = current_self.next
            current_other = current_other.next

        # Append remaining nodes from the self list
        while current_self:
            interleaved.append(current_self.data)
            current_self = current_self.next

        # Append remaining nodes from the other list
        while current_other:
            interleaved.append(current_other.data)
            current_other = current_other.next

        return interleaved

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

ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

print("List 1:")
ll1.print_list()  #1 -> 3 -> 5 -> None

print("List 2:")
ll2.print_list()  #2 -> 4 -> 6 -> None

interleaved_list = ll1.interleave(ll2)
print("Interleaved List:")
interleaved_list.print_list()  #1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
