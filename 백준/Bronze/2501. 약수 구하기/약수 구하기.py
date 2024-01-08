x,y = map(int,input().split())
stack = 0
answer = 0
for i in range(1,x+1):
    if x%i == 0:
        stack += 1
        answer = i
        
    if stack == y:
        print(answer)
        break
        
else:
    print(0)
            