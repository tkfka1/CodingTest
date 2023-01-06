def solution(info, edges):
    # 늑대 딕셔너리
    info_dic = {}
    for i in range(len(info)):
        if info[i] == 1:
            info_dic[i] = 1
        else:
            info_dic[i] = 0
    # 트리 딕셔너리
    edges_dic = {}
    for i in edges:
        if edges_dic.get(i[0]):
            edges_dic[i[0]] = edges_dic[i[0]] + [i[1]]
        else:
            edges_dic[i[0]] = [i[1]]

    def listsum(li):
        goat = 0
        wolf = 0
        if len(li) == len(list(set(li))):
            for i in li:
                if info_dic[i] == 0:
                    goat += 1
                else:
                    wolf += 1
        return goat,wolf

    n = 0
    maxgoat = 1
    temp_list = [[0]]
    while True:
        if n == len(info):
            break
        n += 1
        newtemp_list = []
        for i in temp_list:
            goin = []
            for ii in i:
                if edges_dic.get(ii):
                    goin = goin + edges_dic[ii]
            for ii in list(set(goin)):
                res = i+[ii]
                g,w = listsum(res)
                if g > w:
                    if maxgoat < g:
                        maxgoat = g
                    newtemp_list.append(res)
        temp_list = newtemp_list
        
    answer = maxgoat
    
    return answer