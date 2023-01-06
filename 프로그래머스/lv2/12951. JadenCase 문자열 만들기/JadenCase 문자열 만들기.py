# def solution(s):
#     answer = ''
#     stack = True
#     for i in s:
#         if stack:
#             answer += i.upper()
#             stack = False
#         else:
#             answer += i.lower()
#         if i == " ":
#             stack = True

#     return answer

def solution(s):
    return s[0].upper()+"".join(list(map(lambda a : s[a+1].upper() if s[a] == " " else s[a+1].lower(), range(len(s)-1))))