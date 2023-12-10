for i in range(int(input())):
    temp = [0,0,0,0]
    x = int(input())
    a,x = divmod(x,25)
    temp[0] += a
    a,x = divmod(x,10)
    temp[1] += a
    a,x = divmod(x,5)
    temp[2] += a
    temp[3] += x
    print(" ".join(map(str, temp)))
