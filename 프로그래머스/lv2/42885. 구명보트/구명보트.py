def solution(people, limit):
    answer = 0
    dic = {}
    for i in people:
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 1
    # print(dic)
    people = sorted(people, reverse=True)
    # print(people)
    for i in people:
        # print(i)
        if dic.get(i):
            if dic[i] != 0:
                dic[i] -= 1
                answer += 1
                if limit - i >= 40:
                    for ii in range(limit - i, 39, -1):
                        if dic.get(ii):
                            if dic[ii] != 0:
                                dic[ii] -= 1
                                break

    return answer