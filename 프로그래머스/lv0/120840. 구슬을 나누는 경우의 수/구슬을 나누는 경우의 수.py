def solution(balls, share):
    
    def 공식(m,n):
        a = 1
        b = 1
        for i in range(m,n,-1):
            a *= i
        for i in range(1,m-n+1):
            b *= i
        return a//b
    
    if balls-share >= share:
        return 공식(balls,balls-share)
    else:
        return 공식(balls,share)
