
def sol(x):
    if x == 1:
        print(1)
    
    else:
        a = 1
        b = 6
        stack = 1
        while a < x:
            a += b
            b += 6
            stack += 1
        print(stack)


sol(13)