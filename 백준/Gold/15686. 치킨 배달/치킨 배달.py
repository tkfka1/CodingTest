def solution(n,m,graph):
    answer = 1000000
    ## n은 도시의 크기, m은 치킨집의 개수
    dic_chiken = {}
    dic_house = {}

    ## 딕셔너리에 넣기
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            temp = graph[y][x]
            if temp == 2:
                dic_chiken[(y,x)] = {}
            elif temp == 1:
                dic_house[(y,x)] = 1

    ## 치킨딕셔너리에 각 집마다의 거리 넣기
    for i in dic_chiken.keys():
        for j in dic_house.keys():
            dic_chiken[i][j] = abs(i[0]-j[0]) + abs(i[1]-j[1])


    ## 치킨집 m개를 고르는 모든 경우의 수
    from itertools import combinations
    combi = list(combinations(dic_chiken.keys(),m))

    ## 경우의수 루프
    for i in combi:
        temp = 0
        ## 각 집 루프
        for j in dic_house.keys():
            min_dist = 1000000
            ## 각 집마다의 치킨집 거리 최소값 찾기
            for k in i:
                if dic_chiken[k][j] < min_dist:
                    min_dist = dic_chiken[k][j]
            ## 각 집마다의 치킨집 거리 최소값 더하기
            temp += min_dist

        ## 최소값 찾기
        if temp < answer:
            answer = temp

    return answer

n,m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

print(solution(n,m,arr))