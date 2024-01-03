dic_x = {}
dic_y = {}
for i in range(3):
    x,y = map(int,input().split())
    dic_x[x] = dic_x.get(x,0) + 1
    dic_y[y] = dic_y.get(y,0) + 1

li = []

for i in dic_x:
    if dic_x[i] == 1:
        li.append(i)
for i in dic_y:
    if dic_y[i] == 1:
        li.append(i)
        
print(f"{li[0]} {li[1]}")