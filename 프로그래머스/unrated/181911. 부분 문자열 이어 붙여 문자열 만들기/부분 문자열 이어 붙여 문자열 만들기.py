def solution(my_strings, parts):
    answer = ''
    for k,v in enumerate(parts):
        answer += my_strings[k][v[0]:v[1]+1]
    return answer