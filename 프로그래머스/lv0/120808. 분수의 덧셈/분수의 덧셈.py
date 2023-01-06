import math
def solution(denum1, num1, denum2, num2):
    x = math.gcd(num1,num2)
    
    xx = int((denum1*num2/x)+int(denum2*num1/x))
    yy = int(num1*num2/x)
    
    y = math.gcd(xx,yy)
    
    
    
    return [int(xx/y),int(yy/y)]