def solution(progresses, speeds):
    answer = []
    ans_list = []
    for i in range(len(speeds)):
        res = 100 - progresses[i]
        if res % speeds[i] == 0:
            res = (res) // speeds[i]
        else:
            res = (res) // speeds[i] + 1
        ans_list.append(res)
    print(ans_list)
    n = 0
    count = 0
    while True:
        res = 0
        if ans_list[n] == count:
            for i in ans_list[n:]:
                if i <= count:
                    res += 1
                else:
                    break
            answer.append(res)
            n += res
        count += 1
        if n == len(speeds):
            break
    return answer