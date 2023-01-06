def solution(a, b):
    answer = 0
    # 유클리드 호제법
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a
    
    calgcd = b//gcd(a,b)
    
    while True:
        if calgcd % 2 == 0:
            calgcd = calgcd//2
        else:
            break
    while True:
        if calgcd % 5 == 0:
            calgcd = calgcd//5
        else:
            break
    
    if calgcd == 1:
        return 1
    else:
        return 2
