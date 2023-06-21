from collections import deque

def solution(plans):
    answer = []
    ## 딕셔너리[시작시간(분)] = 이름,길이
    dic_time = {}
    
    dic_name = {}
    
    for i in plans:
        temp = i[1].split(":")
        time = int(temp[0])*60+int(temp[1])
        dic_time[time] = (i[0],int(i[2]))
        dic_name[i[0]] = int(i[2])
    
    stack = []
    
    for i in range(60*24+1):
        if stack:
            dic_name[stack[-1]] -= 1
            if dic_name[stack[-1]] == 0:
                answer.append(stack.pop())
        if dic_time.get(i):
            stack.append(dic_time[i][0])
    while True:
        if stack:
            answer.append(stack.pop())
        else:
            break

    return answer