def merge(intervals):
    intervals.sort(key = lambda x : x[0])
    i = 1
    while i < len(intervals):
        if intervals[i][0] <= intervals[i-1][1]:
            intervals[i-1][0] = min(intervals[i-1][0],intervals[i][0])
            intervals[i-1][1] = max(intervals[i-1][1],intervals[i][1])

            intervals.pop(i)
        else:
            i = i + 1
    return intervals

print(merge([[1, 3], [5, 8], [4, 10], [20, 25]]))
