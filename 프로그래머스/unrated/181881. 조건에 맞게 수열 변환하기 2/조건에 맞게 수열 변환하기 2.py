def solution(arr):
    answer = 0
    while True:
        temp = []
        for i in arr:
            if i >= 50:
                if i % 2 == 0:
                    temp.append(i//2)
                else:
                    temp.append(i)
            else:
                if i % 2 == 1:
                    temp.append(i*2+1)
                else:
                    temp.append(i)
        if arr == temp:
            break
        answer += 1
        arr = temp
        
    return answer