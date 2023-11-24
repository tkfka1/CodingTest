import sys

dic = {"A+":45,"A0":40,"B+":35,"B0":30,"C+":25,"C0":20,"D+":15,"D0":10,"F":0}

su = 0
hak = 0

for i in range(20):
    temp = sys.stdin.readline().split()
    if temp[2] != "P":
        hak += int(temp[1][0])
        su += int(temp[1][0])*dic[temp[2]]

if su == 0:
    print(0)
else:
    su = su/10
    print(su/hak)