# def solution(s, skip, index):
#     answer = ''
    
#     alpa = [chr(i) for i in range(97,123)]
    
#     for i in skip:
#         alpa.remove(i)
    
#     for i in s:
#         x = alpa.index(i)+index
#         x = x%len(alpa)
#         answer += alpa[x]
    
#     return answer

def solution(s, skip, index):
    alpa = [chr(i) for i in range(97,123)]
    alpa = [char for char in alpa if char not in skip]
    return ''.join([alpa[(alpa.index(char) + index) % len(alpa)] for char in s])