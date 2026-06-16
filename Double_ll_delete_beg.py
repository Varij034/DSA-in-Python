class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLikedList:
    def __init__(self):
        self.head=None
        
    def delete_beg(self):
        if self.head is None:
            print("List is empty")
            return
        self.head=self.head.next
        
        if self.head is not None:
            self.head.prev=None
            
    def insert_at_end(self,data):
        newnode = Node(data)
        
        if self.head is None:
            self.head=newnode
            return
        
        current=self.head
        while current.next is not None:
            current = current.next
        current.next=newnode
        newnode.prev=current
        
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end="<=>")
            current=current.next
        print("None")

dll = DoublyLikedList()
dll.insert_at_end(20)
dll.insert_at_end(10)
dll.insert_at_end(30)
dll.delete_beg()
dll.display()