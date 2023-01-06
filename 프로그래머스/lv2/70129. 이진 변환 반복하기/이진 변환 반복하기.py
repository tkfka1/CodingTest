def solution(s):
    zero_x = 0
    by_x = 0
    while True:
        if s == "1":
            break
        temp = 0
        for i in s:
            if i == "0":
                zero_x += 1
            elif i == "1":
                temp += 1
        s = str(bin(temp))[2:]
        by_x += 1

    return [by_x,zero_x]