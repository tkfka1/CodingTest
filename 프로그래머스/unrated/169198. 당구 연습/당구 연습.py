def solution(m, n, startX, startY, balls):
    
    answer = []
    
    before = (startX,startY)
    
    for i in balls:
        
        ## 중간값
        temp = [(i[0]+before[0])/2,(i[1]+before[1])/2]
        ## 각 벽면과의 거리
        right = m-temp[0]
        left = temp[0]
        up = n-temp[1]
        down = temp[1]
        
        ## 같은 y축일때
        if before[0] == i[0]:
            ## 시작공이 더 위에있다면 아래로 못감
            if before[1] > i[1]:
                down = 1000
            else:
                up = 1000
        ## 같은 x축일때
        elif before[1] == i[1]: 
            ## 시작공이 더 오른쪽이라면 왼쪽으로 못감
            if before[0] > i[0]:
                left = 1000
            else:
                right = 1000
            
        templi = [right,left,up,down]
        
        ## 벽에서 제일 가까운것 찾기
        mintemp = min(templi)

        loc = templi.index(mintemp)
        res = []
        ## 오 왼 위 아래 0,1,2,3
        for k,v in enumerate(templi):
            if not v == 1000:
                loc = k
                if loc == 0:
                    res.append((2*m-before[0]-i[0])**2 + (before[1]-i[1])**2)
                elif loc == 1:
                    res.append((before[0]+i[0])**2 + (before[1]-i[1])**2)
                elif loc == 2:
                    res.append((before[0]-i[0])**2 + (2*n-before[1]-i[1])**2)
                elif loc == 3:
                    res.append((before[0]-i[0])**2 + (before[1]+i[1])**2)
                



        
        answer.append(min(res))
    
    return answer