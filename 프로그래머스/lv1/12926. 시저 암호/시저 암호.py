def solution(s, n):
    answer = ""
    
    for i in s:
        x = ord(i)
        if 65<= x <= 90:
            if x+n >90:
                x -= 26
        elif 97 <= x <= 122:
            if x+n > 122:
                x -= 26
                
        elif x == 32:
            x -= n
            
        answer+= chr(x+n)
    
    print(answer)

    return answer