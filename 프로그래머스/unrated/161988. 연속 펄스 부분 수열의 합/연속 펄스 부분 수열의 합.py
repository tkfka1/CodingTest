def solution(sequence):
    answer = 0
    
#     sq_plus = []
    
#     pulse = True
#     for i in sequence:
#         if pulse:
#             sq_plus.append(i)
#             pulse = False
#         else:
#             sq_plus.append(-i)
#             pulse = True

## 시간초과
#     for start in range(len(sq_plus)):
#         for end in range(len(sq_plus),start,-1):
#             # print(sq_plus[start:end])
#             answer = max(answer , abs(sum(sq_plus[start:end])))
    
    nu_li = [0]
    ## 누적합
    pulse = True
    for i in sequence:
        if pulse:
            nu_li.append(nu_li[-1]+i)
            pulse = False
        else:
            nu_li.append(nu_li[-1]-i)
            pulse = True
    
    ### 2, -3, -6, -1, 3, 1, 2, -4
    ### 2, -1,  -7,  -8, -5, -4, -2, -6
    # print(nu_li)
    # print(abs(max(nu_li) - min(nu_li)))

    return abs(max(nu_li) - min(nu_li))