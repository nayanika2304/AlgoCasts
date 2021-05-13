class Solution(object):
    def threeSumBruteForce(self,arr):
        result = []
        for i in range(0,len(arr)):
            for j in range(i + 1,len(arr)):
                for k in range(j+1,len(arr)):
                    if arr[i] + arr[j] + arr[k] == 0 :
                        result.append([arr[i],arr[j],arr[k]])
        return result

    def threeSumHashmap(self,arr):
        arr.sort()
        result = []
        for i in range(0,len(arr)):
            self.twoSumHashMap(arr,i,result)
        return result

    def twoSumHashMap(self,nums,start,result):
        values = {}
        target = -nums[start]
        for i in range(start+1,len(nums)):
            n = nums[i]
            diff = target - n
            if diff in values:
                result.append([n,diff,nums[start]])
            values[n] = 1

    def threeSumIndices(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            self.twoSumIndices(nums, i, result)
        return result

    def twoSumIndices(self, nums, start, result):
        low = start + 1
        high = len(nums) - 1
        while low < high:
            sum = nums[start] + nums[low] + nums[high]
            if sum == 0:
                result.append([nums[start], nums[low], nums[high]])
                low += 1
                high -= 1
            elif sum < 0:
                low += 1
            else:
                high -= 1


#print(Solution().threeSumBruteForce([-1, 0, 1, 2, -4, -3]))
#print(Solution().threeSumHashmap([-1, 0, 1, 2, -4, -3]))
print(Solution().threeSumIndices([-1, 0, 1, 2, -4, -3]))
