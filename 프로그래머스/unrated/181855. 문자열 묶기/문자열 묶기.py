def solution(strArr):
    dic = {}
    for i in strArr:
        dic[len(i)] = dic.get(len(i),0) + 1
    return dic[max(dic, key=dic.get)]