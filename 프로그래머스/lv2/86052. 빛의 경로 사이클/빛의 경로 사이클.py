def solution(grid):
    ## 정답 리스트
    answer = []
    
    ## x,y 길이
    len_x = len(grid[0])
    len_y = len(grid)
    
    ## 여태 모든 경로 수집 전체사이클 딕셔너리
    cycle_dic = {}
    
    ## 방향 처리 오른쪽부터시계(우회전) 오 아래 왼 위 1 2 3 4
    ## x,y,direction
    def go(loc):
        temp = grid[loc[1]][loc[0]]
        direction = loc[2]
        
        ## 좌회전
        if temp == "L":
            direction -= 1
            if direction == 0:
                direction = 4
                
        ## 우회전
        elif temp == "R":
            direction += 1
            if direction == 5:
                direction = 1

        ## 오른
        if direction == 1:
            y = loc[1]
            x = loc[0] + 1
            if x == len_x:
                x = 0
                
        ## 아래
        elif direction == 2:
            y = loc[1] + 1
            x = loc[0]
            if y == len_y:
                y = 0
            
        ## 왼    
        elif direction == 3:
            y = loc[1] 
            x = loc[0] - 1
            if x < 0:
                x = len_x-1
        
        ## 위
        elif direction == 4:
            y = loc[1] - 1
            x = loc[0]
            if y < 0:
                y = len_y-1
        
        return (x,y,direction)

    

    
    ## 경로에 따른 한 사이클 찾기 함수
    def do(loc):
        
        ## 만약 전체 사이클에 현재 사이클이 없다면
        if not cycle_dic.get(loc):
            ## 임시 사이클 딕셔너리
            temp_cycle_dic = {}

            while True:
                if temp_cycle_dic.get(loc):
                    ## 중복이면 정답에 사이클 길이 넣기
                    answer.append(len(temp_cycle_dic))
                    break
                else:
                    ## 최초면 임시사이클딕셔너리와 전체사이클 딕셔너리 둘다 넣기
                    temp_cycle_dic[loc] = 1
                    cycle_dic[loc] = 1

                ## 위에 go 함수
                loc = go(loc)

            # print(temp_cycle_dic)
    
    
    
#     ## 처음 시작 출발방향 네방향이 있음 오 아래 왼 위 1 2 3 4
#     for direction in range(1,5):
#         ## 오른쪽방향
#         if direction == 1:
#             x = 0
#             for y in range(len_y):
#                 loc = (x,y,direction)
#                 ## 전체 경로 찾기
#                 do(loc)
        
#         ## 아래방향
#         elif direction == 2:
#             y = len_y - 1
#             for x in range(len_x):
#                 loc = (x,y,direction)
#                 ## 전체 경로 찾기
#                 do(loc)
            
#         ## 왼쪽방향
#         elif direction == 3:
#             x = len_x - 1
#             for y in range(len_y):
#                 loc = (x,y,direction)
#                 ## 전체 경로 찾기
#                 do(loc)
            
#         ## 위방향
#         elif direction == 4:
#             y = 0
#             for x in range(len_x):
#                 loc = (x,y,direction)
#                 ## 전체 경로 찾기
#                 do(loc)
# ###### 문제 이해 잘못함 각 모든 격자에서의 4방향을 구해야 함 ####
    
    ## 모든 방향 모든 격자 [y][x]
    for direction in range(1,5):
        for y in range(len_y):
            for x in range(len_x):
                loc = (x,y,direction)
                do(loc)

    return sorted(answer)