import math
class Solution(object):
    def sortedSquaredArray(self,nums):
        result = [0] * len(nums)
        left = 0
        right =  len(nums) - 1
        insertLoc = right

        while left <= right:
            leftSq = nums[left] * nums[left]
            rightSq = nums[right] * nums[right]

            if leftSq <= rightSq:
                result[insertLoc] = rightSq
                right -= 1
                insertLoc -= 1
            else:
                result[insertLoc] = leftSq
                left += 1
                insertLoc -= 1
        return result


print(Solution().sortedSquaredArray([-1,-3,-5,0,1,4,5]))
