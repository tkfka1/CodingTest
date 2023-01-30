def solution(e):
    
    e = e+e
    li = []
    
    for k,v in enumerate(e):
        # print(k)
        # print(v)
        if k == len(e)//2:
            break
        for i in range(len(e)//2-1):
            a = sum(e[k:k+i+1])
            li.append(sum(e[k:k+i+1]))
        
    li.append(sum(e[0:len(e)//2]))
    
    return len(set(li))
        

