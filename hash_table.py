class HashTable:
    def __init__(self, size = 10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        # hash function to compute index
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        # Check if the key already exists and update
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Otherwise, insert new key-value pair
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

# | Operation | Average TC | Worst TC | SC   |
# | --------- | ---------- | -------- | ---- |
# | Insert    | O(1)       | O(n)     | O(n) |
# | Search    | O(1)       | O(n)     | O(n) |
# | Delete    | O(1)       | O(n)     | O(n) |