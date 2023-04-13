def solution(park, routes):
    loc = (0,0)
    y = len(park)
    x = len(park[0])
    newPark = []
    
    for yy in range(y):
        templi = []
        for xx in range(x):
            temp = park[yy][xx]
            if temp == "S":
                loc = (yy,xx)
                templi.append(0)
            elif temp == "X":
                templi.append(1)
            else:
                templi.append(0)
        newPark.append(templi)

    for r in routes:
        temploc = loc
        arrow = r[0]
        lenth = int(r[2])
        if arrow == "N":
            if 0 <= (temploc[0] - lenth):
                for i in range(lenth):
                    if newPark[temploc[0]-1][temploc[1]] == 0:
                        temploc = (temploc[0]-1,temploc[1])
                    else:
                        break
                else:
                    loc = temploc
                    
        if arrow == "S":
            if y > (temploc[0] + lenth):
                for i in range(lenth):
                    if newPark[temploc[0]+1][temploc[1]] == 0:
                        temploc = (temploc[0]+1,temploc[1])
                    else:
                        break
                else:
                    loc = temploc
                    
        if arrow == "W":
            if 0 <= (temploc[1] - lenth):
                for i in range(lenth):
                    if newPark[temploc[0]][temploc[1]-1] == 0:
                        temploc = (temploc[0],temploc[1]-1)
                    else:
                        break
                else:
                    loc = temploc
                    
        if arrow == "E":
            if x > (temploc[1] + lenth):
                for i in range(lenth):
                    if newPark[temploc[0]][temploc[1]+1] == 0:
                        temploc = (temploc[0],temploc[1]+1)
                    else:
                        break
                else:
                    loc = temploc

    
    return [loc[0],loc[1]]