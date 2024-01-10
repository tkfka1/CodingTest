m = int(input())
n = int(input())

a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

answer = []
            
for i in range(m,n+1):
    if a[i]:
        answer.append(i)

if answer:
    print(sum(answer))
    print(answer[0])
else:
    print("-1")
