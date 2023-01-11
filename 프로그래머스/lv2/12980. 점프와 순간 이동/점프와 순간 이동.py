def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    ans = 0
    
    while True:
        x,y = divmod(n,2)
        n = x
        if y == 1:
            ans += 1
        if x == 0:
            break

    return ans