a = input()
x = list(map(int,input().split()))
dic = {}
for i in x:
    dic[i] = dic.get(i, 0) + 1
temp = int(input())
if dic.get(temp):
    print(dic[temp])
else:
    print("0")