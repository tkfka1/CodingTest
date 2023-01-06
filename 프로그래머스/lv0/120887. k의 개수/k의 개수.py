def solution(i, j, k):
    answer = 0
    k = str(k)
    for i in range(i,j+1):
        for ii in str(i):
            if ii == k:
                answer+=1
    return answer