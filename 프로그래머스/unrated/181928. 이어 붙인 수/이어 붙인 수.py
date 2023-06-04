def solution(num_list):
    answer = 0
    od = ""
    ev = ""
    
    for i in num_list:
        if i%2 == 1:
            od += str(i)
        else:
            ev += str(i)
    
    return int(od) + int(ev)