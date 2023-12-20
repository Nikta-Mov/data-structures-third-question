class Queue():
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        else:
            return None
    
    def dequeue_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
        else:
            return None
    
    def size(self):
        return len(self.items)
    
    def front(self):
        if self.items:
            return self.items[0]
        else:
            return None
    
    def print_queue(self):
        if self.items:
            print("Current queue: " + str(self.items))
        else:
            print("Queue is empty.")

q = Queue()

q.enqueue("ra'na")
q.enqueue("vez")
q.enqueue("Arya")
q.print_queue()

item_to_remove = input("Please enter the item you want to eliminate from the queue: ")
removed_item = q.dequeue_item(item_to_remove)

if removed_item is not None:
    print(f"Item '{removed_item}' is eliminated from the queue.")
else:
    print("This item is not available in the queue.")

q.print_queue()

