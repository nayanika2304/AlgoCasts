import collections

def hashkey1(s):

    return "".join(sorted(s))

def hashkey2(s):
    arr = [0] * 26
    for c in s:
        arr[ord(c) - ord('a')] += 1
    return tuple(arr)

def groupAnagramWords(strs):
    groups = collections.defaultdict(list)
    for s in strs:
        groups[hashkey1(s)].append(s)
    return groups.values()

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# (['abc', 'cba'], ['bcd', 'cbd'], ['efg'])
