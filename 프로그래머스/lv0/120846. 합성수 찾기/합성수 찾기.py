def solution(n):
    # 1을뺀 숫자
    answer = n-1
    
    def isPrime(a):
        if(a<2):
            return False
        for i in range(2,a):
            if(a%i==0):
                return False
        return True

    for i in range(n+1):
        if(isPrime(i)):
            # 소수면 1뺌
            answer -= 1
    
    return answer