def solution(M, N):
    answer = 0
    if M == 1:
        return N-1
    if N == 1:
        return M-1
    
    answer = M*N-1
    return answer