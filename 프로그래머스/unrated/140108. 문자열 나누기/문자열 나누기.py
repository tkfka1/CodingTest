def solution(s):
    answer = 0
    #최고 빈도수 문자 카운트
    count_max = 0
    #다른 문자가 나온 카온트
    count_diff = 0
    #이전문자
    pre_s = ""
    for i in s:
        if not pre_s:
            pre_s = i
        if i == pre_s:
            count_max += 1
        else:
            count_diff += 1
        
        if count_max == count_diff:
            pre_s = ""
            answer += 1
            count_max = 0
            count_diff = 0
    else:
        if pre_s:
            answer += 1
    
    return answer