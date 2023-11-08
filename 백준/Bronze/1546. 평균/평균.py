n = int(input())
max = 0
sum = 0
li = map(int,input().split())
for i in li:
    if i > max:
        max = i
    sum += i

print(((sum*100)/n)/max)