class BSTNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
            return 
        
        curr = self.root
        while True:
            if value < curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = BSTNode(value)
                    return
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = BSTNode(value)
                    return
                
    def search(self, value):
        curr = self.root
        while curr:
            if value == curr.value:
                return True
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return False
    
    def delete(self, value):
        curr = self.root
        parent = None

        # Step 1: Find the node to delete
        while curr and curr.value != value:
            parent = curr
            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        # Value not found
        if not curr:
            return

        # Step 2: Case 1 & 2 — node has 0 or 1 child
        if not curr.left or not curr.right:
            # Determine child
            child = curr.left if curr.left else curr.right

            # If deleting root
            if not parent:
                self.root = child
            else:
                if parent.left == curr:
                    parent.left = child
                else:
                    parent.right = child
            return

        # Step 3: Case 3 — node has 2 children
        # Find inorder successor (smallest in right subtree)
        succ_parent = curr
        succ = curr.right

        while succ.left:
            succ_parent = succ
            succ = succ.left

        # Replace value
        curr.value = succ.value

        # Delete successor node
        if succ_parent.left == succ:
            succ_parent.left = succ.right
        else:
            succ_parent.right = succ.right
 
        

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    print(bst.search(5))   # True
    print(bst.search(20))  # False

# | Operation | Average  | Worst | SC   |
# | --------- | -------- | ----- | ---- |
# | Insert    | O(log n) | O(n)  | O(n) |
# | Search    | O(log n) | O(n)  | O(n) |
# | Delete    | O(log n) | O(n)  | O(n) |