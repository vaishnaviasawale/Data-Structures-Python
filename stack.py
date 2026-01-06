class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack += [value]

    def pop(self):
        if not self.is_empty():
            val = self.stack[-1]
            self.stack = self.stack[:-1]
            return val
        return None

    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        return self.stack[-1] if not self.is_empty() else None
    

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.peek())     # 30
    print(stack.pop())      # 30
    print(stack.is_empty()) # False
    print(stack.pop())      # 20
    print(stack.pop())      # 10
    print(stack.is_empty()) # True

# | Operation | TC   | SC   |
# | --------- | ---- | ---- |
# | Push      | O(1) | O(1) |
# | Pop       | O(1) | O(1) |
# | Peek      | O(1) | O(1) |
# | Is Empty  | O(1) | O(1) |