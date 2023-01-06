## 정규식 사용 시간초과
# def solution(a):
#     import re
#     for i in range(len(a)//2):
#         before = len(a)
#         for i in range(97,123):
#             alpabet = chr(i)
#             a = re.sub(alpabet+"{2}",'',a)
#         if before == len(a):
#             return 0
#         elif not a:
#             return 1
#     return 0

## deque 사용
from collections import deque

def solution(s):
    temp = deque(s[0])
    for i in range(1,len(s)):
        stack = ""
        if temp:
            stack = temp.pop()
        if stack != s[i]:
            if stack:
                temp.append(stack)
            temp.append(s[i])

    if temp:
        return 0
    else:
        return 1