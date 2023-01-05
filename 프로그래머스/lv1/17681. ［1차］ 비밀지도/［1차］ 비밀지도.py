def solution(n, arr1, arr2):
    answer = []
    arr11 = []
    arr22 = []
    for i in arr1:
        temp = format(i, 'b')
        if len(temp) < n:
            temp = "0"*(n-len(temp)) + temp
        arr11.append(temp)
    for i in arr2:
        temp = format(i, 'b')
        if len(temp) < n:
            temp = "0"*(n-len(temp)) + temp
        arr22.append(temp)
    
    for y in range(n):
        temp = ""
        for x in range(n):
            if arr11[y][x] == "1" or arr22[y][x] == "1":
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
    
    
    
    
    return answer