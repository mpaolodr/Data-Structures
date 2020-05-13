"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if tree is empty
        if self.value is None:
            self.value = BinarySearchTree(value)

        # tree not empty
        else:
            # goes left
            if value < self.value:

                if self.left is not None:
                    self.left.insert(value)
                # left of current node is empty
                else:
                    self.left = BinarySearchTree(value)

            # value is greater than or equal to current node value
            # goes right
            else:

                if self.right is not None:
                    self.right.insert(value)
                    # right of current node is empty
                else:
                    self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):

        if self.value is target:
            return True

        else:
            # goes left
            if target < self.value:

                if self.left is not None:
                    return self.left.contains(target)
                else:
                    return False

            # target is less than current node's value
            # goes right
            else:

                if self.right is not None:
                    return self.right.contains(target)
                else:
                    return False

    # Return the maximum value found in the tree

    def get_max(self):
        if not self.value:
            return

        else:
            if self.right is None:
                return self.value
            else:
                return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if not self.value:
            return

        else:
            fn(self.value)

            if self.left:
                self.left.for_each(fn)

            if self.right:
                self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
