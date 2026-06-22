class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

node1.next=node2
node2.next=node3
node3.next=node4

newnode=Node(50)
current=node1
while current is not None and current.data !=20:
    current=current.next
newnode.next=current.next
current.next=newnode

current=node1
while current:
    print(current.data,end="->")
    current=current.next