class Solution(object):
    def maxSubArray(self,nums):
        if not nums:
            return 0
        maxSum = 0
        sum = 0

        for n in nums:
            sum += n
            if sum < 0:
                sum = 0
            else:
                maxSum = max(maxSum,sum)
        return maxSum

print(Solution().maxSubArray([-2, 1]))
# 6

print(Solution().maxSubArray([-1, -4, 3, 8, 1]))
# 12

