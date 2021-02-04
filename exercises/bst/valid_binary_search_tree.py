class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


class Solution:

    def isValidBST_helper(self, n, low, high):
        if not n:
            return True
        val = n.data
        if low < val < high and self.isValidBST_helper(n.left, low, n.data) and self.isValidBST_helper(n.right, n.data,
                                                                                                       high):
            return True
        return False

    def isValidBST(self, n):
        return self.isValidBST_helper(n, float('-inf'), float('inf'))


node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(Solution().isValidBST(node))
