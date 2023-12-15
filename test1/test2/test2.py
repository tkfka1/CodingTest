n,m = map(int, input().split())
temp = [i+1 for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    temp[a:b] = reversed(temp[a:b])
    print(" ".join(temp))