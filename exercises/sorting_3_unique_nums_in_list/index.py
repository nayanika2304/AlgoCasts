class Solution(object):
    def sortNums(self, nums):
        dict = {}
        for n in nums:
            dict[n] = dict.get(n,0) + 1
        return ([1] * dict.get(1,0) + [2] * dict.get(2,0) + [3] * dict.get(3,0))

    def sortNums2(self,nums):
        one_index = 0
        index = 0
        three_index = len(nums) -1
        while index <= three_index:
            if nums[index] == 1:
                nums[index] , nums[one_index] = nums[one_index], nums[index]
                one_index += 1
                index += 1
            elif nums[index] == 2:
                index += 1
            elif nums[index] == 3:
                nums[index] , nums[three_index] = nums[three_index], nums[index]
                three_index -=1
        return nums

print(Solution().sortNums2([3, 3, 2, 1, 3, 2, 1]))
