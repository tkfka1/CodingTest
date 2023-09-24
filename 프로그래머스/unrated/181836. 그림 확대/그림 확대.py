def solution(picture, k):
    answer = []
    for i in picture:
        temp = ""
        for ii in i:
            for _ in range(k):
                temp += ii
        for _ in range(k):
            answer.append(temp)
    return answer