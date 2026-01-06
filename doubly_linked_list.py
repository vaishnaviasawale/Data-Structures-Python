class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        node = DLLNode(value)
        if not self.head:
            self.head = node
            return  
        node.next = self.head
        self.head.prev = node
        self.head = node        

    def delete(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next

                if curr.next:
                    curr.next.prev = curr.prev
                return
            curr = curr.next

# | Operation | TC   | SC   |
# | --------- | ---- | ---- |
# | Insert    | O(1) | O(1) |
# | Delete    | O(n) | O(1) |
# | Search    | O(n) | O(1) |
