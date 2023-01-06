def solution(array, n):
    array = sorted(array)
    ans = []
    
    for i in range(len(array)):
        ans.append(abs(n-array[i]))
    
    return array[ans.index(min(ans))]