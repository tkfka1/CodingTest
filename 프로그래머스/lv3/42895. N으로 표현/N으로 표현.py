def solution(N, number):
    N = str(N)
    answer = 0
    dic = {}
    dic[0] = [N]

    
    dic[1] = []
    for i in dic[0]:
        dic[1].append(i + N)
        dic[1].append(i + "+" + N)
        dic[1].append(i + "-" + N)
    
    if number == int(N):
        return 1
    
    for ii in range(1,8):
        
        dic[ii] = []
        for i in dic[ii-1]:
            if i.isdigit():
                i = str(int(i))
            
            dic[ii].append(i + N)
            dic[ii].append(i + "+" + N)
            dic[ii].append(i + "-" + N)
            dic[ii].append(str(eval(i + "+" + N)))
            dic[ii].append(str(eval(i + "-" + N)))
            dic[ii].append(i + "*" + N)
            dic[ii].append(i + "//" + N)
            dic[ii].append(str(eval(i+ "*" + N)))
            dic[ii].append(str(eval(i+ "//" + N)))
        
        
        # print(set(dic[ii]))
        dic[ii] = set(dic[ii])
        
        for i in dic[ii]:
            if i.isdigit():
                answer = int(i)
            else:
                answer = eval(i)
            if answer == number:
                return ii+1
    
    
    return -1