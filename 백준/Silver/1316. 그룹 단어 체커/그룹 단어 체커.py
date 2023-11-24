x = int(input())

answer = 0

for i in range(x):
    temp = input()
    bf = ""
    li = []
    for x in temp:
        if x != bf:
            if x not in li:
                bf = x
                li.append(x)
            else:
                break
    else:
        answer += 1
print(answer)
        