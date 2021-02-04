# Convert sorted array to BST
# Take the mid index and make it the root node
class TreeNode(object):
    def __init__(self, x):
        # print x
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) <= 1:
            midIndex = 0
        else:
            midIndex = len(nums) / 2
        print(midIndex, nums)
        node = TreeNode(nums[midIndex])
        if midIndex != 0:
            node.left = self.sortedArrayToBST(nums[0:midIndex])
        if midIndex + 1 != len(nums):
            node.right = self.sortedArrayToBST(nums[midIndex + 1:])
        return node

    def sortedArrayToBSTIterative(self, nums):
        stack = []
        node = TreeNode(0)
        if len(nums) == 0:
            return None
        stack.append([nums, node])

        while len(stack) > 0:
            items = stack.pop()
            arr = items[0]
            parentNode = items[1]
            if len(arr) <= 1:
                midIndex = 0
            else:
                midIndex = len(arr) / 2
            parentNode.val = arr[midIndex]

            if midIndex != 0:
                parentNode.left = TreeNode(0)
                stack.append([arr[0:midIndex], parentNode.left])

            if midIndex + 1 != len(arr):
                parentNode.right = TreeNode(0)
                stack.append([arr[midIndex + 1:], parentNode.right])

        return node


n = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
