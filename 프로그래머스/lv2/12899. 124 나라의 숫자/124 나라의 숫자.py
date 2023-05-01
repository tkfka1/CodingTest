def solution(n):
    answer = ''

    rev_base = ''
    while n > 0:
        n, mod = divmod(n-1, 3)
        rev_base += str(mod)
    
    for i in rev_base[::-1]:
        if i == "0":
            answer += "1"
        elif i == "1":
            answer += "2"
        else:
            answer += "4"

    
    
    
    return answer