def solution(s):
    answer = 0
    s = s.split(" ")
    temp = 0
    for i in s:
        if i == "Z":
            answer-= temp
        else:
            answer += int(i)
            temp = int(i)
        
    return answer