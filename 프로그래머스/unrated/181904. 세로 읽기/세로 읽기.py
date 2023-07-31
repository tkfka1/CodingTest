def solution(my_string, m, c):
    answer = ''
    li = []
    temp = ""
    temp_m = 0
    for k,v in enumerate(my_string):
        temp += v
        temp_m += 1
        if temp_m == m:
            li.append(temp)
            temp = ""
            temp_m = 0
            
    for i in li:
        answer += i[c-1]
    
    return answer