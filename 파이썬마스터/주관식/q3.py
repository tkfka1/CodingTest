'''
【문제 3】 두개의 주어진 조건에서 최대값과 최소값을 구하여라.
1. 9.96, 1.27, 5.07, 6.45, 8.38, 9.29, 4.93, 7.73, 3.71, 0.93 중에서 최대값과 최소값을 구하여라
2. Alotofthingsoccureachday 중에서 최대값과 최소값을 구하여라.
'''

li = [9.96, 1.27, 5.07, 6.45, 8.38, 9.29, 4.93, 7.73, 3.71, 0.93]

st = "Alotofthingsoccureachday"

def maxmin(x):
    return max(x), min(x)

print(maxmin(li))
print(maxmin(st))
