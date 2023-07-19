def solution(a, b, c, d):
    li = [a,b,c,d]
    dic = {}
    for i in li:
        dic[i] = dic.get(i,0) + 1

    stack = 0
    li2 = []
    for i in dic:
        if dic[i] == 4:
            return i*1111
        elif dic[i] == 3:
            if i == max(li):
                return ((10*i)+min(li))**2
            else:
                return ((10*i)+max(li))**2
        elif dic[i] == 2:
            stack += 1
        else:
            li2.append(i)
    
    if stack == 0:
        return min(li)
    elif stack == 1:
        return li2[0]*li2[1]
    else:
        return (max(li)+min(li))*abs(max(li)-min(li))