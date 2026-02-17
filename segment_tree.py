# https://cp-algorithms.com/data_structures/segment_tree.html

# A Segment Tree is a data structure that lets you efficiently answer range queries and perform updates on an array.

# It is commonly used when you need fast:
# range sum
# range minimum / maximum
# range GCD
# frequency counts
# interval updates

# 🧠 Why do we need it?
# Suppose you have an array:
# arr = [2, 1, 5, 3, 4]

# and need to repeatedly answer:
# sum from index L to R
# update an element

# ❌ Naive approach
# range sum → O(N)
# update → O(1)
# Too slow for many queries.

# ❌ Prefix sum
# range sum → O(1)
# update → O(N)
# Still slow for updates.

# ✅ Segment Tree Performance
# Operation	Time
# Build	O(N)
# Range Query	O(log N)
# Update	O(log N)

# 🌳 Core Idea
# Divide the array into segments.
# Example:
# arr = [2,1,5,3,4]

# Tree structure:

#                 [0-4]
#               /       \
#            [0-2]     [3-4]
#           /    \     /   \
#        [0-1]  [2]  [3]  [4]
#       /   \
#     [0]  [1]


# Each node stores information about its range.
# For sum tree:
# node value = sum of its segment

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n) # 4n 
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        # We store tree in an array:
        # index 0 → root
        # index 1 → left child
        # index 2 → right child

        # So children of node i:
        # left = 2*i + 1
        # right = 2*i + 2

        if start == end:
            self.tree[node] = arr[start]
            return 
        
        mid = (start + end) // 2

        self.build(arr, 2 * node + 1, start, mid)
        self.build(arr, 2 * node + 2, mid + 1, end)

        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def query(self, node, start, end, L, R):
        # no overlap
        if R < start or end < L:
            return 0
        
        # total overlap
        if L <= start and end <= R:
            return self.tree[node]
        
        # partial overlap
        mid = (start + end) // 2

        left = self.query(2 * node + 1, start, mid, L, R)
        right = self.query(2 * node + 2, mid + 1, end, L, R)

        return left + right

    def update(self, node, start, end, idx, value):
        if start == end:
            self.tree[node] = value
            return
        
        mid = (start + end) // 2

        if idx <= mid:
            self.update(2 * node + 1, start, mid, idx, value)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, value)

        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

if __name__ == "__main__":
    arr = [2,1,5,3,4]
    st = SegmentTree(arr)

    print(st.query(0,0,4,1,3))   # sum from index 1 to 3 → 1+5+3 = 9

    st.update(0,0,4,2,10)        # arr[2] = 10

    print(st.query(0,0,4,1,3))   # 1+10+3 = 14