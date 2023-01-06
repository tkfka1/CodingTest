def solution(numbers, k):
    if k == 1:
        return 1
    
    temp = []
    for i in range(k*2//len(numbers)+1):
        temp += numbers
    

    return temp[(k-1)*2]