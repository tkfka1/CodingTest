def solution(n, s):
    answer = []
    x,y = divmod(s,n)
    print(x,y)

    if n>s:
        return [-1]

    for i in range(n):
        if y != 0:
            y-=1
            answer.append(x+1)
        else:
            answer.append(x)
    answer = sorted(answer)

    return answer