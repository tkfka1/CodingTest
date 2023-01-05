def solution(n):
    answer = 0
    
    import string

    tmp = string.digits+string.ascii_lowercase
    def convert(num, base) :
        q, r = divmod(num, base)
        if q == 0 :
            return tmp[r] 
        else :
            return convert(q, base) + tmp[r]
        
    x = convert(n,3)

    for i,ii in enumerate(x):
        answer += 3**i*int(ii)
    
    print(int("21",3))
    return answer