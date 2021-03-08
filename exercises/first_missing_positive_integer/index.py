class Solution(object):
    def first_missing_positive(self,arr):
        hash = {}
        for item in arr:
            hash[item] = 1

        for i in range(1,len(arr)):
            if i not in hash:
                return i

        return - 1

print(Solution().first_missing_positive([3,4,-1,1]))
