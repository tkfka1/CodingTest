def solution(brown, yellow):
    answer = []
    sumWH = brown//2+2
    tempY = [1]
    tempA = [1]
    # 옐로우 약수 배열
    for i in range(2,yellow//2+1,1):
        if yellow % i == 0:
            tempY.append(i)
    tempY.append(yellow)
    
    # 옐로우 + 브라운 약수 배열
    for i in range(2,(yellow+brown)//2+1):
        if (yellow+brown) % i == 0:
            tempA.append(i)
    tempA.append(yellow+brown)
    
    templist = []
    for i in tempA:
        if i > 2:
            for ii in tempA:
                if ii > 2:
                    if i>=ii and i+ii == sumWH:
                        templist.append([i,ii])
                
    # print(tempY)
    # print(tempA)
    # print(templist)

    
    
    return templist[0]