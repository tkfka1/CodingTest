def solution(array):
    answer = 0
    for i in array:
        i = str(i)
        for ii in i:
            if ii == "7":
                answer += 1

    return answer