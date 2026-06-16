class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_beg(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head=new_node
            return
        
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    
    def display(self):
        current=self.head
        while current is not None:
            print(current.data , end = "<->")
            current=current.next
        print("None")
        
dll = DoublyLinkedList()
dll.insert_at_beg(30)
dll.insert_at_beg(20)
dll.insert_at_beg(10)
dll.display()