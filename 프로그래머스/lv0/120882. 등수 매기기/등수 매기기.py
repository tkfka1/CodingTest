def solution(score):
    answer = []
    li = []
    dic = {}
    for index,value in enumerate(score):
        tempsum = sum(value)/2
        li.append(tempsum)

    li = sorted(li,reverse = True)

    for i in score:
        tempsum = sum(i)/2
        answer.append(li.index(tempsum)+1)

    return answer