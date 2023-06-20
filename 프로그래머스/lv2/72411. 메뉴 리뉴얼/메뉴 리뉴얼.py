from itertools import combinations
def solution(orders, course):
    answer = []

    dic = {}

    for o in orders:
        if len(o) > 1:
            o = sorted(o)
            o = "".join(o)
            for i in course:
                for combi in combinations(o,i):
                    combi = "".join(combi)
                    dic[combi] = dic.get(combi,0) + 1

    dic_ans = {}
    
    for i in course:
        dic_ans[i] = [0,""]
    
    for key,value in dic.items():
        if dic_ans.get(len(key)):
            if dic_ans[len(key)][0] < value:
                dic_ans[len(key)] = [value,key]
            elif dic_ans[len(key)][0] == value:
                dic_ans[len(key)].append(key)
                    

    for i in dic_ans:
        if dic_ans[i][0] > 1:
            answer += dic_ans[i][1:]
        
    
    return sorted(answer)