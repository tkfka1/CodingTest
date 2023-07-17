def solution(n):
    answer = []
    
    while True:
        answer.append(n)
        if n % 2 == 0:
            n = n//2
        else:
            n = n*3 + 1
        
        if n == 1:
            answer.append(n)
            break
    
    return answer