def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for i, v in enumerate(numbers):
        while stack and v > numbers[stack[-1]]:
            answer[stack.pop()] = v
        stack.append(i)
    return answer