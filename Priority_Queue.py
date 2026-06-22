class priority_queue:
    def __init__(self):
        self.queue=[]
    
    def enqueue(self,item,priority):
        self.queue.append((priority,item))
        self.queue.sort()
    
    def dequeue(self):
        if len(self.queue)==0:
            print("Queue Underflow")
        else:
            return self.queue.pop(0)
    
    def display(self):
        for priority, item in self.queue:
            print(item, end=" ")
        print()
        
q = priority_queue()

q.display()
q.enqueue(40,4)
q.enqueue(10,1)
q.enqueue(30,3)
q.enqueue(20,2)

q.dequeue()
q.dequeue()
q.display()
