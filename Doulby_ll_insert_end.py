class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    
    def insert_at_beg(self,data):
        newnode = Node(data)
        
        if self.head is None:
            self.head=newnode
            return
        
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
        
        
    def insert_at_end(self,data):
        new_node=Node(data)
        
        if self.head is None:
            self.head=new_node
            return
        
        current=self.head
        while current.next is not None:
            current=current.next
            
        current.next=new_node
        new_node.prev=current
        
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end="<=>")
            current=current.next
        print("None")

dll = DoublyLinkedList()
dll.insert_at_beg(40)
dll.insert_at_beg(30)
dll.insert_at_beg(20)
dll.insert_at_beg(10)
dll.insert_at_end(50)
dll.display()