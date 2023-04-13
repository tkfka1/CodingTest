def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    for i in photo:
        sum = 0
        for ii in i:
            if dic.get(ii):
                sum += dic[ii]
        answer.append(sum)
    return answer