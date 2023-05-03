
def solution(n, k):
    answer = []
    li = []
    factorials = [1]
    
    for i in range(1,n+1):
        li.append(i)
    
    for i in range(1, n):
        factorials.append(factorials[-1] * i)
    
    ## print(factorials)
    
    
    k -= 1
    for i in range(n-1, -1, -1):
        print(i)
        index = k // factorials[i]
        answer.append(li[index])
        del li[index]
        k %= factorials[i]

    ## print(answer)
    
    return answer