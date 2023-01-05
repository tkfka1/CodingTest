def solution(N, stages):
    people = len(stages)
    li = []
    
    for i in range(1,N+1):
        x = stages.count(i)
        
        if people == 0:
            li.append((x,-i))
        else:
            li.append((x/people,-i))

        people-=x
    
    li = sorted(li , reverse = True)
    
    return [i[1]*-1 for i in li]