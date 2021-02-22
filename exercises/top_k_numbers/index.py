import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] = counts[n] + 1
            else:
                counts[n] = 1
        return heapq.nlargest(k, counts, key = counts.get)

print(Solution().topKFrequent([1,1,1,2,2,3], 1))
