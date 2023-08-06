def solution(arr, idx):
    for k,v in enumerate(arr):
        if k >= idx:
            if v == 1:
                return k
    return -1