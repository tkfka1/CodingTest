def solution(s1, s2):
    answer = 0
    for i in s1:
        for ii in s2:
            if i == ii:
                answer += 1
    return answer