def solution(participant, completion):
    answer = ''
    dicp = {}
    for i in participant:
        if dicp.get(i):
            dicp[i] = dicp[i] + 1
        else:
            dicp[i] = 1
    dicc = {}
    for i in completion:
        if dicc.get(i):
            dicc[i] = dicc[i] + 1
        else:
            dicc[i] = 1
    for key,value in dicp.items():
        if dicc.get(key):
            if not dicc[key] == value:
                answer = key
        else:
            answer = key
    return answer