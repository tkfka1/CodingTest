def solution(sequence, k):
    answer = []

    if k in sequence:
        temp = sequence.index(k)
        return [temp,temp]
        
    a = 0
    b = 1
    
    s = sequence[a]+sequence[b]
    
    while True:
        if k == s:
            answer.append([b-a,a,b])
            if b == len(sequence)-1:
                s -= sequence[a]
                a += 1
            else:
                b += 1
                s += sequence[b]
        elif k > s:
            if b == len(sequence)-1:
                s -= sequence[a]
                a += 1
            else:
                b += 1
                s += sequence[b]
        else:
            s -= sequence[a]
            a += 1
        
        if a == len(sequence)-1:
            break
            
    answer = sorted(answer)
    
    return [answer[0][1],answer[0][2]]
    