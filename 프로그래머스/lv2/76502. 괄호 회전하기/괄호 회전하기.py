def solution(s):
    def sub(text):
        t = text
        for i in range(len(text)//2+1):
            start = len(t)
            t = t.replace("{}", "").replace("[]", "").replace("()", "")
            if t:
                if start == len(t):
                    return 0
            else:
                return 1
        
    answer = 0
    
    for i in range(len(s)):
        answer += sub(s)
        s = s[1:] + s[0]
    
    return answer