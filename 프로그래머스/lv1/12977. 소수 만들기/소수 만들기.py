def solution(nums):
    answer = 0
    
    from itertools import combinations, permutations

    combi = list(combinations(nums, 3))
    
    for com in combi:
        su = sum(com)

        x = len([i for i in range(1,int(su**0.5)+1) if su%i == 0])

        if x == 1:
            answer += 1
        
    return answer