def solution(sizes):
    x = 0
    y = 0
    for r in sizes:
        if r[1] > r[0]:
            t = r[1], r[0]
            r = t
        if x < r[0]:
            x = r[0]
        if y < r[1]:
            y = r[1]
    answer = x*y
    return answer