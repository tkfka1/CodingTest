import re

def solution(X, Y):
    answer = ''
    dic = {}
    for i in range(9,-1,-1):
        dic[i] = min(X.count(str(i)),Y.count(str(i)))
    
    #print(dic)
    
    for i in dic:
        answer += str(i)*dic[i]
    
    if not answer:
        return "-1"
    if answer[0] == "0":
        return "0"
    
    return answer