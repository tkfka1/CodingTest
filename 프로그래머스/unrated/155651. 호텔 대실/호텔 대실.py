def solution(book_time):
    answer = 0
    
    ## 정보 딕셔너리에 정리
    dic = {}
    for i in book_time:
        temp = i[0].split(":")
        temp1 = i[1].split(":")
        
        time = int(temp[0])*60 + int(temp[1])
        
        ## 퇴실시 10분청소 추가
        time1 = int(temp1[0])*60 + int(temp1[1]) + 10
        
        if dic.get(time):
            dic[time].append(time1)
        
        else:
            dic[time] = [time1]
    
    room = 0
    
    # print(dic)
    
    # 사용중 room
    use_dic = {}
    
    t = 0
    endt = 24*60+1
    while t < endt:
        
        ## 사용중 룸 종료시각된다면 빼기
        if use_dic.get(t):
            # print(t)
            
            room -= use_dic[t]
            
            del use_dic[t]
        
        ## 
        if dic.get(t):
            # print(dic[t])
            
            for i in dic[t]:
                if use_dic.get(i):
                    use_dic[i] += 1
                else:
                    use_dic[i] = 1
                room += 1
                answer = max(answer,room)
        t += 1
        
    return answer