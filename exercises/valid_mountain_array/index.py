# Check if it is a valid mountain array
# [1,2,3,4,5,4,3,2,1]

NONE = 0b00
UP = 0b01
DOWN = 0b10

class Solution(object):
    def mountain_array(self,A):
        direction = NONE
        for i in range(0,len(A)):
            if i <=0 :
                continue
            if direction == NONE:
                if A[i] > A[i-1]:
                    direction = UP
                    continue
            if direction == UP:
                if A[i] > A[i-1]:
                    continue
                if A[i] < A[i-1]:
                    direction = DOWN
            if direction == DOWN:
                if A[i] > A[i-1]:
                    continue
            return False
        return direction == DOWN

print(Solution().mountain_array([1,2,3]))
