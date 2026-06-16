class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((priority, item))
        self.queue.sort()

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Empty")
        else:
            return self.queue.pop(0)

    def display(self):
        print(self.queue)

pq = PriorityQueue()
pq.enqueue("A", 2)
pq.enqueue("B", 1)
pq.enqueue("C", 3)
pq.display()
print("Deleted:", pq.dequeue())
pq.display()