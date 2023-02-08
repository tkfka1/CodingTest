# from itertools import permutations

# def solution(t, p):
#     answer = 0
    
#     tlist = []
#     for i in range(len(t)):
#         temp = []
#         for ii in range(len(p)):
#             temp.append(t[i+ii])
#         tlist.append(temp)
#         if i == len(t)-len(p):
#             break

#     for i in tlist:
#         if int(p) >= int(''.join(i)):
#             answer += 1
#     return answer

def solution(t, p):
    return sum([1 for i in range(len(t) - len(p) + 1) if int(p) >= int(t[i:i+len(p)])])
