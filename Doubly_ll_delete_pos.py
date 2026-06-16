class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insert_end(self,data):
        newnode=Node(data)

        if self.head is None:
            self.head=newnode
            return

        current=self.head

        while current.next is not None:
            current=current.next

        current.next=newnode
        newnode.prev=current

    def delete_pos(self,pos):
        if self.head is None:
            print("List is empty")
            return
        
        if pos == 1:
            self.head=self.head.next
            
            if self.head is not None:
                self.head.prev=None
            
            return
        
        current=self.head
        for i in range(1,pos):
            current=current.next
        current.prev.next=current.next

        if current.next is not None:
            current.next.prev=current.prev
        
    def display(self):
        current=self.head

        while current is not None:
            print(current.data,end=" <-> ")
            current=current.next

        print("None")

dll=DoublyLinkedList()

dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)

dll.delete_pos(3)

dll.display()