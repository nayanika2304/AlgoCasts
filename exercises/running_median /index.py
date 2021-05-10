import heapq


def running_median(stream: List[int]) -> List[int]:
    heapl, heapr = [], []
res = []
for num in stream:
    heapq.heappush(heapl, num)
if len(heapl)-len(heapr) > 1:
    heapq.heappush(heapr, -(heapq.heappop(heapl)))
if len(heapl) > len(heapr):
    res.append(heapl[0])
else:
res.append((heapl[0]-heapr[0])/2)
return res
