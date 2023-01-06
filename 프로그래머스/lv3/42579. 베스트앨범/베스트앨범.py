def solution(genres, plays):
    answer = []
    dicsum = {}
    dic1 = {}
    dic2 = {}
    
    for i in range(len(genres)):
        if dicsum.get(genres[i]):
            dicsum[genres[i]] += plays[i]
            if dic1[genres[i]][0] < plays[i]:
                dic2[genres[i]] = dic1[genres[i]]
                dic1[genres[i]] = plays[i],i
            elif dic2[genres[i]][0] < plays[i]:
                dic2[genres[i]] = plays[i],i
        else:
            dicsum[genres[i]] = plays[i]
            dic1[genres[i]] = plays[i],i
            dic2[genres[i]] = -1,-1
    
    for i in sorted(dicsum.items(), key = lambda item:item[1]):
        a1,b1 = dic1[i[0]]
        a2,b2 = dic2[i[0]]
        if b1 == b2 or b2 == -1:
            answer = [b1] + answer
        else:
            answer = [b1,b2] + answer
    
    return answer