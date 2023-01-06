def solution(places):
    answer = []
    test = places[1]

    def check(locP,locX):
        for i in locP[:-1]:
            # if 맨해튼1
            y, x = i[0], i[1]
            if [y+1,x] in locP:
                return 0
            if [y,x+1] in locP:
                return 0
            # if 맨해튼2
            if y < 4:
                if [y+2,x] in locP:
                    if not [y+1, x] in locX:
                        return 0

            if 5 > y and x < 5:
                if [y+1,x+1] in locP:
                    if not [y+1, x] in locX:
                        return 0
                    if not [y, x+1] in locX:
                        return 0


            if x < 4:
                if [y,x+2] in locP:
                    if not [y, x+1] in locX:
                        return 0
            if 5 > y and x > 0:
                if [y + 1, x - 1] in locP:
                    if not [y, x - 1] in locX:
                        return 0
                    if not [y + 1, x] in locX:
                        return 0
        else:
            return 1


    for i in places:
        locP = []
        locX = []
        for y in range(5):
            for x in range(5):
                if i[y][x] == "P":
                    locP.append([y,x])
                elif i[y][x] == "X":
                    locX.append([y,x])
        answer.append(check(locP,locX))

    return answer