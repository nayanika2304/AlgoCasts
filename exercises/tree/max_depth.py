import math
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def max_depth(self,root):
        if root is None:
            return 0

        left_subtree = self.max_depth(root.left)
        right_subtree = self.max_depth(root.right)

        if left_subtree > right_subtree:
            return left_subtree + 1
        else:
            return right_subtree + 1





