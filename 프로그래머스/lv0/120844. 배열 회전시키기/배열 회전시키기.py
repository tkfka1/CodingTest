def solution(numbers, direction):
    answer = []
    if direction[0] == "r":
        answer = numbers[:-1]
        answer.insert(0,numbers[-1])
    else:
        answer = numbers[1:]
        answer.append(numbers[0])
    return answer