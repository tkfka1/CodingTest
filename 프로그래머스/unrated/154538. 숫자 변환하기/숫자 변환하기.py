def solution(x, y, n):
    
    if x == y:
        return 0
    
    answer = 0
    onN = True
    on2 = True
    on3 = True
    li = [x]
    
    while True:
        temp = []
        answer += 1
        if onN:
            templi = []
            for i in li:
                tempN = i+n
                if tempN < y:
                    templi.append(tempN)
                elif tempN == y:
                    return answer
            else:
                if not templi:
                    onN = False
                else:
                    temp += templi
        
        if on2:
            templi = []
            for i in li:
                temp2 = i*2
                if temp2 < y:
                    templi.append(temp2)
                elif temp2 == y:
                    return answer
            else:
                if not templi:
                    on2 = False
                else:
                    temp += templi
        
        if on3:
            templi = []
            for i in li:
                temp3 = i*3
                if temp3 < y:
                    templi.append(temp3)
                elif temp3 == y:
                    return answer
            else:
                if not templi:
                    on3 = False
                else:
                    temp += templi
                    
        if not temp:
            return -1
        else:
            li = set(temp)
        
    return answer