def solution(n):
    answer = 0
    b = format(n, 'b')
    ans = ""
    num1 = 0
    num0 = 0
    onenext0 = False
    over0 = False
    
    for i in range(len(b)-1,-1,-1):
        if b[i] == "0":
            if onenext0:
                if over0:
                    ans = "0" + ans
                else:
                    ans = ans[1:]
                    ans = "10" + "0"*num0 + "1"*(num1-1)
                    over0 = True
            else:
                ans = "0" + ans
                num0 += 1
                
        else:
            onenext0 = True
            ans = "1" + ans
            num1 += 1
    
    if over0 == False:
        ans = "10"+ "0"*num0 + (num1-1)*"1"

    answer= int(ans,2)

    return answer