<<<<<<< HEAD
def find(x):
    stack = 1
    plus = 1
    time = 0

    if x == 1:
        print("1/1")
        return
    else:
        while stack < x:
            plus += 4
            stack += plus
            time += 1

        if stack == x:
            print("1/" + str(time*2+1))
            return
        
        if stack-plus+1 == x:
            print("1/" + str(time*2))
            return
        
        a,b = 1,time*2
        temp = stack-plus+(time*2)
        if temp >= x:
            temp2 = temp - x + 1
            temp3 = b+1 - temp2
            print(str(temp3)+"/"+str(temp2))
            return
        else:
            b+=1
            temp2 = stack - x
            b -= temp2
            a += temp2
            print(str(a)+"/"+str(b))
            return




find(2)
=======
x = 2
t = 0
end = int(input())
while True:
    if t == end:
        print(x)
        break
    else:
        t += 1
        x = 2*x - 1
>>>>>>> 495900bbb5546bd4f2f8f51f79bfca60fbc595fe
