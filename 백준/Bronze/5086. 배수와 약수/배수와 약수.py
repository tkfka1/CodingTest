while True:
    x,y = map(int,input().split())
    if x == 0:
        if y == 0:
            break
    if x > y:
        temp = divmod(x,y)
        if temp[1] == 0:
            print("multiple")
        else:
            print("neither")
    else:
        temp = divmod(y,x)
        if temp[1] == 0:
            print("factor")
        else:
            print("neither")