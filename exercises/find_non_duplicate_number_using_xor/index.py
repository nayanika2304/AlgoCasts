class Solution(object):
    def singleNumber(self,nums):
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1

        for key,value in count.items():
            if value == 1:
                return key

    def singleNumber2(self,nums):
        unique = 0

        for n in nums:
            unique = unique ^ n
        return unique
print(Solution().singleNumber2([4,3,2,4,1,3,2]))
