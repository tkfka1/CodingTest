s = int(input())
n = int(input())
ss = 0

for i in range(n):
    item, item_n = map(int,input().split())
    ss += item*item_n
    
if ss == s:
    print("Yes")
else:
    print("No")