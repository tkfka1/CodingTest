def solution(number, limit, power):
    import math
    answer = 1
    for ii in range(2,number+1):
        temp = 2
        for i in range(2, int(math.sqrt(ii)) + 1): # 2부터 ii의 제곱근까지의 모든 수를 확인하며
            if ii%i == 0:
                if ii == i*i:
                    temp += 1
                else:
                    temp += 2
                if temp > limit:
                    temp = power
                    break
        
        answer += temp      
    return answer