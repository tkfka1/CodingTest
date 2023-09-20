def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex not in i:
            for ii in i:
                answer += ii
    return answer