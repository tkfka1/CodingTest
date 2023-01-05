def solution(num):
    answer = 0
    count = 0
    while count < 500:
        if num == 1:
            break
        if num%2:
            num = num*3 + 1
        else:
            num = num//2

        count += 1
        

    return -1 if count == 500 else count