def solution(my_str, n):
    answer = []
    temp = ""
    for index, value in enumerate(my_str):
        temp += value
        if (index+1) % n  == 0:
            answer.append(temp)
            temp = ""
            print(answer)
        else:
            if index == len(my_str)-1:
                answer.append(temp)

    return answer