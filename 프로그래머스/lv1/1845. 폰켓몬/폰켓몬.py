def solution(nums):
    answer = 0
    
    nlen = len(nums)
    ndivlen = nlen//2
    num_list = list(set(nums))
    
    answer = len(num_list)
    
    if ndivlen < answer:
        answer = ndivlen
    
    return answer