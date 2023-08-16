def solution(num_list):
    
    sum_odd = 0
    sum_even = 0
    
    for i in range(len(num_list)):
        if i % 2 == 1:
            sum_odd += num_list[i]
        else:
            sum_even += num_list[i]
    
    
    return max(sum_odd,sum_even)