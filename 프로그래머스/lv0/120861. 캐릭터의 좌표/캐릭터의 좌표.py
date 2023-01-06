def solution(keyinput, board):
    over = [board[0]//2,board[1]//2]
    answer = [0,0]
    def inputkey(k,answer):
        a,b = answer[1], answer[0]
        
        if k == "u":
            a = answer[1] + 1
        elif k == "d":
            a = answer[1] - 1
        elif k == "l":
            b = answer[0] -1
        else:
            b = answer[0] + 1
        if abs(a) <= over[1]:
            if abs(b) <= over[0]:
                return [b,a]
        
        return answer
        
                
    for i in keyinput:
        answer = inputkey(i[0],answer)
    
    return answer