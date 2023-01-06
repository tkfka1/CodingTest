def solution(n):
    n2 = 1
    n3 = 1
    if not n%2:
        n2 = 2
    if not n%3:
        n3 = 3
    return n//n2//n3