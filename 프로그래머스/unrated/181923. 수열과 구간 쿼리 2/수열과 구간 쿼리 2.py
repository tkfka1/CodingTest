def solution(arr, queries):
    answer = []
    
    for k,q in enumerate(queries):
        
        for i in range(q[0],q[1]+1):
            if i == len(arr):
                break
            if q[2] < arr[i]:
                if len(answer) == k:
                    answer.append(arr[i])
                else:
                    answer[k] = min(answer[k],arr[i])
        if len(answer) == k:
            answer.append(-1)
            
    return answer