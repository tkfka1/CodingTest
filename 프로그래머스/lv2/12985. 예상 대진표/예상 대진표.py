def solution(n,a,b):
    if a%2:
        a += 1
    if b%2:
        b += 1

    count = 1
    while True:
        if a == b:
            print(count)
            break
        
        a = a//2
        b = b//2
        if a%2:
            a += 1
        if b%2:
            b += 1
        count += 1

    return count