def solution(numbers):
    answer = []
    
    for i in numbers:
        ## 0이면 1
        if i == 0:
            answer.append(1)
        ## 만약 짝수라면 맨 오른쪽비트에 0 이 있으므로
        elif i%2 == 0:
            answer.append(i+1)
        else:
            ## 홀수라면 2가지로 나뉨
            ## case 1 == 모든비트 1일때
            ## case 2 == 중간에 0이 들어있음
            
            ## 비트의 맨 왼쪽에 0 을 넣으면 -> 제일 오른쪽 01비트를 10비트 로 변환으로 계산가능
            ## 2진변환
            temp = '0'+format(i,'b')
            # print(temp)
            
            ## 거꾸로 비트하나씩 확인
            for index,value in enumerate(reversed(temp)):
                ## 만약 0이면 2의 index제곱 더하고 2의 index-1제곱 빼기
                if value == '0':
                    answer.append(i+(2**index)-(2**(index-1)))
                    break
                



        
    return answer