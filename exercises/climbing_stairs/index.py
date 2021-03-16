class Solution(object):
    def staircase(self,n):
        if n<= 1:
            return 1
        return self.staircase(n-1) + self.staircase(n-2)

    def staircase2(self,n):
        prevprev = 1
        prev = 1
        current = 0

        for i in range(2,n+1):
            print(i,current,prev,prevprev)
            current = prev + prevprev
            prevprev = prev
            prev = current
        return current
print(Solution().staircase(5))
print(Solution().staircase2(5))
