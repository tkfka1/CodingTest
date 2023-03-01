def solution(b):
    o_val = 0
    x_val = 0
    
    for i in b:
        for ii in i:
            if ii == "O":
                o_val += 1
            elif ii == "X":
                x_val += 1
    
    if o_val-x_val > 1 or o_val-x_val < 0:
        return 0
    
    def check_win(ox):

        if b[0][0] == ox:
            if b[0][1] == ox:
                if b[0][2] == ox:
                    return 1
            if b[1][0] == ox:
                if b[2][0] == ox:
                    return 1
            if b[1][1] == ox:
                if b[2][2] == ox:
                    return 1
                
        if b[0][1] == ox:
            if b[1][1] == ox:
                if b[2][1] == ox:
                    return 1
                
        if b[0][2] == ox:
            if b[1][2] == ox:
                if b[2][2] == ox:
                    return 1
            if b[1][1] == ox:
                if b[2][0] == ox:
                    return 1
                
        if b[1][0] == ox:
            if b[1][1] == ox:
                if b[1][2] == ox:
                    return 1
                
        if b[2][0] == ox:
            if b[2][1] == ox:
                if b[2][2] == ox:
                    return 1
                
        return 0

    
    o_ans = 0
    x_ans = 0
    if o_val >= 3:
        o_ans = check_win("O")
    if x_val >= 3:
        x_ans = check_win("X")
    
    if o_ans == 0:
        if x_ans == 0:
            return 1
        else:
            if o_val == x_val:
                return 1
            else:
                return 0

    else:
        if x_ans == 0:
            if o_val == x_val:
                return 0
            else:
                return 1
        else:
            return 0