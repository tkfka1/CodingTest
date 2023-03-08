def solution(n):
    # 단순계산
    # global answer
    # answer = 0
    # def cal(n):
    #     global answer
    #     if n == 0:
    #         answer += 1
    #     elif n == 1:
    #         cal(n-1)
    #     else:
    #         cal(n-1)
    #         cal(n-2)
    
    
    '''
        1 = 1
        2 = 2
        3 = 3
        4 = 5
        5 = 8
        6 = 13
        7 = 21
        8 = 34
    '''
    
    li = [0,1,2]
    
    for i in range(2,n):
        li.append((li[i]+li[i-1])%1000000007)
    
    return li[n]%1000000007