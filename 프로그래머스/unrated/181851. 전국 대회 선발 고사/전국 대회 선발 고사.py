def solution(rank, attendance):
    temp_rank = {}
    
    for i in range(len(attendance)):
        if attendance[i]:
            temp_rank[rank[i]] = i
            
    temp = sorted(temp_rank)[:3]
    
    return (10000*temp_rank[temp[0]]) + (100*temp_rank[temp[1]]) + temp_rank[temp[2]]