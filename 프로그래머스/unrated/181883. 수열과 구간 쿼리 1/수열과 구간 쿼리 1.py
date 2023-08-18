def solution(arr, queries):
    
    for v in queries:
        for i in range(v[0],v[1]+1):
            arr[i] += 1
    
    return arr