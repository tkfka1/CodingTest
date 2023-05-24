def solution(number, k):
    answer = ''

    ## k개를 사용하여 맨 앞수를 제일 크도록
    
    number_list = list(map(int,number))
    # print(number_list)
    
    stack = 0
    while k > 0:
        max_val = -1
        max_index = 0
        if stack == len(number_list)-1:
            return answer
        for i in range(stack,stack+k+1):

            if number_list[i] == 9:
                max_index = i
                max_val = 9
                break
            else:
                if max_val < number_list[i]:
                    max_val = number_list[i]
                    max_index = i
        
        answer += str(max_val)
        k -= max_index-stack
        stack = max_index+1
        

    answer += ''.join(map(str,number_list[stack:]))
    
    
    return answer
