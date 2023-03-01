def solution(maps):
    answer = 0
    # s - l
    # l - s
    sle = {}
    dic = {}
    
    
    for i in range(len(maps)):
        for ii in range(len(maps[0])):
            if not maps[i][ii] == "X" and not maps[i][ii] == "O":
                sle[maps[i][ii]] = (i,ii)
    

    
    def findway(yx,n):
        y = yx[0]
        x = yx[1]
        temp = []
        if not y+1 == len(maps):
            if not maps[y+1][x] == "X":
                if not dic.get((y+1,x)):
                    dic[(y+1,x)] = n
                    temp.append((y+1,x))
        if not x+1 == len(maps[0]):
            if not maps[y][x+1] == "X":
                if not dic.get((y,x+1)):
                    dic[(y,x+1)] = n
                    temp.append((y,x+1))
        if not y == 0:
            if not maps[y-1][x] == "X":
                if not dic.get((y-1,x)):
                    dic[(y-1,x)] = n
                    temp.append((y-1,x))
        if not x == 0:
            if not maps[y][x-1] == "X":
                if not dic.get((y,x-1)):
                    dic[(y,x-1)] = n
                    temp.append((y,x-1))
        return temp
    
    dic[sle["S"]] = 1
    temp = [sle["S"]]
    count = 0
    while True:
        temp_new = []
        count += 1
        for i in temp:
            temp_new += findway(i,count)
        temp = temp_new
        
        if dic.get(sle["L"]):
            answer = dic[sle["L"]]
            break
        if not temp:
            return -1

    dic = {}
    
    dic[sle["L"]] = 1
    temp = [sle["L"]]
    count = 0
    while True:
        temp_new = []
        count += 1
        for i in temp:
            temp_new += findway(i,count)
        temp = temp_new
        
        if dic.get(sle["E"]):
            answer += dic[sle["E"]]
            break
        if not temp:
            return -1
        
    return answer