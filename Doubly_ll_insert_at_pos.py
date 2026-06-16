class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.mext=None
    
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_beg(self,data):
        newode= Node(data)
        
        if self.head is None:
            self.head=newode
            return
        
        self.head.prev=newode
        newode.next=self.head
        sefl.head=newode
    
    def insert_at_position(self,pos,data):
        new_node=Node(data)
        
        if pos == 1:
            new_node.next=self.head
            
            if self.head is not None:
                self.head.prev=new_node
            self.head=new_node
            return
        
        current=self.head
        for i in range(1,pos-1):
            current=current.next
        
        new_node.next=current.next
        new_node.prev=current
        if current.next is not None:
            current.next.prev=new_node
        current.next=new_node