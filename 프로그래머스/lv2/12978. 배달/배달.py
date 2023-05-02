def solution(N, road, K):
    answer = 0
    
    graph = [[500001 for _ in range(N)] for __ in range(N)]
    
    for k in road:
        if graph[k[0]-1][k[1]-1] > k[2]:
            graph[k[0]-1][k[1]-1] = k[2]
            graph[k[1]-1][k[0]-1] = k[2]

    # print(graph)
    
    for k in range(N): # via
        graph[k][k] = 0 # 사이클 없으므로 자기 자신 0
        for i in range(N): # src
            for j in range(N): # dst
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])        
    
    # print(graph)
    
    for i in graph[0]:
        if i <= K:
            answer += 1
    
    return answer