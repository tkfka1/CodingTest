def solution(numbers):
    answer = 0
    a = [0,1,2,3,4,5,6,7,8,9]
    for i in set(numbers):
        a.remove(i)
        print(a)
    for i in a:
        answer = answer + i
    return answer