n,m = input().split()
dic = {}

for i in range(int(n)):
    dic[i+1] = 0

for i in range(int(m)):
    a,b,c = map(int,input().split())
    for ii in range(a,b+1):
        dic[ii] = c
        
temp = ""
for i in dic:
    temp += str(dic[i]) + " "

print(temp)