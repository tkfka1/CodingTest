def solution(today, terms, privacies):
    answer = []
    
    def date(ymd):
        temp = 0
        for i,x in enumerate(map(int,(ymd).split("."))):
            if i == 0:
                temp+= x*12*28
            elif i == 1:
                temp+= x*28
            else:
                temp+= x
        return temp
    
    today = date(today)
    dic = {}
    for i in terms:
        i = i.split()
        dic[i[0]] = today-(int(i[1])*28)
        
    for i,x in enumerate(privacies):
        x = x.split()
        if dic[x[1]] >= date(x[0]):
            answer.append(i+1)

    return answer