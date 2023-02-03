def solution(want, number, discount):
    answer = 0
    from collections import deque
    
    dic = {}
    for w,n in zip(want,number):
        dic[w] = n
    
    dqin = deque(discount[:10])
    dqout = deque(discount[10:])
    
    for i in dqin:
        if dic.get(i):
            dic[i] -= 1
        elif dic.get(i) == 0:
            dic[i] = -1
    
    while True:
        for i in dic:
            if dic[i]:
                break
        else:
            answer += 1
        
        if len(dqout):
            temp = dqin.popleft()
            if dic.get(temp):
                dic[temp] += 1
            elif dic.get(temp) == 0:
                dic[temp] = 1
            
            temp = dqout.popleft()
            dqin.append(temp)
            if dic.get(temp):
                dic[temp] -= 1
            elif dic.get(temp) == 0:
                dic[temp] = -1
                
        else:
            break
        
        

    return answer