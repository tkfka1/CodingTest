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
    a = [s[i+1:] + s[:i+1] for i in range(len(s))]
    
    answer = 0
    
    for i in a:
        for x in range(80):
            i = i.replace("{}", "").replace("[]", "").replace("()", "")
        if not i:
            answer+=1
    
    
    return answer