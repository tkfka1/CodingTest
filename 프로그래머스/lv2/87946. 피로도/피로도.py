from itertools import permutations

def solution(k, dungeons):
    answer = -1

    num = []
    for i in range(len(dungeons)):
        num.append(i)
    
    # 완전탐색해버리기
    li = list(permutations(num,len(dungeons)))
    # print(li)
    for i in li:
        tempk = k
        do = 0
        for ii in i:
            if dungeons[ii][0] <= tempk:
                tempk -= dungeons[ii][1]
                do += 1
            else:
                break
        if answer <= do:
            answer = do

    return answer