n,m = map(int,input().split())

li1 = []
li2 = []

for i in range(n):
    li1.append(list(map(int,input().split())))
    
for i in range(n):
    li2.append(list(map(int,input().split())))

for y in range(n):
    for x in range(m):
        li1[y][x] += li2[y][x]

if li1:        
    for i in li1:
        print(" ".join(list(map(str,i))))
else:
    print("")
        