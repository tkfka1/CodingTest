def solution(picks, minerals):
    answer = 0
    
    ##sum picks
    
    pick_sum = sum(picks)
    
    
    ## 모든 피로도 계산
    m_li = []
    m_li_all = []
    stack = 0
    d = 0
    i = 0
    s = 0
    for m in minerals:
        if m[0] == "d":
            d += 1
            i += 5
            s += 25
        elif m[0] == "i":
            d += 1
            i += 1
            s += 5
        else:
            d += 1
            i += 1
            s += 1
            
        stack += 1
        if stack == 5:
            stack = 0
            m_li.append([-(d+i+s),d,i,s])
            d,i,s = 0,0,0
    else:
        if stack != 0:
            m_li.append([-(d+i+s),d,i,s])
            d,i,s = 0,0,0
            
            
    if pick_sum < len(m_li):
        m_li = m_li[:pick_sum]
        
    m_li = sorted(m_li)
    

    stack = 0
    for i in range(3):
        while picks[i] > 0:
            picks[i] -= 1
            answer += m_li[stack][1+i]
            stack += 1
            if stack == len(m_li):
                return answer
    
    
    
    
    
    
    return answer