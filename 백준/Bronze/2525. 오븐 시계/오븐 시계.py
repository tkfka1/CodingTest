x,y = map(int,input().split())
y += int(input())

if y >= 60:
    temp = y//60
    x += temp
    y -= temp * 60

if x >= 24:
    x -= 24

print(str(x)+" "+str(y))