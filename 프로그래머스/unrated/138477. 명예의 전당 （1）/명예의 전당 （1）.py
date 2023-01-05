import heapq
def solution(k, score):

    answer = []
    h = []
    for i in range(k):
        if i >= len(score):
            return answer
        
        heapq.heappush(h, score[i])
        answer.append(h[0])
    

    
    for i in range(k,len(score)):
        if h[0] >= score[i]:
            answer.append(h[0])
        else:
            heapq.heappush(h, score[i])
            heapq.heappop(h)
            answer.append(h[0])

    
    return answer