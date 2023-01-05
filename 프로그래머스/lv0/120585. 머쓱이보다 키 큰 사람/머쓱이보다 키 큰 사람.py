def solution(array, height):
    answer = 0
    for i in sorted(array):
        if height < i:
            answer += 1
    return answer