def solution(r):
    answer = 0
    
    r.sort(key=lambda x:(x[1], x[0]))
    
    # print(r)
    
    while(len(r)):
        idx=0
        camera=r[0][1]
        for i in range(len(r)):
            if r[idx][0]<=camera:
                r.pop(idx)
            else:
                idx+=1

        answer+=1
        
    return answer