def solution(cap, n, deliveries, pickups):
    answer = 0
    
    
    ## 1. 제일 먼 배달을 해야 하는듯
    ## 2. 배달 후 제일 먼 집 쓰레기가져오기
    ## 반복
    
    ## 제일 먼곳에 배달을 한다. 맨뒤 리스트 0이면 pop 0이아니면 pop 후 cap 만큼 사용
    ## 0아닌곳 제일 뒤쪽 index 숫자 저장 (이동 거리)
    ## cap 보다 크면 cap 만큼 빼고 다시 append 작다면 
    def delever(c):
         ## 제일 멀리 간 이동거리
        distance = 0
        while True:
            ## cap 이 0 이 아닐 때
            if c:
                ## 배달할 곳 있나
                if deliveries:
                    if deliveries[-1] == 0:
                        deliveries.pop()
                    else:
                        ## 간곳중에 제일 멀리간거
                        distance = max(len(deliveries),distance)
                        temp = deliveries.pop()
                        if temp > c:
                            temp -= c
                            deliveries.append(temp)
                            return distance
                        else:
                            c -= temp
                else:
                    return distance
                
            ## cap 이 0 (허용치 전부배달)
            else:
                return distance
    
    ### 배달을 하고 현재 집에서 수거를 하러 간다
    ## 현재 거리보다 수거가 더 멀리있을 때
    ## 현재 거리와 수거 길이가 같거나 더 작을 때
    
    def collect(c):
        distance = 0
        ## 수거 할 수 있는 개수 c
        
        while True:
            ## cap 이 0 이 아닐 때
            if c:
                ## 수거할 곳 있나
                if pickups:
                    if pickups[-1] == 0:
                        pickups.pop()
                    else:
                        ## 수거하는곳 제일 멀리간거
                        distance = max(len(pickups),distance)
                        temp = pickups.pop()
                        if temp > c:
                            temp -= c
                            pickups.append(temp)
                            return distance
                        else:
                            c -= temp
                else:
                    return distance
                
            ## cap 이 0 (허용치 전부수거)
            else:
                return distance
            
            
    while True:
        
        ## 배달할 곳 있는가
        if deliveries:
            ## 배달
            temp_delever = delever(cap)
            ## 수거 할 곳 있는가
            temp_collect = 0
            if pickups:
                ## 수거
                temp_collect = collect(cap)
            
            ## 배달, 수거 중 가장 멀리 간 곳 찾기
            temp_distance = max(temp_delever,temp_collect)
            answer += temp_distance*2
            
        else:
            ## 배달은 다 했지만 수거 할 곳 있는가
            if pickups:
                ## 수거
                temp_collect = collect(cap)
                answer += temp_collect*2
            else:
                break
    
    
    
    return answer