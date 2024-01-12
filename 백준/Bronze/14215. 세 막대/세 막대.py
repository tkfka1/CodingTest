li = sorted(list(map(int,input().split())))

if li[2] >= (li[0] + li[1]):
    print(2*(li[0] + li[1]) - 1)
else:
    print(sum(li))