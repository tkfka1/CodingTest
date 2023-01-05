def solution(n):
    answer = n-1
    for i in range(1,n):
        res = n%i
        if res == 1:
            answer = i
            break
    return answer