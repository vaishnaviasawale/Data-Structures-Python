class Deque:
    def __init__(self):
        self.data = []

    def insert_front(self, value):
        self.data = [value] + self.data

    def insert_rear(self, value):
        self.data.append(value)

    def delete_front(self):
        if not self.data:
            return None
        val = self.data[0]
        self.data = self.data[1:]
        return val

    def delete_rear(self):
        if not self.data:
            return None
        return self.data.pop()

    def get_front(self):
        return None if not self.data else self.data[0]

    def get_rear(self):
        return None if not self.data else self.data[-1]

# | Operation    | TC   | SC   |
# | ------------ | ---- | ---- |
# | Insert Front | O(n) | O(1) |
# | Insert Rear  | O(1) | O(1) |
# | Delete Front | O(n) | O(1) |
# | Delete Rear  | O(1) | O(1) |
# | Get Front    | O(1) | O(1) |
# | Get Rear     | O(1) | O(1) |