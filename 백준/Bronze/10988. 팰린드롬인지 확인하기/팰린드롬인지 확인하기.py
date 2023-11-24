temp = input()
for i in range(len(temp) // 2):

  if temp[i] != temp[-i - 1]:
    print("0")
    break
else:
  print("1")
