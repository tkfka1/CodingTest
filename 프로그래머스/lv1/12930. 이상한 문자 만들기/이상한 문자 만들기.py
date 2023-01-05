def solution(s):
    return "".join([z.lower() if x%2 else z.upper() for i in s.split(" ") for x,z in enumerate(i+" ")][:-1])