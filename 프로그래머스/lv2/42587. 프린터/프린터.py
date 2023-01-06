def solution(priorities, location):
    answer = 0
    x = priorities[location]
    ans_list = priorities.copy()
    ans_list[location] = 0
    a = 0
    n = 9
    while True:
        temp = []
        b = -1
        if x == n:
            break
        for i in range(len(priorities)):
            if priorities[i] == n:
                a += 1
                b = i
        if not b == -1:
            temp = priorities[b:]+priorities[:b]
            ans_list = ans_list[b:]+ans_list[:b]
        else:
            temp = priorities
        priorities = temp
        n -= 1
            
    for i in ans_list:
        if i == 0:
            answer += 1
            break
        elif i == x:
            answer += 1
    
    answer += a
    
    return answer