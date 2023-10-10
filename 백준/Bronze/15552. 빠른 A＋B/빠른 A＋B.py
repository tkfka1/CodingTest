import sys

x = int(sys.stdin.readline().rstrip())
for i in range(x):
    temp = sys.stdin.readline().rstrip()
    print(sum(map(int, temp.split())))
