def solution(my_string, is_suffix):
    answer = 0
    
    li = []
    
    for i in range(len(my_string)):
        li.append(my_string[i:])

    
    if is_suffix in li:
        return 1
    else:
        return 0
