dic = {}
for i in range(1,31):
    dic[i] = 1
  
for i in range(28):
    temp = int(input())
    dic[temp] = 0

for i in dic:
  if dic[i] == 1:
    print(i)
