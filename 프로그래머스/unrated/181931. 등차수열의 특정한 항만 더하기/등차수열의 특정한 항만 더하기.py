def solution(a, d, included):
    answer = 0
    li = [a]
    if included[0]:
        answer += a
    for i in range(1,len(included)):
        li.append(li[-1]+d)
        if included[i]:
            answer += li[-1]

    return answer