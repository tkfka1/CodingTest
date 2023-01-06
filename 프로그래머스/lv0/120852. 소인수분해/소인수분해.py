def solution(n):
    answer = []
    li = []
    for i in range(2,n):
        if not n%i:
            li.append(i)
    li.append(n)
    for i in li:
        for ii in range(2,i):
            # 나누어떨어지면
            if i % ii == 0:
                break
        else:
            answer.append(i)
    return answer