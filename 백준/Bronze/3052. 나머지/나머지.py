dic = {}
for i in range(10):
    dic[int(input())%42] = 1
print(len(dic))