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


find(int(input()))