def solution(num, total):
    answer = []
    for i in range(-num,1001):
        sum = 0
        for ii in range(num):
            sum += i+ii
        if sum == total:
            for ii in range(num):
                answer.append(i+ii)
        
    return answer