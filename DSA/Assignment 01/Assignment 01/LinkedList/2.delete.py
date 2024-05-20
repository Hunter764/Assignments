#Deletes the element at the specified index.
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def delete_at_index(self,index):
        if index <0:
            print("Index must be non-negative integer")
            return 
        
        if self.head is None:
            print("List is empty")
            return 
        
        #delete @ head(index=0)
        if index==0:
            self.head=self.head.next
            return 
        
        current=self.head
        count=0

        while current is not None and count <index-1:
            current =current.next
            count +=1

        if current is None or current.next is None:
            print("Index is out of range")
            return 
        
        current.next=current.next.next

    def print_list(self):
        current=self.head
        while current:
            print(current.data,end=" => ")
            current=current.next
        print("None")

l1=LinkedList()
l1.head=Node(1)
l1.head.next=Node(2)
l1.head.next.next=Node(3)
l1.print_list() #1 => 2 => 3 => None
l1.delete_at_index(0) #delete element at index 0
l1.print_list() #2 => 3 => None
    