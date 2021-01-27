class Solution(object):
    def addDigits(self, num):
        n = num
        while (n >= 10):
            sum = 0
            while n > 0:
                sum = sum + n % 10
                n = n / 10
            n = sum
        return n

print(Solution().addDigits(159))
