while True:
    temp = sorted(list(map(int,input().split())))

    if temp[2] == 0:
        break
    else:
        if temp[2] == temp[0]:
            print("Equilateral")
        else:
            if temp[2] >= temp[0] + temp[1]:
                print("Invalid")
            elif temp[0] == temp[1] or temp[1] == temp[2]:
                print("Isosceles")
            else:
                print("Scalene")