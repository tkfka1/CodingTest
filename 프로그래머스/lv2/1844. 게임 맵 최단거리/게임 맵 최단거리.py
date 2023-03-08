def solution(maps):
    answer = 0
    dic = {}
    end_y = len(maps) -1
    end_x = len(maps[0]) - 1
    
    maps[end_y][end_x] = -1
    
    def go(loc):
        y = loc[0]
        x = loc[1]
        temp = []
        if y == 0:
            if not end_y == 0:
                    temp.append((y+1,x))
            
            if x == 0:
                if not end_x == 0:
                    temp.append((y,x+1))
            elif x == end_x:
                temp.append((y,x-1))
            else:
                temp.append((y,x+1))
                temp.append((y,x-1))
        elif y == end_y:
            if x == 0:
                if not end_x == 0:
                    temp.append((y,x+1))
                temp.append((y-1,x))
            elif x == end_x:
                temp.append((y,x-1))
                temp.append((y-1,x))
            else:
                temp.append((y,x+1))
                temp.append((y,x-1))
                temp.append((y-1,x))    
        else:
            if x == 0:
                if not end_x == 0:
                    temp.append((y,x+1))
                temp.append((y-1,x))
                temp.append((y+1,x))
            elif x == end_x:
                temp.append((y-1,x))
                temp.append((y+1,x))
                temp.append((y,x-1))
            else:
                temp.append((y,x+1))
                temp.append((y,x-1))
                temp.append((y+1,x))
                temp.append((y-1,x))
        return temp
    
    loc = (0,0)
    dic[loc] = 1
    temp = go(loc)
    for i in range(1,len(maps)*len(maps[0])):
        temp2 = []
        if temp:
            for ii in temp:
                if not dic.get(ii):
                    if maps[ii[0]][ii[1]] == 1:
                        dic[ii] = i
                        temp2 += go(ii)
                    elif maps[ii[0]][ii[1]] == -1:
                        return i+1
        else:
            return -1
        temp = temp2