def solution(record):
    answer = []
    anstemp = []
    dic = {}
    for i in record:
        x = i[0]
        temp = i.split()
        if x == "E":
            dic[temp[1]] = temp[2]
            anstemp.append([temp[1],1])
        elif x == "C":
            dic[temp[1]] = temp[2]
        else:
            anstemp.append([temp[1], 0])


    for i in anstemp:
        res = dic[i[0]]
        if i[1]:
            answer.append(f"{res}님이 들어왔습니다.")
        else:
            answer.append(f"{res}님이 나갔습니다.")

    return answer