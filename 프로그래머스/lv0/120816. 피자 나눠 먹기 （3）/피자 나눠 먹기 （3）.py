def solution(slice, n):
    x,y = divmod(n,slice)
    if y != 0:
        x += 1
    return x