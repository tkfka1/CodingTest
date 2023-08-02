def solution(my_string):
    answer = [0 for i in range(52)]
    
    for i in my_string:
        temp = ord(i)
        if temp > 90:
            temp -= 71
        else:
            temp -= 65
            
        answer[temp] += 1
    
    
    
    
    return answer