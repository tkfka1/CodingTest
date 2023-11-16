li = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

temp = input()

sum = 0

for i in temp:
    for y in range(len(li)):
        for x in range(len(li[y])):
            if i == li[y][x]:
                print(y,x)
                print(2 + y)
                print(x+1)
                sum += (3 + y)

print(sum)
            