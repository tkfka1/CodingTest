def solution(files):
    
    answer = []
    dic = {}
    
    def findNum(f):
        st = 0
        head = ""
        number = ""
        for v in f:
            if st == 0:
                if v.isdigit():
                    st = 1
                    number += v
                else:
                    head += v
            elif st == 1:
                if v.isdigit():
                    number += v
                else:
                    break
        return head.lower(),int(number),f
        
    # 2중 딕셔너리
    for i in files:
        h,n,t = findNum(i)
        if dic.get(h):
            if dic[h].get(n):
                dic[h][n].append(t)
            else:
                dic[h][n] = [t]           
        else:
            dic[h] = {n:[t]}
    
    # print(dic)
    
    # head - num 순서로 정렬하면서 answer 넣기
    for i in sorted(dic):
        for ii in sorted(dic[i]):
            for iii in dic[i][ii]:
                answer.append(iii)

    
    return answer