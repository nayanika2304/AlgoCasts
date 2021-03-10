class Node(object):
    def __init__(self,val,left=None,right =None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self,n):
        stack = [(1,n)]
        max_depth = 0
        while len(stack) > 0:
            depth,node = stack.pop()
            if node:
                max_depth = max(max_depth,depth)
                stack.append((depth+1,node.left))
                stack.append((depth+1,node.right))
        return max_depth
    def maxDepthRecursive(self,n):
        if not n:
            return 0
        return max(self.maxDepthRecursive(n.left)+1,self.maxDepthRecursive(n.right)+1)
n = Node(1)
n.left = Node(2)
n.right = Node(3)
n.left.left = Node(4)

print(Solution().maxDepth(n))
# 3

print(Solution().maxDepthRecursive(n))
# 3
