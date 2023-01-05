def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    temp = reserve[:]

    for i in reserve:
        for ii in lost:
            if i == ii:
                lost.remove(ii)
                temp.remove(i)

    reserve = temp
    
    print(lost)
    print(reserve)
    
    answer = n - len(lost)
    pre = 0
    for i in lost:
        for ii in reserve:
            if i-1 == ii:
                pre = ii
                answer += 1
                break
                
            if i+1 == ii:
                pre = ii
                answer += 1
                break
        if pre:
            reserve.remove(pre)
        pre = 0

    return answer