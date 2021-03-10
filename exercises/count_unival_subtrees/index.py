class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_unival_subtrees(n):
    count, is_unival = _count_unival_helper(n)
    return count


def _count_unival_helper(n):

    if not n:
        return 0, True
    left_count, is_left_unival = _count_unival_helper(n.left)
    right_count, is_right_unival = _count_unival_helper(n.right)

    if is_left_unival and is_right_unival and (not n.left or n.left.val == n.val) and (
            not n.right or n.right.val == n.val):
        return left_count + right_count + 1, True

    return left_count + right_count, False


#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))
# 5
