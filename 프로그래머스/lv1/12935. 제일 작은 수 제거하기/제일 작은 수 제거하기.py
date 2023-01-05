def solution(arr):
    return arr[:arr.index(min(arr))]+arr[arr.index(min(arr))+1:] if arr[:arr.index(min(arr))]+arr[arr.index(min(arr))+1:] else [-1]