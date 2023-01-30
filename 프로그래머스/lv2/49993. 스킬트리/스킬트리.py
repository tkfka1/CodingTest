def solution(s, st):
    answer = 0
    
    s_dic = {}
    for k,v in enumerate(s):
        s_dic[v] = k+1
    
    for ii in st:
        level = 1
        for i in ii:
            if s_dic.get(i):
                if s_dic[i] == level:
                    level += 1
                else:
                    break
        else:
            answer += 1
        
            
    return answer