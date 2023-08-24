def solution(myString, pat):
    answer = 0
    
    while True:
        temp = myString.find(pat)
        if temp == -1:
            break
        myString = myString[temp+1:]
        answer += 1
    
    return answer