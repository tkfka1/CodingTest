x = int(input())
t = x//4
answer = ""
if x%4 != 0:
    answer = "long "
    
for i in range(t):
    answer += "long "

print(answer + "int")