class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=Node(10)
node2=Node(20)
node3=Node(30)

head.next = node2
node2.next = node3

current=head
if current.next.next is not None:
    current=current.next
current.next=None

current=head
while current:
    print(current.data,end="->")
    current=current.next