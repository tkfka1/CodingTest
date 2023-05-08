from collections import deque
def solution(A, B):
    answer = 0
    
    A = sorted(A)
    B = deque(sorted(B))
    
    for a in A:
        while True:
            if B:
                b = B.popleft()
                if a < b:
                    answer += 1
                    break
            else:
                break
        if not B:
            break
    
    ## 힙을 쓰는게 더 효율적일듯

    return answer
