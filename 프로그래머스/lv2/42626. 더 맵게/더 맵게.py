import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while True:
        if len(scoville) == 2:
            scoville.sort()
            if scoville[0] >= K:
                return answer
            else:
                if scoville[1]*2+scoville[0] >= K:
                    answer += 1
                    return answer
                else:
                    return -1
        res1 = heapq.heappop(scoville)
        if res1 >= K:
            return answer
        res2 = heapq.heappop(scoville)
        heapq.heappush(scoville,res2*2+res1)
        answer += 1
        
    return answer
