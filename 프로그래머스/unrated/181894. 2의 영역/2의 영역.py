def solution(arr):
    start,end = -1,-1
    
    for i in range(len(arr)):
        if arr[i] == 2:
            start = i
            break
            
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == 2:
            end = i
            break

    if start == -1:
        return [-1]
    
    return arr[start:end+1]