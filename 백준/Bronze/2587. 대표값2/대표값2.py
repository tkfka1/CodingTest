aver = 0
mid = 0
li = []
for i in range(5):
    li.append(int(input()))

li = sorted(li)
print(sum(li)//5)
print(li[2])
