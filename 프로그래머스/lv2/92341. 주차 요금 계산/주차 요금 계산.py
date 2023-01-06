def solution(fees, records):
    answer = []
    dic = {}
    for i in records:
        temptime = 0
        temp = i.split()
        temptime += int(temp[0][0]) * 10 * 60
        temptime += int(temp[0][1]) * 60
        temptime += int(temp[0][3:])
        if temp[2][0] == 'I':
            if dic.get(temp[1]) == None:
                dic[temp[1]] = -temptime
            else:
                dic[temp[1]] -= temptime
        else:
            dic[temp[1]] = temptime + dic[temp[1]]
            
    dic = dict(sorted(dic.items()))
    
    for key,value in dic.items():
        if value <= 0:
            value = value + 1200 + 59 + 180

        if value <= fees[0]:
            answer.append(fees[1])
        else:
            tex = (value-fees[0]+fees[2]-1)//fees[2]
            tex = tex * fees[3] + fees[1]
            answer.append(tex)

    return answer