for i in range(int(input())):
    temp = ""
    x,y = map(str,input().split())
    for i in y:
        temp += i*int(x)
    print(temp)