import heapq
class Solution(object):
    def meeting_rooms(self,intervals):
        if len(intervals) <= 1 :
            return intervals.length
        intervals.sort(key= lambda x: x[0])
        roomsUsed = []
        heapq.heappush(roomsUsed,intervals[0][1])

        for i in range(1,len(intervals)):
            if roomsUsed[0] <= intervals[i][0]:
                heapq.heappop(roomsUsed)
            heapq.heappush(roomsUsed,intervals[i][1])
        return len(roomsUsed)

print(Solution().meeting_rooms([[0, 10], [10, 20]]))
# 1

print(Solution().meeting_rooms([[20, 30], [10, 21], [0, 50]]))
# 3
