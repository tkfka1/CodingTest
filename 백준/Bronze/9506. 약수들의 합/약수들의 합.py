while True:
    x = int(input())
    temp = f"{x} = "
    temp_li = []
    if x == -1:
        break
    else:
        for i in range(1,x//2 + 1):
            if x%i == 0:
                temp_li.append(i)
        if x == sum(temp_li):
            if len(temp_li) == 1:
                temp += f"{str(temp_li[0])}"
            else:
                for i in range(len(temp_li)-1):
                    temp += f"{str(temp_li[i])} + "
                temp += f"{str(temp_li[-1])}"
        else:
            temp = f"{x} is NOT perfect."
        
        print(temp)
            
            