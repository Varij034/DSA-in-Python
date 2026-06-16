class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return
        temp = self.top.data
        self.top = self.top.next
        return temp

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Stack Elements:")
s.display()
print("Deleted:", s.pop())
print("After Pop:")
s.display()