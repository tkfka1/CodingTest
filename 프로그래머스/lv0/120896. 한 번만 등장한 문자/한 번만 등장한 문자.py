def solution(s):
    answer = ''
    dic = {}
    for i in s:
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 1
            
    for i in dic:
        if dic[i] == 1:
            answer += i
    return ''.join(sorted(answer))