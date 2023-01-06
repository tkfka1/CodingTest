def solution(hp):
    answer = 0
    a,less = divmod(hp,5)
    b,less = divmod(less,3)
    answer = a+b+less
    return answer