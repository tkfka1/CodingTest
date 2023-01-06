def solution(numlist, n):
    answer = []
    li = []
    for i in numlist:
        temp = i-n
        if temp >= 0:
            li.append((temp,0))
        else:
            li.append((-temp,1))
    li = sorted(li)
    for i in li:
        if i[1]:
            answer.append(-i[0]+n)
        else:
            answer.append(i[0]+n)
    return answer