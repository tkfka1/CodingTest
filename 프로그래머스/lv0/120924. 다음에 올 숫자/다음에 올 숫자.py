def solution(common):
    answer = 0
    
    if common[1]+(common[1]-common[0]) == common[2]:
        # 등차
        answer = common[-1] + common[1] - common[0]
    else:
        # 등비
        answer = (common[1]//common[0])*common[-1]
    
    return answer