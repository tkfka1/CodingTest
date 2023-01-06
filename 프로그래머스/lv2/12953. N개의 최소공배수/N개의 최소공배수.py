import math
def solution(arr):

    def GCD(a, b):
        if(a % b == 0):
            return b
        return GCD(b, a % b)

    def LCM(a, b):
        return a * b / GCD(a, b)
    
    answer = 1
    for i in arr:
        answer = LCM(answer,i)

    return answer