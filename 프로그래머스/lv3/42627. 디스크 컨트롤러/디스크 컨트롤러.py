from heapq import heappop as hpop
from heapq import heappush as hpush
from heapq import heapify as hify

def solution(jobs):
    lenth = len(jobs)
    answer = 0
    alltime = 0
    temp = []
    time = 0
    run = 0
    hify(jobs)
    
    while True:
        # temp 만들기
        # 뽑고 그거 비교
        while jobs:
            if jobs[0][0] == time:
                min = hpop(jobs)
                # temp에는 인덱스 1,0 바꿔 넣어서 제일 작은 시간을 가진 숫자가 뽑힐 수 있게
                hpush(temp,[min[1],min[0]])
            else:
                break


        # 현재 동작중인지 검사
        # 동작 중이라면 
        if run:
            run -= 1
            # temp의 갯수 + 동작만큼 동작 시간 더하기
            answer += len(temp)+1
            
        # 동작 중이 아니라면 temp에서 하나를 뽑기
        else:
            # temp가 존재 할때는
            if temp:
                run = hpop(temp)[0]-1
                # temp의 갯수 + 동작만큼 동작 시간 더하기
                answer += len(temp)+1
            else:
                if not jobs:
                    break


        time += 1
            
    answer = int(answer / lenth)
    return answer