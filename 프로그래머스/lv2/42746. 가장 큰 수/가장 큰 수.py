def solution(numbers):
    answer = ''
    li0 = []
    li1 = [0]
    li10 = [0]
    li100 = [0]
    li1000 = []
    
    for i in numbers:
        if i == 1000:
            li1000.append(i)
        elif 100 <= i < 1000:
            li100.append(i*1001)
        elif 10 <= i < 100:
            li10.append((i*10101))
        elif 1 <= i < 10:
            x = i
            li1.append(i*111111)
        else:
            li0.append(i)
    
    li1 = sorted(li1,reverse=True)
    li10 = sorted(li10,reverse=True)
    li100 = sorted(li100,reverse=True)

    countli1 = 0
    countli10 = 0
    countli100 = 0

    while True:
        if li1[countli1] == 0 and li10[countli10] == 0 and li100[countli100] == 0:
            break

        if li100[countli100] >= li10[countli10]:
            if li100[countli100] >= li1[countli1]:
                answer += str(li100[countli100]//1001)
                countli100 += 1
            else:
                answer += str(li1[countli1]//111111)
                countli1 += 1
        else:
            if li10[countli10] >= li1[countli1]:
                answer += str(li10[countli10]//10101)
                countli10 += 1
            else:
                answer += str(li1[countli1]//111111)
                countli1 += 1    

    if li1000:
        answer+= "1000"*len(li1000)
    
    if li0:
        answer+= "0"*len(li0)
        
    if answer[0] == "0":
        return "0"
    
    return answer