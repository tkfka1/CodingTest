t = input()
li = list(map(int, input().split()))

n=max(li)
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

answer = 0
            
for i in li:
    if a[i]:
        answer += 1
            
print(answer)
