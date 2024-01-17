from itertools import combinations

x,y = map(int,input().split())
li = list(map(int,input().split()))

combi = list(combinations(li, 3))
m = 0

for i in combi:
    temp = sum(i)
    if temp <= y:
        m = max(m,temp)
print(m)