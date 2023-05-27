def solution(num_list, n):
    answer = []
    s = 0
    while s < len(num_list):
        answer.append(num_list[s])
        s += n
    return answer