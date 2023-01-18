a = int(input())
b = int(input())

for i in reversed(list(map(int,str(b)))):
    print(a*i)
print(a*b)