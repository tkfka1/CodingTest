def solution(my_string):
    answer = ''
    li = []
    for i in my_string:
        temp = ord(i)
        if temp <= 90:
            temp += 32
        li.append(temp)

    li = sorted(li)
    for i in li:
        answer += chr(i)
    return answer