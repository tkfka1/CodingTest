import heapq
def solution(n, costs):
    answer = 0
    
    li = []
    for i in costs:
        a = min(i[0],i[1])
        b = max(i[0],i[1])
        heapq.heappush(li,(i[2],a,b))
    
    dic = {}
    
    ## 간선 연결 확인
    def find(a,b):
        temp = [a]
        temp_dic = {}
        while True:
            if temp:
                a = temp.pop()
                if not temp_dic.get(a):
                    if dic.get(a):
                        if b in dic[a]:
                            return True
                        else:
                            temp += dic[a]
                    else:
                        return False
                temp_dic[a] = 1
            else:
                return False
        
    
    while li:
        c,a,b = heapq.heappop(li)
        if not find(a,b):
            if dic.get(a):
                dic[a].append(b)
            else:
                dic[a] = [b]

            if dic.get(b):
                dic[b].append(a)
            else:
                dic[b] = [a]
            answer += c
        
#         print(c,a,b)
        
#     print(li)
#     print(dic)
    
    return answer