def solution(numbers):
    answer = 0
    # start = time.time()

    # 움직인 가중치 리턴 함수
    def move(start,end):
        sol = abs(start-end)
        mul = (start*end)
        if start == end:
            return 1

        # 0일때
        if start == 0 or end == 0:
            # 1,3 = 7
            if sol == 1 or sol == 3:
                return 7
            # 2 = 6
            elif sol == 2:
                return 6
            # 4,6 = 5
            elif sol == 4 or sol == 6:
                return 5
            # 5 = 4
            elif sol == 5:
                return 4
            # 7,9 = 3
            elif sol == 7 or sol == 9:
                return 3
            # 8 = 2
            elif sol == 8:
                return 2
            

        # 0아닐때
        else:
            # 1차이 바로옆 2 or 대각세로 5
            if sol == 1:
                if mul ==12 or mul == 42:
                    return 5
                else:
                    return 2
            # 2차이 옆두칸 4 or 대각한칸 3
            elif sol == 2:
                if mul == 3 or mul == 24 or mul == 63:
                    return 4
                else:
                    return 3
            # 3차이 위아래차이
            elif sol == 3:
                return 2
            # 4차이 대각한칸 or 3,7 대각두칸
            elif sol == 4:
                if mul == 21:
                    return 6
                else:
                    return 3
            # 5차이 대각+가로세로한칸
            elif sol == 5:
                return 5
            # 6차이 세로두칸
            elif sol == 6:
                return 4
            # 7차이 대각+가로세로한칸
            elif sol == 7:
                return 5
            # 8차이 1~9 대각두칸
            elif sol == 8:
                return 6


    # 받은 튜플들을 오른쪽,왼쪽 한번씩해서 반환 
    def click(li,end_num,n,end_n,min_ans):
        click_list = []
        ans = 700000
        
        # 값넣을 딕셔너리 초기화
        dic = {}
        for i in li:
            
            # 양쪽 한번씩 무브함수에 넣어서 가중치 저장
            ml = move(i[0],end_num)
            mr = move(i[1],end_num)

            # 만약 마지막이아니라면
            if n != end_n:
                # 최대가 7이므로 제일 작은것과 (end_n - n)*7 만큼 차이나는 것은 추가 안함
                if i[2] - min_ans < (end_n-n)*7:
                    if end_num == i[0] or end_num == i[1]:
                        if dic.get((i[0],i[1])):
                            if i[2]+1 < dic[(i[0],i[1])]:
                                dic[(i[0],i[1])] = i[2]+1
                        else:
                            dic[(i[0],i[1])] = i[2]+1

                    elif end_num < i[0]:
                        if dic.get((end_num,i[1])):
                            if i[2]+ml < dic[(end_num,i[1])]:
                                dic[(end_num,i[1])] = i[2]+ml
                        else:
                            dic[(end_num,i[1])] = i[2]+ml

                        if dic.get((end_num,i[0])):
                            if i[2]+mr < dic[(end_num,i[0])]:
                                dic[(end_num,i[0])] = i[2]+mr
                        else:
                            dic[(end_num,i[0])] = i[2]+mr

                    elif i[1] > end_num > i[0]:
                        if dic.get((i[0],end_num)):
                            if i[2]+mr < dic[(i[0],end_num)]:
                                dic[(i[0],end_num)] = i[2]+mr
                        else:
                            dic[(i[0],end_num)] = i[2]+mr

                        if dic.get((end_num,i[1])):
                            if i[2]+ml < dic[(end_num,i[1])]:
                                dic[(end_num,i[1])] = i[2]+ml
                        else:
                            dic[(end_num,i[1])] = i[2]+ml

                    elif i[1] < end_num:
                        if dic.get((i[0],end_num)):
                            if i[2]+mr < dic[(i[0],end_num)]:
                                dic[(i[0],end_num)] = i[2]+mr
                        else:
                            dic[(i[0],end_num)] = i[2]+mr

                        if dic.get((i[1],end_num)):
                            if i[2]+ml < dic[(i[1],end_num)]:
                                dic[(i[1],end_num)] = i[2]+ml
                        else:
                            dic[(i[1],end_num)] = i[2]+ml

            if ml >= mr:
                if ans > i[2]+mr:
                    ans = i[2]+mr
            else:
                if ans > i[2]+ml:
                    ans = i[2]+ml
        
        for key, value in dic.items():
            click_list.append((key[0],key[1],value))

        return click_list,ans

    # 기본 튜플 (왼,오,가중)
    left = 4
    right = 6
    temp_answer = 0
    answer_list = {(4,6,0)}

    # 루프 number
    for i in range(len(numbers)):
        answer_list,answer = click(answer_list,int(numbers[i]),i,len(numbers)-1,answer)
        #print(answer_list)

    # 범인의 미천한 코드

    # print("time :", time.time() - start)

    return answer