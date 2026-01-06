class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:

    # ---------- HEIGHT ----------
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # ---------- BALANCE ----------
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # ---------- RIGHT ROTATION ----------
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    # ---------- LEFT ROTATION ----------
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    # ---------- INSERT ----------
    def insert(self, root, value):
        # Normal BST insertion
        if not root:
            return AVLNode(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        else:
            return root  # duplicates not allowed

        # Update height
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Balance factor
        balance = self.get_balance(root)

        # LL
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # RR
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # LR
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # ---------- DELETE----------
    def delete(self, root, value):
        if not root:
            return root

        # BST delete
        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        # Update height
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        # LL
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current


    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

avl = AVLTree()
root = None

for val in [10, 20, 30, 40, 50, 25]:
    root = avl.insert(root, val)

avl.inorder(root)
print()

root = avl.delete(root, 40)
avl.inorder(root)
print()

# | Operation | Time     | Space    |
# | --------- | -------- | -------- |
# | Insert    | O(log n) | O(log n) |
# | Delete    | O(log n) | O(log n) |
# | Search    | O(log n) | O(1)     |
