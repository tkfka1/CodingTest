dic = {}

for i in range(97, 123):
  a = chr(i)
  dic[a] = -1

temp = input()

for k, v in enumerate(temp):
  if dic[v] == -1:
    dic[v] = k

print(" ".join(map(str, list(dic.values()))))
