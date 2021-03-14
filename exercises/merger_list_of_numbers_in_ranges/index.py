def makerange(low,high):
    return str(low) + '-' +str(high)

def findRanges(arr):
    if not arr:
        return []

    ranges= []
    low = arr[0]
    high = arr[0]

    for n in arr:
        if high + 1 < n:
            ranges.append(makerange(low,high))
            low = n
        high = n
    ranges.append(makerange(low,high))
    return ranges


print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
