def solution(arr, k):
    temp = [i for i in dict.fromkeys(arr,0)]
    
    if len(temp) <= k:
        for i in range(k-len(temp)):
            temp.append(-1)
    else:
        temp = temp[:k]
    return temp