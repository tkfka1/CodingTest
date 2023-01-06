def solution(my_string):
    answer = ''
    dic = {}
    for i in my_string:
        if not dic.get(i):
            dic[i] = 1
            answer += i
    return answer