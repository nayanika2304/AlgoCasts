class Solution(object):
    def checkPossibility(self, nums):
        index = -1
        for i in range(0,len(nums)):
            if nums[i] > nums[i+1]:
                if index != -1:
                    return False
                index = i

        if index == -1:
            return True
        if index == 0:
            return True
        if index == len(nums) -2:
            return True
        if nums[index] <= nums[index+2]:
            return True
        if nums[index -1] <= nums[index+1]:
            return True
        return False



print(Solution().checkPossibility([4, 1, 2]))
#True
print(Solution().checkPossibility([3, 2, 4, 1]))
#False
print(Solution().checkPossibility([1,5,2,3,4]))
#True
