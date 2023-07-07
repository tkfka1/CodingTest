def solution(data, col, row_begin, row_end):
    answer = 0
    
    data_sort = sorted(data, key=lambda x: (x[col-1] , -x[0]))
    S = []
    
    for i in range(row_begin-1,row_end):
        temp = data_sort[i]
        mod_sum = 0
        for t in temp:
            mod_sum += t%(i+1)
        S.append(mod_sum)
    
    answer = S[0]
    if len(S) == 1:
        return answer
    
    for i in range(1, len(S)):
        answer = answer ^ S[i]
    
    return answer