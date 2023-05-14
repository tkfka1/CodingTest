def solution(n, stations, w):
    answer = 0
    
    lange = w+w+1
    
    pre_cover = 0
    
    for i in stations:
        
        temp =  (i - w - 1) - pre_cover
        
        if temp > 0:
            answer += temp // lange
            ## 나누어 떨어지지 않는다면 하나 더 추가
            if not temp % lange == 0:
                answer += 1

        pre_cover = i+w
            
        ## 완료후 mi에 기지국 마지막 설치 범위 넣기

    ## 만약 N이 남았다면
    if pre_cover < n:
        temp = n - pre_cover
        answer += temp // lange
        ## 나누어 떨어지지 않는다면 하나 더 추가
        if not temp % lange == 0:
            answer += 1
        
        

    return answer