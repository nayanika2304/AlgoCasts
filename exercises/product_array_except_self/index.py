class Solution(object):
    def productExceptSelf(self, nums):
        right = [1] * len(nums)
        prod = 1
        for i in range(len(nums)-2,-1,-1):
            prod = prod * nums[i+1]
            right[i] = prod
        prod = 1
        for i in range(1,len(nums)):
            prod = prod * nums[i-1]
            right[i] = right[i] * prod
        return right


print(Solution().productExceptSelf([1, 2, 3, 4]))
