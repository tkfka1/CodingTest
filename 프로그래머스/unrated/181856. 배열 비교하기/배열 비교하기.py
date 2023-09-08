def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        temp = sum(arr1) - sum(arr2)
        if temp > 0:
            return 1
        else:
            if temp == 0:
                return 0
            else:
                return -1
    else:
        if len(arr1) > len(arr2):
            return 1
        else:
            return -1
