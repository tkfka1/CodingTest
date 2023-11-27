x = int(input())

for i in range(x):
    print(" "*(x-i-1) + "*"*(i*2+1) + " ")
for i in range(x-1):
    print(" "*(i+1) + "*"*(2*(x-i)-3) + " ")