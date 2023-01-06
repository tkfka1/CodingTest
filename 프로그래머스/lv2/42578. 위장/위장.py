def solution(clothes):
    dic = {}
    for i in clothes:
        if dic.get(i[1]):
            dic[i[1]] += 1
        else:
            dic[i[1]] = 2
    answer = 1
    for key,value in dic.items():
        answer = answer*(value)
    
    answer -= 1
    return answer