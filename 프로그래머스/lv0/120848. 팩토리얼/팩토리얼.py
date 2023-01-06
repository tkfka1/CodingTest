def solution(n):
    answer = 0
    an = 1
    a = [2,3,4,5]
    if n == 1:
        return n
    if n in a:
        return 2
    
    for i in range(2,n):
        an = an * i
        if an > n:
            return i-1