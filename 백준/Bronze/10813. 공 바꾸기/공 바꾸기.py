n, m = map(int, input().split())
li = [i + 1 for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    li[a-1], li[b-1] = li[b-1], li[a-1]  # Swapping elements

print(" ".join(map(str, li)))