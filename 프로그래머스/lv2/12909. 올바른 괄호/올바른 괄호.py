def solution(s):
    answer = True
    count1 = 0
    count2 = 0
    for i in s:
        if i == "(":
            count1 += 1
        else:
            count2 += 1
            
        if count2 > count1:
            return False
    if not count2 == count1:
        return False
    return True