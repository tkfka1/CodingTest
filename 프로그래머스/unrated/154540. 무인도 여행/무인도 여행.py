import sys

def solution(maps):
    answer = []
    stack_dic = {}
    sys.setrecursionlimit(10000)
    
    def find(lo):
        
        s = 0
        y = lo[0]
        x = lo[1]
        
        ## 오른
        r_y = y
        r_x = x+1
        
        ## 왼
        l_y = y
        l_x = x-1
        
        ## 위
        u_y = y-1
        u_x = x
        
        ## 아래
        d_y = y+1
        d_x = x
        
        if 0 <= r_x < len(maps[0]):
            if maps[r_y][r_x] != "X":
                if not stack_dic.get((r_y,r_x)):
                    s += int(maps[r_y][r_x])
                    stack_dic[(r_y,r_x)] = 1
                    s += find((r_y,r_x))
                    
        if 0 <= l_x:
            if maps[l_y][l_x] != "X":
                if not stack_dic.get((l_y,l_x)):
                    s += int(maps[l_y][l_x])
                    stack_dic[(l_y,l_x)] = 1
                    s += find((l_y,l_x))
                    
        if 0 <= u_y:
            if maps[u_y][u_x] != "X":
                if not stack_dic.get((u_y,u_x)):
                    s += int(maps[u_y][u_x])
                    stack_dic[(u_y,u_x)] = 1
                    s += find((u_y,u_x))
        
        if 0 <= d_y < len(maps):
            if maps[d_y][d_x] != "X":
                if not stack_dic.get((d_y,d_x)):
                    s += int(maps[d_y][d_x])
                    stack_dic[(d_y,d_x)] = 1
                    s += find((d_y,d_x))
            
        return s
        
    
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] != "X":
                if not stack_dic.get((y,x)):
                    temp_answer = int(maps[y][x])
                    stack_dic[(y,x)] = 1
                    temp_answer += find((y,x))
                    answer.append(temp_answer)
                    
    
    
    if answer:
        return sorted(answer)
    else:
        return [-1]