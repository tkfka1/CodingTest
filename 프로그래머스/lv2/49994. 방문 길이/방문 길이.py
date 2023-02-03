def solution(dirs):
    global x
    global y
    x = 0
    y = 0
    dic = {}
    
    def go(arrow):
        global x
        global y
        temp_x = x
        temp_y = y
        
        def gogo():
            global x
            global y
            temp = min(x,temp_x),min(y,temp_y),max(x,temp_x),max(y,temp_y)
            if not dic.get(temp):
                dic[temp] = 1
        
        if arrow == "U":
            if not y == -5:
                y -= 1
                gogo()
        if arrow == "D":
            if not y == 5:
                y += 1
                gogo()
        if arrow == "R":
            if not x == 5:
                x += 1
                gogo()
        if arrow == "L":
            if not x == -5:
                x -= 1
                gogo()
        
    for i in dirs:
        go(i)

    return len(dic)