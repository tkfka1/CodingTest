def solution(code):
    answer = ''
    mode = 0
    for k,i in enumerate(code):
        if mode == 0:
            if i == "1":
                mode = 1
            elif k % 2 == 0:
                answer += i
        else:
            if i == "1":
                mode = 0
            elif k % 2 == 1:
                answer += i
    if answer:
        
        return answer
    else:
        return "EMPTY"