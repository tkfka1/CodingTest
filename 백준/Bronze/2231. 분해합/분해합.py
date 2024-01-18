N = int(input())
for i in range(max(1, N - 9 * len(str(N))), N):
    if i + sum(map(int, str(i))) == N:
        print(i)
        break
else:
    print(0)