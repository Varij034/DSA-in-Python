class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            return self.stack.pop()

    def display(self):
        print(self.stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Stack elements:")
s.display()
print("Deleted element:", s.pop())
print("Stack after deletion:")
s.display()