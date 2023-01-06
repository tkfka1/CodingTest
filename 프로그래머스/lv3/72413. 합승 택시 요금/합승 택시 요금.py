def solution(n, s, a, b, fares):
    answer = 0

    # 요금의 최대치 + 1 이론상 무한 1000001
    infi = 1000001
    # 2차원 n*n 배열 생성
    list = [[infi]*n for _ in range(n)]

    # 가운데거리 0
    for y in range(n):
        for x in range(n):
            if x == y:
                list[y][x] = 0
    # 기본값 집어넣기
    for i in fares:
        list[i[0]-1][i[1]-1] = i[2]
        list[i[1]-1][i[0]-1] = i[2]

    # 0~n 번 지날때를 list 업데이트
    for i in range(n):
        for y in range(n):
            for x in range(n):
                if x == y:
                    # 같을떄는 아무것도 안함
                    continue
                elif x == i:
                    # 같은행일때도 아무것도 안함
                    continue
                elif y == i:
                    # 같은열일때도 아무것도 안함
                    continue
                else:
                    #만약 i 를 거쳐간다면 그것이 더 작으면 반환
                    sum = list[y][i] + list[i][x]
                    if list[y][x] > sum:
                        list[y][x] = sum

    # a에서 파생될 경우의 숫자
    sum_list = []
    for i in range(n):
        # i 에서 떨어졌을 때 # a 도착
        # list[s][i] == s에서 i를 갔고, 그곳에서 a에 가고 b 에가고
        sum = list[s-1][i] + list[i][a-1] + list[i][b-1]
        sum_list.append(sum)
    answer = min(sum_list)
    return answer