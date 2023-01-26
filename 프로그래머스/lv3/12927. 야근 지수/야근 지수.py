import heapq

def solution(n, works):
    
    # works의 합
    sum_works = sum(works)
    print(sum_works)    
    
    # 만약 합이 근무 시간보다 크다면
    if sum_works > n:
        
        ## 효율성 걸러짐
        # # n의 개수만큼 가장큰 웍스에서 숫자1씩빼기
        # for i in range(n):
        #     works[works.index(max(works))] -= 1
        # print(works)
        
        ## 최대힙 이용
        max_heap = []
        for i in works:
            heapq.heappush(max_heap, (-i))
        
        ## n의 개수만큼 가장 큰 웍스에서 숫자1씩 빼기(음수로 계산하므로 더하기)
        for i in range(n):
            m = heapq.heappop(max_heap)+1
            heapq.heappush(max_heap, m)
        
        #print(max_heap)
        
        return sum([i**2 for i in max_heap])
        
    # 크지 않다면 야근안함
    else:
        return 0