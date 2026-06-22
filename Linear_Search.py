class linear_queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)
        
    def dequeue(self):
        if len(self.queue)==0:
            print("Queue Underflow")
        else:
            return self.queue.pop(0)
    
    def display(self):
        print(self.queue)
        
q = linear_queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()

q.dequeue()
q.dequeue()

q.display()