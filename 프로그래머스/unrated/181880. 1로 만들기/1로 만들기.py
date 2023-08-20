def solution(num_list):
    answer = 0
    
    def go(x):
        if x % 2 == 1:
            x -= 1
        x = x//2
        return x
        
    for i in num_list:
        while i != 1:
            i = go(i)
            answer += 1
        
    return answer