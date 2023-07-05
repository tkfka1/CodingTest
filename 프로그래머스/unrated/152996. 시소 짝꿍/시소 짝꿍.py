

def solution(weights):
    answer = 0
    weights = sorted(weights)

    
    ## 추가 딕셔너리 저장
    dic = {}
    
    ## 한쪽에 올 수 있는 모든 것
    
    for k,v in enumerate(weights):
        
        dic[v] = dic.get(v,0) + 1
    
    ## 같,(2,3) , (2,4) , (3,4)
    
    for i in dic:
        if dic.get(i):
            
            ## 같은거
            if dic[i] >= 2:
                answer += dic[i]*(dic[i]-1)//2
            
            ## 3 : 2 비율 맞는지
            if i%2 == 0:
                temp = (i//2)*3
                if dic.get(temp):
                    answer += dic[i]*dic[temp]
            
            ## 4:2 비율 맞는지
            temp = i*2
            if dic.get(temp):
                answer += dic[i]*dic[temp]
                
            
            ## 4:3 비율 맞는지
            if i%3 == 0:
                temp = (i//3)*4
                if dic.get(temp):
                    answer += dic[i]*dic[temp]
    
    return answer