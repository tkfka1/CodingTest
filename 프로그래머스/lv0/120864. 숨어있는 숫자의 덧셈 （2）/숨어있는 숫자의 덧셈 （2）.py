def solution(my_string):
    answer = 0
    temp = ""
    for i in my_string:
        if ord(i) > 57:
            temp += " "
        else:
            temp += i

    for i in temp.split(" "):
        if i:
            answer += int(i)
    return answer