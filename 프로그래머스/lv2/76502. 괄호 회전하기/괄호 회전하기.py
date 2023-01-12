def solution(s):
    import re

    def sub(text):
        temp = text
        for i in range(len(text)//2+1):
            start = len(temp)
            temp = temp.replace("()", "")
            temp = temp.replace("[]", "")
            temp = temp.replace("{}", "")
            if temp:
                if start == len(temp):
                    return 0
            else:
                return 1
        
    answer = 0
    
    for i in range(len(s)):
        answer += sub(s)
        s = s[1:] + s[0]
    
    return answer