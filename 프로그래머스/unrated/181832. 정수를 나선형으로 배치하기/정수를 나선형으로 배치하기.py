def solution(n):
    answer = [[0]*n for i in range(n)]
    
    im = (0,-1)
    ro = (0,1)
    rangeY = (0,n-1)
    rangeX = (0,n-1)
    
    
    def change(r):
        if r == (0,1):
            r = (1,0)
        elif r == (1,0):
            r = (0,-1)
        elif r == (0,-1):
            r = (-1,0)
        else:
            r = (0,1)
        return r
    
    
    
    for i in range(1,n*n+1):
        y = im[0] + ro[0]
        x = im[1] + ro[1]
        if 0 <= y <= n-1:
            if 0 <= x <= n-1:
                if answer[y][x] == 0:
                    answer[y][x] = i
                    im = (y,x)
                else:
                    ro = change(ro)
                    y = im[0] + ro[0]
                    x = im[1] + ro[1]
                    answer[y][x] = i
                    im = (y,x)
            else:
                ro = change(ro)
                y = im[0] + ro[0]
                x = im[1] + ro[1]
                answer[y][x] = i
                im = (y,x)
        else:
            ro = change(ro)
            y = im[0] + ro[0]
            x = im[1] + ro[1]
            answer[y][x] = i
            im = (y,x)
    
    
    return answer