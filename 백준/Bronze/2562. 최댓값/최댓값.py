a,b = 0,0
    
for i in range(9):
    temp = int(input())
    if a <= temp:
        a = temp
        b = i+1
print(f"{a} {b}")