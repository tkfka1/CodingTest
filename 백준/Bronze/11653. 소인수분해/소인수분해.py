x = int(input())
answer = x
for i in range(2,x+1):
    if answer < i:
        break
    while True:
        if answer >= i:
            if answer%i == 0:
                answer = answer//i
                print(i)
            else:
                break
        else:
            break