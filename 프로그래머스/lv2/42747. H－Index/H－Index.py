def solution(citations):
    li = sorted(citations, reverse = True)
    count = 0
    suminyong = 0
    for i in range(len(li),0,-1):
        while True:
            if li[count] >= i:
                suminyong += 1
            else:
                break
            count += 1
            if count == len(li):
                break
        if count == len(li)-1:
            break
        if suminyong >= i:
            break
    
    if suminyong < i:
        return suminyong

    return i