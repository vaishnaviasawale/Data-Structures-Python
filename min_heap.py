# Parent index     = (i - 1) // 2
# Left child       = 2*i + 1
# Right child      = 2*i + 2


class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        self.heap += [value]
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._heapify_up(parent)

    def search(self, value):
        for i in range(len(self.heap)):
            if self.heap[i] == value:
                return i   # return index
        return -1
    
    def delete_min(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_value
    
    def delete(self, value):
        index = self.search(value)
        if index == -1:
            return False

        last_index = len(self.heap) - 1

        if index == last_index:
            self.heap.pop()
            return True

        self.heap[index] = self.heap.pop()

        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self._heapify_up(index)
        else:
            self._heapify_down(index)

        return True
    
    def _heapify_down(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)


# | Operation   | TC       | SC   |
# | ----------- | -------- | ---- |
# | Insert      | O(log n) | O(1) |
# | Delete Min  | O(log n) | O(1) |
# | Search      | O(n)     | O(1) |
# | Delete      | O(n)     | O(1) |

if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert(10)
    min_heap.insert(5)
    min_heap.insert(20)
    print(min_heap.delete_min())  # 5
    print(min_heap.search(10))     # 0
    min_heap.delete(10)
    print(min_heap.search(10))     # -1