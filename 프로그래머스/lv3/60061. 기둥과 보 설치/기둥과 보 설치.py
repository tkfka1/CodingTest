def solution(n, build_frame):
    answer = []
    
    ##보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
    ## 설치된것
    dic_install = {}
    
    ## 기둥이 설치 가능한지
    def install_pillar(x,y):
        if 0 <= x <= n:
            if 0 <= y <= n-1:
                ## 맨 바닥이거나 기둥의 위, 보의 양끝위에
                if y == 0:
                    return True
                if dic_install.get((x,y-1,0)):
                    return True
                if dic_install.get((x-1,y,1)):
                    return True
                if dic_install.get((x,y,1)):
                    return True
        return False
        
    
    ## 기둥 해체 가능한지
    def delete_pillar(x,y):
        ## 내위에 뭐있냐 일단 지워놓고
        del dic_install[(x,y,0)]
        ## 기둥있다면
        if dic_install.get((x,y+1,0)):
            if not install_pillar(x,y+1):
                dic_install[(x,y,0)] = 1
                return
        ## 내위 보 있다면
        if dic_install.get((x,y+1,1)):
            if not install_bo(x,y+1):
                dic_install[(x,y,0)] = 1
                return
        if dic_install.get((x-1,y+1,1)):
            if not install_bo(x-1,y+1):
                dic_install[(x,y,0)] = 1
                return 
        
            
            
    ## 보가 설치 가능한지
    ## 양쪽 끝중 한곳에 기둥이 있거나 양쪽모두에 보가 있다면 
    def install_bo(x,y):
        if 0 <= x <= n-1:
            if 0 <= y <= n:
                ## 기둥이 있다면
                if dic_install.get((x,y-1,0)):
                    return True
                if dic_install.get((x+1,y-1,0)):
                    return True
                ## 보가 양쪽에 있다면
                if dic_install.get((x-1,y,1)) and dic_install.get((x+1,y,1)):
                    return True
        return False
    
    ## 보 해체 가능한지
    def delete_bo(x,y):
        ## 내위에 뭐있냐 일단 지워놓고 있나보고 못만들면 다시 설치 후 리턴
        del dic_install[(x,y,1)]
        ## 왼쪽 보 
        if dic_install.get((x-1,y,1)):
            if not install_bo(x-1,y):
                dic_install[(x,y,1)] = 1
                return

        ## 내자리 기둥
        if dic_install.get((x,y,0)):
            if not install_pillar(x,y):
                dic_install[(x,y,1)] = 1
                return

        ## 오른 기둥
        if dic_install.get((x+1,y,0)):
            if not install_pillar(x+1,y):
                dic_install[(x,y,1)] = 1
                return

        ## 오른 보
        if dic_install.get((x+1,y,1)):
            if not install_bo(x+1,y):
                dic_install[(x,y,1)] = 1
                return

    for x,y,a,b in build_frame:
        ## 기둥
        if a == 0:
            ## 설치인가
            if b == 1:
                ## 기둥 설치 조건
                if install_pillar(x,y):
                    dic_install[(x,y,0)] = 1
            
            ## 해체라면
            else:
                if dic_install.get((x,y,0)):
                    ## 기둥 해체 조건
                    delete_pillar(x,y)
                        
        ## 보
        else:
            ## 설치인가
            if b == 1:
                ## 보 설치 조건
                if install_bo(x,y):
                    dic_install[(x,y,1)] = 1
            ## 해체인가
            else:
                if dic_install.get((x,y,1)):
                    ## 보 해체 조건
                    delete_bo(x,y)
                
                         
    for a,b,c in sorted(dic_install):
        answer.append([a,b,c])

    return answer