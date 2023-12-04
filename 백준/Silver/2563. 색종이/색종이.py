li = [[0 for i in range(100)] for ii in range(100)]

answer = 0

for i in range(int(input())):
    x,y = map(int,input().split())
    for yy in range(10):
        yyy = yy+y
        if yyy < 100:
            for xx in range(10):
                xxx = xx+x
                if xxx < 100:
                    if li[yyy][xxx] == 0:
                        li[yyy][xxx] = 1
                        answer += 1

print(answer)