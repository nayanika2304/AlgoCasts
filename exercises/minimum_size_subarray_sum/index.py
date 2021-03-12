class Solution(object):
    def minimum_subarray_sum(self, sum, arr):
        result = float('inf')
        left = 0
        val_sum = 0
        for i in range(len(arr)):
            val_sum += arr[i]
            while val_sum >= sum:
                result = min(result,i+1-left)
                val_sum -= arr[left]
                left += 1
        return result


print(Solution().minimum_subarray_sum(7, [2, 3, 1, 2, 4, 3]))
#2 because [2,3,1,2] and [4,3]
