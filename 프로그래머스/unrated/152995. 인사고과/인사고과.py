def solution(scores):
    answer = 0
       
#     ## 평점 최소점 딕셔너리
#     score_dic = {}
#     for s in scores:
#         if score_dic.get(s[0]):
#             score_dic[s[0]] = min(score_dic[s[0]],s[1])
#         else:
#             score_dic[s[0]] = s[1]
        
#     # print(score_dic)
    
#     ## 석차 딕셔너리
#     rank_dic = {}
#     for k,v in enumerate(scores):
#         # print(v)
#         for i in score_dic:
#             if i > v[0]:
#                 if score_dic[i] > v[1]:
#                     ## 못받는 사람이 완호라면 -1 리턴 끝
#                     if k == 0:
#                         return -1
#                     break
#         else:
#             # print(k,v)
#             sum_v = sum(v)
#             rank_dic[sum_v] = rank_dic.get(sum_v , 0) + 1
            
#     # print(rank_dic)
    
#     ## 완호의 점수 합계
#     find_sum = sum(scores[0])
    
#     ## 점수 구하기 제일 높은 합계부터 내림차순
#     for i in sorted(rank_dic , reverse = True):
#         # print(i)
#         if i == find_sum:
#             break
#         else:
#             answer += rank_dic[i]
## 시간초과
            
            
    
    ### 내림차순, 오름차순으로 정렬을 한다면 근무 태도 점수 높은 순으로 확인하면서 동료평가점수의 최소값을 비교가능
    
    ## 임시 동료평가 점수
    temp_s = 0
    ## 석차 딕셔너리
    rank_dic = {}
    ## 완호의 점수
    w_s0 = scores[0][0]
    w_s1 = scores[0][1]
    
    ## 앞은 내림차순 뒤는 오름차순 정렬
    for s0,s1 in sorted(scores, key=lambda s: (-s[0], s[1])):
        if temp_s <= s1:
            temp_s = s1
            # print(s0,s1,"인센티브허용")
            # 인센티브를 받는 사람이라면 석차 딕셔너리에 넣기
            sum_v = s0+s1
            rank_dic[sum_v] = rank_dic.get(sum_v , 0) + 1
        else:
            ## 완호인지
            if s0 == w_s0:
                if s1 == w_s1:
                    return -1
            
            ## print(s0,s1,"인센티브비허용")
            
    
    ## 완호의 점수 합계
    w_sum = sum(scores[0])
    
    ## 점수 구하기 제일 높은 합계부터 내림차순
    for i in sorted(rank_dic , reverse = True):
        # print(i)
        if i == w_sum:
            break
        else:
            answer += rank_dic[i]
            
            
    ## 자신의 석차 더해줘야 되므로
    return answer + 1