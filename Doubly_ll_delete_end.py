class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_end(self,data):
        newnode=Node(data)
        
        if self.head is None:
            self.head=newnode
            return
        
        current=self.head
        while current.next is not None:
            current=current.next
        current.next = newnode
        newnode.prev=current
        
    def delete_end(self):
        if self.head is None:
            print("List is Empty")
            return
        
        if self.head.next is None:
            self.head=None
            return
        
        current=self.head
        while current.next is not None:
            current=current.next
        current.prev.next=None
    
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=" <=> ")
            current=current.next
        print("None")

dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.delete_end()
dll.display()