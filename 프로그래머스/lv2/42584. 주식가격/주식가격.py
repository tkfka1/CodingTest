def solution(prices):
    answer = []
    plen = len(prices)

    for i in range(plen):
        tempcount = -1
        for x in range(i,plen):
            tempcount += 1
            if prices[i] > prices[x]:
                break
        answer.append(tempcount)


    return answer