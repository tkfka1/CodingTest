x,y = map(int, input().split())
li = ""
for i in list(map(int,input().split())):
    if i < y:
        li += str(i)+" "
print(li)