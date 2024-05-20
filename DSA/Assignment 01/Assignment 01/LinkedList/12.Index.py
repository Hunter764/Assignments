"""Returns the index of the first occurrence of the specified element in the linked list,
or -1 if the element is not found."""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find_index(self, target):  #find_index => traverse & compare 
        current = self.head
        index = 0

        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1

        return -1

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

print("Original List:")
ll.print_list()  #1 -> 2 -> 3 -> 4 -> 5 -> None

target_element = 3
index = ll.find_index(target_element)
print(f"Index of {target_element}:", index)  #Index of 3: 2
