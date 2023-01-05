def solution(n):
    # return len([a for a in [len([i for i in range(1,x+1) if not x%i]) for x in range(1,n+1)] if a==2])
    
    
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    
    return len(primes)