def solution(a, b):
    
    # 일단 각 월의 1일의 날짜 넣기
    dic = {}
    
    dic[1] = "FRI"
    dic[2] = "MON"
    dic[3] = "TUE"
    dic[4] = "FRI"
    dic[5] = "SUN"
    dic[6] = "WED"
    dic[7] = "FRI"
    dic[8] = "MON"
    dic[9] = "THU"
    dic[10] = "SAT"
    dic[11] = "TUE"
    dic[12] = "THU"
    
    # 2월이 29일까지 알바없음
    
    li = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

    return li[(li.index(dic[a])+(b%7)-1)%7]