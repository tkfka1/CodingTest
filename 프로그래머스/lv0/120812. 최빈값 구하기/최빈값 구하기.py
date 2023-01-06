def solution(array):
    dic = {}
    for i in array:
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 1
    maxdic = max(dic,key=dic.get)
    for key, value in dic.items():
        if value == dic[maxdic]:
            if key != maxdic:
                return -1
    return maxdic