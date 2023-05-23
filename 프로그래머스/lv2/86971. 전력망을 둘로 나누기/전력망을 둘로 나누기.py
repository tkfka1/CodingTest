def solution(n, wires):
    answer = 100

    if n == 2:
        return 0

    ## 딕셔너리에 간선 전부 넣기
    dic = {}
    for i in wires:
        if dic.get(i[0]):
            dic[i[0]].append(i[1])
        else:
            dic[i[0]] = [i[1]]
            
        if dic.get(i[1]):
            dic[i[1]].append(i[0])
        else:
            dic[i[1]] = [i[0]]
    
    print(dic)
    
    ## 간선 따라 전부 방문하고 방문한 개수 리턴 함수 n = 방문할것 ,no_n = 방문안할곳
    def net_visit(node,no_node):
        
        visit_dic = {}
        visit_dic[no_node] = 1
        
        li = []
        newli = []
        
        for i in dic[node]:
            if not visit_dic.get(i):
                visit_dic[i] = 1
                li.append(i)
        
        while True:
            newli = []
            
            for i in li:
                for ii in dic[i]:
                    if not visit_dic.get(ii):
                        visit_dic[ii] = 1
                        newli.append(ii)
                        
            li = newli
            if not newli:
                break
                
        ## 위코드로는 1개일때는 1개로안되고 0으로됨 예외처리
        if len(visit_dic) == 1:
            return 1
        else:
            return len(visit_dic)-1
    
    
    
    ## 간선 하나씩 제거해 보면서 최저 개수 찾기
    for i in wires:
        n1 = net_visit(i[0],i[1])
        # n2 = net_visit(i[1],i[0])
        
        # print(n1,n2)
        
        answer = min(abs(n-(n1*2)),answer)
        
        
    return answer
    