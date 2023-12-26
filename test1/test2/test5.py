def sol(x,y,v):
    v -= x
    if v < 1:
        print("1")
        return
    a,b = divmod(v,x-y)
    if b == 0:
        print(a+1)
        return
    else:
        print(a+2)
        return
    
x,y,v =map(int, input().split())
sol(x,y,v)