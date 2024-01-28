x,y = map(int, input().split())
li = sorted(list(map(int,input().split())),reverse = True)
print(li[y-1])