def solution(rows, columns, queries):
    answer = []
    graph = []
    stack = 1
    
    ## 그래프 생성
    for y in range(rows):
        temp = []
        for x in range(columns):
            temp.append(stack)
            stack += 1
        graph.append(temp)
    
    def do(y1,x1,y2,x2):
        x = x1
        y = y1
        pre = graph[y][x]
        min_pre = pre
        # 1 - 윗줄 가로
        for i in range(x1+1,x2+1):
            x = i
            temp = graph[y][x]
            graph[y][x] = pre
            pre = temp
            if pre < min_pre:
                min_pre = pre
        
        ## 2 - 오른 세로
        x = x2
        for i in range(y1+1,y2+1):
            y = i
            temp = graph[y][x]
            graph[y][x] = pre
            pre = temp
            if pre < min_pre:
                min_pre = pre
        
        ## 3 - 아래 가로
        y = y2
        for i in range(x2-1,x1-1,-1):
            x = i
            temp = graph[y][x]
            graph[y][x] = pre
            pre = temp
            if pre < min_pre:
                min_pre = pre
                
        ## 4 - 왼 세로
        x = x1
        for i in range(y2-1,y1-1,-1):
            y = i
            temp = graph[y][x]
            graph[y][x] = pre
            pre = temp
            if pre < min_pre:
                min_pre = pre
                
        return min_pre
    
    for i in queries:
        answer.append(do(i[0]-1,i[1]-1,i[2]-1,i[3]-1))
    
    
    return answer
