import math

def solution(arr):
    x = math.log2(len(arr))
    if x == int(x):
        return arr
    else:
        for i in range(len(arr),2**(int(x)+1)):
            arr.append(0)
        return arr