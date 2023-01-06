def solution(n, t, m, timetable):
    answer = 0
    timetable_list = []
    for i in timetable:
        timetable_list.append((int(i[0])*600) + (int(i[1])*60) + (int(i[3])*10) + int(i[4]))

    ans_list = sorted(timetable_list)
    print(ans_list)

    # 540 == 9시
    # 막차일때,
    for i in range(n):
        bustime = 540+i*t
        count = 0
        tans_list = ans_list[:]
        for ii in ans_list:
            if bustime >= ii:
                count += 1
                tans_list.remove(ii)
            # else:
            #     answer = bustime
            if count == m:
                print(f"{i}끝")
                if i == n-1:
                    answer = ii-1
                break
        else:
            answer = bustime
        ans_list = tans_list


    t1 , res = divmod(answer, 600)
    t2 , res = divmod(res, 60)
    t3 , t4 = divmod(res,10)
    answer = str(t1) + str(t2) + ":" + str(t3) + str(t4)
    return answer