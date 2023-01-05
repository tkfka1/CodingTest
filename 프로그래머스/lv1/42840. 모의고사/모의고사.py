def solution(answers):
    answer = []
    ans = [0,0,0]
    s2 = 1
    s3 = 1
    dic = {1:1,2:2,3:3}
    for i in answers:
    #for i in range(100):
        #print(dic[1],dic[2],dic[3])
        for ii in dic:
            if i == dic[ii]:
                ans[ii-1] += 1
            
            if ii == 1:
                dic[1] += 1
                if dic[1] == 6:
                    dic[1] = 1
            elif ii == 2:
                if dic[2] == 2:
                    dic[2] = s2
                    s2 += 1
                    if s2 == 2:
                        s2 += 1
                    elif s2 == 6:
                        s2 = 1
                else:
                    dic[2] = 2
            else:
                if s3 == 2:
                    dic[3] += 1
                    if dic[3] == 6:
                        dic[3] = 3
                    elif dic[3] == 3:
                        dic[3] = 4
                    elif dic[3] == 4:
                        dic[3] = 1
                    s3 = 0
                s3 += 1

    maxans = max(ans)        
    for i in range(3):
        if ans[i] == maxans:
            answer.append(i+1)
    
            
        
    return answer