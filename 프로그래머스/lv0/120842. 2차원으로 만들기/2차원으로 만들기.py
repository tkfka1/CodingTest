def solution(num_list, n):

    answer = [[0]* n for _ in range(len(num_list)//n)]
    staty = 0
    statx = 0
    for i in num_list:
        answer[staty][statx] = i
        statx += 1
        if statx == n:
            staty += 1
            statx = 0

    return answer