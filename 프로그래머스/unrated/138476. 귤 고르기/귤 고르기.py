def solution(k, t):
    import collections
    for a,b in enumerate(sorted(collections.Counter(t).values(),reverse = True)):
        k -= b
        if k < 1:
            return a+1