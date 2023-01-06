def solution(polynomial):
    answer = 0
    polynomial.replace("x","*10000")
    if polynomial[0] == "x":
        polynomial = polynomial[3:]
        answer += 10000
    polynomial = polynomial.replace(" x","10000")
    polynomial = polynomial.replace("x","*10000")
    
    if polynomial:
        answer += eval(polynomial)

    a = answer//10000
    b = answer-(answer//10000*10000)
    if a == 1:
        a = "x"
    elif a == 0:
        a = ""
        return str(b)
    else:
        a = f"{a}x"
    
    if b == 0:
        b = ""
        return a
    else:
        b = str(b)
        return f"{a} + {b}"