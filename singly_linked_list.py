class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def delete(self, value):
        if not self.head:
            return 
        
        curr = self.head
        prev = None

        while curr:
            if curr.val == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next

    def search(self, value):
        curr = self.head
        while curr:
            if curr.val == value:
                return True
            curr = curr.next
        return False
    
if __name__ == "__main__":
    sll = SingleLinkedList()
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    print(sll.search(2))  # True
    print(sll.search(4))  # False
    sll.delete(2)
    print(sll.search(2))  # False

# | Operation | TC   | SC   |
# | --------- | ---- | ---- |
# | Insert    | O(n) | O(1) |
# | Delete    | O(n) | O(1) |
# | Search    | O(n) | O(1) |
