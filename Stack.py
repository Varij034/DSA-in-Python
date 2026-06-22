class stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,item):
        self.stack.append(item)
        print(f"Pushed : {item}")
    
    def is_empty(self):
        return len(self.stack)==0
    
    def pop(self):
        if self.is_empty():
            return "Stack underflow"
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        print(self.stack [-1])
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        print("Current sytate of stack(Top to Bottom)",self.stack[::-1])
        
s = stack()

print(s.pop())
s.peek()
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.peek()
s.size()
s.display()