maxint = 0
maxx = 0
maxy = 0

for i in range(9):
    temp = list(map(int,input().split()))
    for ii in range(len(temp)):
        if temp[ii] > maxint:
            maxint = temp[ii]
            maxy = i
            maxx = ii
            
print(maxint)
print(f"{maxy+1} {maxx+1}")