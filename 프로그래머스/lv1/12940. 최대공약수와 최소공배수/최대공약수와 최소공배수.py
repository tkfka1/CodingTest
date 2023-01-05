def solution(n, m):

    def gcd(x,y):
        if(y==0):
            return x
        return gcd(y,x%y)
    
    return gcd(n,m) , n*m//gcd(n,m)