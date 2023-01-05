def solution(lottos, win_nums):
    answer = [0,0]
    zero = lottos.count(0)
    res = lottos + win_nums
    all = set(res)
    try:
        all.remove(0)
    except:
        pass
    t = len(all) + zero

    if t < 11:
        answer[1] = t - 5
    else:
        answer[1] = 6

    if zero == 0:
        answer[0] = answer[1]
    elif zero == 6:
        answer[0] = 1
    else:
        answer[0] = answer[1]-zero

    return answer