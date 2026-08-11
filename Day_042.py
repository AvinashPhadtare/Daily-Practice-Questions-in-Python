# Question:-
# Build a BST to store gym member IDs for fast lookup.
#
# Operations:
# insert(val)  -> insert value
# search(val)  -> return True/False
# inorder()    -> return sorted list of all values
# min_val()    -> return smallest ID
# max_val()    -> return largest ID
# delete(val)  -> remove a value
#
# Insert: [50, 30, 70, 20, 40, 60, 80]
# Delete 30
# Print inorder.


# Solution:- 
# Node represents one element of the BST
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Binary Search Tree
class BST:

    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, val):

        if self.root is None:
            self.root = Node(val)
            return

        self._insert(self.root, val)

    def _insert(self, root, val):

        if val < root.value:

            if root.left is None:
                root.left = Node(val)
            else:
                self._insert(root.left, val)

        elif val > root.value:

            if root.right is None:
                root.right = Node(val)
            else:
                self._insert(root.right, val)

    # Search for a value
    def search(self, val):

        return self._search(self.root, val)

    def _search(self, root, val):

        if root is None:
            return False

        if val == root.value:
            return True

        if val < root.value:
            return self._search(root.left, val)

        return self._search(root.right, val)

    # Inorder traversal
    def inorder(self):

        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):

        if root is None:
            return

        self._inorder(root.left, result)
        result.append(root.value)
        self._inorder(root.right, result)

    # Find minimum value
    def min_val(self):

        if self.root is None:
            return None

        current = self.root

        while current.left is not None:
            current = current.left

        return current.value

    # Find maximum value
    def max_val(self):

        if self.root is None:
            return None

        current = self.root

        while current.right is not None:
            current = current.right

        return current.value

    # Delete a value
    def delete(self, val):

        self.root = self._delete(self.root, val)

    def _delete(self, root, val):

        # Value not found
        if root is None:
            return None

        # Search in left subtree
        if val < root.value:
            root.left = self._delete(root.left, val)

        # Search in right subtree
        elif val > root.value:
            root.right = self._delete(root.right, val)

        # Value found
        else:

            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: Only right child
            if root.left is None:
                return root.right

            # Case 2: Only left child
            if root.right is None:
                return root.left

            # Case 3: Two children
            successor = root.right

            while successor.left is not None:
                successor = successor.left

            root.value = successor.value

            root.right = self._delete(root.right, successor.value)

        return root



# Example Usage:-
# Create BST
bst = BST()

# Insert gym member IDs
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.insert(value)

# Delete 30
bst.delete(30)

# Print sorted values
print("Inorder:", bst.inorder())

# Other operations
print("Search 60:", bst.search(60))
print("Minimum:", bst.min_val())
print("Maximum:", bst.max_val())
