x,y = map(str,input().split())

y = int(y)

answer = 0                  
               
for i in range(len(x)):
    if x[i].isdigit():
        print(x[i])
        print(int(x[i])*(y**(len(x)-i)))
        answer += int(x[i])*(y**(len(x)-i-1))
    else:
        print(x[i])
        print((ord(x[i])-55)*(y**(len(x)-i)))
        answer += (ord(x[i])-55)*(y**(len(x)-i-1))

print(answer)