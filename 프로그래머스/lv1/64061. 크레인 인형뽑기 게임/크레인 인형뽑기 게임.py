def solution(board, moves):
    answer = 0
    prev = []
    for r in moves:
        for br in board:
            if br[r-1] != 0:
                if prev != [] and prev[-1] == br[r - 1]:
                    answer += 2
                    prev.pop()
                else:
                    prev.append(br[r - 1])
                br[r - 1] = 0
                break
    return answer
