from heapq import heappop as hpop
from heapq import heappush as hpush
from heapq import heapify as hify

def solution(operations):
    answer = []
    min = []
    max = []
    delist = []
    count = 0
    for i in operations:
        if i[0]== "I":
            #삽입짱
            hpush(min,int(i[2:]))
            hpush(max,-int(i[2:]))
            count += 1
        elif i[0] == "D" and i[2] == "-":
            #최소짱
            if count != 0:
                count -= 1
                hpop(min)

        else:
            #최대짱
            if count != 0:
                count -= 1
                ma = hpop(max)
                delist.append(-ma)

    if count == 0:
        return [0,0]
    templist = list(min)

    for i in delist:
        templist.remove(i)

    ans = sorted(templist)

    return [ans[-1],ans[0]]