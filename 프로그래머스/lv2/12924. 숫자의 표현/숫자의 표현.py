def solution(n):
    answer = 0
    
    # 자기자신
    # 2일때
    # 12, 23, 34 , 45 = 3,5,7,9 => 2씩증가
    # 3일때
    # 123,234,345 = > 6,9,12 => 3씩증가
    # 4일때
    # 1234 => 10 =>4씩증가
    #~~~
    # n개일때
    # 기본값 = 1~n의 합  => n씩증가

    # 반복문구성
    # n개가 성립하는지 확인   12~~n 더하면서 자신의 값이 나올 때 까지
    # 반복중에 더한 값이 자신의 값보다 작으면 그 값을 뺀 후 n으로 나눠서 나머지가 0인지 확인 후 break
    # 자신의 값이 나오면 그만

    permutaion_add = 0
    for i in range(1,n+1):
        permutaion_add += i
        if permutaion_add <= n:
            if (n-permutaion_add)%i == 0:
                answer+=1
        else:
            break
    return answer