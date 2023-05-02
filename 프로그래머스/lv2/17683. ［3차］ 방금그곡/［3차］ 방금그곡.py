def solution(m, musicinfos):
    answer = []
    
    ## m 리스트로 변환
    tempm = []
    for i in m:
        if i == "#":
            tempm[-1] += "#"
        else:
            tempm.append(i)        
    
    m = tempm

    
    for i in musicinfos:
        
        ## 나누기
        i=i.split(",")
        ## print(i[3])
        
        ## 몇분 재생
        hour = int(i[1][:2])-int(i[0][:2])
        minute = 60*(hour) + (int(i[1][3:]) - int(i[0][3:]))
        ## print(minute)
        
        
        templi = []
        ## i[3] 음악 리스트 생성 templi
        for ii in i[3]:
            if ii == "#":
                templi[-1] += "#"
            else:
                templi.append(ii)        
        ## print(templi)
        
        
        ## 음악 길이에 따른 리스트 생성
        musicli = []
        stack = 0
        for _ in range(minute):
            musicli.append(templi[stack])
            stack += 1
            if stack == len(templi):
                stack = 0
        # print(musicli)
        
        
        ## 음악 순회하면서 m 포함하는지
        stack = 0
        for ii in musicli:
            ## 음악리스트의 한부분 m0 와 같다면
            if ii == m[stack]:
                ## 다음거 찾기
                stack += 1
            ## 같지 않다면
            else:
                stack = 0
                if ii == m[stack]:
                    stack += 1
            
            if stack == len(m):
                ## 찾는다면 answer에 분, 이름 넣기
                answer.append((minute,i[2]))
                # print("차잣당")
                break

    if answer:
        maxtime = 0
        for i in answer:
            if maxtime <= i[0]:
                maxtime = i[0]
        for i in answer:
            if i[0] == maxtime:
                return i[1]
    else:
        return "(None)"