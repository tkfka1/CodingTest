str = input()
str2 = ""
for i in str:
    if i.islower():
        str2 += i.upper()
    else:
        str2 += i.lower()
print(str2)