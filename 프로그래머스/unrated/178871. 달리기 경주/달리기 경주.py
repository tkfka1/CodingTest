def solution(players, callings):
    answer = []
    
    dicp = {}
    dicn = {}
    for i in range(len(players)):
        dicp[players[i]] = i
        dicn[i] = players[i]
    
    for i in callings:
        ## 불린사람 등수
        n = dicp[i]
        
        ## 불린사람 앞사람 이름
        p = dicn[n-1]
        
        ## p의 순서 앞사람현재사람 교체
        dicp[p] += 1
        dicp[i] -= 1
        
        ## n의 순서 앞사람현재사람 교체
        dicn[n] = p
        dicn[n-1] = i

    for i in range(len(players)):
        answer.append(dicn[i])
    return answer