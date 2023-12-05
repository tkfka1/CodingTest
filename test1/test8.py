li = [["" for ii in range(15)] for i in range(5)]

for y in range(5):
    temp = input().split()
    for x in range(len(temp)):
        li[y][x] = temp[x]

answer = ""

for x in range(15):
    for y in range(5):
        if li[y][x]:
            answer += li[y][x]   

print(li)
print(answer)
