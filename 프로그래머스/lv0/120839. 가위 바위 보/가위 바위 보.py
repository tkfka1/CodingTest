def solution(rsp):
    answer = ''
    def win(x):
        if x == "2":
            return "0"
        elif x == "0":
            return "5"
        else:
            return "2"
        
    for i in rsp:
        answer+= win(i)
        
    return answer