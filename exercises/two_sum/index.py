class Solution(object):
    def twoSumB(self,arr,target):
        values = {}
        for i,num in enumerate(arr):
            diff = target - num
            if diff in values:
                return [i, values[diff]]
            values[num] = i
        return []


print(Solution().twoSumB([2, 7, 11, 15], 18))

