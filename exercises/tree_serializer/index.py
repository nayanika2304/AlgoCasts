class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result

class Solution(object):
    def serialize(self,node):
        if not node:
            return '#'
        return str(node.val) + " " + self.serialize(node.left) + " " + self.serialize(node.right)
    def deserialize(self,str):
        values = iter(str.split())
        return self.deserialize_helper(values)

    def deserialize_helper(self,values):
        value = next(values)
        if value == '#':
            return None

        node = Node(int(value))
        node.left = self.deserialize_helper(values)
        node.right = self.deserialize_helper(values)

        return node


#      1
#     / \
#    3   4
#   / \   \
#  2   5   7
tree = Node(1)
tree.left = Node(3)
tree.right = Node(4)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right.right = Node(7)
print(Solution().serialize(tree))
print(Solution().deserialize(Solution().serialize(tree)))
