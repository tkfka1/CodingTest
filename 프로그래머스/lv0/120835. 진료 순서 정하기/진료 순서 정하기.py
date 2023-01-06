def solution(emergency):
    answer = [0 for _ in range(len(emergency))]
    dic = {}
    for i in range(len(emergency)):
        dic[emergency[i]] = i
    
    dic = sorted(dic.items())
    print(dic)
    

    stat = len(emergency)

    for i in dic:
        answer[i[1]] = stat
        stat -= 1
    return answer