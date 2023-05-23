def solution(s):
    answer = 0
    
#     ## (n) = len(s)//2개단위 ~ 2개단위
    
#     n = len(s)//2
#     # print(11//2)
    
#     test_s = "abcdabcde"
#     test_n = len(test_s)//2
    
#     if test_s[0:test_n] == test_s[test_n:test_n+test_n]:
#         print(test_s[0:test_n])
#         print("yes")
    
    
#     "abcbcabcbcbcbc"
#     "2abcbc 2bc"
#     "a2bca 4bc"
    
#     "abcbcabcbc"
#     "2abcbc"
#     "a2bca2bc"

## 문제 이해 다시함
## 1개 ~~~ n//2 개의 단위로 자를때 하나만 정해서 제일 짧은 경우의 길이 찾기
    
    answer = len(s)
    
    for i in range(1,(len(s)//2)+ 1):
        ## 임시 답
        temp_answer = len(s)
        
        ## i 개 단위로 잘라 압축
        # print(i)
        
        ## 문자열 저장
        stack_num = i
        stack = s[:stack_num]
        
        ## 첫 검색시 숫자 쓰는 비용 따져야됨
        find_first = 0
        
        ## i 부터 시작해서 i 씩 커지게, 끝은 len(s)
        for ii in range(i+i,len(s)+1,i):
            
            temp_string = s[stack_num:ii]
            # print(stack,temp_string)
            
            if stack == temp_string:
                # print("find")
                
                ## 첫검색 아니라면
                if find_first:
                    find_first += 1
                    # print(find_first)
                    
                    ## 만약 10개 100개 등등 자릿수가 올라가면 문자열길이도늘어나므로
                    ## 매번 문자변환및 제곱연산은 무거우므로 10의배수만계산
                    if find_first%10 == 0:
                        if find_first == 10**(len(str(find_first)) - 1):
                            temp_answer += 1
                        
                ## 첫검색이라면
                else:
                    find_first = 2
                    ## 첫검색이므로 문자열길이 하나 더함
                    temp_answer += 1
                
                ## 중복 문자열 길이 만큼 빼기
                temp_answer -= i
                    
            else:
                ## 첫검색으로 초기화
                find_first = 0
                
            stack_num = ii
            stack = temp_string
        
        ## 제일 작은 답
        answer = min(answer,temp_answer)
        # print(answer)
            
    
    
    
    
    return answer