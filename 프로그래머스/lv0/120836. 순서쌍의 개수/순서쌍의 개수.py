def solution(n):
    answer = 2
    list = []
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            answer+=1
    
    if n == 1:
        return 1
    return answer