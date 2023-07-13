def solution(l, r):
    answer = []
    fz = ["0","5"]
    
    for i in range(l,r+1):
        temp = str(i)
        for x in temp:
            if not x in fz:
                break
        else:
            answer.append(i)
    
    if answer:
        return sorted(answer)
    else:
        return [-1]
