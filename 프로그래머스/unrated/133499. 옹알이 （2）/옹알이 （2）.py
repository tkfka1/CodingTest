import re

def solution(babbling):
    answer = 0

    for i in babbling:
        a = i
        a = re.sub("aya", "1", a)
        a = re.sub("ma", "2", a)
        a = re.sub("woo", "3", a)
        a = re.sub("ye", "4", a)

        if a.isdigit():
            pre = ""
            for i in a:
                if pre == i:
                    answer-=1
                    break
                else:
                    pre = i
            answer+=1
        
    return answer