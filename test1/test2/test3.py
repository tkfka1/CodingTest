x = 2
t = 0
end = int(input())
while True:
    if t == end:
        print(x)
        break
    else:
        t += 1
        x = 2*x - 1