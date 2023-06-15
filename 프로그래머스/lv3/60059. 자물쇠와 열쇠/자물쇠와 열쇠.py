def solution(key,lock):
    ## 자물쇠의 크기와 열쇠의 크기를 받아온다.
    n = len(lock)
    m = len(key)

    ## 문제에는 무조건 정사각형이라는 조건이 있다.
    ## 자물쇠 크기 넓히기 대각선으로 하나만 겹쳐질 경우 가장크다고 생각하면 n + (m-1) * 2 만큼 넓혀주면 된다.
    new_lock = [[0] * (n + 2 * (m - 1)) for _ in range(n + 2 * (m - 1))]

    ## 가운데에 자물쇠를 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + m - 1][j + m - 1] = lock[i][j]

    ## print(*new_lock, sep='\n')


    ## 리스트를 받으면 90도 회전하는 함수 만들기
    def lotate(l):
        ## 위아래 뒤집기
        temp = l[::-1]
        # print(*temp,sep='\n')

        ## 대각 뒤집기
        temp = list(zip(*temp))
        # print(*temp,sep='\n')

        return temp


    ## 아까 넓힌 새로운 자물쇠에서 키값을 집어넣고 자물쇠 크기를 확인해서 모두 맞물려 있다면 모든 값이 1이다.
    ## 아니라면 0이거나 겹쳤으면 2이기에 바로 False를 리턴한다.
    def check(l):
        ## m-1 은 자물쇠의 크기 시작 m+n-1은 자물쇠의 크기 끝
        for y in range(m-1,m+n-1):
            for x in range(m-1,m+n-1):
                if l[y][x] != 1:
                    return False
        return True


    ## 4번 회전하면서 확인하기 0, 90, 180, 270
    for i in range(4):
        ## 첫번째 0도는 그대로 진행하고 90, 180, 270도는 회전시킨다.
        if i != 0:
            key = lotate(key)

        ## new_lock의 리스트에서 한칸씩 이동하면서 열쇠를 집어넣고 check 함수로 확인하기
        ## 범위는 0부터 열쇠크기오른쪽하단이 딱 맞는 마지막인 n+m-1까지이다.
        for new_lock_y in range(n + m - 1):
            for new_lock_x in range(n + m - 1):

                ## new_lock에 열쇠 넣기
                for key_y in range(m):
                    for key_x in range(m):
                        new_lock[new_lock_y + key_y][new_lock_x + key_x] += key[key_y][key_x]
                
                ## 만약 check 함수가 True를 리턴하면 True를 리턴하고 끝내기
                if check(new_lock):
                    ## print(*new_lock, sep='\n')
                    return True
                
                ## 사용했던 열쇠 제거
                for key_y in range(m):
                    for key_x in range(m):
                        new_lock[new_lock_y + key_y][new_lock_x + key_x] -= key[key_y][key_x]
                

    ## 
    return False