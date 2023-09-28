def solution(arr):
    l = max(len(arr),len(arr[0]))
    answer = [[0 for __ in range(l)] for _ in range(l)]
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            answer[y][x] = arr[y][x]
    return answer