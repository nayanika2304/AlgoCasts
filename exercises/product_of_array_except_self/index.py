# input - [1,2,3,4]
# output - [24,12,8,6]

class Solution(object):
    def productExceptSelf(self, nums):
        L = [0] * len(nums)
        R = [0] * len(nums)

        for i in range(0, len(nums)):
            if i == 0:
                L[i] = 1
            else:
                L[i] = L[i - 1] * nums[i - 1]

        for i in reversed(range(0, len(nums))):
            if i == len(nums) - 1:
                R[i] = 1
            else:
                R[i] = R[i + 1] * nums[i + 1]

        output = []
        for i in range(0, len(nums)):
            output.append(L[i] * R[i])
        return output


print(Solution().productExceptSelf([1, 2, 3, 4]))
