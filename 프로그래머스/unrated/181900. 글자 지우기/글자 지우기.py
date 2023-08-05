def solution(my_string, indices):
    answer = ''
    
    dic = {}
    
    for i in indices:
        dic[i] = 1
    
    for k,v in enumerate(my_string):
        if not dic.get(k):
            answer += v
        
    
    return answer