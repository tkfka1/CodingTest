x = list(map(int,input().split()))

if x[1] >= 45:
    print(x[0], x[1]-45)
    
else:
    if x[0] == 0:
        x[0] = 23
    else:
        x[0] -= 1
        
    print(x[0], x[1]+15)