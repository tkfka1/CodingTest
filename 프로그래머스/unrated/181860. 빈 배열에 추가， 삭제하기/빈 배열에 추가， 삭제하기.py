def solution(arr, flag):
    answer = []
    for k,v in enumerate(flag):
        if v:
            for i in range(arr[k]):
                answer.append(arr[k])
                answer.append(arr[k])
        else:
            for i in range(arr[k]):
                answer.pop()
    return answer