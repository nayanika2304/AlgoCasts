def hIndex(pubs):
    n = len(pubs)
    freq = [0] * (n+1)

    for pub in pubs:
        if pub >= n:
            freq[n] += 1
        else:
            freq[pub] += 1

    total = 0
    i = n

    while i >= 0:
        total += freq[i]
        if total >= i :
            return i
        i -= 1

    return 0


print(hIndex([5, 3, 3, 1, 0]))
