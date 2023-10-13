for i in range(int(input())):
    temp = list(map(int, input().split()))
    print(f"Case #{i+1}: {temp[0]} + {temp[1]} = {sum(temp)}")