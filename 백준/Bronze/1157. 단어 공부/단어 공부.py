temp = input()
dic = {}
ma = 0
maxli = []
for i in range(len(temp)):
    x = temp[i].upper()
    dic[x] = dic.get(x,0) + 1
    if dic[x] > ma:
        ma = dic[x]
        maxli = []
        maxli.append(x)
    elif dic[x] == ma:
        maxli.append(x)
if len(maxli) == 1:
    print(maxli[0])
else:
    print("?")