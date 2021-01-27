class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        # l1 = self.leaves(root1)
        # l2 = self.leaves(root2)
        l1 = self.leavesRecursive(root1)
        l2 = self.leavesRecursive(root2)
        return l1 == l2

    def leaves(self, root):
        stack = []
        stack.append(root)
        leaves = []
        while len(stack) > 0:
            n = stack.pop()
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
            if not n.left and not n.right:
                leaves.append(n.val)
        return leaves

    def leavesRecursive(self, n):
        leaves = []
        self.leavesRecursiveHelper(n, leaves)
        return leaves

    def leavesRecursiveHelper(self, n, leaves):
        if not n:
            return
        if not n.left and not n.right:
            leaves.append(n.val)
        self.leavesRecursiveHelper(n.left, leaves)
        self.leavesRecursiveHelper(n.right, leaves)

t1 = TreeNode(3)
t1.left = TreeNode(5)
t1.right = TreeNode(1)
t1.left.left = TreeNode(6)
t1.left.right = TreeNode(2)

t2 = TreeNode(7)
t2.left = TreeNode(2)
t2.right = TreeNode(1)
t2.left.left = TreeNode(6)
t2.left.right = TreeNode(2)

print(Solution().leafSimilar(t1, t2))
