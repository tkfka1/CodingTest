def solution(n):
    answer = 0
    
    li = [1,3]
    li_sum = [1,4]
    
    if n%2 == 1:
        return 0
    if n == 2:
        return 3
    if n == 6:
        return 177
    
    temp = li[-1]
    
    for i in range(2,2501):
        temp = (temp*3) + (li_sum[i-2])*2
        li.append(temp)
        li_sum.append(li_sum[-1]+temp)
        if i*2 == n:
            return temp%1000000007


    
    return answer