def solution(a, b, n):
    answer = 0
    
    pre = 0
    while True:
        if n < a:
            break
        
        n,x = divmod(n,a)
        answer += n*b
        n = n*b+x
    
    
    return answer