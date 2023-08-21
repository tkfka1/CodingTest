def solution(myString):
    answer = ''
    for i in myString:
        i = i.lower()
        if i == "a":
            i = "A"
        answer += i
    return answer