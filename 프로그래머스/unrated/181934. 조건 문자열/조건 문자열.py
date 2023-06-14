def solution(ineq, eq, n, m):
    answer = 1
    a = ""
    if eq == "!":
        if ineq == "<":
            if n < m:
                return 1
            else:
                return 0
        else:
            if n > m:
                return 1
            else:
                return 0
    else:
        if ineq == "<":
            if n <= m:
                return 1
            else:
                return 0
        else:
            if n >= m:
                return 1
            else:
                return 0

