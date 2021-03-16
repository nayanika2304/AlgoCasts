class Node(object):
    def __init__(self,val,left = None,right= None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        result = self.val
        result += f"{self.left}" if self.left else ''
        result += f"{self.right}" if self.right else ''
        return result
class Solution(object):
    def invert(self,n):
        if not n:
            return None
        left = self.invert(n.left)
        right = self.invert(n.right)
        n.right = left
        n.left = right

        return n
n = Node('a')
n.left = Node('b')
n.right = Node('c')
n.left.left = Node('d')
n.left.right = Node('e')
n.right.left = Node('f')

#       a
#     /  \
#    b    c
#   / \  /
#  d  e  f

print(n)

#       a
#     /  \
#    c    b
#     \  / \
#     f e   d
print(Solution().invert(n))
# acfbed
