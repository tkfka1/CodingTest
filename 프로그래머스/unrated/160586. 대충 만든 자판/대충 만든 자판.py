def solution(k, t):
    answer = []
    dic = {}
    for i in k:
        for index,value in enumerate(i):
            if dic.get(value):
                if dic[value] > index+1:
                    dic[value] = index+1
            else:
                dic[value] = index+1
    
    for i in t:
        temp = 0
        for ii in i:
            if dic.get(ii):
                temp += dic[ii]
            else:
                temp = -1
                break
        answer.append(temp)

    return answer