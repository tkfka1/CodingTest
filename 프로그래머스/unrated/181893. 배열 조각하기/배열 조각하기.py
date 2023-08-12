def solution(arr, query):

    for k,v in enumerate(query):
        ## 짝수 인덱스
        if k%2 == 0:
            arr = arr[:v+1]
            
        ## 홀수 인덱스
        else:
            arr = arr[v:]

    return arr