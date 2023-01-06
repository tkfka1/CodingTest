def solution(lines):
    answer = 0
    dic = {}
    for i in lines:
        temp = i[0]
        for ii in range(i[1]-i[0]):
            if dic.get((temp,temp+1)):
                dic[(temp,temp+1)] += 1
            else:
                dic[(temp,temp+1)] = 1
            temp+=1

    for i in dic:
        if dic[i] > 1:
            answer += 1
    return answer