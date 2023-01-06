def solution(sides):
    answer = 0
    ma = max(sides)
    mi = min(sides)
    for i in range((ma-mi)+1,(ma+mi)):
        answer += 1
    return answer