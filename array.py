class Array:

    def __init__(self):
        self.arr = []

    def insert(self, value):
        self.arr += [value]

    def delete(self, index):
        for i in range(index, len(self.arr) - 1):
            self.arr[i] = self.arr[i + 1]

        self.arr.pop() # remove last element

    def access(self, index):
        return self.arr[index]
    
    def search(self, value):
        for i in range(len(self.arr)):
            if self.arr[i] == value:
                return i
        return -1
    
if __name__ == "__main__":
    array = Array()
    array.insert(10)
    array.insert(20)
    array.insert(30)
    print(array.access(1))  # 20
    print(array.search(30))  # 2
    array.delete(1)
    print(array.search(20))  # -1

# | Operation    | TC   | SC   |
# | ------------ | ---- | ---- |
# | Insert (end) | O(1) | O(1) |
# | Delete       | O(n) | O(1) |
# | Access       | O(1) | O(1) |
# | Search       | O(n) | O(1) |

