class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)

head.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
new_node=Node(60)

current=head
while current is not None and current.data != 40:
    current=current.next
new_node.next=current.next
current.next=new_node

while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")


"""
insert at end
current=head
while current.next is not None:
    current=current.next
current.next = new_node
"""
"""
insert at beginning
current=head
new_node.next=current
current=new_node
"""
