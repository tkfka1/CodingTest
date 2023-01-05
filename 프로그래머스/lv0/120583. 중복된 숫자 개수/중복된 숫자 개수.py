def solution(array, n):
    answer = 0
    for i in sorted(array):
        if i > n:
            break
        elif i == n:
            answer += 1
            
            
    return answer