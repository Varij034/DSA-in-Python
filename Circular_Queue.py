class circular_queue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
    
    def enqueue(self,item):
        if(self.rear + 1) % self.size == self.front:
            print("Queue Overflow")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear +1) % self.size
            self.queue[self.rear]=item
        print(item,"inserted")
            
    def dequeue(self):
        if self.front == -1:
            print("Queue Empty")
        elif self.front == self.rear:
            temp=self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp=self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
    
    def display(self):
        if self.front == -1:
            print("Queue empty")
            return
        print("Queue Elements: ",end=" ")
        i=self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
        

cq = circular_queue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)

cq.display()

print("Deleted:", cq.dequeue())
print("Deleted:", cq.dequeue())

cq.display()

cq.enqueue(60)
cq.enqueue(70)

cq.display()