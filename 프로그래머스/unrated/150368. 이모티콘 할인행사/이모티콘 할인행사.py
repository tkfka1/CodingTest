def solution(users, emoticons):
    answer = [0,0]
    
    users = sorted(users)
    
    emoticons = sorted(emoticons)
    
    user_dic = {}
    user_dic[10] = []
    user_dic[20] = []
    user_dic[30] = []
    user_dic[40] = []
    
    ## 할인율 정리
    for i in users:
        if i[0] > 30:
            user_dic[40].append(i[1])
        elif i[0] > 20:
            user_dic[30].append(i[1])
        elif i[0] > 10:
            user_dic[20].append(i[1])
        else:
            user_dic[10].append(i[1])
    
    prices_dic = {}
    
    for i in range(10,41,10):
        discount = i
        for e in emoticons:
            prices_dic[discount] = prices_dic.get(discount,[]) + [e-((e//100)*discount)]
    
    
    temp = [[prices_dic[10][0],0,0,0],[prices_dic[20][0],prices_dic[20][0],0,0],[prices_dic[30][0],prices_dic[30][0],prices_dic[30][0],0],[prices_dic[40][0],prices_dic[40][0],prices_dic[40][0],prices_dic[40][0]]]
    

                    
    
    def make(l,index):
        li = []
        for r in range(10,41,10):
            if r == 10:
                li.append([t[0]+prices_dic[r][index],t[1],t[2],t[3]])
            elif r == 20:
                li.append([t[0]+prices_dic[r][index],t[1]+prices_dic[r][index],t[2],t[3]])
            elif r == 30:
                li.append([t[0]+prices_dic[r][index],t[1]+prices_dic[r][index],t[2]+prices_dic[r][index],t[3]])
            else:
                li.append([t[0]+prices_dic[r][index],t[1]+prices_dic[r][index],t[2]+prices_dic[r][index],t[3]+prices_dic[r][index]])
        return li
    
    
    
        
    if len(emoticons) > 1:
        for i in range(1,len(emoticons)):
            li = []
            for t in temp:
                li += make(t,i)
            temp = li
    
    for i in temp:
        plus = 0
        earn = 0
        for x in range(4):
            for u in user_dic[(x+1)*10]:
                if u <= i[x]:
                    plus += 1
                else:
                    earn += i[x]
        if answer[0] < plus:
            answer = [plus,earn]
        elif answer[0] == plus:
            if answer[1] < earn:
                answer[1] = earn
    
    return answer