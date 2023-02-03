def solution(land):
    length = len(land) - 1

    st = 0
    while True:
        temp = sorted(land[st])       
        max1 = land[st].index(temp[-1])     
        st += 1
        for k,v in enumerate(land[st]):
            if k == max1:
                land[st][k] = v + temp[-2]
            else:
                land[st][k] = v + temp[-1]
        
        if st == length:
            return max(land[st])