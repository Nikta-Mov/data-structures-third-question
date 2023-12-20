class Queue():
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0) if self.items else None
    
    def size(self):
        return len(self.items)
    
    def front(self):
        return self.items[0] if self.items else None

    def print_element_at(self, index):
        if 0 <= index < self.size():
            print(self.items[index])
        else:
            print("Index is out of the valid range.")

queue = Queue()
queue.enqueue("ra'na") # ["ra'na"]
queue.enqueue("vez")   # ["ra'na", "vez"]
queue.enqueue("Arya")  # ["ra'na", "vez", "Arya"]
print("Queue size is:", queue.size())
print("Front of the queue is:", queue.front() if queue.front() is not None else "empty")

index_input = input("Enter the index of the element to print: ")
index = int(index_input)  

if 0 <= index < queue.size():
    print(queue.items[index])
else:
    print("Index is out of the valid range.")
print("queue size is:",q.size ())

print ("front of queue is:" , q.front())