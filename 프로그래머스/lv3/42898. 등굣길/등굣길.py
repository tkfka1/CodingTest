def solution(m, n, puddles):
    answer = 0
    
    li = [[0 for x in range(m)] for y in range(n)]
    
    for i in range(n):
        li[i][0] = 1
    for i in range(m):
        li[0][i] = 1
    
    dic = {}
    for i in puddles:
        li[i[1]-1][i[0]-1] = 0
        dic[(i[1]-1,i[0]-1)] = 1
        
    for i in range(n):
        if li[i][0] == 0:
            for ii in range(i,n):
                li[ii][0] = 0
            break
    for i in range(m):
        if li[0][i] == 0:
            for ii in range(i,m):
                li[0][ii] = 0
            break
    
        
    for y in range(1,n):
        for x in range(1,m):
            if not dic.get((y,x)):
                li[y][x] = li[y-1][x] + li[y][x-1]

    #print(li)
    
    return li[n-1][m-1]%1000000007