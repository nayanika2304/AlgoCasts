class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # returns (True,height)
    def _is_balancedHelper(self,n):
        if not n:
            return True, 0
        lbalanced,lheight = self._is_balancedHelper(n.left)
        rbalanced,rheight = self._is_balancedHelper(n.right)

        return lbalanced and rbalanced and abs(lheight - rheight) <= 1, max(lheight,rheight) + 1

    def is_balanced(self,n):
        return self._is_balancedHelper(n)[0]

n = Node(1)
n.left = Node(2)
n.left.left = Node(4)
n.right = Node(3)
#    1
#   / \
#  2   3
# /
#4
print(Solution().is_balanced(n))

n.right = None
#    1
#   /
#  2
# /
#4
print(Solution().is_balanced(n))
# False
