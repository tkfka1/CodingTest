def solution(arr):
    stk = []
    
    i = 0
    while True:
        if stk:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()
        else:
            stk.append(arr[i])
            i += 1
        
        if i+1 > len(arr):
            break
            
    return stk