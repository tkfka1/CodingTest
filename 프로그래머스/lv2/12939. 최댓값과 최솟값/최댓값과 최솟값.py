def solution(s):
    res = list(map(int, s.split()))
    res.sort()
    answer = f"{res[0]} {res[-1]}"
    return answer