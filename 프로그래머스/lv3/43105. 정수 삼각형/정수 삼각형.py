def solution(triangle):
    answer = 0
    t_len = len(triangle)
    t_list = triangle[t_len-1]
    n = t_len-1
    if t_len == 1:
        answer = triangle[0][0]
    else:
        while True:
            temp = []
            for i in range(n):
                res = 0
                x = t_list[i]
                y = t_list[i+1]
                if x > y:
                    res = x + triangle[n-1][i]
                else:
                    res = y + triangle[n - 1][i]
                temp.append(res)
            t_list = temp
            n -= 1
            if n == 0:
                break
        answer = t_list[0]
    return answer