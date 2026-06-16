class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CircularLinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,data):
        newnode = Node(data)
        
        if self.head is None:
            self.head=newnode
            newnode.next=self.head
            return
        
        current=self.head
        while current.next != self.head:
            current=current.next
        newnode.next=self.head
        current.next=newnode
        self.head=newnode
        
    def insert_at_pos(self,pos,data):
            newnode=Node(data)
            
            if pos == 1:
                self.insert_at_beginning(data)
                return
            current=self.head
            for i in range(1,pos-1):
                current=current.next
            newnode.next=current.next
            current.next=newnode
            
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        
        current=self.head
        while current.next != self.head:
            print(current.data,end="->")
            current=current.next
        print(current.data,end="->")
        print("(Head)")

cll = CircularLinkedList()
cll.insert_at_beginning(30)
cll.insert_at_beginning(20)
cll.insert_at_beginning(10)
cll.insert_at_pos(2,15)
cll.display()