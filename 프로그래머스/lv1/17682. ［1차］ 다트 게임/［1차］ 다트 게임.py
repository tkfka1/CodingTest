import re

def solution(dartResult):

    l1 = list(map(int, re.findall(r'\d+', dartResult)))
    l2 = re.findall(r'\D+', dartResult)

    for i in range(3):

        if l2[i][0] == "D":
            l1[i] = l1[i]*l1[i]
        elif l2[i][0] == "T":
            l1[i] = l1[i]*l1[i]*l1[i]
        
        if len(l2[i]) == 2:
            if l2[i][1] == "*":
                if i != 0:
                    l1[i-1] = l1[i-1] * 2
                l1[i] = l1[i] * 2
            else:
                l1[i] = l1[i] * -1
    
    return sum(l1)