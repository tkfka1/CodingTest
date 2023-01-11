def solution(n):
    a,b = (1,1)
    for i in range(0,n-1):
        temp = a
        a = a+b
        b = temp
    return a%1234567