class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue += [value]

    def dequeue(self):
        if not self.is_empty():
            val = self.queue[0]
            self.queue = self.queue[1:]
            return val
        return None

    def is_empty(self):
        return len(self.queue) == 0
    
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.dequeue())  # 10
    print(queue.dequeue())  # 20
    print(queue.is_empty()) # False
    print(queue.dequeue())  # 30
    print(queue.is_empty()) # True

# | Operation | TC   | SC   |
# | --------- | ---- | ---- |
# | Enqueue   | O(1) | O(1) |
# | Dequeue   | O(n) | O(1) |
# | Is Empty  | O(1) | O(1) |