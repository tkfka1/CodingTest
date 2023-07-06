def solution(storey):
    answer = 0
    
    s_str = str(storey)
    stack = 0
    while True:
        if s_str[stack-1] == "0":
            stack -= 1
        else:
            break
    if stack != 0:
        storey = int(s_str[:stack])
    
    
    while True:
        s = str(storey)

        do_m = int(s[-1])
        s_m = storey - int(s[-1])
        s_m_str = str(s_m)
        s_m_sum = 0
        
        if s_m == 0:
            s_m_sum = do_m
        else:
            temp = int(str(s_m)[-2])
            if temp > 5:
                temp = 10 - temp
            s_m_sum = temp + do_m

            
        do_p = 10-do_m
        s_p = storey + do_p
        s_p_str = str(s_p)
        temp = int(s_p_str[-2])
        if temp > 5:
            temp = 10 - temp
        s_p_sum = temp + do_p

        if s_m_sum <= s_p_sum:
            answer += do_m
            if s_m == 0:
                break
            else:
                stack = 0
                while True:
                    if s_m_str[stack-1] == "0":
                        stack -= 1
                    else:
                        break
                
                storey = int(s_m_str[:stack])
                print(storey)
        else:
            answer += do_p
            stack = 0
            while True:
                if s_p_str[stack-1] == "0":
                    stack -= 1
                else:
                    break
            
            storey = int(s_p_str[:stack])
            print(storey)
    
        
    return answer
    
            