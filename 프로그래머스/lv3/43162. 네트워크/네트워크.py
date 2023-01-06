def solution(n, computers):
    answer = 1

    # 어떤 컴퓨터에서의 연결된 네트워크를 찾아서 리스트로 반환
    def connect(list):

        temp = list[:]
        for i in range(n):
            if list[i] == 1:
                for ii in range(n):
                    if computers[i][ii] == 1:
                        temp[ii] = 1
        if list == temp:
            return temp
        else:
            return connect(temp)

    temp = connect(computers[0])

    for i in range(n):
        # 만약 커넥트가 0인것이 존재
        if temp[i] == 0:
            #네트워크의 갯수 1개 늘리면서
            answer += 1

            temp2 = connect(computers[i])
            for ii in range(n):
                # temp2가 1이면
                if temp2[ii] == 1:
                    # temp에 업데이트
                    temp[ii] = 1

    return answer