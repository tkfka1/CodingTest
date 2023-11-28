x,y = map(int, input().split())

li1 = []
li2 = []
answer = []

for i in range(x):
    li1.append(list(map(int, input().split())))

for i in range(y):
    li2.append(list(map(int, input().split())))
    
def sum_li(a,b):
    temp = []
    if not a:
        if not b:
            return temp
        return b
    if not b:
        if not a:
            return temp
        return a

    if len(a) >= len(b):
        temp = a
        for i in range(len(b)):
            temp[i] += b[i]
    else:
        temp = b
        for i in range(len(a)):
            temp[i] += a[i]
    return temp

if x >= y:
    for i in range(x):
        answer.append(sum_li(li1[i],li2[i]))
else:
    for i in range(y):
        answer.append(sum_li(li1[i],li2[i]))

for i in answer:
    print(" ".join(map(str,i)))