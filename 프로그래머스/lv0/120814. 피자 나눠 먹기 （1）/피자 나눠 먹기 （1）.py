def solution(n):
    x,y =  divmod(n,7)
    if y != 0:
        x+=1
    return x