#import random
def solution(before, after):
    answer = 0
    dic = {}
    for i in before:
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 2
    for i in after:
        if dic.get(i):
            dic[i] -= 1
        else:
            return 0
    for i in dic:
        if dic[i] != 1:
            return 0
        
    return 1
    #answer = random.randrange(0,2)
