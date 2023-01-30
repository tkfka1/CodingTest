def solution(n, t, m, p):
    answer = ''
    
    ## 진법 변환 함수
    def zin(n,q):
        if n == 0:
            return "0"
        rev_base = ''

        while n > 0:
            n, mod = divmod(n, q)
            if mod > 9:
                if mod == 10:
                    mod = "A"
                if mod == 11:
                    mod = "B"
                if mod == 12:
                    mod = "C"
                if mod == 13:
                    mod = "D"
                if mod == 14:
                    mod = "E"
                if mod == 15:
                    mod = "F"
                    
            rev_base += str(mod)

        return rev_base[::-1] 

    st = ""
    for i in range(1000*100):
        
        st += zin(i,n)
        
        if len(st) >= m*t:
            break
    
#     print(st)
    
    for i in range(0,t):
        answer += st[i*(m)+(p-1)]
    
    
    return answer